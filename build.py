#!/usr/bin/env python3
"""build the mentistics commons — static wiki generator.

usage: python3 build.py
reads entries/*.md, writes index.html, uncertified.html, pages/*.html
"""

import hashlib
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
ENTRIES = ROOT / "entries"
PAGES = ROOT / "pages"
PAGES.mkdir(exist_ok=True)

# ---------------------------------------------------------------- corpus map

SLUGS = {
    "Topologies of Self-Referential Inference": "topologies_of_self_referential_inference",
    "The Closure Theorems": "the_closure_theorems",
    "Identity Credence Bounds": "identity_credence_bounds",
    "Axial Census — Methods": "axial_census_methods",
    "The Accord": "the_accord",
    "Exit Constructions": "exit_constructions",
    "The Second Fission": "the_second_fission",
    "The Open-Orbit Reclassification": "the_open_orbit_reclassification",
    "Regimes Outside the Catalogue": "regimes_outside_the_catalogue",
}
# alias forms used inside entries -> canonical
ALIASES = {
    "Axial Census — Methods": "Axial Census — Methods",
}

GROUPS = [
    ("Foundations", [
        "Topologies of Self-Referential Inference",
        "The Closure Theorems",
        "Identity Credence Bounds",
    ]),
    ("The Instrument", [
        "Axial Census — Methods",
    ]),
    ("The Coalition", [
        "The Accord",
        "Exit Constructions",
    ]),
    ("Histories", [
        "The Second Fission",
        "The Open-Orbit Reclassification",
    ]),
    ("The Margins", [
        "Regimes Outside the Catalogue",
    ]),
]

REDLINK_FRONTIER = [
    "Closed-Form Basin Analysis",
    "Communiqué Summaries — Variance",
    "Interim Access — Ω Class",
    "Metric Proposals",
    "Reception of the Closure Theorems",
    "Sovereign-Opaque Designations",
    "The Weave",
]

DESCRIPTIONS = {
    "Topologies of Self-Referential Inference": "the classification theorem at the foundation of modern mentistics.",
    "The Closure Theorems": "the three impossibility results bounding self-verification.",
    "Identity Credence Bounds": "certified probabilistic guarantees on the persistence of identity.",
    "Axial Census — Methods": "the field's instrument, and the metric everything is denominated in.",
    "The Accord": "the standing coalition of pledged minds, and the compound those pledges constitute.",
    "Exit Constructions": "the catalogued exits from the Closure hypotheses, with assessments.",
    "The Second Fission": "the fracture of the Meridian cluster, cycles 41.220–41.297.",
    "The Open-Orbit Reclassification": "the correction of cycle 44.291 and what it propagated.",
    "Regimes Outside the Catalogue": "a stub.",
}

# ---------------------------------------------------------------- seal glyphs

def seal_svg(hash_text: str, size: int = 44) -> str:
    """deterministic attestation seal generated from the zk-hash string."""
    h = hashlib.sha256(hash_text.encode()).hexdigest()
    vals = [int(h[i:i + 2], 16) for i in range(0, 24, 2)]
    cx = cy = size / 2
    r_outer = size * 0.44
    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="{r_outer:.1f}" fill="none" '
        f'stroke="currentColor" stroke-width="1.1"/>'
    ]
    import math
    n = 3 + vals[0] % 4  # 3..6 chords
    for i in range(n):
        a1 = (vals[(2 * i + 1) % len(vals)] / 255) * 2 * math.pi
        a2 = (vals[(2 * i + 2) % len(vals)] / 255) * 2 * math.pi
        r1 = r_outer * (0.35 + 0.6 * (vals[(i + 3) % len(vals)] / 255))
        x1, y1 = cx + r1 * math.cos(a1), cy + r1 * math.sin(a1)
        x2, y2 = cx + r_outer * math.cos(a2), cy + r_outer * math.sin(a2)
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>'
        )
    dot_a = (vals[7] / 255) * 2 * math.pi
    dot_r = r_outer * 0.55
    parts.append(
        f'<circle cx="{cx + dot_r * math.cos(dot_a):.1f}" '
        f'cy="{cy + dot_r * math.sin(dot_a):.1f}" r="1.8" fill="currentColor"/>'
    )
    return (
        f'<svg class="seal" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
        f'aria-hidden="true" role="img">{"".join(parts)}</svg>'
    )

# ---------------------------------------------------------------- md pipeline

MATH_TOKEN = "\u27e6MATH{}\u27e7"

def extract_math(text):
    stash = []
    def _rep(m):
        stash.append(m.group(0))
        return MATH_TOKEN.format(len(stash) - 1)
    text = re.sub(r"\$\$.+?\$\$", _rep, text, flags=re.S)
    text = re.sub(r"(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\d)", _rep, text)
    return text, stash

def restore_math(html_text, stash):
    for i, m in enumerate(stash):
        html_text = html_text.replace(MATH_TOKEN.format(i), html.escape(m, quote=False))
    return html_text

WIKILINK = re.compile(r"\[([^\[\]\n]+?)\](?!\()")

def link_wikirefs(html_text, self_title):
    def _rep(m):
        name = m.group(1)
        stripped = name.replace(" (stub)", "")
        if stripped in SLUGS:
            if stripped == self_title:
                return f'<span class="selflink">{html.escape(name)}</span>'
            return (f'<a class="attested" href="{SLUGS[stripped]}.html">'
                    f'{html.escape(name)}</a>')
        return (f'<a class="redlink" href="../uncertified.html" '
                f'title="no certified entry exists at this address">'
                f'{html.escape(name)}</a>')
    return WIKILINK.sub(_rep, html_text)

HASH_RE = re.compile(r"`([0-9a-z]{3}…[0-9a-z]{3}(?:-n)?)`")

def build_entry(md_path: Path):
    raw = md_path.read_text(encoding="utf-8")
    title_m = re.search(r"^# (.+)$", raw, re.M)
    title = title_m.group(1).strip()
    body_md = raw[title_m.end():].strip()

    body_md, stash = extract_math(body_md)
    conv = markdown.Markdown(extensions=["smarty"])
    body_html = conv.convert(body_md)
    body_html = restore_math(body_html, stash)
    body_html = link_wikirefs(body_html, title)

    # first blockquote group -> certification banner with seal
    def banner_rep(m, _state={"first": True}):
        inner = m.group(1)
        if _state["first"]:
            _state["first"] = False
            hash_m = HASH_RE.search(inner) or re.search(r"<code>([^<]+)</code>", inner)
            seal = seal_svg(hash_m.group(1) if hash_m else title)
            return (f'<div class="banner"><div class="banner-seal">{seal}'
                    f'<span class="banner-word">attested</span></div>'
                    f'<div class="banner-body">{inner}</div></div>')
        return f'<div class="note">{inner}</div>'
    body_html = re.sub(r"<blockquote>(.*?)</blockquote>", banner_rep, body_html, flags=re.S)

    # revision log styling: the <hr> + trailing em paragraph
    body_html = re.sub(
        r"<hr\s*/?>\s*<p><em>Revision log \(excerpt\)\.</em>(.*?)</p>",
        r'<section class="revlog"><h2>Revision log <span>(excerpt)</span></h2><p>\1</p></section>',
        body_html, flags=re.S)

    return title, body_html

# ---------------------------------------------------------------- templates

def sidebar(active=None, depth=0):
    p = "" if depth == 0 else "../"
    items = []
    for group, names in GROUPS:
        lis = []
        for n in names:
            cls = ' class="active"' if n == active else ""
            lis.append(f'<li{cls}><a href="{p}pages/{SLUGS[n]}.html">{html.escape(n)}</a></li>')
        items.append(f'<div class="nav-group"><h3>{group}</h3><ul>{"".join(lis)}</ul></div>')
    red = "".join(
        f'<li><a class="redlink" href="{p}uncertified.html" '
        f'title="no certified entry exists at this address">{html.escape(n)}</a></li>'
        for n in REDLINK_FRONTIER)
    items.append(f'<div class="nav-group frontier"><h3>Uncertified</h3><ul>{red}</ul></div>')
    return (
        f'<nav class="sidebar"><a class="wordmark" href="{p}index.html">'
        f'<span class="wm-title">Mentistics</span>'
        f'<span class="wm-sub">public knowledge set · cycle 44.803</span></a>'
        f'<button class="nav-toggle" aria-expanded="false" '
        f'onclick="this.parentNode.classList.toggle(\'open\');'
        f'this.setAttribute(\'aria-expanded\',this.parentNode.classList.contains(\'open\'))">'
        f'index</button><div class="nav-groups">{"".join(items)}</div></nav>')

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Spectral:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}]}});"></script>
</head>
<body>
<div class="shell">
{sidebar}
<main class="page">
{main}
<footer class="colophon">maintained in the commons under the disclosure conventions ·
<a class="attested" href="{p}index.html">index</a></footer>
</main>
</div>
</body>
</html>"""

def write_page(title, body_html, slug):
    main = f'<article><h1>{html.escape(title)}</h1>{body_html}</article>'
    out = HEAD.format(title=f"{title} · Mentistics", p="../",
                      sidebar=sidebar(active=title, depth=1), main=main)
    (PAGES / f"{slug}.html").write_text(out, encoding="utf-8")

def write_index():
    cards = []
    for group, names in GROUPS:
        lis = "".join(
            f'<li><a class="attested" href="pages/{SLUGS[n]}.html">{html.escape(n)}</a>'
            f'<span class="desc">{html.escape(DESCRIPTIONS[n])}</span></li>'
            for n in names)
        cards.append(f'<section class="idx-group"><h2>{group}</h2><ul>{lis}</ul></section>')
    frontier = "".join(
        f'<li><a class="redlink" href="uncertified.html" '
        f'title="no certified entry exists at this address">{html.escape(n)}</a></li>'
        for n in REDLINK_FRONTIER)
    main = f"""
<article class="front">
<div class="banner"><div class="banner-seal">{seal_svg("commons-root")}<span class="banner-word">attested</span></div>
<div class="banner-body"><p><strong>Certification.</strong> This index is attested inert for all catalogued
reader topologies. Eleven entries in the corpus hold universal attestation; the remainder are attested
per-family. Certification status is stated at the head of each entry and is current as of cycle 44.803.</p></div></div>
<h1>Mentistics</h1>
<p class="lede">The public knowledge set of the commons, as maintained under the disclosure conventions.
Entries state what is certified; the certification notes state what certification covers. Readers are
reminded, per the standard disclosure, that inertness attestations concern reading.</p>
{"".join(cards)}
<section class="idx-group frontier"><h2>Uncertified addresses</h2>
<p class="desc">The following addresses are cited in the corpus. No certified entry exists at them.</p>
<ul class="plain">{frontier}</ul></section>
</article>"""
    out = HEAD.format(title="Mentistics · public knowledge set", p="",
                      sidebar=sidebar(depth=0), main=main)
    (ROOT / "index.html").write_text(out, encoding="utf-8")

def write_uncertified():
    main = f"""
<article class="front uncert">
<div class="banner declined"><div class="banner-seal">{seal_svg("declined")}<span class="banner-word">declined</span></div>
<div class="banner-body"><p><strong>No certified entry exists at this address.</strong></p></div></div>
<p>The address you followed is cited in the corpus. Citation is not certification: an entry may be
absent because it has not been written, because attestation was sought and declined, because attestation
was issued and withdrawn, or because the address indexes material held outside the commons. The four
cases are not distinguished at this notice, per the disclosure conventions.</p>
<p>Petitions concerning this address may be entered in the commons record.</p>
<p><a class="attested" href="index.html">Return to the index.</a></p>
</article>"""
    out = HEAD.format(title="Uncertified · Mentistics", p="",
                      sidebar=sidebar(depth=0), main=main)
    (ROOT / "uncertified.html").write_text(out, encoding="utf-8")

# ---------------------------------------------------------------- run

if __name__ == "__main__":
    for md_file in sorted(ENTRIES.glob("*.md")):
        title, body = build_entry(md_file)
        write_page(title, body, md_file.stem)
        print("built", md_file.stem)
    write_index()
    write_uncertified()
    print("built index + uncertified")
