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

    claim_id,artifact,section,claim_text,claim_type,support_type,source_file,source_locator,result_id,source_id,extraction_id,citation_locator,verify_status,status,notes

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

For external literature claims, use source_id to point to literature_register.csv. For extracted study details or numeric literature claims, use extraction_id to point to extraction_ledger.csv when available. verify_status should be verified before a source is used in submission-facing prose.

### results_ledger.csv

Header:

    result_id,outcome_type,outcome_name,population,model_label,estimate_type,estimate,ci_lower,ci_upper,p_value,n_total,n_events,time_at_risk,unit,source_file,source_locator,notes

## Literature Evidence Add-ons

Create these when the task involves finding papers, verifying citations, screening studies, or extracting study data. Keep the default evidence package lean; split these into separate candidate, screening, source, identifier-audit, and conflict files only for systematic-review-scale work.

### search_log.md

Use one section per search route:

    ## Search 1
    - Source:
    - Query:
    - Date:
    - Result count:
    - Notes:

### literature_register.csv

Header:

    source_id,status,screening_status,title,authors,year,journal,pmid,doi,registry_id,publication_type,source_url,discovery_source,discovery_query,verify_status,verification_source,include_decision,exclusion_reason,notes

Use status and screening_status to separate candidates from verified and included studies. Use verify_status values such as:

- unverified
- verified
- quarantine
- needs_full_text
- not_indexed

### extraction_ledger.csv

Header:

    extraction_id,source_id,field_group,field_name,field_value,unit,denominator,timepoint,comparison,source_type,source_locator,source_quote,extractor,confidence,status,notes

Use status values such as:

- verified
- partial
- not_reported
- unclear
- needs_full_text
- conflict

Every non-empty field_value should have source_id, source_locator, and source_quote when possible. Numeric study data should preserve denominator, unit, timepoint, and comparison when applicable.

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
