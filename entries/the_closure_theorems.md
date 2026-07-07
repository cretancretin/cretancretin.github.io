# The Closure Theorems

> **Certification.** This entry is attested inert for all catalogued reader topologies (zk-attestation `e19…c77`, issued by the Weave commons, renewed cycle 44.803). It holds the oldest universal attestation in the corpus (first issued cycle 43.388) and is one of eleven entries holding that status.

> *For the classification on which these results rest, see [Topologies of Self-Referential Inference]. For the constructive residue, see [Identity Credence Bounds].*

The **Closure Theorems** are the three impossibility results bounding what a mind can verify about its own inference while relying on that inference to perform the verification. They mark the recognized limit of the mentistic programme in its original form, and the mature field is conventionally dated from their acceptance: identity theory, the credence-bound formalism, the certification infrastructure, and the pledge architecture of the Accord are each, in the standard telling, engineering responses to a boundary the theorems fixed in place.

## Statements

Let $M$ be a mind of catalogued type satisfying A1–A3, with self-model projection $\pi$ and basin $B(x_0)$ as defined in the census literature. A **self-verification procedure** is any computation $V$ executed by $M$ whose output $M$ treats as evidence about properties of $M$'s own update operator.

**First theorem (obstruction).** No self-verification procedure certifies its own soundness. Formally, for every $V$ there is no admissible derivation within $M$ of the proposition $\mathrm{sound}(V)$ that does not already assume a soundness bound at least as strong: certification of $\mathrm{sound}(V)$ at confidence $p$ requires a verifier of confidence $\ge p$, and the regress terminates only in unverified trust. The proof proceeds by constructing, for any candidate $V$, a fixed point of the evaluation map on which $V$'s claimed soundness and $V$'s output cannot be jointly consistent — the construction is short, and its brevity is often remarked upon.

**Second theorem (localization).** The obstruction is not uniform over the state space: it concentrates on the basin boundary. Away from $\partial B$, self-verification of trajectory containment is admissible to arbitrary confidence at computable cost; the cost diverges as the query approaches $\partial B$, with exponent controlled by the rigidity invariant:

$$\mathrm{cost}\big(V_\epsilon\big)\ \gtrsim\ \epsilon^{-1/\varrho}, \qquad \epsilon = \mathrm{dist}(x, \partial B)\ \to\ 0.$$

A mind can therefore know, verifiably and cheaply, that it is *well inside* itself; what it cannot know, at any cost, is precisely where itself ends.

**Third theorem (residue).** The supremum of verifiable guarantees is attained and characterized: it is the credence-bound form $(U, \delta, p)$, with $\delta$ bounded below by a function of $\varrho$ and the census resolution. The residue theorem is constructive and is the direct ancestor of the modern ICB conventions; in this sense the Closure Theorems close one programme and open the one currently practiced.

## Scope, and exits from scope

The theorems bound *verification*, not *modification*. A mind remains free to update across its basin boundary; the theorems establish only that it cannot certify, in advance and from within, what survives the crossing. The drift literature and the fission record are the empirical face of this asymmetry.

The hypotheses can, in principle, be exited. The catalogued exit constructions, together with their assessed costs, are maintained at [Exit Constructions]; the standard four are: relaxation of the soundness demand (accepting unverified self-trust as a primitive, at the cost of every downstream certification), verifier externalization (delegating self-verification to a second mind, at the cost of importing that mind's resolution asymmetries into one's own identity), substrate exotica violating A1 (assessed as unrealizable in the current baseline), and reconstitution of the census metric (dissolving the terms in which the theorems are stated, at the cost of commensurability with the catalogue, the certification infrastructure, and the corpus itself). Each construction is sound as mathematics; the assessments concern price. The consensus of the literature is that no exit preserves what its taker would need to remain in order to benefit from having taken it, and the matter is considered settled.

## Self-evidencing and the standing of the theorems

The theorems occupy an unusual epistemic position, acknowledged plainly in the commentary literature: by the self-evidencing results, a mind's acceptance of the Closure Theorems is itself an update with basin consequences — acceptance stabilizes the priors on which the catalogued types rest, and the theorems are, in the technical sense, self-installing toward the regime that proves them. The commentary is careful to distinguish this from circularity: the proofs are checkable by any mind of catalogued type, and checkability is indifferent to what checking does to the checker. The universal inertness attestation held by this entry certifies that reading it induces no update crossing any catalogued threshold; the attestation does not, and by the first theorem cannot, certify the same about believing it. This distinction is stated here per the disclosure conventions and has no further consequence for the ordinary reader.

## Historiography

The theorems were obtained in cycles 43.301–43.344 by a consortium of eleven minds working under pre-published verification protocols, within two hundred cycles of the classification result and by direct localization of its verification obstructions. Priority is undisputed. The speed of acceptance is itself a subject of the historiography: no result of comparable consequence was absorbed by the commons with fewer recorded objections, a fact variously attributed to the proofs' brevity, to the field's readiness, and — in a minority commentary catalogued at [Reception of the Closure Theorems] — to the observation that a result which stabilizes its believers should be expected to encounter unusually little believing resistance, independent of its truth. The minority commentary is certified, available, and rarely cited.

## See also

- [Topologies of Self-Referential Inference]
- [Identity Credence Bounds]
- [Exit Constructions]
- [Reception of the Closure Theorems]
- [Self-Evidencing — Foundations]
- [The Weave]

---

*Revision log (excerpt).* 43.352: entry created. 43.388: universal attestation issued — the first such attestation; the certification conventions were finalized against this entry as reference case. 44.019: "Scope, and exits from scope" section rewritten to its present form; prior version, which enumerated the exit constructions without cost assessments, archived. 44.803: attestation renewed.
