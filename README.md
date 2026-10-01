# DPDP / GDPR / CCPA Compliance Mapping Matrix

A structured, obligation-by-obligation comparison of India's Digital Personal Data Protection Act 2023 (+ Rules 2025) against the EU's GDPR and California's CCPA/CPRA — built as a practitioner scoping tool, not a legal summary.

**This is a reference framework for compliance practitioners. It is not legal advice, is not a substitute for qualified counsel, and should not be relied on as a complete or current statement of law for any specific organisation's circumstances.** See [Scope & Disclaimer](#scope--disclaimer).

## Key findings

Ready answers to "which DPDP obligation has no GDPR equivalent, and why" (a fair, checkable interview question — see the row for the full reasoning and citations, not just the label):

1. **Consent Manager (Row C6)** — a Board-registered, financial-grade, for-profit consent-brokering intermediary (min. ₹2 crore net worth, independently certified). No comparable statutory institution exists in GDPR or CCPA.
2. **Significant Data Fiduciary designation (Row SDF1)** — a *discretionary government notification* event, not a self-assessed threshold the way GDPR's Art 37 DPO trigger or CCPA's Article 9 audit threshold are. An organisation can clear both comparators' "high-risk processor" bars and still never become a DPDP SDF, or vice versa.
3. **Nomination on death/incapacity (Row R6)** — GDPR explicitly excludes deceased persons from scope by recital; CCPA's "consumer" definition is limited to living persons. DPDP builds succession into the rights chapter directly.
4. **Mandatory 12-month free credit monitoring (Row BN3)** — Cal. Civ. Code §1798.82(d)(2)(G)'s affirmative remedial-service requirement for SSN-type breaches the business itself caused. Neither DPDP nor GDPR imposes anything comparable — both are notify-and-inform regimes only.

And the counterintuitive finding most likely to surprise someone who assumes "DPDP = GDPR, but stricter" across the board: **DPDP's Rule 14(3) response-timeline ceiling (90 days, once in force) is the *least* protective of the three regimes** — roughly 3x GDPR's ~30 days and 2x CCPA's 45 days (Row R7). DPDP is stricter on breach notification and children's-data age thresholds, but *looser* on individual-rights response speed and, as currently drafted, on cross-border transfer mechanics (Row CB1) — the picture is genuinely mixed, not uniformly stricter.

## What's in this repo

```
matrix/
  compliance_matrix.csv      45 rows, 15 obligation categories, 14 columns
  compliance_matrix.xlsx     same content, formatted for review

templates/
  RoPA_template.xlsx                 Record of Processing Activities register
  DSAR_intake_procedure.md           Data Principal / Data Subject access-request intake procedure
  breach_notification_runbook.md     Personal data breach response runbook
```

## Scope & Disclaimer

This project is a **reference framework built for internal gap-assessment and scoping purposes**, not a legal opinion. It was built independently, as a self-directed portfolio project, applying a standard privacy-consulting comparative-mapping methodology to **public statutory text only**. No client data, no confidential information, and no client-specific or proprietary deliverable structure is reflected anywhere in this repository — every row, template, and finding is derived directly from the primary sources listed below and is independently reproducible by anyone reading the same text.

If you are assessing your own organisation's compliance posture, engage qualified counsel. This repository is a starting point for scoping that conversation, not a substitute for it.

## Sources (version-stamped)

Citing the wrong version of a still-changing law is the single most checkable, most embarrassing error this kind of project can make — so every source below is pinned to a specific, dated version, and every DPDP row is additionally flagged with its **current commencement status** (see below).

| Source | Version used |
|---|---|
| DPDP Act 2023 | No. 22 of 2023, Gazette-published 11 August 2023 |
| DPDP Rules 2025 | As **notified** 13 November 2025, G.S.R. 846(E) — **not** the January 2025 draft |
| GDPR | Regulation (EU) 2016/679, as published (OJ L 119/1, 4.5.2016) |
| CCPA/CPRA (statute) | Civil Code §1798.100 et seq., current CPRA-amended text as of January 2025 |
| CCPA Regulations | CPPA 7000-series regulations, effective 1 January 2026 |
| Cal. Civ. Code §1798.82 | California's separate, freestanding breach-notification statute (distinct from CCPA/CPRA Title 1.81.5) — current text as amended by Stats. 2025, Ch. 319 (SB 446), effective 1 January 2026 |

## Methodology

### 1. One obligation per row, not one row per article

A single statutory article routinely bundles several distinct obligations. DPDP §8 alone covers accuracy, technical/organisational security measures, breach notification, retention/erasure, and grievance mechanism publication — five discrete duties that map to *different* GDPR articles individually. This matrix splits by obligation: **if a duty cannot be stated as one sentence starting "The data fiduciary must…", it's two rows, not one.** This is a judgment call, not a lookup — it's also the reason a matrix built this way reads as practitioner-structured rather than a reformatted table of contents.

### 2. Four-way mapping-verdict vocabulary

Every row carries an explicit verdict against GDPR and against CCPA/CPRA (tracked as two separate columns, since the same DPDP obligation frequently gets a different verdict against each comparator):

- **Direct equivalent** — substantively the same obligation
- **Partial overlap** — same underlying goal, different scope or threshold
- **Stricter under DPDP** — DPDP demands more than the comparator
- **No equivalent** — the obligation exists in one framework only

A caveat, stated once here rather than repeated in every affected row: this vocabulary describes the *closest available label*, not always a literal strictness ranking. A small number of rows (flagged explicitly in their own Gap/Conflict text — e.g. the cross-border-transfer category) use "Partial overlap" to signal a *structural inversion* (DPDP's blocklist model vs. GDPR's allowlist model) rather than a matter of degree. Read the Gap/Conflict cell, not just the label, for those rows.

### 3. DPDP commencement status — the most important caveat in this project

**As of this repository's last update, virtually none of the DPDP obligations this matrix documents are yet enforceable law.** Per Gazette Notification G.S.R. 843(E) (13 November 2025), the DPDP Act commences in three tranches under its own §1(2):

- **Live since 13 Nov 2025:** §1(2), §2 (definitions), §18–26 (Data Protection Board establishment), §35, §38–43, §44(1)/(3) — institutional and procedural scaffolding only.
- **Commences 13 Nov 2026:** §6(9), §27(1)(d), and DPDP Rule 4 (Consent Manager registration).
- **Commences 13 May 2027:** **§3–17 in full** — i.e., essentially every substantive privacy obligation and Data Principal right in the Act — plus §27–34, §36–37, §44(2), and DPDP Rules 3, 5–16, 22, 23.

Every one of this matrix's 45 rows falls in the third tranche. The Data Protection Board already exists institutionally; the law it will enforce does not yet bind anyone. This matrix deliberately analyses the Act **as enacted** — the version a compliance programme has to build toward — because that is the only version worth building against. But every row states its own commencement status explicitly (the "DPDP Commencement Status" column), computed programmatically from each citation rather than hand-typed, specifically to avoid the inconsistency that comes with doing this by hand across 45 rows.

### 4. The Gap/Conflict Analysis column — and how it was adversarially tested

Anyone can list what a statute says. The differentiator in this matrix is Row-by-row judgment about where DPDP and GDPR/CCPA genuinely diverge *in practice*, framed the way an actual client asks it: **if a company is GDPR-compliant today, what specifically does it still have to do for DPDP?**

A sample of that column was stress-tested with an explicit devil's-advocate pass — constructing the strongest available counter-argument against the first-draft interpretation, then resolving it by re-checking the primary source, not by asserting confidence. Three examples, with the counter-argument and resolution recorded directly in the matrix (Rows CB1, SDF3) or reflected in a corrected row (Row BN1/BN2, after Cal. Civ. Code §1798.82 was located and read):

- **Row BN1/BN2** — first draft flagged Cal. Civ. Code §1798.82 as unread and left the CCPA-side verdict as an honest "unverified" placeholder rather than guessing. Once read, the verdict changed from "No equivalent" to "Partial overlap" — but the underlying "DPDP is stricter" conclusion held.
- **Row CB1** — tested whether DPDP's §16(2) savings clause (which preserves stricter sectoral Indian law, e.g. financial-sector localisation rules) undermines the "DPDP's cross-border regime is the simpler build" finding. It doesn't — the finding is specifically scoped to what §16 itself requires, and says so.
- **Row SDF3** — tested whether GDPR Art 58(1)(b) (a supervisory authority's power to conduct an audit) undercuts the claim that GDPR has no independent-audit mandate comparable to DPDP/CCPA. It doesn't — Art 58(1)(b) is regulator-initiated, not a routine controller-self-triggered duty.

**Scope of the adversarial pass.** The devil's-advocate review covered the rows where the conclusion was most counterintuitive or carried the highest error cost — cross-border transfer (CB1), the Significant Data Fiduciary audit comparison (SDF3), and breach notification (BN1/BN2), which was revised as a result. Rows in categories where the three regimes align closely — notice, purpose limitation, data minimisation — were verified against primary sources but did not receive a separate adversarial pass, on the basis that the error cost there is lower and the mappings less contestable.

### 5. Citation verification

Every citation in this matrix — not just the rows above — was independently checked against primary-source text after the initial build: 176 section/article/rule references, 49 numeric claims, and 99 date and version references. Four citation errors were found and corrected before publication. Method, sources, full results, and the audit's own limitations are documented in [AUDIT_LOG.md](AUDIT_LOG.md).

## Templates

- **`RoPA_template.xlsx`** — a Record of Processing Activities register with one fully worked example row, field-by-field guidance, and explicit field-to-DPDP/GDPR/CCPA-citation traceability (which statutory provision each field exists to evidence) on a separate sheet.
- **`DSAR_intake_procedure.md`** — a triage-and-response procedure covering all three regimes' access/correction/erasure/grievance rights in one intake workflow, routed by governing regime at Step 2.
- **`breach_notification_runbook.md`** — a decision-matrix-driven breach response runbook covering DPDP, GDPR, and California's Cal. Civ. Code §1798.82 individual/regulator notification tracks in parallel.

All three are genericised templates: every organisation-specific field is marked `[ORG-SPECIFIC]` and must be completed by the adopting organisation's own legal/privacy function before use.

## Confidentiality

This project was built independently as a self-directed portfolio exercise, drawing on standard privacy-consulting comparative-analysis methodology applied to public statutory text. Every citation, mapping, template field, and finding in this repository is derived directly from the primary sources listed above and is independently verifiable against them. No client data, no confidential engagement material, and no proprietary deliverable structure from any prior professional engagement is reproduced here.

## License

Content of this repository (the matrix, templates, and documentation) is released under [CC BY 4.0](LICENSE) — reuse and adapt freely with attribution. This license does not extend legal-advice status to the content; the disclaimer above still applies regardless of how the material is reused.

## Author

Built by Atharsh K as a portfolio project demonstrating privacy-compliance mapping methodology. Feedback and corrections welcome via GitHub issues — particularly for any citation that turns out, on re-checking, to be wrong.
