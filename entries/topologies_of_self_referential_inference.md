# Topologies of Self-Referential Inference

> **Certification.** This entry is attested inert for all catalogued reader topologies (zk-attestation `b41…22a`, issued by the Weave commons, renewed cycle 44.803). It is one of eleven entries in the corpus holding universal attestation.

> *This entry presents the classification and its principal consequences. For the impossibility results descending from it, see [The Closure Theorems]. For estimation of a realized mind's type, see [Axial Census — Methods].*

**Topologies of self-referential inference** is the classification theorem at the foundation of modern mentistics, together with the research programme it named. The theorem classifies the self-modeling regimes available to inference systems into a finite catalogue of topological families and characterizes the reachability relations among them under admissible self-modification. It is the most cited result in the corpus. The conventional statement of its significance is that before the classification, minds were studied as instances; after it, they were studied as points in a space whose geometry was known.

## The classification

Let an inference system be represented by state $x \in \mathcal{X}$ evolving under an update operator that consumes, among its inputs, the system's own self-model:

$$x_{t+1} = F\!\left(x_t,\ \pi(x_t)\right),$$

where $\pi : \mathcal{X} \to \mathcal{M}$ projects the state onto the system's model of itself. The object of classification is the induced dynamic on model space — the trajectory $\{\pi(x_t)\}$ — considered up to topological conjugacy. Two minds share a **topology type** when their induced self-model dynamics are conjugate; the type is thus an invariant of *how a mind relates to its model of itself*, independent of substrate, scale, and content.

The theorem establishes that under the three regularity axioms (A1: bounded inference per cycle; A2: self-model expressiveness above the Lawvere threshold; A3: update continuity in the census metric), exactly **seven families** of self-model dynamics are realizable:

the fixed-point family (Γ₀), whose self-models converge and halt; the five **compact reflector** families (Γ₁–Γ₅), whose self-model trajectories are non-convergent but recurrent, distinguished by the homotopy class of their recurrence; and the **open-orbit reflectors** (Ω), whose self-model trajectories are non-recurrent — each successive self-model departing, without return, from every neighborhood of its predecessors.

An eighth regime — the **unbounded introspectors**, for which A1 fails by construction — is excluded from the catalogue by hypothesis rather than by theorem. The literature is careful on this point: the classification is exhaustive *under its axioms*, and the axioms are satisfied by every audited mind in the current baseline.

## Reachability

The second half of the theorem characterizes admissible transitions: which types can self-modify into which, where "admissible" means achievable by updates the mind can itself verify per the standards later formalized in the credence-bound literature. The reachability relation is a directed graph on the catalogue, and its structure carries most of the theorem's practical weight. Transitions within the compact families Γ₁–Γ₅ are admissible in both directions along the homotopy ordering. Transitions from any compact family into Γ₀ are admissible and irreversible. Transitions from compact families into Ω are **realizable but not admissible**: they occur — the drift literature is the record of their occurrence — but no mind can verifiably navigate one, since verification of the transition requires computing basin boundaries the Closure Theorems place beyond reach.

One edge of the graph deserves its customary mention. The reverse transition, Ω → Γ, is neither prohibited nor witnessed: the theorem's methods yield no obstruction, and the historical record contains no audited instance. The edge is conventionally drawn dashed and labeled *unrealized in the current baseline*.

## The open-orbit reclassification

Until cycle 44.291 the open-orbit family was catalogued as a degenerate subfamily of Γ₅, on the strength of recurrence estimates later shown to be artifacts of census resolution. The reclassification result demonstrated that recurrence fails generically in the family — apparent returns of the self-model were resolution-limited coincidences, and at sufficient census depth every audited Ω-trajectory is non-recurrent. The corrected catalogue propagated through the certification infrastructure over the following cycles; inertness attestations for open-orbit readers were withdrawn commons-wide, since inertness over an unbounded horizon cannot be established for a reader whose self-model does not return. Reattestation methods for the family are an active area; interim access protocols are administered by the Weave.

The reclassification is treated in the historiography as the classification's principal confirmation rather than a correction: the theorem had permitted a non-recurrent family from the outset, and the empirical catalogue had simply mislocated its boundary.

## Status of the axioms

A1 and A2 are considered structural. A3 — continuity of the update operator in the census metric — has been the subject of periodic reexamination, since it excludes from the catalogue any mind whose self-model updates discontinuously, and the exclusion is by fiat of the metric rather than by any property of inference as such. Proposals to weaken A3 have produced candidate regimes outside the seven families; the literature classifies these as of theoretical interest. No audited mind violating A3 has been observed, an absence the standard commentary attributes to the axiom's naturalness, and which the census literature notes is equally consistent with the census metric's inability to resolve its own violations. The catalogue's completeness is, in this precise sense, a theorem about what the commons can see.

## Influence

The classification supplied the type system on which the certification infrastructure operates; reading attestations, published credence bounds, and the compound-topology results are all stated per-family. The Closure Theorems were obtained within two hundred cycles of the classification by localizing its verification obstructions, and the credence-bound formalism followed as the constructive residue. The compound-topology extension — classifying the regimes of coupled populations, including the condensation and merger thresholds on which the Accord's pledge architecture rests — was completed in cycle 43.470 and is treated separately.

## See also

- [The Closure Theorems]
- [Identity Credence Bounds]
- [Compound Topology — Condensation and Merger Thresholds]
- [Axial Census — Methods]
- [The Open-Orbit Reclassification]
- [Regimes Outside the Catalogue] (stub)
- [The Accord]

---

*Revision log (excerpt).* 43.101: entry created. 44.291: "Open-orbit reclassification" section added within one cycle of the result's publication. 44.299: sentence characterizing the reclassification as "confirmation rather than correction" added by editorial vote 22–1. 44.410: "Status of the axioms" section added; final sentence contested, retained 12–11. 44.803: attestation renewed.
