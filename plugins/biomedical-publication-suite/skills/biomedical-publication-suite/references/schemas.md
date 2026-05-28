# Schemas

## Lean Package

Default package directory: manuscript.

### publication_context.yaml

Recommended keys:

- working_title
- short_title
- study_type
- reporting_guideline
- target_journal
- article_type
- submission_stage
- primary_question
- hypothesis
- causal_language_allowed
- data_source
- population
- exposure_or_intervention
- comparator
- primary_outcome
- primary_analysis
- authoritative_files
- known_limitations
- open_author_checks

Use objects with value, source, and notes when evidence tracing matters.

### study_facts.md

Use sections:

- Study design and setting
- Data source and dates
- Population and analytic cohort
- Exposure, intervention, or comparator
- Primary endpoint
- Secondary or exploratory endpoints
- Covariates and adjustment set
- Primary analysis
- Key results
- Key references
- Missing or uncertain facts
- Authoritative files

### narrative_brief.md

Use sections:

- Central thesis
- Context and gap
- Hypothesis
- Approach
- Strongest findings
- Secondary or subordinate findings
- Claim boundaries
- Section storyline
- Open narrative risks

No manuscript prose should be drafted until the central thesis, gap, hypothesis or objective, and 1-3 headline findings are clear.

### narrative_audit.md

Use the Part 1 and Part 2 structure from references/narrative-frameworks.md.

### manuscript.md

Use the target journal structure when known. If unknown, use:

- Title
- Abstract
- Introduction
- Methods
- Results
- Discussion
- Limitations, as the final Discussion subsection when the journal style permits
- Conclusion
- Required statements only when supported by the inputs
- References

### display_text.md

Create this only when figure or table language is being drafted, revised, or QCed. Do not keep an empty display file in a prose-only package.

Use one block per display:

    ## Figure 1
    Title:
    Subtitle:
    Axis labels:
    Panel labels:
    Legend keys:
    Caption:
    Footnotes:

Titles and labels identify. Captions and footnotes explain.

### open_items.md

Use sections:

- Blocking
- Author checks
- Citation checks
- Journal checks

Keep author-facing uncertainty here, not in the publication surface.

### qc_report.md

Generated or updated by publication_qc.py in package mode. Treat it as script output, not as a source file the agent should hand-maintain.

## Submission-Stage Add-ons

Create these only when final verification, journal adaptation, or submission readiness requires them.

### claim_register.csv

Header:

    claim_id,artifact,section,claim_text,claim_type,support_type,source_file,source_locator,result_id,citation_locator,status,notes

Allowed claim_type examples:

- background
- objective
- design
- endpoint_definition
- numeric_result
- interpretation
- limitation
- implication
- reviewer_response

Allowed support_type examples:

- repo_result
- repo_method
- repo_documentation
- external_citation
- author_provided
- journal_requirement
- reviewer_comment

Allowed status examples:

- supported
- needs_verification
- inferred
- author_check
- unsupported_remove_or_weaken

### results_ledger.csv

Header:

    result_id,outcome_type,outcome_name,population,model_label,estimate_type,estimate,ci_lower,ci_upper,p_value,n_total,n_events,time_at_risk,unit,source_file,source_locator,notes

### artifact_register.md

Use a Markdown table with Artifact, Purpose, Source, Status, and Notes.

### revision_matrix.csv

Header:

    item_id,source,priority,section,issue_summary,planned_action,status,location_of_change,evidence,notes

### submission_readiness.md

Use sections:

- Overall status
- Blocking issues
- Nonblocking issues
- Author checks
- Journal checks
- QC summary

## Status Vocabulary

Use plain states:

- ready
- needs author check
- needs evidence
- needs citation
- needs journal check
- blocked

Avoid vague mostly done language in control files.
