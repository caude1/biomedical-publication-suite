# Manuscript Voice

Use this reference when drafting or revising any publication-facing biomedical text. The goal is not prettier prose. The goal is external-reader authorship: a senior investigator stating what was studied, what was found, why it matters, and where the evidence stops.

## Write Like A Paper, Not A Project Memo

The manuscript is read by a stranger who knows the field and has never seen the repository, chat, analysis history, team deliberations, or draft evolution. Write every sentence for that reader.

Default voice: confident, plain, design-matched, and self-contained. Not a lab update, not an analysis rationale, not a defense brief, not a record of how the work was assembled.

Four rules carry most of the quality:

1. Forest before trees. Every section and major paragraph opens with the scientific point, then supports it. Results opens with the primary endpoint and its estimate, not setup, sensitivity analyses, or model logistics.
2. Final logic, not chronology. Reconstruct why the question, design, and findings belong together. Do not narrate the order of work.
3. Objectives from the gap, not from the analysis. The objective follows from literature or mechanism to unresolved gap to natural question. It must not read reverse-engineered from the cleanest output.
4. Confidence inside the evidence boundary. State findings at full strength with estimates and intervals. Match verbs to design. Put real threats in limitations, not in hedges scattered across the narrative.

## Memo Voice: Seven Anti-Patterns

Each anti-pattern has a signature, a memo example, and the paper fix.

### 1. Chronology Voice

Signature: first, next, then, subsequently, we then, we proceeded to.

Memo:

> We first fit an unadjusted Cox model, then added comorbidity covariates, and selected the fully adjusted model as primary.

Paper:

> In Cox models adjusted for age, sex, and comorbidity burden, [exposure] was associated with [outcome] (HR 1.4; 95% CI, 1.1-1.8).

Methods state the adjustment set once. Results report the result.

### 2. Rationale Voice

Signature: we chose, was selected because, was deemed more appropriate.

Memo:

> We used overall survival rather than progression-free survival because progression dates were less reliable in this dataset.

Paper:

> The primary endpoint was overall survival.

If the data gap is a true limitation:

> Progression dates were not uniformly available; progression-free survival was not analyzed.

### 3. Lab-Update Voice

Signature: we were able to, we successfully, this analysis demonstrates.

Memo:

> Our analysis was able to show a difference between the two groups.

Paper:

> Thirty-day mortality was lower with [intervention] (4.1% vs 7.8%; risk difference, -3.7 percentage points; 95% CI, -5.9 to -1.5).

### 4. Artifact-About-The-Artifact Voice

Signature: this figure was designed to, in this section we will, as mentioned above.

Memo:

> This figure was designed to make the subgroup effect easier to see.

Paper caption:

> Hazard ratios for [outcome] by [subgroup], fully adjusted model.

The figure shows. It does not announce its own design.

### 5. Defensive-Preempt Voice

Signature: concessive openers in abstract, introduction, or results: although limited by, it should be acknowledged, admittedly, we acknowledge that.

Memo:

> Although this association could be confounded by indication, we nonetheless observed lower mortality.

Paper:

> [Exposure] was associated with lower mortality after multivariable adjustment.

Limitations:

> Confounding by indication is possible; patients receiving [exposure] differed in baseline illness severity, which could bias the association away from the null.

### 6. Hedge-Pile Voice

Signature: may potentially, could possibly suggest, appears somewhat, seems to.

Memo:

> These data may potentially suggest a possible benefit.

Paper:

> [Exposure] was associated with [outcome].

If the mechanism is uncertain:

> This association may reflect [mechanism].

One hedge is enough, and only when it does real scientific work.

### 7. Strategy Voice

Signature: key takeaway, maximize impact, major strength of our approach, importantly, notably, clinically meaningful without a concrete implication.

Memo:

> Importantly, this is a major strength of our study.

Paper:

> The cohort included all eligible registry patients over 12 years, limiting selection by referral pattern.

## When Hedging Earns Its Place

A hedge does scientific work only when it marks genuine uncertainty the reader must calibrate.

Earns its place:

- Mechanistic interpretation in Discussion: This association may reflect earlier detection rather than slower progression.
- A design-limited inference: Whether this reflects treatment effect or residual confounding cannot be determined here.

Does not earn its place:

- Softening a measured result that met the stated evidentiary threshold.
- Reflexive qualifiers such as appears to, seems to, somewhat, relatively, and to some extent.
- Stacked hedges such as may potentially or could possibly suggest.

Rule: Results states what was found. Discussion may hedge interpretation, once per idea. Limitations names threats directly.

## Where Caveats Go

Each kind of uncertainty has one home. Anywhere else is overclaiming or self-sabotage.

| Concern | Correct Home | Wrong Home |
|---|---|---|
| Confounding, selection, measurement bias | Limitations, named with likely direction when possible | Abstract hedge, introduction caveat, results topic sentence |
| Why an analysis choice was made | Methods for the choice; editorial note for the reasoning | Results narration |
| Missing data or data quality | Methods and Limitations | Parenthetical asides in Results |
| What was tried and dropped | Editorial rationale only | Manuscript body |
| Sparse cells or suppression | Figure footnote, caption, or exact threshold | Figure title or subtitle |
| Author checks or unresolved facts | Open items | Publication-facing text |

A caveat in the main narrative bounds a claim; it does not pre-argue with a reviewer. If a caveat would retract the sentence beside it, fix the sentence.

## Spirit Before Letter

The voice rules are judgment tools, not a banned-word game. The agent's job is to read the artifact as an external editor and decide whether each sentence belongs in the paper, whether the claim is supported, and whether the wording is normal in the relevant biomedical field.

Use the QC script as a prompt for this read. Do not contort manuscript prose to dodge a warning when the flagged phrase is the right field-standard term, the correct endpoint language, or the clearest design-matched wording. Keep technically necessary language such as established risk factor, critically ill patients, pivotal trial, antibody-mediated rejection, mutational landscape, or death due to cardiovascular causes when it is literal and appropriate.

If a script flag is right, revise the prose. If the flag is wrong or overbroad, keep the prose and, for package work, record the adjudication in open_items.md. The goal is a manuscript a skeptical senior investigator would recognize as normal publication writing, not a draft optimized for a regex.

## Manuscript Voice Audit

Run this before returning any publication-facing text. Start with one uninterrupted cold read, as if reviewing the artifact for a journal. Then run the checks below and fix failures in place.

### Holistic Read

- Does the artifact read like a finished paper or publication artifact rather than a project memo?
- Can a reader unfamiliar with the repository understand the clinical problem, design, finding, and interpretation in order?
- Does each paragraph earn its place in the scientific argument?
- Is anything written for the team managing the project rather than the reader evaluating the study?
- Would avoiding a QC warning make the prose less accurate, less field-standard, or less readable?

### Forest First

- Does the abstract's first result sentence state the primary finding?
- Does Results open with the primary endpoint and its estimate?
- Does each section's first paragraph state its conclusion before support?
- Reverse-outline the draft as one sentence per paragraph. Does that list alone tell the story?

### Memo Voice

- Any sentence narrating the order of work?
- Any sentence explaining a choice to a supervisor rather than a reader?
- Any we were able to, successfully, this analysis demonstrates, or as a sanity check?
- Any sentence about the document or figure instead of the science?

### Hedging

- Every may, might, appears, seems, somewhat, and relatively: does it mark uncertainty the reader must calibrate? If not, delete or commit.
- Any stacked hedges? Reduce to one.
- Any hedged limitation? State it directly.

### Caveat Placement

- Any design threat in Introduction or a Results topic sentence?
- Any concessive opener outside Discussion or Limitations?
- Any caveat that would retract the sentence it sits beside?

### Leakage

- Any repository path, filename, tool, pipeline, team, version, package, claim register, results ledger, or QC wording?
- Any what-we-tried or analysis-history language?
- Any TODO, pending item, or author check in the publication surface?

### Labels

- Does each title state what is shown in 15 words or fewer?
- Does any title explain, defend, apologize, hedge, or carry a caveat?
- Do captions explain how to read the display, and footnotes hold thresholds?

### Citations

- Any citation group with 4 or more references?
- Any sentence with 2 or more citation groups?
- Is each claim supported by the best 1 or 2 sources rather than citation piles?

### Confidence

- Any threshold-meeting finding reported timidly? State it.
- Any verb stronger than the design supports? Match the verb to design.

## Two Voices

Publication surface: manuscript, abstract, titles, captions, legends, cover letter, reviewer responses. External senior-investigator voice. Confident, plain, design-matched, self-contained.

Control surface: narrative brief, open items, editorial rationale, QC report. Blunt internal voice. Incomplete is acceptable. Name what is missing, weak, or dropped.

Spend drafting effort in the narrative brief and manuscript. Every other file is scaffolding. Keep scaffolding short, and never let its administrative register leak into prose.
