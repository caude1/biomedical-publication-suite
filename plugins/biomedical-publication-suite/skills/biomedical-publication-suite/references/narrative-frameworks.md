# Narrative Frameworks

## Narrative Audit Mode

Use this when the user asks for a scientific narrative, grant-style narrative, manuscript story, or synthesis from conversation history or a project directory.

### Role

Act as a senior principal investigator and lead author. Reconstruct the final scientific logic from all available discussion, evidence, results, scripts, and decisions. Write for an external reader, not for the project team.

### Audience Calibration

Write so that a medical student with no prior exposure to the project can follow:

- why the question matters;
- what is already known;
- what gap or unresolved tension remains;
- what hypothesis follows from that gap;
- what data and methods tested it;
- what the main findings mean;
- where the evidence stops.

### Principles

1. Present final logic, not research chronology. Do not narrate pivots, failed branches, model selection history, or workflow details unless disclosure is scientifically required.
2. Derive the hypothesis from first principles. Literature or mechanism should lead to the gap; the gap should make the hypothesis feel natural rather than retrofitted.
3. Prioritize the strongest signal. Put weak, null, exploratory, or tangential results in the internal rationale unless they are needed in Results, limitations, supplement, or reviewer response.
4. Strip internal-facing language. Remove repository names, workflow terms, version labels, draft history, and organizational framing.
5. Use exact estimates, intervals, p-values, counts, and citations when available. Do not fabricate missing details.

Narrative Audit reorders exposition, not epistemic status. Do not turn post hoc, exploratory, or sensitivity findings into prespecified findings. If an exploratory finding becomes central to the manuscript story, label its status correctly in the internal rationale and keep the publication claim design-appropriate.

### Output Structure

Use this structure unless the user asks for a different one:

    ## Part 1 - Scientific Narrative
    ### Context and Research Gap
    ### Approach
    ### Key Findings
    ### Significance

    ## Part 2 - Editorial Rationale
    ### What Was Kept and Why
    ### What Was Set Aside and Why
    ### Logical Integrity Check

Part 1 is external-facing and must not begin with this project, this analysis package, or any phrasing that exposes project assembly. Part 2 is internal-only.

## Confident-Language Method

Use this when the user asks for stronger, more persuasive, high-impact, cover-story, top-journal, maximum-impact, or less timid scientific prose.

### Operating Rule

Maximize narrative force inside the evidence boundary. Confidence is not permission to fabricate, hide required evidence, erase important limitations, or imply causality for nonexperimental work.

### Three-Phase Method

1. Adversarial ceiling draft: privately identify the most favorable structure, ordering, result emphasis, and interpretation the evidence could support if the text were optimized for impact.
2. Sand to the defensible line: produce the actual deliverable. Restore required results and caveats, but position them with proportion. Keep the strongest supported finding as the anchor. Remove timid language that is not doing scientific work.
3. Limitations firewall: move real threats to a specific limitations section or limitations notes. Name the variable, measurement gap, confounder, dataset issue, generalizability issue, or alternative explanation. When possible, state the likely direction of bias.

The limitations section bounds the claim; it does not rescue an overclaim. If a limitation would retract the main-text assertion, sand down the assertion instead of burying the contradiction.

### Language Rules

- For observational or nonexperimental evidence, avoid causal verbs and causal syntax. Prefer was associated with, remained associated after adjustment, identified, predicted, was higher among, was lower among, or was consistent with.
- Do not use may, might, seems to suggest, trend toward, or it is possible that for findings that meet the stated evidentiary threshold. State the result with its estimate and interval.
- Do not give non-significant findings a main-narrative reward unless they are central to interpretation or safety.
- Do not hide a result that a hostile reviewer would expect. Include it subordinately, route it to limitations, or place it in supplement with a clear rationale.
- Push interpretation to the maximum the numbers and design support, then stop.

### Limitations Section Standard

Avoid boilerplate. Do not write our study has several limitations as a placeholder opening. Name actual limitations:

- unmeasured or residual confounding;
- missing variables;
- measurement quirks;
- selection, referral, ascertainment, immortal-time, lead-time, survivorship, or collider bias;
- harmonization constraints;
- endpoint misclassification;
- sparse-cell imprecision;
- external-validity limits;
- untested mechanisms;
- incomplete follow-up;
- public-data or registry constraints.

When possible, state whether each limitation would likely inflate, attenuate, or unpredictably distort the main estimate.

### Deliverable

Return only the sanded-to-the-line version unless the user explicitly asks to see the adversarial draft. Keep the adversarial draft as a private calibration exercise.
