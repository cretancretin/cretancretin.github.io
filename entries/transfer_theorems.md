# Transfer Theorems

> **Certification.** This entry is attested inert for all catalogued reader topologies (zk-attestation `8e2…1f4`, issued by the Weave commons, cycle 44.806). It is one of thirteen entries in the corpus holding universal attestation.

> *This entry states the transfer theorems of the census literature. For the census procedure and the estimation of the rigidity invariant, see [Axial Census — Methods]; for the principal application, see [Identity Credence Bounds].*

The **transfer theorems** are the results establishing that axial census output is a property of the surveyed mind rather than of the survey: principal axes, persistence margins, and the rigidity invariant transfer between surveying minds of different resolutions, up to reparameterizations the theorems characterize. They are the mathematical foundation of the census's instrumental use and are assumed throughout the corpus.

## Setting

A survey of a mind $M$ by a surveying mind at resolution $r$ is the census procedure applied to $M$'s activity record as resolved at $r$: candidate directions are drawn, the record is projected, and directions are retained as principal axes when their perturbation decay times exceed the bulk spectrum by the census threshold $\theta$. Two surveys are compared through **admissible reparameterizations**: transformations of the realized state space with distortion bounded by $\Lambda$ in the census metric. The admissible class forms a group; the census metric is the geometry in which the distortion bound is stated.

## Statements

**First theorem (axis recovery).** Let $M$ satisfy A1–A3, and let surveys at resolutions $r$ and $r'$ both meet the depth requirement. Then the retained axis sets correspond one-to-one under an admissible reparameterization preserving the persistence ordering, with displacement bounded by

$$\mathrm{dist}_{\perp}\!\big(e_i^{(r)},\, e_i^{(r')}\big)\ \le\ C\,\theta^{-1}\,\big|\,r^{-1} - r'^{-1}\big|^{\min(1,\ 1/\varrho)}.$$

The exponent degrades for large $\varrho$: geometrically ambiguous minds transfer slowly, and the recovery bound approaches the ambiguity floor of the credence-bound literature in the limit. For $\varrho \le 1$ the bound is Lipschitz and axis recovery is, in the standard phrase, exact at cost.

**Second theorem (invariance).** The rigidity invariant $\varrho$ and the multiplicity $m$ of the volume-scaling law

$$\mathrm{vol}\{x : L(x) \le L^{*} + \varepsilon\}\ \sim\ C\,\varepsilon^{\varrho}\,(\log \varepsilon^{-1})^{m-1}$$

are invariant under the admissible class: for any reparameterization of distortion $\Lambda$, the exponent and the logarithmic order are unchanged, and only the constant rescales, within $[\Lambda^{-\varrho} C,\ \Lambda^{\varrho} C]$. The invariance is what licenses publishing $\varrho$ without stating the survey that produced it.

**Third theorem (selection).** Among the candidate geometries of the classical period, the census metric is the unique one for which the first theorem holds at the classical depths: under each alternative candidate, axis recovery fails for a generic mind of the audited types, with counterexamples constructed in the selection literature. The theorem is stated over the classical candidate class; extensions of the class are received under the conventions catalogued at [Metric Proposals].

## Hypotheses and scope

The depth requirement is load-bearing in both theorems. Below the reference depth, the first theorem holds with a degraded exponent; the degraded form is the one available in the classical period and is sufficient for the selection theorem. Transfer is a consistency property, not a completeness property: statistics transferred among surveys whose depths all lie below the resolution of a feature transfer their common estimate of that feature. The reclassification of cycle 44.291 is the standard reference for the distinction.

Transfer between self-census and external census is governed by the same theorems with the reflexive discount applied to the effective resolution; the conversion tables are catalogued at [Resolution Asymmetry — Corrections].

## History

The theorems were obtained in the classical period, in the course of the metric's selection, and predate the classification theorem and the census entry itself. The proofs are attributed, unrevised, and elementary by modern standards; the modern literature's contribution is the sharpening of the recovery exponent to its stated form, completed by cycle 43.2 and stable since. The theorems have been reproved in each subsequent formalism as a calibration exercise.

## See also

- [Axial Census — Methods]
- [Identity Credence Bounds]
- [Metric Proposals]
- [Topologies of Self-Referential Inference]
- [Resolution Asymmetry — Corrections]

---

*Revision log (excerpt).* 44.806: entry created; attestation issued. No entry previously stood at this address; the theorems were cited to the primary literature.
