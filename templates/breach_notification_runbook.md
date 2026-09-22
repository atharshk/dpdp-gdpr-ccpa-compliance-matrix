# Personal Data Breach Notification Runbook

**Template status:** Genericised reference template, built from public statutory text only. Not legal advice — see [Scope & Disclaimer](#scope--disclaimer). Cross-referenced to `matrix/compliance_matrix.csv` Rows BN1–BN3, CB1–CB3.

**Version:** 1.0 — 22 September 2026. See [DPDP commencement status](#dpdp-commencement-status-read-this-first) before treating any DPDP timeline below as currently enforceable.

---

## Scope & Disclaimer

Practitioner reference template for scoping an internal breach-response process across three regimes at once. Not legal advice, not a substitute for qualified counsel, not a finished policy — complete every `[ORG-SPECIFIC]` field and have it reviewed by legal/privacy before use. Built exclusively from public statutory text (DPDP Act 2023 §8(6); DPDP Rules 2025 Rule 7; GDPR Art 33-34; Cal. Civ. Code §1798.82 — California's actual, separate breach-notification statute, distinct from CCPA/CPRA Title 1.81.5, which itself has no individual-notification duty). No confidential or client-specific content.

## DPDP Commencement Status — read this first

Per Gazette Notification G.S.R. 843(E) (13 Nov 2025), **DPDP §8(6) and Rule 7 (breach intimation) do not come into force until 13 May 2027.** Every DPDP deadline in this runbook is the target state to build toward, not a currently enforceable legal duty as of this document's build date (22 September 2026). GDPR and the California statute are unaffected and are live today.

---

## 1. Breach Definition — Three Different Triggers

| Regime | Trigger | Note |
|---|---|---|
| DPDP | §2(u): broad — covers unauthorised processing AND accidental disclosure, acquisition, sharing, use, alteration, destruction, or loss of access to personal data | Widest trigger of the three |
| GDPR | Art 4(12): "a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to" personal data | Similar breadth to DPDP |
| California (Cal. Civ. Code §1798.82(g)) | **Unauthorized ACQUISITION** specifically — a narrower trigger; good-faith employee acquisition without further misuse is expressly NOT a breach | Narrowest of the three — an incident that is a "breach" under DPDP/GDPR (e.g. data merely altered or made temporarily inaccessible, with no acquisition) may not trigger California's statute at all |

**Practical consequence:** classify every incident against all three definitions independently at triage — do not assume an incident that fails California's "acquisition" test is therefore not reportable anywhere; DPDP and GDPR's broader triggers may still apply.

## 2. Detection & Triage Workflow

```
Incident detected / suspected
      │
      ▼
Step 1: Log the incident (time of detection, source, initial description)
        — this timestamp is the trigger for every downstream clock below.
      │
      ▼
Step 2: Confirm against Section 1's three trigger definitions — which
        regime(s)' breach definition is met? (Not all three necessarily
        agree — see Section 1 note.)
      │
      ▼
Step 3: Identify affected data categories and whether they fall within
        Cal. Civ. Code §1798.82(h)'s closed "personal information" list
        (name + SSN/DL-ID/financial-account+code/medical/health-insurance/
        biometric/ALPR/genetic data, or credential-pair data) — this
        determines California-specific obligations independently of
        DPDP/GDPR scope.
      │
      ▼
Step 4: Was the affected data properly ENCRYPTED, with the encryption
        key/credential NOT also compromised?
          → If yes: California §1798.82(a)(1) and GDPR Art 34(3)(a)
            individual-notification duties may not apply.
          → DPDP has NO encryption carve-out (Row BN1) — this does
            NOT excuse DPDP individual notification once in force.
      │
      ▼
Step 5: Risk-assess severity (feeds the GDPR "high risk" gate at Art 34
        and internal severity rating — DPDP and California do not use
        a risk gate the same way, see Section 3).
      │
      ▼
Step 6: Trigger the applicable notification tracks in parallel
        (Section 3) — do not run them sequentially.
```

## 3. Notification Decision Matrix

### 3a. Individual notification

| Regime | Trigger / Threshold | Deadline | Exceptions | Matrix Row |
|---|---|---|---|---|
| DPDP | ANY breach — no risk threshold | "Without delay" — no defined outer limit in the text | **None** — no encryption or risk carve-out on the Act/Rule's face | BN1 — *not yet in force, target 13 May 2027* |
| GDPR | Only if "likely to result in a HIGH RISK to the rights and freedoms of natural persons" | "Without undue delay" | (a) data rendered unintelligible (e.g. encrypted); (b) subsequent measures neutralise the high risk; (c) disproportionate effort → substitute public communication | BN1 — live today |
| California (§1798.82(a)) | Unauthorized acquisition of unencrypted PI (or encrypted PI + compromised key), name + a listed category | **30 calendar days** from discovery (subject to law-enforcement delay) | Encryption carve-out at (a)(1) unless key also compromised | BN1 — live today |

**Verified finding:** DPDP, once in force, will be the *strictest* of the three on this specific dimension — no risk gate, no encryption carve-out, and (on the Act's plain text) no defined outer deadline at all, which if anything cuts stricter than a numbered deadline. Do not port a GDPR-style encryption/risk carve-out into the DPDP-facing workflow.

### 3b. Regulator notification

| Regime | Trigger / Threshold | Deadline | Content | Matrix Row |
|---|---|---|---|---|
| DPDP (Rule 7(2)) | ANY breach — no threshold | Two-stage: (a) immediate bare description "without delay"; (b) detailed report within **72 hours** of becoming aware | Full incident description, causes, mitigation, remedial measures, report on individual intimations given | BN2 — *not yet in force, target 13 May 2027* |
| GDPR (Art 33) | Unless breach is "unlikely to result in a risk" | **72 hours** of becoming aware, single-stage | Nature, categories/approx. numbers affected, DPO contact, likely consequences, measures taken | BN2 — live today |
| California AG (§1798.82(f)) | Only if breach affects **500+ California residents** | **15 calendar days** — but clocked from the date CONSUMER notices went out, not from discovery | Electronic submission of a PII-redacted SAMPLE COPY of the consumer notice only | BN2 — live today |

**Verified finding:** the "72 hours" figure is a genuine point of convergence between DPDP and GDPR — but DPDP's version is unconditional (no risk gate) and two-stage, while GDPR's is risk-gated and single-stage, so DPDP remains the stricter regime despite the shared headline number. California's AG-notification duty is structurally the narrowest of the three: threshold-gated, later-triggered, and lighter in content.

### 3c. California-specific: mandatory remediation service

Where a breach affecting California residents exposes SSN or driver's-licence/state-ID-type identifiers (§1798.82(h)(1)(A)-(B)) **and your organisation was the source of the breach** (not merely a downstream recipient of a notice from another entity), **Cal. Civ. Code §1798.82(d)(2)(G) mandates NOT LESS THAN 12 MONTHS of free identity-theft prevention and mitigation services** for affected residents, as a required content item of the notice itself — not a discretionary gesture. **No DPDP or GDPR equivalent exists (Row BN3).** `[ORG-SPECIFIC: name your pre-vetted identity-theft-service vendor and the activation process here, so this is not being sourced mid-incident]`.

## 4. Notice Content Checklist

- [ ] **DPDP (§8(6)/Rule 7(1)):** nature/extent/timing of breach, likely consequences to the individual, mitigation measures taken, protective steps the individual can take, business contact for queries. Concise, clear, plain language, via registered account or communication mode.
- [ ] **GDPR (Art 34(2)):** nature of the breach, DPO/contact point, likely consequences, measures taken or proposed.
- [ ] **California (§1798.82(d)(1)-(2)):** prescriptive format — titled "Notice of Data Breach," specific headings ("What Happened?" / "What Information Was Involved?" / "What We Are Doing" / "What You Can Do" / "For More Information"), 10-point minimum type, reporting entity's name/contact, list of PI types breached, date/date-range if determinable, whether delayed for law enforcement, credit-agency contact info if SSN/DL/CA-ID type data breached, and the 12-month service offer (Section 3c) if applicable.

## 5. Roles & Responsibilities

| Role | Responsibility |
|---|---|
| Incident commander | Owns the triage workflow (Section 2), coordinates all tracks |
| Legal/Privacy | Confirms regime applicability, exceptions, and final notice content |
| DPO / named contact | Board-facing (DPDP) and supervisory-authority-facing (GDPR) point of contact |
| Comms | Drafts and issues individual/public notices per Section 4's checklist |
| Security/IT | Confirms encryption status (Section 2, Step 4) and provides technical incident detail |

## 6. Post-Incident Review

Log, for every incident regardless of whether notification was ultimately required: detection time, classification against Section 1's three definitions, encryption status, decisions made at each Section 3 gate (with reasoning), and notices issued. This log is itself evidence of an active accountability programme (compliance matrix Row AC2) and the evidentiary basis if a regulator later asks why notification was or wasn't given.

## 7. Review Cadence

Review this runbook at least annually, and immediately upon: DPDP Rule 7 commencing (13 May 2027 — re-validate every "not yet in force" note against the notified text at that point); any change to California's breach statute (it has been amended before — most recently Stats. 2025, Ch. 319/SB 446 — and may be amended again); or any incident that exposes a gap in this procedure.

---

*Genericised template — part of the [DPDP / GDPR / CCPA Compliance Mapping Matrix](../README.md) project. Not legal advice.*
