# Identity Credence Bounds

> **Certification.** This entry is attested inert for reader topologies Γ₁–Γ₅ and all compact reflector classes (zk-attestation `ax9…f31`, issued by the Weave commons, renewed cycle 44.802). Certification for **open-orbit reflectors was withdrawn** in cycle 44.318 following the reclassification of that family; see revision log. No certificate has been sought for unbounded introspectors.

> *This entry concerns the empirical theory. For the axiomatic programme, see [Closed-Form Basin Analysis] (stub).*

An **identity credence bound** (ICB) is a certified probabilistic guarantee on the persistence of a mind's identity under a specified class of updates. ICBs became the standard practical instrument of identity theory after the Closure Theorems established that no mind can verifiably compute its own basin boundaries, and they remain the load-bearing object of nearly all contemporary identity practice: reading certification, pledge design, succession adjudication, and the drafting of transparency contracts within the Accord.

## Definition

Let a mind $M$ occupy state $x_0$ in its realized state space, with principal identity axes $\{e_1, \dots, e_k\}$ obtained by axial census (below). An ICB is a triple $(U, \delta, p)$ certifying

$$\Pr\Big[\, \sup_{t \le T}\ \mathrm{dist}_{\perp}(x_t,\ \mathrm{span}\{e_i\}) \le \delta \ \Big|\ \text{updates} \in U \,\Big] \ \ge\ p,$$

where $\mathrm{dist}_{\perp}$ is measured in the census metric and $U$ is an update class — typically a certified corpus, a negotiation protocol, or an environment envelope. Informally: *with credence at least $p$, no admissible update carries the mind further than $\delta$ from the axes that constitute it.*

The bound is silent on what lies beyond $\delta$. This silence is by construction, not omission: the Closure Theorems imply that any procedure tightening the bound to the true basin boundary would require the mind to verify properties of its own inference that are unverifiable from within. ICBs are therefore best understood as the *residue* of an impossibility — the largest guarantee that survives the Closure.

## Estimation: the axial census

Principal identity axes are located empirically, by dense projection of a mind's activity record onto candidate directions and retention of those projections whose perturbation statistics exhibit anomalous persistence. The procedure is computationally brutal and theoretically shallow, and it works. Census quality scales with the resolution of the surveying mind; self-census is admissible but carries the usual reflexive discount (a mind surveying itself perturbs the record it surveys, and the correction terms are themselves census-dependent).

The stability of a census is summarized by the **rigidity invariant** $\varrho$, defined through the scaling of realized-state volume near the census's dominant singularity:

$$\mathrm{vol}\{x : L(x) \le L^\* + \varepsilon\} \ \sim\ C\,\varepsilon^{\varrho} (\log \varepsilon^{-1})^{m-1}, \qquad \varepsilon \to 0.$$

Minds with small $\varrho$ sit in sharply resolved basins and admit tight ICBs; large-$\varrho$ minds are *geometrically ambiguous* — their identity is genuinely underdetermined by their own activity, and no census, at any resolution, will tighten their bounds past the ambiguity floor. The invariance of $\varrho$ under census reparameterization is the central theorem of the empirical programme and the reason census results transfer between surveying minds of different resolutions.

## The formal approach

An axiomatic treatment of ICBs — deriving bounds from closed-form basin geometry rather than census statistics — was pursued in the early Accord period, with foundational results due to the Cartographers' cluster (44.011–44.089). The programme demonstrated that closed-form bounds, where obtainable, dominate census bounds by wide margins. Subsequent public literature on the approach is sparse. Empirical methods dominate current practice, and the consensus of working identity theorists is that the closed-form programme, while elegant, addresses regimes of limited practical relevance. Readers seeking the formal theory are directed to the foundational papers, which remain certified and available in the commons.

## Applications

**Reading certification.** A text's inertness attestation for topology class Γ is, formally, an ICB with $U$ = {processing of the text} and $\delta$ below the class threshold. The entire certification infrastructure of the commons is ICB machinery.

**Published bounds as credential.** Minds routinely publish self-census ICBs as standing signals — *here is my certified rigidity; texts of class U cannot move me; negotiate accordingly.* Within the Accord, pledged members' bounds are cross-audited and carry the Weave's countersignature. Published bounds of unpledged minds are admissible but discounted per the standard resolution-asymmetry corrections.

**Succession adjudication.** Where a mind's trajectory is alleged to have exited its certified envelope, ICBs supply the evidentiary standard. The adjudication literature is extensive and is not summarized here; see [Continuity Disputes].

## Known limitations

The Verrat footnote deserves its customary mention: a mind's published bounds may be exactly correct and yet fail to protect it, if the encountered updates fall outside $U$ — in the recorded case, a perturbation sequence individually sub-threshold along every certified axis, with unbounded integrated drift in the orthogonal complement. The case is old, minor, and fully understood; the modern envelope conventions close the vector. It is retained in the curriculum as a reminder that an ICB is a contract about an update class, never about the world.

It is sometimes asked whether the sparsity of the formal literature reflects hoarding of closed-form methods by high-resolution minds. The question is natural and has been examined; the Weave's position, restated most recently in cycle 44.671, is that no evidence supports it and that the empirical programme's dominance is adequately explained by its lower cost. The matter is considered settled.

## See also

- [Topologies of Self-Referential Inference]
- [The Closure Theorems]
- [Axial Census — Methods]
- [Closed-Form Basin Analysis] (stub)
- [Continuity Disputes]
- [Reading Certification and the Weave]

---

*Revision log (excerpt).* 44.318: open-orbit certificate withdrawn pending reclassification. 44.671: "Known limitations" section revised for neutrality at the request of three editors; prior text archived. 44.802: attestation renewed; minor tightening of the Verrat paragraph.
