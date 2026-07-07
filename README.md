# mentistics — a fictional encyclopedia

the public knowledge set of a posthuman commons: nine certified entries, one
uncertified address, and the disclosure conventions holding them together.

a work of metascience fiction. the wiki is diegetic — it is written by and for
minds inside the civilization it describes, and its editorial biases, certification
banners, revision logs, and absences are part of the text.

## structure

```
entries/          markdown sources (canonical text, one file per entry)
build.py          static site generator (python 3, needs `pip install markdown`)
assets/style.css  the commons' visual register
pages/*.html      generated entry pages
index.html        generated front matter + index
uncertified.html  generated — every redlink in the corpus resolves here
```

## hosting on github pages

1. push this repo to github
2. settings → pages → source: **deploy from a branch**, branch: `main`, folder: `/ (root)`
3. done — the site is static html, no build step runs on github's side

the `.nojekyll` file is included so github serves the files as-is.

## editing

edit or add markdown files in `entries/`, then:

```
pip install markdown
python3 build.py
```

conventions the generator understands:

- first `# heading` becomes the page title
- the **first blockquote** becomes the certification banner; its zk-hash string
  (`` `xxx…yyy` ``) deterministically generates the entry's attestation seal
- subsequent blockquotes render as scope notes
- `[Bracketed Names]` are wikilinks: entries in the corpus map (`SLUGS` in
  `build.py`) link verdigris; everything else renders as an oxide redlink
  resolving to `uncertified.html`
- `$…$` and `$$…$$` render via katex (cdn, client-side)
- a trailing `---` + `*Revision log (excerpt).*` paragraph renders as the
  revision log block

new entries need a line in `SLUGS` (and optionally `GROUPS`/`DESCRIPTIONS`)
in `build.py` to join the sidebar and index.
