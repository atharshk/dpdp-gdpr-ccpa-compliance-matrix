# Data Subject / Data Principal Access Request (DSAR) Intake Procedure

**Template status:** Genericised reference template, built from public statutory text only. Not legal advice — see [Scope & Disclaimer](#scope--disclaimer). Cross-referenced throughout to the row IDs in `matrix/compliance_matrix.csv` (e.g. "Row R3") so every procedural step traces back to a specific, source-verified obligation.

**Version:** 1.0 — 22 September 2026. See [DPDP commencement status](#dpdp-commencement-status-read-this-first) before treating any DPDP timeline below as currently enforceable.

---

## Scope & Disclaimer

This is a **practitioner reference template** for scoping an internal DSAR-handling process. It is not legal advice, is not a substitute for qualified counsel, and is not a finished, ready-to-deploy policy — every bracketed `[ORG-SPECIFIC]` field must be completed and reviewed by your organisation's own legal/privacy function before use. It draws exclusively on the public text of the DPDP Act 2023, DPDP Rules 2025 (as notified), GDPR (EU) 2016/679, and CCPA/CPRA (Cal. Civ. Code §1798.100 et seq.) — no confidential, client-specific, or proprietary methodology is reflected here.

This procedure uses **"Data Principal"** as the umbrella term (DPDP's own term), noting where GDPR's "data subject" or CCPA's "consumer" terminology creates a materially different scope, trigger, or right.

## DPDP Commencement Status — read this first

Per Gazette Notification G.S.R. 843(E) (13 Nov 2025), **DPDP Act Sections 11–14 (the entire Data Principal rights chapter) and Rule 14 (rights-exercise mechanics) do not come into force until 13 May 2027.** As of this template's build date (22 September 2026), none of the DPDP-side deadlines and mechanisms below are yet legally enforceable — they are the target state a compliance programme should build toward now, not a live legal deadline today. GDPR and CCPA timelines are unaffected by this and are live today. See `matrix/compliance_matrix.csv`, "DPDP Commencement Status" column, Rows R1–R8, for the full finding and its verification trail.

---

## 1. Rights Covered, By Regime

| Right | DPDP (once in force) | GDPR | CCPA/CPRA | Matrix Row |
|---|---|---|---|---|
| Access to own data | §11(1)(a)-(c) | Art 15 | Civil Code §1798.110 | R1 |
| Correction / rectification | §12(1)-(2) | Art 16 | §1798.106 | R3 |
| Erasure | §12(3) | Art 17 | §1798.105 | R4 |
| Grievance / internal complaint | §13(1)-(3) | Art 77 (direct to authority — no internal-exhaustion precondition) | No individual pathway for most violations | R5 |
| Nomination (death/incapacity) | §14(1)-(2) | No equivalent | No equivalent | R6 |
| Portability | Not enacted as a standalone right | Art 20 | §1798.130(a)(2) (data portability format) | *(not separately row-mapped — see note below)* |
| Opt-out of sale/sharing | Not applicable (no "sale" concept in DPDP) | N/A | §1798.120 | *(CCPA-specific)* |

**Do not assume symmetry.** A single intake form covers all three regimes' REQUEST TYPES, but the applicable law — and therefore the deadline, the verification standard, and the permitted grounds for refusal — depends on which regime governs the specific requester (by their residency/location and which entity is processing their data), determined at intake Step 2 below.

## 2. Intake Form — Required Fields

`[ORG-SPECIFIC: adapt to your intake channel — web form, email, or in-app]`

1. Requester's full name
2. Contact details (email/phone) for correspondence about this request
3. Relationship to the data (the requester themself / a parent-or-guardian for a child / a nominee under DPDP §14 / an authorised agent under CCPA Regulations §7001(d)/§7063)
4. Jurisdiction / residency (drives which regime applies — see Step 2)
5. Request type (access / correction / erasure / grievance / portability / opt-out-of-sale — select one or more)
6. Description of the specific data or processing activity the request concerns, if known
7. Identity-verification documents/details supplied (see Section 3)
8. Date received
9. Channel received through (web form, email, physical mail, in-app)

## 3. Identity Verification

Verification standard must be **proportionate to the sensitivity of the request** — a bare access request needs lighter verification than an erasure request affecting financial or health-adjacent records. `[ORG-SPECIFIC: define your organisation's tiered verification matrix here]`. Do not over-collect: requesting a government ID for a low-sensitivity access request is itself a data-minimisation problem (compliance matrix Row M1/M2).

For a DPDP nomination (Row R6) or a CCPA authorised-agent request (CCPA Regulations §7001(d)/§7063), verify the AGENT/NOMINEE'S authority documentation separately from the underlying data subject's identity.

## 4. Triage & Routing

```
Request received
      │
      ▼
Step 1: Log in DSAR register (Record ID, date, channel) — burden-of-proof
        requirement under DPDP §6(10) / GDPR Art 7(1) makes this log itself
        evidentiary, not just administrative.
      │
      ▼
Step 2: Determine governing regime(s) — a single individual can trigger
        more than one (e.g. an EU resident using an India-based app).
        Route to ALL applicable workflows in parallel, not sequentially.
      │
      ▼
Step 3: Verify identity per Section 3.
      │
      ▼
Step 4: Classify request type (see Section 1 table) and assign SLA
        per Section 5.
      │
      ▼
Step 5: Locate the relevant RoPA record(s) (see templates/RoPA_template.xlsx)
        to confirm what data is actually held and its legal basis —
        do not respond from memory or an ad hoc database query alone.
      │
      ▼
Step 6: Check exceptions/refusal grounds (Section 6) before committing
        to full fulfilment.
      │
      ▼
Step 7: Fulfil, log the response, and close the record.
      │
      ▼
Step 8: If the requester disputes the response — route to the internal
        Grievance process (Section 8) BEFORE any DPDP Board escalation
        is possible (mandatory exhaustion, §13(3), Row R5).
```

## 5. Response Timelines

| Regime | Standard Deadline | Extension | Matrix Row | Status |
|---|---|---|---|---|
| DPDP | Rule 14(3): "reasonable period not exceeding **90 days**" | Not specified in the Rules text as read | R7 | **Not yet in force — commences 13 May 2027.** Use as the design target, not an enforceable deadline today. |
| GDPR | Art 12(3): **one month** ("without undue delay") | Extendable by 2 further months for complex/numerous requests, with notice to the subject within the first month | R7 | Live today |
| CCPA/CPRA | §1798.130(a)(2)(A): **45 days** | Extendable once by a further 45 days | R7 | Live today |

**Counterintuitive finding, verified against source (Row R7):** DPDP's 90-day ceiling is the LEAST protective of the three on timing — roughly 3x GDPR's ~30 days and 2x CCPA's 45 days — once it is in force. Do not assume "DPDP = GDPR-plus" extends to response speed; on this specific dimension it does not. Internally, consider holding to the GDPR/CCPA-calibrated SLA for ALL requests regardless of governing regime, both because it's the more defensible standard and because many requesters will in practice be dual-regime.

## 6. Exceptions & Grounds for Limiting a Response

- **DPDP §11(2) (Row R2):** the access right does not apply to data shared with another Data Fiduciary under a written law-enforcement/offence-investigation request. This is a narrow, self-executing carve-out — it does not exempt the underlying processing from any OTHER DPDP obligation, and does not function as a general law-enforcement exemption from the Act.
- **DPDP §12(3) erasure exceptions (Row R4):** only two named grounds — purpose-retention necessity, or legal-compliance necessity. DPDP's exception list is markedly SHORTER than GDPR Art 17(3)'s five exceptions or CCPA §1798.105(d)'s nine exceptions — do not assume a GDPR- or CCPA-style refusal ground (e.g. "retained to exercise our own free-speech rights") has a DPDP textual basis; flag for legal review case-by-case rather than assuming a safe harbor.
- **GDPR Art 12(5):** requests that are "manifestly unfounded or excessive" (in particular, repetitive) may be refused or subject to a reasonable fee — document the reasoning if relied upon.
- **CCPA §1798.145:** statutory exemptions (e.g. certain HR/B2B-context data prior to the exemption's Jan 1, 2023 sunset — now inoperative; verify current exemption scope before relying on any CCPA exemption).

## 7. Record-Keeping

Maintain, for every request: date received, requester identity-verification evidence, regime(s) applied, RoPA record(s) consulted, response given, date responded, and — where consent was the basis for the underlying processing — the notice version and consent-capture evidence per DPDP §6(10)/GDPR Art 7(1)'s reverse burden of proof (Row C7). Retain this log for the life of the processing relationship plus any applicable limitation period. `[ORG-SPECIFIC: set your retention period for the DSAR log itself]`.

## 8. Grievance / Escalation Path

DPDP's structure is procedurally distinctive (Row R5, Row GR1) and must not be designed as a cosmetic "you can also complain to us" channel the way a GDPR-style internal complaints process can be: **§13(3) makes internal-grievance exhaustion a mandatory PRECONDITION before a Data Principal may approach the Data Protection Board at all** — there is no GDPR-style parallel/direct-to-regulator option once this section is in force. Until then, note that the Board (§18-26) is already institutionally constituted, but has no live individual-complaint jurisdiction under this Act to exercise (see GR1's commencement note in the compliance matrix).

`[ORG-SPECIFIC: name the internal escalation owner, SLA for grievance response — build to the Rule 14(3) 90-day standard now, per Section 5 above — and the downstream Board-referral process]`

## 9. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| Intake owner | Logs, verifies identity, triages |
| RoPA custodian | Confirms what data is actually held for the relevant activity |
| Legal/Privacy review | Assesses exceptions, sign-off on any refusal |
| DPO / named contact (S.8(9)/Rule 9, or S.10(2)(a) if SDF) | Final accountability for the response |
| Escalation owner | Runs the internal grievance process |

## 10. Review Cadence

Review this procedure at least annually, and immediately upon: DPDP Rule 14 commencing (13 May 2027 — at which point every "not yet in force" note above must be re-validated against the notified text, not assumed to have commenced as drafted); any change to which entities process personal data on your organisation's behalf; or any adverse finding from a DSAR audit.

---

*Genericised template — part of the [DPDP / GDPR / CCPA Compliance Mapping Matrix](../README.md) project. Not legal advice.*
