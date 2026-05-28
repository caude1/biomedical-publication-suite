# Reporting and Journal Routing

## Reporting Guideline Router

| Study signal | Default guideline | Language discipline |
|---|---|---|
| randomized, placebo, allocation, treatment arm, trial | CONSORT | cautious causal language may be justified for prespecified randomized comparisons |
| cohort, case-control, cross-sectional, registry, public database, interrupted time series, difference-in-differences | STROBE | association language |
| sensitivity, specificity, ROC, AUC, index test, reference standard | STARD | diagnostic performance language |
| prognostic model, risk model, prediction, calibration, discrimination, external validation, machine learning model | TRIPOD or TRIPOD-AI | prediction performance language |
| systematic review, meta-analysis, evidence synthesis | PRISMA | evidence-synthesis and certainty language |
| preclinical, cell line, organoid, animal, biomarker discovery | domain-specific plus translational caveats | model-system language |

Tie breakers:

- Prediction papers with external validation usually route to TRIPOD/TRIPOD-AI even if observational data are used.
- Diagnostic prediction papers may need both STARD and TRIPOD logic.
- Mixed clinical/translational papers should route the main claim to the primary study design and isolate translational caveats.

## Journal Adaptation

When a target journal is provided:

1. Identify article type, word limits, abstract structure, display limits, reference style, reporting checklist expectations, data/code policy, graphical abstract expectations, highlights, and administrative statements.
2. Record unknowns in journal_requirements.md.
3. Adapt structure and voice without changing evidence.
4. Keep journal style from overriding scientific accuracy.

When journal instructions are unavailable:

- use the likely family style;
- keep unresolved details in open items;
- do not invent requirements.

## Journal Fit Memo

Use a short memo when fit is uncertain:

- target journal and article type;
- strongest fit arguments;
- likely editor/reviewer objections;
- article-length or display constraints;
- what must change before submission.
