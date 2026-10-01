#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the DPDP / GDPR / CCPA Compliance Mapping Matrix.
Columns follow the exact spec given in the project brief, with two
extra "Mapping Verdict" columns added per the architecture doc's
Layer-2 methodology, and a "DPDP Commencement Status" column computed
automatically per row (see README.md, Methodology section 3) rather
than hand-typed. Run from the scripts/ directory: `python3 build_matrix.py`
regenerates ../matrix/compliance_matrix.csv and .xlsx in place.
"""
import pandas as pd

COLUMNS = [
    "Row ID",
    "Obligation Category",
    "Status",
    "DPDP Article/Rule",
    "DPDP Commencement Status (as of 22 Sep 2026)",
    "DPDP Requirement (plain English)",
    "GDPR Equivalent Article",
    "GDPR Requirement",
    "CCPA/CPRA Equivalent (Civil Code §)",
    "Mapping Verdict vs GDPR",
    "Mapping Verdict vs CCPA/CPRA",
    "Compliance Mechanism",
    "Gap / Conflict Analysis",
    "Common Implementation Pitfall",
]

rows = []

def add(row_id, cat, status, dpdp_cite, dpdp_req, gdpr_cite, gdpr_req, ccpa_cite,
        v_gdpr, v_ccpa, mechanism, gap, pitfall):
    # Commencement Status is NOT passed in here -- it is computed
    # automatically from dpdp_cite by commencement_status() in the
    # post-processing pass below, with a small manual-override table
    # for rows whose citation spans provisions in more than one
    # commencement tranche. This keeps the 44 add() calls above from
    # needing a 14th positional argument, and keeps the tranche logic
    # in exactly one place rather than re-typed 44 times.
    rows.append([row_id, cat, status, dpdp_cite, dpdp_req, gdpr_cite, gdpr_req, ccpa_cite,
                 v_gdpr, v_ccpa, mechanism, gap, pitfall])

# ============================================================
# SKELETON — placeholder rows for the 12 categories NOT built this
# session, so the full 15-category architecture is visible from Session 1.
# ============================================================
# (Session 1 skeleton removed in Session 2 — all 15 categories are now
# either COMPLETE or explicitly marked with a Session-2-specific caveat
# in their own text; see SESSION_2_NOTES.md for what remains genuinely
# open, e.g. GDPR Art 51-76 institutional/EDPB detail was skimmed for
# context but not cited as a row comparator anywhere below.)

# ============================================================
# CATEGORY 3 — CONSENT (COMPLETED)
# ============================================================
CAT = "3. Consent (incl. withdrawal, Consent Manager)"

add("C1", CAT, "COMPLETE — Session 1",
    "Section 4(1)(a), read with Section 6(1)",
    "The data fiduciary must process personal data on the basis of the data principal's consent as one of only two lawful grounds for processing (the other being the enumerated 'certain legitimate uses' under Section 7); consent is the default/residual basis for any processing not falling within Section 7.",
    "Article 6(1)(a), read with Article 6(1) generally",
    "Consent is one of six independent lawful bases for processing (Art 6(1)(a)-(f)) -- alongside contract necessity, legal obligation, vital interests, public task, and legitimate interests; controllers may choose whichever basis fits without consent being privileged over the others.",
    "None directly -- Civil Code Section 1798.100(a)-(c) (general duties/notice at collection); CCPA has no lawful-basis gate at all",
    "Partial overlap",
    "No equivalent",
    "Data Fiduciary must run a two-track processing-basis assessment for every activity: (i) does it fall within one of the nine closed S.7 'certain legitimate uses' categories? If not, (ii) valid Section-6 consent is mandatory before processing begins.",
    "DPDP's architecture is binary and closed -- consent or one of nine enumerated S.7 uses -- with no open-ended 'legitimate interests' balancing test comparable to GDPR Art 6(1)(f). A company relying today on GDPR's legitimate-interests basis (fraud prevention, network security, B2B marketing) cannot assume that basis survives under DPDP; it must re-test against the narrower closed list, and if none of the nine S.7 categories fit, obtain fresh Section-6 consent. This is the single biggest architectural gap in the Consent category: GDPR-compliant does not equal DPDP-compliant here. CCPA doesn't gate processing on a lawful basis at all -- a CCPA-compliant company may be collecting/using data today with zero consent step (only a notice-at-collection duty), so DPDP consent is a net-new operational requirement, not a mapping exercise.",
    "Assuming that because a data flow is justified under GDPR's legitimate-interests basis, it is automatically fine under DPDP -- many 'legitimate interest' use cases (analytics, internal research, security beyond what S.7(i) covers) have no DPDP-legitimate-use equivalent and silently require a consent retrofit.")

add("C2", CAT, "COMPLETE — Session 1",
    "Section 5(1), read with DPDP Rules 2025, Rule 3(a)-(c)",
    "Before or together with every consent request, the Data Fiduciary must give the Data Principal a notice describing (i) the personal data to be processed and the purpose, (ii) how to exercise withdrawal/rights under S.6(4) and S.13, and (iii) how to complain to the Board; Rule 3 further requires the notice to be presented independently of other information, in clear/plain language, itemising the personal data and specific purpose, with a functioning communication link for exercising those options.",
    "Article 13(1)-(2)",
    "Where data is collected from the data subject, the controller must give, at collection, a longer fixed list of disclosures: identity/contact of controller and DPO, purposes AND legal basis, legitimate interests relied on, recipients, international-transfer details, retention period/criteria, existence of rights (access, rectification, erasure, restriction, portability, objection), right to withdraw consent, right to complain to a supervisory authority, whether provision is a statutory/contractual requirement, and existence of automated decision-making.",
    "Civil Code Section 1798.100(a) (Notice at Collection) + CCPA Regulations Section 7012",
    "Partial overlap",
    "Partial overlap",
    "Build a layered notice: a short, itemised, stand-alone consent-request notice (S.5/Rule 3, satisfies DPDP) nested inside or linked from a longer GDPR Art 13 / CCPA Notice-at-Collection privacy notice, since the DPDP notice is deliberately minimal and the GDPR/CCPA notices are deliberately exhaustive.",
    "DPDP's notice is structurally thinner than GDPR's -- it does not require disclosure of legal basis, retention period, recipients, cross-border transfer safeguards, or DPO identity in the same notice. A GDPR Art 13 notice over-satisfies DPDP's content requirements in substance but will NOT automatically satisfy Rule 3(a)'s formal requirement that the notice be 'presented and be understandable independently of any other information' -- a long, bundled GDPR-style privacy policy fails this independence test unless the DPDP-required elements are carved into a distinct, standalone surface at the point of consent capture. CCPA's Notice at Collection (1798.100(a)) is closer in spirit (itemised categories + purposes + retention) but is a disclosure obligation independent of any consent step, since CCPA doesn't gate collection on consent.",
    "Reusing an existing GDPR Art 13 long-form privacy notice as the DPDP consent notice without extracting it into a separate, self-contained surface -- this satisfies content but fails Rule 3(a)'s standalone-presentation requirement, a formal (not merely substantive) defect examiners can flag on inspection.")

add("C3", CAT, "COMPLETE — Session 1",
    "Section 6(1)",
    "Consent must be free, specific, informed, unconditional and unambiguous, given through clear affirmative action, and must signify agreement to processing limited to the personal data necessary for the specified purpose.",
    "Article 4(11) (definition) + Article 7(4)",
    "'Consent' means any freely given, specific, informed and unambiguous indication of wishes by a clear affirmative action; Art 7(4) directs that, in assessing whether consent is 'freely given', utmost account be taken of whether contract performance was made conditional on consent to processing not necessary for that contract (the conditionality test).",
    "CCPA Regulations Section 7004 -- 'symmetry in choice', dark-pattern prohibition, no consent via silence/inaction",
    "Direct equivalent",
    "Partial overlap",
    "Consent-capture UX must independently satisfy: DPDP's 'unconditional' test (no forced bundling of unrelated purposes/services), GDPR's Art 7(4) conditionality test (near-identical in effect), and, where CCPA opt-in flows exist (minors, financial incentives, re-opt-in after opt-out), CCPA's symmetry-of-choice and anti-dark-pattern rules (Reg. Section 7004).",
    "DPDP's five-adjective consent standard (free, specific, informed, unconditional, unambiguous) is close enough to GDPR's four-part definition that a genuinely GDPR-Art.7-compliant consent flow will very likely also satisfy DPDP S.6(1) -- one of the few rows where 'GDPR-compliant today' is a reasonably strong starting point for DPDP, not a false-confidence trap. The CCPA angle differs in kind: Reg. Section 7004's dark-pattern/symmetry rules apply narrowly to the specific opt-in/opt-out choices CCPA actually mandates (sale/sharing opt-out, minors' opt-in, financial-incentive opt-in) -- CCPA has no general 'consent as gateway to all processing' concept for Section 7004 to attach to broadly, so the overlap is real but structurally narrower in scope.",
    "Treating 'consent' as satisfied by a single global accept-all toggle bundling multiple, unrelated processing purposes into one click -- this fails DPDP's 'specific' and 'unconditional' limbs (illustrated in the Act's own worked example at S.6, Illustration to sub-section (1): consent for telemedicine services does not extend to contact-list access) exactly as it would fail GDPR Art 7(4) bundling and CCPA's anti-bundling rule (Reg. Section 7004(a)(4)(B)-(C)).")

add("C4", CAT, "COMPLETE — Session 1",
    "Section 6(2)",
    "Any part of a consent that constitutes an infringement of the Act, the Rules, or any other law is invalid to the extent of that infringement (severability) -- the rest of the consent remains valid.",
    "Article 7(2), second sentence",
    "Any part of a written declaration which constitutes an infringement of the Regulation shall not be binding -- closely mirrors DPDP's severability rule.",
    "None specific -- closest is the general rule that any agreement obtained through dark patterns shall not constitute consumer consent (CCPA Regulations Section 7004(b))",
    "Direct equivalent",
    "No equivalent",
    "Draft consent clauses as severable, independently-assessable units (not a single omnibus clause) so an invalid sub-clause (e.g. an unlawful liability waiver bundled into consent, per the Act's own Illustration at S.6(2)) doesn't void the entire consent.",
    "A rare case of near-verbatim structural convergence between DPDP and GDPR -- both severability rules exist to stop fiduciaries/controllers using consent as a vehicle to smuggle in unlawful terms (e.g. rights waivers). CCPA has no direct analogue because CCPA consent is not a general processing gateway with attached 'terms' the way DPDP/GDPR consent is -- CCPA's closest cousin is the dark-pattern voidance rule, which invalidates the whole consent event rather than severing an offending clause from an otherwise-valid one.",
    "Assuming a single defective term (e.g. an unlawful grievance-waiver clause bundled into a consent form) invalidates the entire consent and requires re-consent from every user -- DPDP S.6(2), like GDPR Art 7(2), only voids the offending part, not the whole; over-correcting into a full re-consent campaign is unnecessary operational cost.")

add("C5", CAT, "COMPLETE — Session 1",
    "Section 6(4)-(5)",
    "Where consent is the basis of processing, the Data Principal has the right to withdraw consent at any time, and the ease of withdrawal must be comparable to the ease with which consent was given; the consequences of withdrawal are borne by the Data Principal, and withdrawal does not affect the lawfulness of prior processing.",
    "Article 7(3)",
    "The data subject has the right to withdraw consent at any time; withdrawal must be as easy as giving consent; withdrawal does not affect the lawfulness of processing based on consent before its withdrawal; the data subject must be informed of the right to withdraw before giving consent.",
    "Civil Code Section 1798.120(a) (opt-out of sale/sharing 'at any time') + CCPA Regulations Section 7004(a)(2) (symmetry in choice)",
    "Direct equivalent",
    "Partial overlap",
    "Build symmetric consent/withdrawal UX -- same number of steps and comparable friction in both directions -- and log the pre-withdrawal processing period separately, since it stays lawful.",
    "The 'ease of withdrawal comparable to ease of giving' standard is functionally identical to GDPR Art 7(3) and to CCPA's regulatory symmetry-of-choice principle -- a genuine convergence point across all three regimes and a strong candidate for a single shared engineering control. The partial-overlap flag against CCPA exists only because CCPA frames the underlying right differently: it is an opt-out of sale/sharing (a specific commercial act), not a general withdrawal of a blanket processing consent, so the CCPA right is narrower in scope even though the ease-of-exercise standard converges.",
    "Making withdrawal technically possible but operationally harder than consent (e.g. consent via a single in-app toggle, withdrawal requiring an emailed request processed manually within days) -- this is the most common real-world violation the Act's 'comparable ease' language is specifically drafted to catch, and is trivially detectable on a UX audit.")

add("C6", CAT, "COMPLETE — Session 1",
    "Section 6(7)-(9), read with DPDP Rules 2025 Rule 4 and First Schedule",
    "A Data Principal may give, manage, review or withdraw consent through a Consent Manager -- a Board-registered intermediary (minimum Rs. 2 crore net worth, interoperable platform, independently certified per First Schedule Part A) that must act accountably on the Data Principal's behalf; every Consent Manager must be registered with the Board under prescribed conditions (First Schedule Part B obligations).",
    "None -- closest analogues are the non-binding 'consent management platform' (CMP) industry practice and Article 80 (representation of data subjects by not-for-profit bodies, which concerns complaint/redress representation, not consent brokering)",
    "N/A -- no statutory Consent Manager concept exists in the GDPR text; consent must be given directly to (or via a processor acting for) the controller.",
    "Civil Code Section 1798.135(a)(3) (Alternative Opt-out Link) / opt-out preference signals (Section 1798.135(b), CCPA Regulations Section 7025) -- closer in function to a technical signal than a licensed intermediary",
    "No equivalent",
    "No equivalent",
    "Data Fiduciaries above a certain scale should evaluate onboarding to a Board-registered Consent Manager platform once Rule 4 is in force (commencement: one year after the Rules' Gazette notification of 13 November 2025, i.e. on/around 13 November 2026) rather than building a bespoke consent-capture stack, since DPDP treats the Consent Manager as the principal-facing interoperability layer.",
    "One of DPDP's genuinely novel, India-specific institutions -- a textbook 'no equivalent' row -- no other major privacy regime licenses a for-profit consent-brokering intermediary as a statutory feature. GDPR's/CCPA's opt-out preference signals (e.g. Global Privacy Control) are technical, browser-level signals with no registration, net-worth, or certification regime attached; DPDP's Consent Manager is a regulated, financial-grade intermediary business. COMMENCEMENT CAVEAT (material): per the Rules' staggered-commencement schedule at Rule 1(3), Rule 4 (Consent Manager registration/obligations) only comes into force one year after the 13 November 2025 Gazette notification -- so this obligation, while law, has no live registrants or enforceable deadline yet as of this matrix's build date (22 Sept 2026, i.e. still ~7 weeks before Rule 4 itself commences). Any 'already compliant' claim about Consent Manager integration today is premature by definition.",
    "Treating an off-the-shelf CMP (built for GDPR/IAB TCF cookie-consent signalling) as DPDP Consent-Manager-compliant -- a CMP is not a Board-registered entity, has no Rs. 2 crore net-worth threshold, and is not certified against Board-published interoperability standards; the two categories look similar (both manage consent state) but are legally distinct, and DPDP's is a licensed, third-party accountable intermediary.")

add("C7", CAT, "COMPLETE — Session 1",
    "Section 6(10)",
    "Where consent is the basis of processing and a dispute arises, the Data Fiduciary bears the burden of proving that notice was given and valid consent was obtained in accordance with the Act and Rules.",
    "Article 7(1)",
    "Where processing is based on consent, the controller shall be able to demonstrate that the data subject has consented to processing of his or her personal data -- an equivalent reverse burden of proof on the controller.",
    "None explicit for a general burden-of-proof rule; closest is the business record-keeping duty under CCPA Regulations Section 7101 and the general compliance-demonstration posture the regulations impose",
    "Direct equivalent",
    "No equivalent",
    "Maintain immutable, timestamped consent logs (notice version shown, purpose, data categories, IP/device context, consent-capture mechanism) retrievable for the life of the processing relationship plus any applicable limitation period.",
    "Both DPDP and GDPR place the evidentiary burden squarely on the data controller/fiduciary, a deliberate consumer-protection design choice in both regimes that converges cleanly. CCPA doesn't need an equivalent provision in the same place because CCPA's default posture isn't consent-gated -- the burden question there arises differently, around verifying identity for a request (CCPA Regulations Article 5), not around proving a prior consent event.",
    "Relying on a third-party Consent Manager's records as sufficient proof without also retaining an independent, exportable copy -- S.6(10) puts the burden on the Data Fiduciary, not the Consent Manager, so if the Consent Manager's records become unavailable (platform shutdown, dispute, deregistration under Rule 4(5)) the Fiduciary is still on the hook and needs its own evidentiary trail.")

# ============================================================
# CATEGORY 4 — PURPOSE LIMITATION (COMPLETED)
# ============================================================
CAT = "4. Purpose limitation"

add("P1", CAT, "COMPLETE — Session 1",
    "Section 4(1)(a) read with Section 5(1)(i) and DPDP Rules 2025 Rule 3(b)(i)-(ii)",
    "The Data Fiduciary must specify the purpose of processing to the Data Principal in the pre-consent notice, itemising the personal data and giving a specific description of the purpose/goods/services involved, before or together with the consent request.",
    "Article 5(1)(b), first limb ('collected for specified, explicit and legitimate purposes')",
    "Personal data shall be collected for specified, explicit and legitimate purposes -- a freestanding processing principle (Art 5) that applies to a controller regardless of which of the six Art 6 lawful bases is used, and is independently enforceable outside the consent context.",
    "Civil Code Section 1798.100(a)(1)-(2) (Notice at Collection: categories + purposes)",
    "Partial overlap",
    "Partial overlap",
    "Maintain a single processing-purpose register per data category that feeds the DPDP notice, the GDPR Art 30 record of processing, and the CCPA Notice-at-Collection simultaneously, since all three demand purpose specification but at different levels of formality.",
    "The functional requirement (tell people why you're collecting their data, specifically) converges across all three laws, but DPDP embeds this obligation inside the consent-notice mechanism (S.5) rather than as GDPR's freestanding Article 5 principle binding a controller irrespective of legal basis. Practical effect: under GDPR, purpose specification is independently auditable/enforceable even for non-consent processing; under DPDP, because there are only two processing gateways (consent or S.7 'certain legitimate uses', each already purpose-bound by its own wording), there is no separate freestanding 'Art 5(1)(b)-style' purpose-limitation clause to violate independently of the gateway itself. A structural difference worth flagging even though the practical outcome looks similar.",
    "Copying a GDPR Art 13(1)(c) 'purposes of the processing' disclosure verbatim into a DPDP consent notice without itemising the personal data alongside each purpose -- Rule 3(b)(i)-(ii) requires an itemised description of the personal data AND the specific purpose/goods-or-services together, more granular than GDPR's purposes-listed-separately-from-categories approach.")

add("P2", CAT, "COMPLETE — Session 1",
    "Section 6(1), second limb ('for the specified purpose')",
    "Consent-based processing is lawful only for the specified purpose to which the Data Principal consented; DPDP has no mechanism authorising a Data Fiduciary to repurpose consent-based data for a new, merely 'compatible', purpose without obtaining fresh notice and consent for that new purpose.",
    "Article 5(1)(b), second limb + Article 6(4) (compatibility test)",
    "Data shall not be further processed in a manner incompatible with the original purposes; Article 6(4) provides a multi-factor compatibility test for further processing on bases OTHER than consent, but explicitly does not create a compatibility escape hatch for consent-based processing -- new purposes still require fresh consent under GDPR too when the original basis was consent.",
    "Civil Code Section 1798.100(a)(1) (new Notice at Collection required for additional incompatible purposes) + CCPA Regulations Section 7002(c) (compatibility factors)",
    "Direct equivalent",
    "Partial overlap",
    "Build a purpose-change trigger into the consent-management system: any new use case against previously-collected, consent-based data must be blocked pending a fresh Rule-3-compliant notice and Section-6 consent capture, mirroring the gate GDPR applies to consent-based processing.",
    "A case where a common assumption (that GDPR gives more repurposing flexibility than DPDP) is simply wrong for the consent scenario: GDPR's Art 6(4) compatibility test is expressly disapplied where the original basis was consent, so GDPR and DPDP converge here -- both require fresh consent for a new purpose. They diverge for DPDP's S.7 non-consent bases, which have no compatibility-test equivalent at all (each S.7 category is a closed, purpose-specific carve-out, not a general lawful basis with a compatibility escape valve the way GDPR's Art 6(1)(b)-(f) bases have via Art 6(4)). CCPA's 1798.100(a)(1) requires new notice for 'incompatible' additional purposes but, consistent with its non-consent-gated model, requires only updated disclosure, not an opt-in consent event -- so the remedy differs (notice vs. notice+consent) even where the underlying 'don't silently repurpose' principle overlaps.",
    "Assuming that because GDPR permits further processing for 'compatible' purposes under certain non-consent bases, the same latitude exists under DPDP for consent-based data -- DPDP has no compatibility test at all; any purpose not literally covered by the original specified purpose requires a fresh consent cycle, full stop.")

add("P3", CAT, "COMPLETE — Session 1",
    "Section 6(1), third limb ('limited to such personal data as is necessary for such specified purpose')",
    "The personal data collected/processed under a consent must be limited to what is necessary for the specified purpose -- DPDP fuses the data-minimisation test directly into the definition of valid consent, rather than stating it as an independent principle (contrast the separate 'Data minimisation' category, to be built in Session 2).",
    "Article 5(1)(c) ('data minimisation' -- a separate principle from Art 5(1)(b) purpose limitation)",
    "Personal data shall be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed -- a standalone Article 5 principle, textually and conceptually distinct from purpose limitation (5(1)(b)), applicable to all lawful bases.",
    "Civil Code Section 1798.100(c) ('reasonably necessary and proportionate')",
    "Stricter under DPDP",
    "Partial overlap",
    "Cross-reference this row when Session 2 builds the standalone 'Data minimisation' category -- a minimisation failure under DPDP is not merely a housekeeping gap, it can invalidate the consent itself (triggering S.6(2) severability / S.4 lawful-basis failure), a materially higher-stakes consequence than GDPR's Art 5(1)(c) minimisation breach (typically a standalone Art 83 fining ground, not a basis-invalidating defect).",
    "The row that most rewards close reading rather than assumption. GDPR treats purpose limitation (5(1)(b)) and data minimisation (5(1)(c)) as two separate principles that can be breached independently -- over-collecting for a valid purpose is a minimisation violation, not automatically a purpose-limitation or consent-validity problem. DPDP collapses both into a single sentence defining what 'consent' even means (S.6(1)): data 'limited to such personal data as is necessary for such specified purpose' is baked into the definition of valid consent itself. Practical consequence: over-collection under DPDP isn't just a separate violation to remediate -- it can taint the underlying consent's validity, with knock-on effects for S.4 lawful-basis-failure. Arguably a stricter, higher-stakes framing than GDPR's, even though the substantive 'collect only what you need' test is similar.",
    "Treating over-collection as a low-severity 'we'll fix data minimisation later' backlog item, the way many GDPR compliance programs triage Art 5(1)(c) findings -- under DPDP the same over-collection can be read as invalidating the consent basis itself, a Section 4 lawful-processing failure, not a lower-tier housekeeping issue.")

add("P4", CAT, "COMPLETE — Session 1",
    "Section 7 (chapeau + clauses (a)-(i))",
    "Where processing does not rely on consent, it must fall within one of nine enumerated 'certain legitimate uses', each narrowly purpose-defined by its own statutory wording: voluntary data disclosure with no expressed refusal (7(a)); State subsidy/benefit administration (7(b)); sovereign functions (7(c)); legal-disclosure compliance (7(d)); judgments/orders (7(e)); medical emergencies (7(f)); public health/epidemic response (7(g)); disaster response (7(h)); employment-related safeguarding of the employer (7(i)). There is no open-ended, discretionary non-consent basis.",
    "Article 6(1)(b)-(f)",
    "Five additional lawful bases beyond consent -- contract necessity, legal obligation, vital interests, public task, and legitimate interests pursued by the controller (Art 6(1)(f), subject to a balancing test against the data subject's rights and freedoms) -- of which legitimate interests in particular is an open-textured, balancing-test basis rather than a closed enumerated list.",
    "None directly -- CCPA does not use a lawful-basis gate; closest functional cousin is the 'business purpose' list at Civil Code Section 1798.140(e)(1)-(8), which defines permitted uses for data disclosed to service providers/contractors",
    "Partial overlap",
    "No equivalent",
    "For every non-consent processing activity, map it against the nine S.7 categories individually and document which specific clause and sub-fact pattern applies -- a generic 'legitimate interest' justification (GDPR-style) is not a valid DPDP defense on its own.",
    "The clearest illustration of this gap: a company relying on GDPR Art 6(1)(f) 'legitimate interests' for, say, internal fraud analytics, network security hardening, or first-party marketing to existing customers has no automatic DPDP home for that processing -- none of the nine S.7 categories is a general-purpose legitimate-interests basis, and S.7(i)'s employment carve-out is narrowly about safeguarding the employer from loss/liability (trade secrets, corporate espionage, IP, confidentiality), not a general employment-processing basis. This is precisely the kind of 'GDPR-compliant today, DPDP-gap tomorrow' finding Attack 1's defense depends on, and it is judgment-intensive -- two lawyers could reasonably disagree whether a specific fraud-analytics use case survives under S.7(i)'s language, which is the kind of honest, checkable boundary this matrix should carry into the README's Known Limitations rather than paper over.",
    "Porting a GDPR Legitimate Interests Assessment (LIA) directly into a DPDP compliance file as if it were transferable evidence of a lawful basis -- an LIA is irrelevant under DPDP unless the underlying activity also happens to fall within one of the nine closed S.7 categories; if it doesn't, the LIA proves nothing and consent is the only remaining lawful path.")

# ============================================================
# CATEGORY 10 — DATA PRINCIPAL / DATA SUBJECT RIGHTS (COMPLETED)
# ============================================================
CAT = "10. Data principal / data subject rights"

add("R1", CAT, "COMPLETE — Session 1",
    "Section 11(1)(a)-(c)",
    "A Data Principal who has given consent has the right to obtain from the Data Fiduciary: (a) a summary of personal data being processed and the processing activities undertaken; (b) the identities of all other Data Fiduciaries and Data Processors with whom the personal data has been shared, with a description of the data shared; and (c) any other prescribed information.",
    "Article 15(1)(a)-(h)",
    "Right of access: confirmation of processing, plus a substantially longer fixed list -- purposes, categories of data, recipients, envisaged storage period, existence of rectification/erasure/restriction/objection rights, right to complain to a supervisory authority, source of data (if not collected from the subject), and existence of automated decision-making/profiling with meaningful logic information.",
    "Civil Code Section 1798.110 (Right to Know / access) + Section 1798.115 (Right to Know sold/shared)",
    "Partial overlap",
    "Partial overlap",
    "Build a single subject-access-request (SAR) fulfilment pipeline that outputs the GDPR/CCPA superset of disclosures, which will always satisfy DPDP's narrower list as a strict subset, rather than three separate SAR templates.",
    "DPDP's access right is deliberately thinner than GDPR's -- it does not explicitly guarantee disclosure of retention periods, the legal basis relied upon, or the existence of automated decision-making/profiling logic as freestanding access-right line items the way Art 15(1)(d),(h) do; those appear (if at all) elsewhere in the Act as fiduciary-side obligations, not principal-facing access-right entitlements. CCPA's right to know is itself split into two separate statutory rights (1798.110 general categories/specific-pieces access, 1798.115 sold/shared/disclosed-to-whom) rather than DPDP's single consolidated S.11 right -- a company satisfying CCPA's two-track disclosure will substantively over-satisfy DPDP's single-track S.11(1)(a)-(b), but the reverse is not automatically true.",
    "Building the DPDP access-response template as a literal, narrow reading of S.11(1)(a)-(c) only, then discovering under audit or Rule-14 grievance escalation that data principals expect a fuller GDPR-style response -- under-delivering relative to rising user expectations is a reputational risk even where it is technically S.11-compliant.")

add("R2", CAT, "COMPLETE — Session 1",
    "Section 11(2)",
    "The access right under S.11(1)(b)-(c) does NOT apply to sharing of personal data by the Data Fiduciary with another Data Fiduciary pursuant to a written request made for the purpose of prevention, detection, investigation or prosecution of offences or cyber incidents, or for prosecution/punishment of offences.",
    "Article 23(1)(d) (restrictions ground: prevention/investigation/prosecution of criminal offences)",
    "Member State or Union law MAY restrict the scope of Art 15 access rights (among others) where necessary and proportionate to safeguard the prevention, investigation, detection or prosecution of criminal offences -- a Member-State legislative option, not a self-executing statutory carve-out written directly into the Regulation's rights chapter the way DPDP writes it directly into Section 11 itself.",
    "None directly comparable at the individual-right level -- closest is the broad statutory exemptions list at Civil Code Section 1798.145 (not law-enforcement-request-specific in this form)",
    "Partial overlap",
    "No equivalent",
    "Maintain a documented log of law-enforcement/offence-related data-sharing requests invoking S.11(2), including the requesting fiduciary's written request, so the carve-out can be defended if a Data Principal disputes an incomplete S.11(1) response.",
    "DPDP writes this restriction directly into the primary statute as a self-executing carve-out -- no further domestic legislation is needed to activate it, unlike GDPR Art 23 which requires a Member State (or Union) legislative act to actually restrict any given right; the GDPR restriction is a framework provision, not an automatically-operative rule. The DPDP carve-out is immediately available to any Data Fiduciary today, whereas an EU controller cannot invoke Art 23 restrictions without pointing to a specific national implementing law.",
    "Over-reading S.11(2) as a general law-enforcement exemption from the whole Act (it is not) -- it only narrows the specific S.11(1)(b)-(c) access-right disclosure regarding data shared under a qualifying written request; it does not exempt the underlying processing from any other DPDP obligation (security, breach notification, retention, etc.).")

add("R3", CAT, "COMPLETE — Session 1",
    "Section 12(1)-(2)",
    "A Data Principal who has given consent has the right to correction, completion, updating and erasure of her personal data; on receiving such a request the Data Fiduciary must correct inaccurate/misleading data, complete incomplete data, and update the data.",
    "Article 16",
    "Right to rectification: the data subject has the right to obtain rectification of inaccurate personal data without undue delay, and to have incomplete data completed, including by means of a supplementary statement -- near-identical in substance to DPDP S.12(1)-(2).",
    "Civil Code Section 1798.106 (Right to Correct)",
    "Direct equivalent",
    "Direct equivalent",
    "A single correction-request workflow (verify identity -> assess accuracy -> correct/complete/update -> notify downstream processors/third parties) satisfies all three regimes' correction rights with no material re-engineering required between them.",
    "A genuine three-way convergence row, useful in the matrix precisely because it shows the mapping exercise isn't always about finding gaps -- sometimes the honest finding is 'these three regimes agree.' The only textual nuance: DPDP's timing standard for correction is unspecified in the Act itself (contrast GDPR's explicit 'without undue delay'), with the actual response-time obligation instead surfacing at the Rule level (Rule 14(3): 'reasonable period not exceeding ninety days' for grievance-system responses generally) -- so the effective DPDP SLA is materially longer than GDPR's 'without undue delay' norm (commonly operationalised as ~30 days under Art 12(3) for the broader Art 15-22 rights) and CCPA's fixed 45-day response window (1798.130(a)(2)(A)).",
    "Assuming DPDP's correction-right timeline matches GDPR's ~30-day or CCPA's 45-day SLA -- Rule 14(3)'s up-to-90-day grievance-response ceiling is the operative DPDP timing anchor (once Rule 14 is in force), and building a 30- or 45-day internal SLA isn't wrong, but claiming it as a DPDP-mandated deadline overstates what the text actually requires.")

add("R4", CAT, "COMPLETE — Session 1",
    "Section 12(3)",
    "A Data Principal may request erasure of her personal data, in the prescribed manner, and upon receipt of such a request the Data Fiduciary shall erase the data unless retention is necessary for the specified purpose or for compliance with applicable law.",
    "Article 17(1)-(3) ('right to be forgotten')",
    "Right to erasure applies where data is no longer necessary for its original purpose, consent is withdrawn (with no other legal ground), the data subject objects and no overriding legitimate grounds exist, data was unlawfully processed, erasure is required by law, or the data was collected in relation to a child's consent to information-society services -- subject to detailed exceptions (freedom of expression, legal compliance, public-interest archiving/research, legal claims).",
    "Civil Code Section 1798.105 (Right to Delete)",
    "Partial overlap",
    "Partial overlap",
    "Build a single deletion-request pipeline whose exception logic is configured to the broadest applicable exception set across all three regimes (DPDP's two grounds, GDPR's five sub-grounds and named Art 17(3) exceptions, and CCPA's Section 1798.105(d) nine-item exception list), flagged per jurisdiction of the requester.",
    "DPDP's erasure right is drafted with only two named exceptions (purpose-retention necessity, legal-compliance necessity) -- a much shorter list than either GDPR's Art 17(3) (five named exceptions including freedom of expression and archiving/research) or CCPA's Section 1798.105(d) (nine specific exceptions including completing the transaction, security/integrity, debugging, free-speech exercise, scientific/statistical/historical research with informed consent, internal uses reasonably aligned with the relationship, and legal-obligation compliance). A deletion refusal lawful under GDPR or CCPA's more elaborate exception schemes (e.g. refusing deletion to preserve another party's free-speech rights, or for internal-use retention 'reasonably aligned with expectations') has no explicit textual anchor under DPDP as currently drafted -- fiduciaries relying on GDPR/CCPA-style deletion refusals should treat this as an open, unresolved-by-statute question, flagged for legal review case by case, not an assumed safe harbor.",
    "Refusing a DPDP erasure request on a GDPR- or CCPA-style ground (e.g. 'we're retaining this to exercise our own free-speech rights' or 'retention is reasonably aligned with your relationship expectations with us') without independently confirming that ground maps onto DPDP's narrower 'specified purpose or legal compliance' language -- a refusal textbook-defensible under GDPR Art 17(3)(a) or CCPA Section 1798.105(d)(4)/(7) may simply have no DPDP legal basis at all.")

add("R5", CAT, "COMPLETE — Session 1",
    "Section 13(1)-(3)",
    "A Data Principal has the right to readily available means of grievance redressal provided by the Data Fiduciary or Consent Manager in respect of any act/omission regarding her personal data or the exercise of her rights; the Fiduciary/Consent Manager must respond within a prescribed period; and the Data Principal must exhaust this internal grievance opportunity before approaching the Board.",
    "Article 77 (right to lodge a complaint with a supervisory authority) -- no exhaustion requirement",
    "Every data subject has the right to lodge a complaint directly with a supervisory authority, with no requirement to first exhaust an internal complaints mechanism with the controller.",
    "None equivalent at the individual-complaint level -- CCPA enforcement runs through the Attorney General/Agency, not a controller-side mandatory internal-grievance-first model; closest is the narrow private right of action for specific data-breach scenarios (Section 1798.150)",
    "No equivalent",
    "No equivalent",
    "Stand up a documented, timestamped internal grievance-redressal system (per Rule 14(3)) as a mandatory precondition/first line of defense before any Board escalation -- this is not optional infrastructure the way an EU controller's voluntary complaints-handling process is.",
    "DPDP's most consequential procedural departure from both comparator regimes in the rights category: GDPR gives data subjects a direct, unmediated right to complain to a supervisory authority with no internal-exhaustion precondition, and CCPA's enforcement is largely regulator-driven (Agency/AG) rather than routed through a mandatory business-side grievance system first. DPDP instead builds mandatory internal exhaustion directly into the individual right itself (S.13(3)) -- the Data Principal literally cannot approach the Board until the Fiduciary/Consent Manager's own internal process has been used. Real practical consequence: this shifts first-line dispute-resolution cost and friction onto the Fiduciary, and it means a well-run internal grievance function is now a genuine compliance-risk mitigant -- a slow or ineffective one becomes the actual point of Board exposure -- rather than a customer-service nicety.",
    "Building a DPDP grievance mechanism as a cosmetic, GDPR-style 'you can also complain to us if you want' channel -- because exhaustion is mandatory before Board escalation, an inadequate internal process doesn't just create customer dissatisfaction, it becomes the direct trigger for Board scrutiny once principals are forced through it and file complaints about the process itself.")

add("R6", CAT, "COMPLETE — Session 1",
    "Section 14(1)-(2)",
    "A Data Principal has the right to nominate any other individual who shall, in the event of her death or incapacity, exercise her rights under the Act; 'incapacity' means inability to exercise rights due to unsoundness of mind or infirmity of body.",
    "None -- GDPR Recital 27 expressly excludes deceased persons from the Regulation's scope entirely, leaving post-mortem data rights to Member State law (which varies and is not harmonised)",
    "N/A",
    "None -- Civil Code Section 1798.140's definition of 'consumer' excludes deceased individuals from CCPA rights by definition; the separate 'authorized agent' mechanism (defined at CCPA Regulations Section 7001(d), with operative provisions at Section 7063 -- NOT a Civil Code statutory term) is for a living consumer delegating exercise of rights, not a post-mortem nominee",
    "No equivalent",
    "No equivalent",
    "Build a nomination-capture and verification workflow (identity of nominee, proof of the Data Principal's death/incapacity) as a wholly new feature with no reusable GDPR/CCPA counterpart to borrow design patterns from.",
    "DPDP's second clean 'no equivalent' row for the matrix (alongside the Consent Manager) and one of the strongest Attack-2 answers available: GDPR explicitly carves deceased persons out of its scope by recital, treating post-mortem data governance as a matter for national (Member State) law rather than the Regulation itself; CCPA's 'consumer' definition is similarly limited to living natural persons, with no statutory nominee/successor mechanism. DPDP instead builds succession directly into the individual-rights chapter as a first-class right -- a meaningfully different design philosophy that treats the Data Principal's rights as something that can survive her in the hands of a designated individual, rather than lapsing or falling to unharmonised external law.",
    "Assuming an 'authorized agent' (CCPA Regulations Section 7001(d)/7063) or an EU Art 80 not-for-profit-body concept can stand in for a DPDP nomination -- both are mechanisms for a LIVING data subject to delegate exercise of rights during their lifetime; neither addresses post-mortem/incapacity succession, which is the entire point of DPDP S.14.")

add("R7", CAT, "COMPLETE — Session 1",
    "DPDP Rules 2025, Rule 14(1)-(4)",
    "The Data Fiduciary (and Consent Manager, where applicable) must prominently publish on its website/app the means and particulars (e.g. username/identifier requirements) for a Data Principal to exercise her rights; must respond to grievances within a reasonable period not exceeding ninety days under its grievance-redressal system, implementing appropriate technical/organisational measures to ensure timeliness; and the Data Principal may separately nominate individuals to exercise her rights per the Fiduciary's terms of service under Rule 14(4) (distinct from the Section 14 death/incapacity nomination).",
    "Article 12(2)-(3)",
    "The controller must facilitate the exercise of data subject rights and provide information on action taken within one month of the request (extendable by two further months for complex/numerous requests, with the data subject informed of the extension within the first month).",
    "Civil Code Section 1798.130(a)(2)(A) -- 45-day response window, extendable once by an additional 45 days",
    "Stricter under DPDP [see note]",
    "Stricter under DPDP [see note]",
    "Set internal SLAs to the SHORTEST applicable deadline across all three regimes for any multi-jurisdiction data subject (effectively GDPR's ~30 days or CCPA's 45 days, not DPDP's up-to-90-day ceiling), since defaulting to DPDP's longer window would breach GDPR/CCPA obligations for overlapping data subjects.",
    "NOTE ON VERDICT LABEL: the 'Stricter under DPDP' tag is used loosely here and flagged explicitly rather than mechanically applied, because on THIS specific point DPDP is actually the LEAST strict/protective of the three regimes on response timing -- the opposite of the vocabulary's ordinary meaning ('DPDP demands more'). Rule 14(3)'s up-to-90-day response ceiling is nearly triple GDPR's baseline one-month period and double CCPA's 45-day window. This is a genuinely counter-intuitive, highly checkable finding worth surfacing for the 'where does DPDP diverge' interview question -- the popular assumption that DPDP is 'GDPR but stricter' is simply false on this specific point. A global compliance program built to the tightest applicable SLA (GDPR's) will always over-satisfy DPDP's Rule 14(3) ceiling, but a program built only to DPDP's 90-day ceiling would violate GDPR/CCPA for the same overlapping data subject.",
    "Assuming DPDP is uniformly the 'strictest' of the three regimes (a common but lazy assumption, given DPDP is the newest and often described in Indian press as 'GDPR-plus') and therefore that a DPDP-only compliance build is a safe floor for GDPR/CCPA obligations too -- this specific row is a direct counterexample and should be flagged prominently in the README's methodology section as exactly the kind of assumption this project is designed to test rather than repeat.")

add("R8", CAT, "COMPLETE — Session 1",
    "Section 15(a)-(e)",
    "A Data Principal has correlative duties when exercising rights under the Act: comply with applicable laws; not impersonate another person when providing personal data for a specified purpose; not suppress material information when providing personal data for any document/identifier/proof of identity/address issued by the State; not register a false or frivolous grievance/complaint; and furnish only verifiably authentic information when exercising correction/erasure rights.",
    "None -- GDPR imposes no correlative statutory duties on the data subject as a condition of exercising Chapter III rights (the closest concept, Art 12(5)'s 'manifestly unfounded or excessive' request provision, is a controller-side defense against abusive requests, not a data-subject-side duty)",
    "N/A",
    "None -- CCPA's verification requirements (Regulations Article 5, Sections 7060-7063) impose identity-verification burdens on the consumer as a precondition to fulfilment, but this is a procedural fulfilment mechanic, not a statutory 'duty' whose breach has standalone legal consequences for the consumer",
    "No equivalent",
    "No equivalent",
    "No Fiduciary-side compliance mechanism is strictly required to give effect to this row (it binds the Data Principal, not the Fiduciary) -- but Fiduciaries should build request-intake processes that can detect and document apparent S.15 violations (impersonation, frivolous/false grievances), since these create a defensible basis for declining or deprioritising a request.",
    "Arguably DPDP's most philosophically distinctive feature in the entire rights category and the strongest 'no equivalent' answer available for interview purposes, because it inverts the usual privacy-law framing: GDPR and CCPA both treat the individual purely as a rights-holder whose only 'obligation' is the practical one of proving their own identity to receive a benefit; DPDP explicitly frames data principals as having reciprocal statutory duties, breach of which (frivolous complaints, impersonation, suppression of material information for government documents) is itself named misconduct under the Act. DPDP's Chapter III heading itself -- 'Rights AND Duties of Data Principal' -- makes this structural choice explicit rather than incidental. UPDATE (Session 2, verified against the Act's Schedule, [See section 33(1)]): S.15 violations DO carry a specific, named penalty -- Schedule Item 5, 'Breach in observance of the duties under section 15', penalty 'may extend to ten thousand rupees.' This closes the Session 1 open item and is itself a strong finding: ₹10,000 is by a huge margin the smallest figure anywhere in the Schedule -- roughly 1/25,000th of the ₹250 crore ceiling for a Data Fiduciary's own security-safeguard failure (Schedule Item 1, S.8(5)) and 1/20,000th of the ₹200 crore ceiling for a breach-notification failure (Item 2, S.8(6)). The Act deliberately keeps individual-side (data-principal) liability nominal/symbolic while fiduciary-side liability is calibrated to be genuinely deterrent at enterprise scale -- confirming that S.15's 'duties' framing is more a normative/interpretive statement about the character of the Data Principal-Fiduciary relationship than a meaningfully enforced financial deterrent against individuals, which is itself worth saying plainly rather than overselling the duty framing's practical bite.",
    "Treating Section 15 as toothless 'consumer education' boilerplate because it names no fiduciary-side compliance action -- even though this row requires no Fiduciary compliance mechanism, it is operationally useful as a documented defense when declining a bad-faith or impersonation-tainted request, and failing to build detection/documentation capability for S.15 violations forfeits that defense.")

# ============================================================
# CATEGORY 1 — LAWFUL BASIS / GROUNDS FOR PROCESSING (Session 2)
# ============================================================
CAT = "1. Lawful basis / grounds for processing"

add("L1", CAT, "COMPLETE — Session 2",
    "Section 3(a)-(c)",
    "The Act applies to digital personal data processed in India (collected digitally, or collected non-digitally and later digitised) and, extraterritorially, to processing outside India if connected with offering goods/services to Data Principals in India; it does NOT apply to purely personal/domestic processing, or to personal data that the Data Principal herself has made publicly available, or that another person is legally obligated to make public.",
    "Article 2(2)(c) (household exemption) + Article 3(1)-(2) (territorial scope, incl. the goods/services and monitoring-of-behaviour targeting tests)",
    "GDPR applies to processing wholly or partly by automated means (plus structured manual filing systems) except purely personal/household activity; territorially it applies to any EU establishment's processing regardless of where the processing occurs, and extraterritorially to non-EU controllers offering goods/services to, or monitoring the behaviour of, EU data subjects. GDPR has no general carve-out for data the data subject has made public -- publicly available personal data remains fully in scope (it only affects which Art 6/9 basis applies, e.g. Art 9(2)(e)).",
    "Civil Code Section 1798.140(d) -- applicability turns on a business meeting one of three revenue/volume/data-sale thresholds, not on a territorial test as such (though CCPA is understood to apply to businesses doing business in California and processing California consumers' data)",
    "Partial overlap",
    "Partial overlap",
    "Run every processing activity through a three-part scope filter: (i) does it touch digital personal data connected to India (collection or targeting test)? (ii) is it purely personal/domestic, or (iii) is the specific data element one the Data Principal herself already made public -- if (ii) or (iii), DPDP simply does not apply to that slice of the activity, unlike GDPR/CCPA where the analysis continues.",
    "The publicly-available-data carve-out (S.3(c)(ii)) is the sharpest, most checkable divergence in this row: DPDP categorically excludes data a Data Principal made public herself (or that another person is legally obliged to publish) from the Act's application entirely -- no notice, no consent, no fiduciary obligations attach to it at all. GDPR treats the same public LinkedIn profile or public social-media post as still fully in-scope personal data; publicity only narrows which lawful basis or special-category exception applies (Art 9(2)(e)), it never removes the data from the Regulation altogether. A company scraping or aggregating publicly posted personal data for, say, a recruiting or credit-risk product could be DPDP-clean on this basis alone while remaining fully GDPR-regulated for the identical dataset -- a genuine, not merely cosmetic, compliance-footprint difference for public-data-driven products.",
    "Assuming 'the data is public, so privacy law doesn't apply' as a universal rule -- it is close to true under DPDP S.3(c)(ii) but is not the GDPR or CCPA position; a global data-aggregation product built on the DPDP public-data logic will be non-compliant the moment the same dataset includes EU or California residents.")

add("L2", CAT, "COMPLETE — Session 2",
    "Section 4(1)-(2)",
    "A person may process personal data only in accordance with the Act and for a 'lawful purpose' -- defined negatively as 'any purpose which is not expressly forbidden by law' -- and only on one of two gateways: (a) the Data Principal's consent, or (b) one of the nine S.7 certain-legitimate-uses. The 'lawful purpose' test itself is a low, permissive bar; the real gatekeeping happens at the consent/S.7 gateway layer (see Row C1).",
    "Article 6(1)(a)-(f)",
    "GDPR's lawful-basis test is a positive, closed enumeration: processing is unlawful unless it affirmatively fits one of six named bases (consent, contract, legal obligation, vital interests, public task, legitimate interests). There is no general 'anything not expressly forbidden' permissive default anywhere in Article 6 -- the absence of a prohibition is never itself sufficient.",
    "No lawful-purpose or lawful-basis gate of any kind -- CCPA regulates HOW disclosed/collected data may be used (the 'business purpose' list at Section 1798.140(e)) and gives consumers opt-out/access/deletion rights, but does not require a business to identify or satisfy any legal basis before processing begins",
    "Partial overlap",
    "No equivalent",
    "Do not rely on S.4(2)'s 'not expressly forbidden by law' language as doing any real compliance work -- it is a low-value formal gate; document lawful basis at the S.4(1)(a)/(b) (consent-or-S.7) layer, which is where DPDP's actual permission architecture lives.",
    "A structural-philosophy gap easy to misstate: it is tempting to read S.4(2)'s negative/permissive definition of 'lawful purpose' as DPDP being looser than GDPR's positive enumerated-basis model. In practice the two converge in outcome, because S.4(1) still requires EITHER consent OR one of the nine closed S.7 categories -- the permissive 'lawful purpose' language only describes what kind of PURPOSE is acceptable (almost anything legal), not what GATEWAY authorises processing (which remains binary and closed). The real, substantively meaningful gap is the one already documented at Row C1/P4 (DPDP's nine closed S.7 categories vs. GDPR's open-textured Art 6(1)(f) legitimate-interests balancing test) -- this row exists to prevent that gap being mis-stated as 'DPDP has no lawful-basis requirement at all,' which is not accurate.",
    "Citing Section 4(2) alone ('lawful purpose means any purpose not expressly forbidden by law') as evidence that DPDP imposes a lighter lawful-basis burden than GDPR -- this reads only half the gate; S.4(1)'s consent-or-S.7 requirement is the operative constraint, and it is at least as closed as GDPR's Article 6 list for any processing not consent-based.")

# ============================================================
# CATEGORY 2 — NOTICE AND TRANSPARENCY (Session 2)
# ============================================================
CAT = "2. Notice and transparency"

add("N1", CAT, "COMPLETE — Session 2",
    "Section 5(2)",
    "Where a Data Principal gave consent BEFORE the Act's commencement, the Data Fiduciary must, as soon as reasonably practicable, retrospectively give her a notice covering the same three elements as a fresh S.5(1) notice (personal data and purpose, how to exercise S.6(4)/S.13 rights, how to complain to the Board) -- a one-time transitional/backfill notice obligation for the Act's entire pre-existing user base.",
    "None directly -- the GDPR text itself (Article 99, entry into force/application) contains no equivalent mandatory backfill-notice duty for consents predating 25 May 2018; Recital 171 instead addressed whether PRE-EXISTING consents remained VALID under the new Art 7 standard, not a duty to re-notify",
    "N/A",
    "None directly -- no equivalent transitional re-notice obligation tied to CCPA's various operative dates was located in the sections reviewed",
    "No equivalent",
    "No equivalent",
    "Run a one-time transitional-notice campaign covering every Data Principal whose consent predates the Act's Section-1(2) notified commencement date, using the same content template as the ordinary S.5(1)/Rule 3 notice, and log completion since this is a one-off, time-bound obligation rather than an ongoing operational control.",
    "A genuinely DPDP-specific obligation created by the mechanics of a brand-new statute retrofitting an existing user base, rather than by any difference in privacy philosophy -- GDPR and CCPA both existed alongside earlier, less protective regimes (the 1995 Directive; prior California law) but neither text mandates an affirmative backfill-notice exercise the way DPDP S.5(2) does for its own pre-Act consents. This is a useful example of a row where the 'gap' is a function of legislative transition mechanics, not of substantively different privacy values -- worth distinguishing from the philosophically-driven gaps elsewhere in this matrix (e.g. the Consent Manager, or S.15 duties) when explaining methodology.",
    "Treating S.5(2) as a dead-letter, one-time historical obligation now fully discharged and irrelevant going forward -- any Data Fiduciary onboarded users on a consent basis before the Act's S.1(2) commencement notification and never ran this backfill notice remains in ongoing breach of S.5(2) today, not merely of a historical, time-barred requirement.")

add("N2", CAT, "COMPLETE — Session 2",
    "Section 5(1), by omission -- there is no DPDP provision requiring a Data Fiduciary to publish and maintain a standing, general privacy policy",
    "DPDP's only notice obligation is transaction-bound: a notice must accompany or precede each S.6 consent request (S.5(1)) or be given retrospectively for pre-Act consent (S.5(2), Row N1). There is no separate statutory duty to publish, or keep updated, a standing privacy policy document independent of a specific consent event.",
    "Article 5(1)(a) (fairness/transparency principle) + Article 12(1) (information must be provided 'in a concise, transparent, intelligible and easily accessible form')",
    "GDPR's transparency principle and Article 12's accessibility standard are widely operationalised (and, in supervisory-authority guidance, effectively required) as maintaining a standing, generally accessible privacy notice/policy, in addition to point-of-collection notices under Articles 13-14 -- though the text itself does not use the words 'privacy policy'.",
    "Civil Code Section 1798.130(a)(5) -- an explicit, standing statutory duty: a business must maintain a privacy policy containing specified content and UPDATE IT AT LEAST ONCE EVERY TWELVE MONTHS",
    "Partial overlap",
    "No equivalent",
    "Maintain a standing, publicly accessible privacy policy as a matter of good practice and to satisfy GDPR/CCPA even though DPDP itself does not textually require one -- do not assume that satisfying S.5's transaction-bound notice duty is a substitute for the always-on CCPA Section 1798.130(a)(5) publication-and-annual-update obligation for any business also subject to CCPA.",
    "A genuinely counterintuitive finding worth having ready: DPDP, often described as the 'newest and strictest' of the three regimes, is actually the ONLY one of the three with no explicit statutory duty to publish and maintain a standing privacy policy document. CCPA's Section 1798.130(a)(5) is the most explicit and operationally concrete of the three (specific content, mandatory 12-month refresh cadence); GDPR's duty is principle-derived rather than textually explicit but is near-universally treated as mandatory in practice and enforcement. DPDP's silence here does not mean a company can skip a published privacy policy in India -- Rule 3's per-transaction notice content requirements are, if anything, MORE granular than a generic policy page -- but it does mean the specific compliance ARTEFACT (one evergreen, dated, versioned policy page) that GDPR/CCPA compliance programs are built around has no direct DPDP-mandated counterpart.",
    "Assuming a single, generic, GDPR/CCPA-style privacy policy page automatically satisfies DPDP -- DPDP instead requires an itemised, purpose-specific, STANDALONE notice presented at or before each consent request (Rule 3(a), see Row C2); a company that only ever updates one omnibus policy page and never triggers a distinct, itemised consent-time notice is CCPA/GDPR-postured but not necessarily DPDP-Rule-3-compliant.")

# ============================================================
# CATEGORY 5 — DATA MINIMISATION (Session 2)
# ============================================================
CAT = "5. Data minimisation"

add("M1", CAT, "COMPLETE — Session 2",
    "Section 6(1), third limb (data 'limited to such personal data as is necessary for such specified purpose') -- see also Row P3",
    "DPDP's minimisation constraint is textually embedded inside the definition of valid CONSENT (S.6(1)) and is not restated as a freestanding principle applicable to the nine S.7 non-consent processing grounds; each S.7 category is instead self-limiting by its own narrow wording (e.g. S.7(f) medical emergencies), with no explicit, generally-applicable minimisation test layered on top.",
    "Article 5(1)(c)",
    "Data minimisation is a freestanding processing principle in Article 5, textually and conceptually independent of which Article 6 lawful basis is used -- it applies with equal force to consent-based, contract-based, legitimate-interest-based, or any other GDPR-lawful processing.",
    "Civil Code Section 1798.100(c) -- collection, use, retention and sharing of personal information must be 'reasonably necessary and proportionate' to the disclosed purposes, applying to essentially all business processing regardless of any consent concept",
    "Partial overlap",
    "Partial overlap",
    "Do not assume S.7-based (non-consent) processing is minimisation-exempt merely because S.6(1)'s minimisation language is textually attached to consent -- apply a GDPR-Art-5(1)(c)-style necessity test to S.7 processing as a matter of prudent practice, since each S.7 category's own narrow wording provides only partial, category-specific minimisation coverage, not a general principle.",
    "Of the three regimes, CCPA's Section 1798.100(c) is actually the most UNIVERSALLY applicable minimisation constraint -- it binds essentially all business processing with no lawful-basis gate to attach to or exempt from. GDPR's Article 5(1)(c) is the next most universal (binds all six Art 6 bases equally). DPDP is the narrowest in formal textual scope: its clearest minimisation language lives inside the definition of valid consent, so a literalist reading leaves S.7 non-consent processing without an explicit, generally-stated minimisation backstop -- though each S.7 category's own narrow drafting does real limiting work in practice. This is a scope-of-application gap, not a values gap: DPDP clearly intends over-collection to be constrained everywhere, but the ENFORCEABLE TEXTUAL HOOK for that constraint is genuinely narrower outside the consent pathway.",
    "Treating minimisation as a purely consent-pathway concern under DPDP and skipping a necessity/proportionality review for S.7-based processing on the theory that 'S.6(1) doesn't apply here' -- regulators and the Board are likely to read the Act's overall purpose-limitation architecture (S.4, S.5, S.6, S.7 read together) as implicitly requiring necessity even for S.7 processing, so this literalist gap should not be relied on operationally even though it is textually real.")

add("M2", CAT, "COMPLETE — Session 2",
    "Section 8(4) (general obligation only -- no DPDP provision uses 'privacy by design' or 'by default' language, or names minimisation as a required default setting)",
    "A Data Fiduciary must implement 'appropriate technical and organisational measures to ensure effective observance' of the Act and Rules -- a generic, outcome-focused compliance-measures duty, not a specific by-design/by-default engineering mandate.",
    "Article 25(1)-(2)",
    "Data protection by design and by default: the controller must implement appropriate technical/organisational measures (e.g. pseudonymisation) designed to implement data-protection principles effectively, AND must ensure that, by default, only personal data necessary for each specific purpose is processed -- an explicit, minimisation-focused default-settings requirement (e.g. no additional-fields-collected-by-default, no default-public visibility settings).",
    "No explicit privacy-by-design/by-default statutory mandate located in the sections reviewed; the closest functional analogue is the Article 10 Risk Assessment regime (CCPA Regs Section 7150 et seq.), which requires identifying minimum-necessary data categories (Section 7152(a)(2)) but only for the specific high-risk processing activities enumerated in Section 7150(b), not as a universal default-settings rule",
    "No equivalent",
    "No equivalent",
    "Adopt GDPR Art 25-style by-design/by-default engineering practices (minimal default field sets, opt-in rather than opt-out defaults, privacy-protective default visibility) as good practice for the DPDP build too, since S.8(4)'s generic 'appropriate measures' language is broad enough to be read as encompassing this, even though it does not say so explicitly the way Article 25 does.",
    "A clean 'no equivalent' finding, though a quieter one than the Consent Manager or S.15 duties: GDPR's Article 25 is unusual among privacy statutes for legislating a specific ENGINEERING DEFAULT (data minimisation baked into product default settings, not merely a policy commitment) -- neither DPDP nor CCPA's core text goes this far. CCPA's Article 10 risk-assessment regime moves partway there but only for the specific high-risk processing activities it enumerates (selling/sharing PI, sensitive-PI processing, ADMT for significant decisions, systematic profiling, certain biometric/facial-recognition training), not as a universal default-settings principle for all processing the way Article 25 is drafted.",
    "Assuming DPDP's S.8(4) 'appropriate technical and organisational measures' language is a drop-in equivalent for a GDPR Art 25 by-design/by-default programme and treating the two compliance workstreams as interchangeable -- S.8(4) is outcome-focused and general; it will not, on its own text, satisfy a regulator expecting the specific default-settings evidence GDPR Art 25(2) demands.")

# ============================================================
# CATEGORY 6 — ACCURACY OBLIGATIONS (Session 2)
# ============================================================
CAT = "6. Accuracy obligations"

add("AC-A1", CAT, "COMPLETE — Session 2",
    "Section 8(3)",
    "A Data Fiduciary's proactive duty to ensure completeness, accuracy and consistency of personal data is CONDITIONAL -- it applies only where the data is (a) likely to be used to make a decision affecting the Data Principal, or (b) likely to be disclosed to another Data Fiduciary. Data that is neither decision-relevant nor disclosed carries no explicit proactive accuracy duty under this sub-section (the Data Principal's own request-triggered correction right under S.12 is separate and unconditional -- see Row R3).",
    "Article 5(1)(d)",
    "Accuracy is a freestanding, UNCONDITIONAL processing principle: personal data must be accurate and, where necessary, kept up to date, with 'every reasonable step' taken to erase/rectify inaccurate data 'without delay' -- applying to all personal data regardless of whether it will be used for a decision or disclosed onward.",
    "No freestanding proactive fiduciary-side accuracy duty located; Section 1798.106 (Right to Correct) is, like DPDP's S.12, principal-request-triggered rather than an independent, ongoing business obligation",
    "Stricter under DPDP [see note]",
    "No equivalent",
    "Do not rely on S.8(3)'s conditional trigger as the sole accuracy control -- apply a GDPR-Art-5(1)(d)-style unconditional accuracy standard across all held personal data as a matter of prudent practice, both because good data hygiene reduces downstream S.8(3)/S.12 risk and because a global compliance programme built to GDPR's unconditional standard will always over-satisfy DPDP's narrower, conditional one.",
    "NOTE ON VERDICT LABEL: 'Stricter under DPDP' is used loosely here and should be read as flagged, not literal -- on the specific proactive-duty question, DPDP is actually the NARROWER regime (a conditional, two-trigger duty vs. GDPR's unconditional universal principle), so the honest characterisation is that GDPR is stricter on this point, the mirror image of the R7 response-timeline finding. A company treating S.8(3) as its accuracy ceiling would under-comply with GDPR's Article 5(1)(d) for the same dataset. The practical upside for DPDP-only compliance is narrower scope, not stronger protection -- exactly the kind of nuance this project's methodology is designed to surface rather than paper over with a lazy 'DPDP = stricter' assumption.",
    "Mechanically applying the 'Stricter under DPDP' verdict label to this row without reading the gap analysis -- the label vocabulary is a starting heuristic, not a substitute for checking which direction the actual textual comparison runs; this row and Row R7 are both examples where a superficial application of the label would get the direction backwards.")

# ============================================================
# CATEGORY 7 — RETENTION AND ERASURE (Session 2)
# ============================================================
CAT = "7. Retention and erasure"

add("RE1", CAT, "COMPLETE — Session 2",
    "Section 8(7)-(8), read with DPDP Rules 2025 Rule 8(1)-(2) and the Third Schedule",
    "Independent of any Data Principal request, a Data Fiduciary of a prescribed class must itself erase personal data once the specified purpose is 'deemed no longer served' -- defined as the Data Principal neither approaching the Fiduciary for the specified purpose nor exercising any rights, for a period fixed per Data-Fiduciary-class/purpose in the Third Schedule -- and must give at least 48 hours' advance warning before that automatic erasure, unless the Data Principal re-engages.",
    "Article 5(1)(e)",
    "Storage limitation: personal data shall be kept in a form permitting identification for no longer than necessary for the purposes for which it is processed -- an abstract 'necessary' standard, with no fixed statutory time periods and no advance-warning-before-deletion mechanic in the text itself (specific retention periods are instead a matter of the controller's own documented policy and, per Art 30, its record of processing).",
    "No equivalent proactive/automatic fiduciary-side deletion duty; Section 1798.105 (Right to Delete) is, like DPDP's S.12(3), a Data-Principal-request-triggered right, not a fiduciary-initiated obligation",
    "Stricter under DPDP",
    "No equivalent",
    "Build the Third-Schedule-driven automatic-erasure clock and the mandatory 48-hour pre-erasure warning as a standing operational control (not merely a policy commitment), since this is a DPDP-specific, independently enforceable, proactive obligation with no equivalent operational precedent to borrow from a GDPR or CCPA compliance build.",
    "DPDP is the only one of the three regimes that legislates a FIDUCIARY-INITIATED, no-request-needed erasure duty with prescribed timing mechanics (Third-Schedule fixed periods, 48-hour warning) -- GDPR's storage-limitation principle and CCPA's deletion right both leave the operative trigger either to the controller's own documented retention schedule (GDPR) or to the consumer's own request (CCPA's Section 1798.105). This is a genuinely more operationally prescriptive design than either comparator and a strong 'Stricter under DPDP' row, distinct from the individual-request-triggered erasure right already covered at Row R4.",
    "Building only a request-triggered deletion pipeline (satisfying GDPR/CCPA-style compliance expectations) and treating it as DPDP-complete -- S.8(7)-(8)/Rule 8 impose a SEPARATE, proactive, automatic-erasure obligation that fires with no Data Principal request at all once the Third-Schedule 'deemed no longer served' clock runs out; a request-only deletion pipeline misses this entirely.")

add("RE2", CAT, "COMPLETE — Session 2",
    "DPDP Rules 2025, Rule 6(1)(e) and Rule 8(3) [neither Rule 6 nor Rule 8 is yet in force -- both commence 13 May 2027 per Rule 1(4); the one-year log-retention floor discussed in this row is not yet a live legal requirement]",
    "Independent of, and in apparent tension with, the Act's own erasure principle, a Data Fiduciary must RETAIN security logs and associated processing traffic data for a minimum of one year (Rule 6(1)(e)), and Rule 8(3) separately confirms a Data Fiduciary must retain personal data, traffic data and logs for at least one year from the date of processing for the purposes specified in the Seventh Schedule, after which erasure follows -- unless a longer period is required by other law or Government notification.",
    "None -- Article 32 (security of processing) requires 'a process for regularly testing, assessing and evaluating the effectiveness' of security measures but sets no specific minimum log-retention duration in the Regulation's own text",
    "N/A",
    "No equivalent minimum log-retention duration in the Civil Code sections reviewed; the closest CCPA-side figure is unrelated in kind -- CCPA Regs Section 7122(g) requires the BUSINESS and AUDITOR to retain cybersecurity-audit DOCUMENTATION for five years, not raw security/access logs, and only for businesses subject to the Article 9 audit threshold",
    "No equivalent",
    "No equivalent",
    "Treat the Rule 6(1)(e)/Rule 8(3) one-year log-retention floor as a distinct retention track from the underlying personal data's own Third-Schedule erasure clock (Row RE1) -- logs/traffic data must survive for the mandatory minimum even where the personal data they relate to has already been erased under S.8(7)-(8), and the retention-schedule design must keep the two tracks independently auditable.",
    "A built-in internal tension the Act resolves by design rather than leaving unresolved: DPDP simultaneously mandates erasure of personal data once its purpose lapses (S.8(7)-(8)) AND mandates a hard one-year MINIMUM retention floor for security logs and traffic data covering that same processing (Rule 6(1)(e)/8(3)) -- a genuine 'Conflict' half of this row's own column heading, resolved by treating logs/traffic-metadata as a legally distinct retention category from the personal data itself. Neither GDPR's Article 32 nor CCPA's Article 9 audit-documentation rule sets a comparable fixed minimum floor on ordinary security/access logs (Article 32 is a testing-and-evaluation process duty with no retention-duration figure; the CCPA five-year figure governs cybersecurity AUDIT REPORTS, an entirely different artefact).",
    "Erasing security/access logs on the same schedule as the personal data they relate to, on the theory that 'the purpose is no longer served' under S.8(7) -- Rule 6(1)(e) and Rule 8(3) impose an independent one-year retention FLOOR on those logs specifically, precisely so that post-breach forensic investigation remains possible even after the underlying personal data has been lawfully erased.")

# ============================================================
# CATEGORY 8 — SECURITY SAFEGUARDS (Session 2)
# ============================================================
CAT = "8. Security safeguards"

add("SEC1", CAT, "COMPLETE — Session 2",
    "Section 8(5), read with DPDP Rules 2025 Rule 6(1)(a)-(g)",
    "A Data Fiduciary must protect personal data in its possession/control (including via any Data Processor) by taking 'reasonable security safeguards' to prevent a personal data breach; Rule 6(1) fixes a seven-part minimum floor: (a) encryption/obfuscation/masking or virtual tokenisation, (b) access-control measures, (c) monitoring/logging for detecting and remediating unauthorised access, (d) measures to continue processing / restore access on compromise (incl. backups), (e) one-year minimum retention of those logs (see Row RE2), (f) a mandatory security-safeguards clause in any Data-Processor contract, and (g) general appropriate technical/organisational measures.",
    "Article 32(1)(a)-(d)",
    "Controllers/processors must implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, taking into account the state of the art, costs, and the nature/scope/context/purposes of processing and the risk to natural persons -- with an illustrative, non-exhaustive list: pseudonymisation and encryption; ongoing confidentiality, integrity, availability and resilience of systems; timely restoration of availability/access after an incident; and a process for regularly testing/assessing/evaluating effectiveness.",
    "Civil Code Section 1798.150(a)(1) -- a general 'reasonable security procedures and practices appropriate to the nature of the information' standard (relevant to the private right of action for breach, Row BN1); a materially more prescriptive, itemised standard applies only to businesses meeting the Article 9 Cybersecurity Audit thresholds (Row SDF3)",
    "Direct equivalent",
    "Partial overlap",
    "Build a single risk-based security programme against the UNION of DPDP Rule 6(1)(a)-(g)'s specific minimum list and GDPR Art 32(1)'s illustrative list (they overlap heavily -- encryption, access control, resilience/continuity, testing) and treat CCPA's baseline Section 1798.150(a)(1) reasonableness standard as automatically satisfied by that union; layer the more prescriptive Article 9 audit-scope controls (Row SDF3) on top only if the CCPA size thresholds are met.",
    "A rare, genuine three-way architectural convergence: all three regimes use a risk-based, non-exhaustive-illustrative-list style for baseline security (rather than a single prescriptive checklist), and DPDP's Rule 6(1) list maps closely onto GDPR Art 32(1)'s own illustrative items (encryption/tokenisation <-> pseudonymisation/encryption; continuity/backup measures <-> availability/resilience; monitoring/logging <-> the general risk-appropriateness test). The CCPA comparison is only a partial overlap because CCPA's BASELINE standard (Section 1798.150(a)(1)) is looser and more general than either DPDP's Rule 6(1) or GDPR's Art 32(1) -- CCPA reaches DPDP/GDPR-comparable prescriptiveness only for the subset of large businesses caught by the Article 9 audit regime (Row SDF3), not as a universal floor.",
    "Assuming CCPA's general Section 1798.150(a)(1) 'reasonable security' language is as prescriptive as DPDP's Rule 6(1) seven-part list or GDPR's Art 32(1) illustrative list -- for a business below the CCPA Article 9 audit thresholds, CCPA's textual security bar is meaningfully lower and less itemised than either DPDP or GDPR's, even though the surrounding privacy-marketing language often implies parity across 'the big three' regimes.")

add("SEC2", CAT, "COMPLETE — Session 2",
    "DPDP Rules 2025, Rule 6(1)(f)",
    "A Data Fiduciary's contract with any Data Processor must contain 'appropriate provision... for taking reasonable security safeguards' -- a mandatory contractual flow-down of the S.8(5)/Rule 6 security duty to processors, distinct from (and additional to) the general S.8(2) requirement that any processor engagement be under a valid contract at all.",
    "Article 28(3)(c)",
    "A controller-processor contract must, among other mandatory terms, oblige the processor to take all measures required under Article 32 (security of processing) -- a closely analogous mandatory contractual security flow-down.",
    "CCPA Regulations Section 7051 (mandatory service-provider/contractor contract terms) -- required contract terms focus primarily on purpose restriction and use limitation rather than being framed specifically as a security-measures flow-down, though security-relevant terms (e.g. deletion/return of data on completion) are also required",
    "Direct equivalent",
    "Partial overlap",
    "Use a single processor/service-provider contract template with a dedicated security-safeguards clause satisfying DPDP Rule 6(1)(f) and GDPR Art 28(3)(c) simultaneously (they require materially the same commitment), and layer CCPA Section 7051's purpose-restriction and data-handling terms on top as a distinct, additional set of clauses rather than assuming the security clause alone satisfies CCPA's contracting requirements.",
    "Another clean convergence row between DPDP and GDPR specifically -- both regimes independently arrived at the same design choice of making the fiduciary/controller directly responsible for contractually binding its processor to the same baseline security standard, rather than treating processor security as the processor's problem alone. CCPA's Section 7051 contracting requirements exist for a different primary purpose (constraining what a service provider/contractor may DO with the data -- purpose limitation -- rather than specifically mandating security-measures flow-down), so while overlap exists in practice (a well-drafted CCPA service-provider contract will usually include security terms too), the textual anchor and regulatory intent differ.",
    "Treating a CCPA-compliant service-provider contract (built primarily around Section 7051's purpose-restriction requirements) as automatically satisfying DPDP Rule 6(1)(f)'s specific security-safeguards flow-down requirement -- the two contracting regimes were not drafted with the same primary target and a purpose-restriction-only contract may be textually silent on security specifically.")

# ============================================================
# CATEGORY 9 — BREACH NOTIFICATION (Session 2)
# ============================================================
CAT = "9. Breach notification"

add("BN1", CAT, "COMPLETE — Session 2 (revised in adversarial pass: Cal. Civ. Code §1798.82 now read in full)",
    "Section 8(6), read with DPDP Rules 2025 Rule 7(1)",
    "On becoming aware of ANY personal data breach, a Data Fiduciary must intimate EVERY affected Data Principal, without delay, in concise/clear/plain language via her registered user account or other registered communication mode -- covering the breach's nature/extent/timing, likely consequences to her, mitigation measures taken, protective steps she can take, and a business contact for queries. There is no risk-based threshold and no stated exception -- the individual-notification duty is triggered by ANY breach, however minor.",
    "Article 34(1)-(3)",
    "Individual notification is required ONLY where the breach is 'likely to result in a HIGH RISK to the rights and freedoms of natural persons' -- a materiality gate DPDP's text does not have -- and even then THREE statutory exceptions can excuse individual notification entirely: (a) the affected data was rendered unintelligible (e.g. properly encrypted), (b) the controller has taken subsequent measures ensuring the high risk no longer applies, or (c) individual notification would involve disproportionate effort (substitutable with public communication).",
    "Cal. Civ. Code Section 1798.82(a)-(d), (g)-(h) (California's separate, freestanding breach-notification statute -- NOT part of CCPA/CPRA Title 1.81.5, which itself creates no individual-notification duty; this is the actual operative California individual-notification law, now read and verified directly rather than flagged as an unread gap)",
    "Stricter under DPDP",
    "Partial overlap",
    "Build the individual-breach-notification pipeline to DPDP's no-exceptions, every-breach standard as the compliance floor for the Indian population (it remains the strictest trigger of the three), while separately configuring the California-resident workflow to Section 1798.82's own mechanics: an unauthorized-ACQUISITION trigger (narrower than DPDP's broader breach definition), a closed-list 'personal information' category test, an encryption carve-out at (a)(1) unless the encryption key/credential was also compromised, and a hard 30-calendar-day outer deadline -- different trigger logic that cannot share a single DPDP-calibrated decision tree.",
    "Correcting the source-coverage gap honestly flagged in the first draft of this row: Cal. Civ. Code Section 1798.82 has now been read in full (current text as amended by Stats. 2025, Ch. 319 / SB 446, effective 1 Jan 2026). Corrected finding: California DOES have a real individual-notification duty, so 'No equivalent' was wrong -- the accurate verdict is 'Partial overlap,' and the interesting gap is about SCOPE, not existence. Three concrete divergences from DPDP Rule 7(1): (1) TRIGGER -- Section 1798.82 fires on unauthorized ACQUISITION of a closed list of 'personal information' categories (SSN, driver's-licence/state-ID, financial account+access code, medical/health-insurance info, biometric data, etc., paired with a name) or credential-pair data; DPDP's S.2(u) breach definition is broader, covering any personal data and also accidental disclosure, alteration, destruction, or loss of access, not just acquisition of a closed category list. (2) ENCRYPTION -- Section 1798.82(a)(1) exempts properly encrypted data UNLESS the encryption key/credential was also compromised -- a real carve-out DPDP's Rule 7(1) does not have, meaning DPDP is the outlier among all three regimes on this point, not just against GDPR. (3) TIMING -- Section 1798.82(a)(2) sets a hard 30-CALENDAR-DAY outer ceiling from discovery (subject to law-enforcement delay); DPDP's 'without delay' standard has no defined outer limit at all, which cuts the other way -- DPDP could in principle require faster notification with no safe-harbor window, keeping it the stricter regime on timing even without a headline number. A DPDP-calibrated playbook (no encryption carve-out, no defined outer deadline) will over-satisfy Section 1798.82's narrower, capped, category-gated duty for the same incident. See new Row BN3 for Section 1798.82(d)(2)(G)'s distinctive mandatory 12-month free identity-theft-service remedy, which has no DPDP or GDPR counterpart at all.",
    "Two pitfalls now that the CCPA-side comparator is properly verified rather than flagged as unread: (1) assuming Title 1.81.5's silence on individual notification means California has none at all -- it does, just codified in a separate, older statute (Section 1798.82, most recently amended by SB 446 effective 1 Jan 2026) that CCPA-focused compliance material often fails to cross-reference; and (2) porting a GDPR-style encryption carve-out into the DPDP playbook remains the core pitfall for the Indian workflow (Rule 7(1) has none), but do NOT assume the same no-carve-out policy should also apply to the California workflow -- Section 1798.82(a)(1) DOES have its own encryption exemption, so a single global 'no encryption carve-out anywhere' policy over-notifies California residents relative to what their own statute actually requires.")

add("BN2", CAT, "COMPLETE — Session 2 (revised in adversarial pass: Cal. Civ. Code §1798.82 now read in full)",
    "Section 8(6), read with DPDP Rules 2025 Rule 7(2)(a)-(b)",
    "On becoming aware of any personal data breach, a Data Fiduciary must ALSO intimate the Board: (a) without delay, a description of the breach (nature, extent, timing, location of occurrence, likely impact); and (b) within a hard SEVENTY-TWO HOURS of becoming aware (or such longer period as the Board allows on a written request), updated/detailed information covering the events/circumstances/causes, mitigation measures, findings on the person who caused the breach, remedial measures, and a report on the intimations given to affected Data Principals. There is no risk-based exemption -- the Board-notification duty, like the individual duty, is triggered by ANY breach.",
    "Article 33(1)-(5)",
    "Notification to the supervisory authority is required 'without undue delay and, where feasible, not later than 72 hours after having become aware of it,' UNLESS the breach is unlikely to result in a risk to the rights and freedoms of natural persons -- a single-stage, risk-gated 72-hour deadline, with reasons for any delay beyond 72 hours to be given.",
    "Cal. Civ. Code Section 1798.82(f) -- a narrow, threshold-gated Attorney General notification duty triggered only where a breach affects 500+ California residents, clocked from the CONSUMER-notification date (not breach discovery)",
    "Stricter under DPDP",
    "Partial overlap",
    "Build the Board-notification workflow around DPDP's unconditional, discovery-triggered two-stage structure as the default (immediate bare description, then a 72-hour detailed report); layer a SEPARATE, threshold-gated tracker for Section 1798.82(f) that activates only once a breach is confirmed to affect 500+ California residents, calculates its 15-calendar-day deadline from the date consumer notices go out (not from discovery), and submits a PII-redacted sample copy of the consumer notice electronically to the California Attorney General -- a materially different trigger, threshold, and clock-start than either DPDP Rule 7(2) or GDPR Art 33.",
    "The Section 1798.82(f) AG-notification duty, now verified, is real but far narrower and differently structured than either DPDP's or GDPR's regulator-facing duty: (1) THRESHOLD-GATED -- only breaches affecting 500+ California residents trigger any AG filing at all, whereas DPDP and GDPR both apply their regulator-notification duty to breaches of any size (GDPR gates on risk, not headcount); (2) LATE-STARTING CLOCK -- the 15-calendar-day deadline runs from the date consumers were notified, not from breach discovery, unlike DPDP's and GDPR's discovery-triggered clocks; and (3) NARROWER CONTENT -- the AG filing is just a redacted sample of the consumer notice, not the fuller incident-description-plus-remedial-measures report DPDP Rule 7(2)(b) or GDPR Art 33(3) require. Net effect, stated plainly rather than oversold: the adversarial check changed the CITED BASIS and the VERDICT LABEL (No equivalent -> Partial overlap) but did NOT change the underlying conclusion -- DPDP remains the strictest regulator-facing regime of the three even after properly incorporating the corrected CCPA-side source.",
    "Assuming California's 500-resident AG-notification threshold is a reasonable proxy for when DPDP's Board-notification duty should apply -- it is not; DPDP requires Board notification for a breach of even a single Data Principal's records, so a materiality/headcount filter calibrated to the California threshold will silently under-notify the Board for smaller Indian incidents that would fall well below the 500-person CA bar.")

add("BN3", CAT, "COMPLETE — Session 2 (added in adversarial pass)",
    "No DPDP provision located -- Section 8(6)/Rule 7 govern notification CONTENT and PROCESS only, with no affirmative remedial-service obligation to the affected Data Principal",
    "DPDP's breach-notification duty (Rows BN1-BN2) is purely informational and procedural: notify the individual and the Board, with prescribed content. Nothing in Section 8(6) or Rule 7 requires the Data Fiduciary to affirmatively PROVIDE or FUND any remedial service (credit monitoring, identity-theft insurance, etc.) to affected Data Principals as a matter of statutory obligation.",
    "None",
    "GDPR's Article 34 individual-notification duty is likewise purely informational -- it requires communicating the breach and (Art 34(2)) recommending measures the data subject can take, but imposes no obligation on the controller to fund or provide any remedial service itself.",
    "Cal. Civ. Code Section 1798.82(d)(2)(G)",
    "No equivalent",
    "No equivalent",
    "Where a breach affecting California residents exposes SSN or driver's-licence/state-ID-type identifiers (Section 1798.82(h)(1)(A)-(B)) AND the notifying business was itself the SOURCE of the breach (not merely a downstream recipient of a (b)-notice from another entity), budget and stand up NOT LESS THAN TWELVE MONTHS of free identity-theft prevention and mitigation services for affected California residents as a hard statutory deliverable, not a discretionary goodwill gesture -- track it as a distinct compliance line item with no DPDP or GDPR counterpart to piggyback on.",
    "The single most concretely 'extra' individual remedy found anywhere in this matrix, on either the DPDP or GDPR side: Section 1798.82(d)(2)(G) does not merely require California residents to be TOLD about a breach -- where the breach exposed SSN-type identifiers and the business itself caused it, the business must AFFIRMATIVELY FUND at least 12 months of identity-theft prevention/mitigation services as a mandatory content item of the notice itself. Neither DPDP's Rule 7(1) nor GDPR's Art 34 imposes any comparable affirmative-service obligation -- both are notify-and-inform regimes only, leaving post-breach remediation to the individual's own initiative or to voluntary business practice rather than statutory compulsion. This is a genuinely distinctive, American consumer-protection-style feature (with roots in the broader US state-breach-law tradition) that a company operating across all three jurisdictions needs a California-specific remediation-services vendor contract ready to activate -- something neither an Indian nor an EU breach playbook would otherwise budget for.",
    "Assuming a DPDP- or GDPR-calibrated breach playbook (notify, describe, recommend self-protective steps) is sufficient for a breach also affecting California residents where SSN-type data was exposed and the company was the source -- it is not; Section 1798.82(d)(2)(G)'s 12-month free-service mandate is an independent, additional line item that must be built and budgeted for separately, and failing to offer it is a standalone statutory violation regardless of how compliant the rest of the notice is.")

# ============================================================
# CATEGORY 11 — CHILDREN'S DATA (Session 2)
# ============================================================
CAT = "11. Children's data"

add("CHD1", CAT, "COMPLETE — Session 2",
    "Section 2(f) (definition) + Section 9(1), read with DPDP Rules 2025 Rule 10(1)-(2)",
    "A 'child' is defined, flatly and without tiers, as anyone who has not completed EIGHTEEN years of age. Before processing ANY child's personal data, a Data Fiduciary must obtain VERIFIABLE consent of the parent (or lawful guardian), using technical/organisational due-diligence measures to confirm the consenting adult is (a) actually an adult and (b) identifiable, by reference to reliable identity/age details already held, voluntarily provided details, or a virtual token issued by an authorised entity (incl. Digital Locker-style providers).",
    "Article 8(1)-(2)",
    "For 'information society services' offered directly to a child, processing based on Article 6(1)(a) consent is lawful only where the child is at least 16 -- but Member States may, by law, lower this to as low as 13, so the EU consent-age threshold is tiered/harmonisation-optional (13-16) and, textually, applies specifically to the information-society-services/consent-basis scenario, not as a universal 'processing any child's data' gate the way DPDP's S.9(1) is drafted.",
    "Civil Code Section 1798.120(c)-(d) -- opt-in (not blanket processing) consent required for SALE/SHARING of a minor's data: affirmative authorisation required from the minor herself if aged 13-15, or from a parent/guardian if under 13; this targets only the sale/sharing decision, not general processing",
    "Stricter under DPDP",
    "Stricter under DPDP",
    "Set the DPDP-facing age gate at a flat 18 (not 16 or 13) and require verifiable-parental-consent infrastructure (identity/age verification per Rule 10) for the ENTIRE 0-17 age band before any processing begins, layering the narrower GDPR 13-16 information-society-services consent gate and CCPA's 13/16 sale-and-sharing opt-in gate on top for those specific comparator scenarios -- a DPDP-calibrated build will always over-satisfy both narrower regimes on age threshold alone.",
    "One of the cleanest, most dramatic, and most checkable numeric divergences in the whole matrix: DPDP's 18-year flat threshold is materially higher than either comparator's tiered 13-16 range, and DPDP's trigger is 'any processing of a child's data' rather than being scoped to a specific scenario (information-society-services consent under GDPR; sale/sharing under CCPA). A company whose GDPR/CCPA compliance programme treats 16- or 17-year-olds as ordinary adult users -- a legitimate position under both comparator regimes -- is squarely non-compliant under DPDP, which still requires verifiable parental consent for that same user. This is a strong, ready answer to 'where does DPDP diverge from the GDPR-is-the-gold-standard assumption in a way that surprised you' -- DPDP is unambiguously the MOST protective of the three on this specific point, the opposite of the R7 response-timeline finding.",
    "Reusing an existing GDPR/CCPA age-gate (typically built around 13, 16, or a 'are you over 16' checkbox) as the DPDP age gate -- DPDP's flat 18-year threshold with mandatory verifiable-parental-consent infrastructure for the entire under-18 population is a materially larger compliance build than either comparator's narrower, tiered gate, and a 16-or-older self-declared adult under GDPR/CCPA is still legally a 'child' requiring parental consent under DPDP S.9(1)/S.2(f).")

add("CHD2", CAT, "COMPLETE — Session 2",
    "Section 9(2)-(3)",
    "A Data Fiduciary may NOT undertake processing of a child's personal data likely to cause any detrimental effect on the child's well-being, and may NOT undertake tracking or behavioural monitoring of children, OR targeted advertising directed at children -- an absolute, non-consent-curable prohibition (parental consent under S.9(1) does not cure or permit S.9(3)-barred tracking/targeted-advertising activity).",
    "None as an absolute statutory prohibition -- GDPR relies on the general Article 5/6 lawful-basis framework plus the Article 8 consent-age gate for children, and on soft-law/regulatory guidance (e.g. supervisory-authority children's-design codes) rather than a hard textual ban on tracking or targeted advertising to children in the Regulation itself",
    "N/A",
    "No equivalent absolute prohibition -- CCPA's child-specific protection is limited to the Section 1798.120(c)-(d) opt-in requirement for SALE/SHARING of a minor's data; first-party targeted advertising or behavioural tracking that does not constitute a 'sale' or 'sharing' as CCPA defines those terms may fall outside CCPA's minor-specific protections entirely",
    "No equivalent",
    "No equivalent",
    "Treat S.9(3) as a hard product-design constraint, not a consent-manageable risk: disable behavioural tracking and targeted-advertising delivery entirely for any user flagged (or reasonably identifiable) as a child, regardless of whether verifiable parental consent under S.9(1)/Rule 10 has been obtained for other processing -- consent does not create an exception to this specific prohibition.",
    "Arguably DPDP's strongest children's-data protection and a genuinely distinctive, non-consent-curable design choice: most comparable regimes let a valid legal basis (consent, in particular) authorise otherwise-restricted processing, but DPDP S.9(3) is drafted as an absolute bar that obtaining parental consent under S.9(1) does not override. Neither GDPR nor CCPA's core statutory text contains an equivalent flat, non-waivable prohibition on tracking/behavioural-monitoring or targeted advertising specifically directed at children -- GDPR addresses this space through the general lawful-basis/consent-age framework and largely non-binding regulatory guidance, and CCPA's protection is narrower still, tied only to the defined 'sale'/'sharing' concepts and therefore potentially inapplicable to some first-party targeted-advertising arrangements.",
    "Assuming that obtaining valid Rule-10 verifiable parental consent authorises ad-targeting or behavioural-tracking products aimed at children, because 'we got consent' -- S.9(3) is drafted as an independent, absolute prohibition that parental consent under S.9(1) does not cure; a consented-to tracking/ad-targeting feature for a known child user remains a standalone S.9(3) violation.")

# ============================================================
# CATEGORY 12 — CROSS-BORDER TRANSFER (Session 2)
# ============================================================
CAT = "12. Cross-border transfer"

add("CB1", CAT, "COMPLETE — Session 2",
    "Section 16(1)-(2)",
    "The Central Government MAY, by notification, restrict transfer of personal data to a specified country/territory outside India -- a BLOCKLIST model: transfer is permitted by default to any destination unless and until that destination is affirmatively notified as restricted. S.16(2) is a savings clause: nothing in this section restricts the applicability of any OTHER Indian law that itself imposes a higher degree of protection or restriction on cross-border transfer for particular data/Fiduciaries.",
    "Article 44 (general principle) + Article 45 (adequacy decisions) + Article 46 (appropriate safeguards)",
    "GDPR uses the structurally OPPOSITE ALLOWLIST model: any transfer to a third country is prohibited by default unless the controller/processor affirmatively establishes one of the Chapter V gateways -- an EU Commission adequacy decision for that country (Art 45), or 'appropriate safeguards' such as Standard Contractual Clauses or Binding Corporate Rules (Art 46), or (failing both) a specific Art 49 derogation.",
    "No cross-border-transfer-specific statutory gate exists in CCPA/CPRA -- a transfer outside California/the US is treated identically to any other 'sale,' 'sharing,' or disclosure to a service provider/contractor/third party under the ordinary Sections 1798.100-135 framework, with no separate geography-based restriction mechanism",
    "Partial overlap",
    "No equivalent",
    "Do not assume a GDPR-style transfer-safeguards programme (SCCs, BCRs, adequacy-tracking) is required for DPDP purposes -- as currently drafted, S.16(1)'s operative compliance step is simply checking whether the destination country/territory has been notified as restricted; if it has not, no further DPDP-specific transfer mechanism, documentation, or safeguard is textually mandated. Separately verify S.16(2)'s savings clause against any OTHER applicable Indian sectoral law (e.g. financial-sector data-localisation rules) that may independently restrict the same transfer -- DPDP's own permissiveness does not override those.",
    "The single most structurally significant finding in this category, and arguably in the whole matrix: DPDP and GDPR do not merely differ in strictness on cross-border transfer, they are built on OPPOSITE default assumptions -- GDPR presumes a transfer is unlawful until proven safe (allowlist); DPDP presumes a transfer is lawful until specifically blocked (blocklist). 'Partial overlap' is used advisedly here rather than a strictness label, because the two regimes address the identical subject matter (should personal data be allowed to leave the jurisdiction) with genuinely inverted default logic, not merely different thresholds on the same logic. A multinational's existing GDPR Chapter V transfer-safeguards programme (SCCs, TIAs, BCR approvals) is not merely sufficient but drastically over-built relative to DPDP's current textual requirement -- the practical Attack-1 answer here is that DPDP compliance on cross-border transfer is, today, the SIMPLER build of the two, not the harder one, which cuts against the common assumption that 'the newest law is always the strictest.' ADVERSARIAL CHECK (Session 2 second pass): the obvious counter-argument is that S.16(2)'s savings clause quietly reintroduces GDPR-style strictness through sectoral back doors -- e.g. RBI's payment-systems data-localisation mandate already requires certain financial data to stay in India with no transfer option at all, so calling DPDP's cross-border regime 'the simpler build' could mislead a company that is also RBI-regulated. Re-checked against S.16(2)'s actual text: this counter-argument does NOT defeat the finding, it CONFIRMS the row was already correctly scoped -- the claim above is specifically about what DPDP's OWN Section 16 requires as a horizontal law, not about the totality of Indian law a given company faces, and the Compliance Mechanism cell already instructs the reader to separately check sectoral overlays. The finding stands: verified, not weakened, by the adversarial pass.",
    "Assuming DPDP's cross-border regime demands the same SCC/BCR/adequacy-tracking documentation burden as GDPR's -- as textually drafted, S.16 imposes no such requirement; over-building a DPDP-specific transfer-safeguards program mirroring GDPR's is not wrong as a risk-management choice, but citing it as a DPDP-MANDATED requirement misstates what the Act actually says.")

add("CB2", CAT, "COMPLETE — Session 2",
    "DPDP Rules 2025, Rule 13(4)",
    "A Significant Data Fiduciary specifically (not Data Fiduciaries generally) must ensure that personal data and associated traffic data the Central Government specifies -- on the recommendation of a government-constituted committee (which may include officials from the Ministry of Electronics and IT and other ministries/departments) -- is NOT transferred outside India at all: a hard, category-specific LOCALISATION mandate layered on top of S.16's general blocklist regime, and applicable only to the narrower SDF-designated population.",
    "None -- GDPR's Chapter V transfer regime (Articles 44-49) applies uniformly to every controller/processor regardless of size or any government-conferred 'significant' designation; there is no GDPR-equivalent, tiered, designation-gated data-localisation overlay",
    "N/A",
    "No equivalent data-localisation concept exists within the CCPA/CPRA statutory text reviewed",
    "No equivalent",
    "No equivalent",
    "Any entity notified (or reasonably expecting to be notified) as a Significant Data Fiduciary should build a SEPARATE compliance track specifically for Rule 13(4) localisation-eligible data categories once the Central Government specifies them, distinct from and in addition to the general S.16 blocklist check that applies to all Data Fiduciaries -- this is a two-tier cross-border framework, not a single uniform one.",
    "A second DPDP-specific, no-clean-comparator feature in the Cross-Border Transfer category (alongside the blocklist/allowlist inversion at Row CB1): DPDP layers a TIERED cross-border architecture -- a permissive general blocklist for everyone (S.16), plus a potential hard localisation mandate for specific data categories, but ONLY for the narrower population of government-designated Significant Data Fiduciaries (Rule 13(4)). Neither GDPR nor CCPA conditions the strictness of its cross-border rules on a government-conferred 'significant'/'large' designation the way DPDP does -- GDPR's Chapter V binds a two-person controller and a multinational identically; CCPA has no comparable transfer-restriction concept to tier in the first place.",
    "Assuming Rule 13(4) localisation applies to all Data Fiduciaries, or conversely assuming it currently applies to none because SDF designation is still relatively uncommon -- it is a category-specific, government-triggered mandate whose actual bite depends entirely on (a) whether an entity has been notified as an SDF under S.10, and (b) whether the Government has specified particular data categories under Rule 13(4) for that SDF; both are administratively contingent facts to verify per entity, not a fixed rule.")

add("CB3", CAT, "COMPLETE — Session 2",
    "Section 16(1), by contrast with GDPR's fuller Chapter V toolkit",
    "DPDP's S.16 text provides only the single blocklist mechanism described at Row CB1 -- it names no consent-based derogation, no contract-necessity derogation, no public-interest derogation, and no equivalent to GDPR's Binding Corporate Rules or Standard Contractual Clauses toolkit for a transfer to a (hypothetically) restricted destination.",
    "Article 46 (appropriate safeguards toolkit: SCCs, BCRs, approved codes of conduct, certification mechanisms) + Article 49(1)(a)-(g) (derogations for specific situations: explicit consent, contract necessity, public interest, legal claims, vital interests, public register, compelling legitimate interests)",
    "GDPR provides a full, multi-layered toolkit of alternative transfer mechanisms (adequacy, multiple categories of 'appropriate safeguards,' and a further seven-item derogations list for situations where neither adequacy nor safeguards are available) -- a considerably richer, more heavily documented compliance menu than DPDP currently offers.",
    "N/A -- see Row CB1 (no cross-border-specific mechanism of any kind in CCPA)",
    "Partial overlap",
    "No equivalent",
    "Do not attempt to port a GDPR SCC/BCR-style transfer-mechanism menu into a DPDP compliance file as if DPDP required one -- for any DPDP-governed transfer to a destination that has not been notified as restricted under S.16(1), no such mechanism is currently required; retain the GDPR toolkit only for the EU-regulated slice of the same data flows.",
    "The flip side of Row CB1's finding, worth stating as its own row because it changes the PRACTICAL COMPLIANCE WORKLOAD conclusion rather than the structural-comparison one: GDPR's Chapter V is not just stricter by default (Row CB1), it is also far more heavily INSTRUMENTED, with named alternative mechanisms and a derogations menu for edge cases. DPDP's S.16, as currently drafted, has no equivalent menu at all -- there is nothing resembling an SCC, a BCR-approval process, or an Art 49 derogations list to build compliance documentation around. For Attack 1's 'what does a GDPR-compliant company still need to do for DPDP' framing, this row's honest answer for cross-border transfer specifically is: less paperwork, not more -- an unusual and useful counterpoint to the matrix's more common 'DPDP requires something extra' rows.",
    "Building an elaborate DPDP-specific SCC/BCR-equivalent documentation suite because 'GDPR needed one, so DPDP probably does too' -- this over-engineers the DPDP compliance build relative to what S.16 actually requires today, and risks obscuring the row that DOES require real, DPDP-specific extra work (Row CB2's SDF localisation overlay).")

# ============================================================
# CATEGORY 13 — SIGNIFICANT DATA FIDUCIARY OBLIGATIONS (Session 2)
# ============================================================
CAT = "13. Significant Data Fiduciary obligations"

add("SDF1", CAT, "COMPLETE — Session 2",
    "Section 10(1)(a)-(f)",
    "The Central Government MAY notify any Data Fiduciary or class of Data Fiduciaries as a 'Significant Data Fiduciary' (SDF), based on an assessment of relevant factors including: (a) volume and sensitivity of personal data processed; (b) risk to Data Principals' rights; (c) potential impact on India's sovereignty and integrity; (d) risk to electoral democracy; (e) security of the State; and (f) public order. This is a DISCRETIONARY EXECUTIVE DESIGNATION mechanism -- an entity does not self-determine SDF status by meeting an objective threshold; it becomes an SDF only when and if the Government affirmatively notifies it.",
    "Article 37(1)(a)-(c)",
    "A controller/processor MUST (self-determine and) designate a DPO wherever: (a) it is a public authority/body; (b) its core activities require regular and systematic large-scale monitoring of data subjects; or (c) its core activities involve large-scale processing of special-category/criminal-offence data -- a self-assessed, QUALITATIVE trigger based on the nature of processing, with no government designation step.",
    "CCPA Regulations Article 9 (Section 7120(b)) -- an OBJECTIVE, QUANTITATIVE, self-assessed threshold: processing 250,000+ consumers'/households' personal information, OR 50,000+ consumers' sensitive personal information, in the preceding calendar year (combined with a revenue gate at Civil Code Section 1798.140(d)(1)(A))",
    "Partial overlap",
    "Partial overlap",
    "Track SDF exposure as a REGULATORY-RELATIONS/government-affairs monitoring item (watch for notification, since the trigger is not self-assessable the way GDPR/CCPA's are) in addition to, not instead of, self-assessing against GDPR's Art 37 qualitative criteria and CCPA's Article 9/10 quantitative thresholds independently -- meeting either comparator's trigger does not mean, and meeting neither does not mean, SDF status has or has not been notified.",
    "The clearest illustration of why this category has 'no clean GDPR equivalent' as the project brief anticipated, now precisely characterised: the underlying CONCEPT (a heightened compliance tier for higher-risk data processors) is shared across all three regimes, but the TRIGGER MECHANISM is fundamentally different in kind, not just degree, across all three -- DPDP uses discretionary government designation (including overtly political/national-security factors like electoral-democracy risk and public order that have no analogue in either comparator's criteria at all), GDPR uses self-assessed qualitative criteria tied to the nature of processing, and CCPA uses self-assessed objective numeric thresholds. A company could meet CCPA's 250,000-consumer threshold and GDPR's large-scale-monitoring test and still never become a DPDP SDF (if never notified), or conversely be notified as an SDF for national-security-adjacent reasons having nothing to do with data volume at all.",
    "Assuming SDF status is self-determinable by benchmarking against GDPR's Art 37 criteria or CCPA's Article 9 thresholds -- it is not; SDF status under DPDP is a government-notification event, meaning an entity that comfortably clears both comparator regimes' 'high-risk processor' bars can be, at the same time, entirely un-notified (and therefore not yet subject to any S.10 obligation) under DPDP, and vice versa.")

add("SDF2", CAT, "COMPLETE — Session 2",
    "Section 10(2)(a)(i)-(iv)",
    "Once notified, a Significant Data Fiduciary must appoint a Data Protection Officer who: represents the SDF under the Act; is based in India; is responsible to the SDF's Board of Directors or equivalent governing body; and is the point of contact for the Act's grievance-redressal mechanism. Unlike GDPR, DPDP has NO general/universal DPO requirement for ordinary (non-SDF) Data Fiduciaries -- see also Row AC1.",
    "Article 37(1)-(7) + Article 38",
    "GDPR's DPO trigger (Row SDF1) is tied to the nature of the processing itself, not to any government designation, meaning a genuinely small organisation doing qualifying large-scale/special-category processing is self-executingly DPO-obligated the moment it meets Art 37's criteria -- there is no administrative contingency comparable to waiting for a DPDP SDF notification. GDPR also imposes no residency requirement analogous to DPDP's 'based in India' rule.",
    "No statutory DPO-equivalent role requirement located anywhere in the CCPA/CPRA sections reviewed",
    "Partial overlap",
    "No equivalent",
    "Do not treat 'we have not been notified as an SDF, so we have no DPO obligation' as the end of the analysis if the same organisation's processing would independently trigger GDPR Art 37 -- the GDPR DPO obligation is self-executing regardless of DPDP SDF status, so a company subject to both regimes may be GDPR-DPO-mandated well before (or entirely independent of) any DPDP SDF notification.",
    "The administrative-contingency gap already flagged at Row SDF1 has its sharpest practical consequence here: a company can be doing exactly the kind of large-scale, high-risk processing GDPR's Art 37 is designed to catch, and be GDPR-DPO-mandated TODAY, while remaining entirely DPO-optional under DPDP indefinitely, simply because no SDF notification has issued. This is a timing/certainty gap as much as a substantive one -- the DPDP obligation exists in the statute but its ACTIVATION is outside the regulated entity's own control, unlike GDPR's self-executing trigger.",
    "Building DPO governance (India-based appointment, Board-reporting line, grievance-contact-point role) only after receiving SDF notification -- given the Government's designation timing is unpredictable and the S.10(2)(a) requirements are specific (India residency, Board-level reporting), a company with a plausible SDF-designation risk profile should have this governance structure ready to stand up quickly rather than starting design work only after notification.")

add("SDF3", CAT, "COMPLETE — Session 2",
    "Section 10(2)(b)-(c), read with DPDP Rules 2025 Rule 13(1)-(3)",
    "A Significant Data Fiduciary must appoint an INDEPENDENT data auditor to carry out a data audit evaluating the SDF's compliance, and must undertake periodic Data Protection Impact Assessments and periodic audits; Rule 13(1)-(2) fixes the cadence at once every twelve months, with a report of 'significant observations' from the DPIA and audit furnished to the Board, and Rule 13(3) requires due diligence that technical measures (including algorithmic software) used for processing do not pose a risk to Data Principals' rights.",
    "Article 35",
    "Data Protection Impact Assessment -- SELF-assessment only; no GDPR provision mandates an INDEPENDENT third-party audit of a controller's overall data-protection compliance the way DPDP S.10(2)(b) does (the closest adjacent concepts -- Art 41/43 code-of-conduct monitoring bodies and certification bodies -- are voluntary, opt-in mechanisms, not a mandatory audit duty)",
    "CCPA Regulations Article 9 (Sections 7120-7124) -- Cybersecurity Audits: an ANNUAL, INDEPENDENT (internal-with-firewall-from-management or external), qualified-auditor requirement for businesses meeting objective thresholds (Row SDF1), with a prescribed audit scope spanning ~18 enumerated components (MFA, encryption, access controls, logging, vulnerability testing, incident-response planning, etc.) and a signed certification of completion submitted to the CPPA",
    "No equivalent",
    "Direct equivalent",
    "Build the SDF independent-audit function against CCPA's Article 9 cybersecurity-audit architecture as the closest available real-world template (auditor independence safeguards, defined scope, management-reporting line, documentation retention) rather than against GDPR's Art 35 DPIA process, which is self-assessment only and the wrong structural model for what S.10(2)(b) actually requires.",
    "A genuinely counterintuitive and high-value finding for Attack 1/Attack 2: on the specific 'mandatory independent third-party audit of the data-protection programme' concept, DPDP's closest true structural peer among the three regimes is CCPA's Article 9 Cybersecurity Audit regime, NOT anything in GDPR -- inverting the default assumption that GDPR is always the nearer comparator. Both DPDP S.10(2)(b) and CCPA Article 9 share: a mandatory (not voluntary) independent-auditor requirement, a defined periodic cadence, and a report/certification channel to the relevant regulator (India's Board; California's CPPA). GDPR's Art 35 DPIA, by contrast, is textually and functionally a SELF-assessment the controller conducts itself (with only optional DPO/supervisory-authority consultation), never an independent third party's audit product -- a materially different governance model despite being the instinctively 'obvious' GDPR comparator for a Big-Four-style audit requirement. ADVERSARIAL CHECK (Session 2 second pass): the strongest counter-argument is that GDPR DOES have an independent-audit concept the row ignores -- Article 58(1)(b) empowers a supervisory authority to 'carry out investigations in the form of a data protection audit.' Re-checked against the Art 51-76 text read this session: this does not defeat the finding, it sharpens it -- Art 58(1)(b) is a REGULATOR-INITIATED investigative power (triggered by the authority's own risk assessment, a complaint, or a breach), not a routine, periodic, controller-self-triggered mandatory obligation the way DPDP S.10(2)(b)/Rule 13 and CCPA Article 9 both are. No GDPR provision requires a controller to proactively commission and fund an independent audit of itself on a fixed cadence absent a specific supervisory-authority trigger -- the DPDP/CCPA structural parallel holds.",
    "Mapping DPDP's SDF independent-audit requirement to GDPR's Article 35 DPIA as the 'obvious' comparator without checking whether Article 35 actually requires INDEPENDENCE from the controller -- it does not; treating a self-conducted DPIA as satisfying S.10(2)(b)'s 'independent data auditor' requirement would misread both the DPDP text (which specifically requires an independent auditor, not a self-assessment) and the GDPR text (which specifically does not require one).")

# ============================================================
# CATEGORY 14 — GRIEVANCE REDRESSAL (institutional/Board-level)
# ============================================================
CAT = "14. Grievance redressal (institutional/Board-level mechanism)"

add("GR1", CAT, "COMPLETE — Session 2",
    "Section 13(3) (mandatory internal exhaustion, see also Row R5), read with Chapter V (Sections 18-26, Board establishment/composition) and Chapter VI (Sections 27-28, Board powers/procedure) and Chapter VII (Sections 29-32, appeal to the Appellate Tribunal and alternative dispute resolution)",
    "A Data Principal must exhaust the internal Fiduciary/Consent-Manager grievance process before approaching the Board; the Board itself is a Government-established statutory body vested with civil-court-equivalent procedural powers for its inquiries (summoning and examining persons, requiring discovery/production of documents, receiving evidence on affidavit, inspecting records) but WITHOUT search-and-seizure power; Board decisions are appealable to the (Telecom Disputes Settlement) Appellate Tribunal designated for this Act.",
    "Article 77 (complain to a supervisory authority) + Article 78 (judicial remedy against the supervisory authority) + Article 79 (judicial remedy DIRECTLY against a controller/processor)",
    "GDPR gives a data subject THREE cumulative, non-sequential avenues with no exhaustion precondition: complain to a supervisory authority (Art 77), seek judicial review of that authority's handling (Art 78), and -- critically -- go DIRECTLY to a competent court against the controller/processor itself (Art 79), entirely independent of whether a supervisory-authority complaint was ever filed.",
    "No equivalent individual-complaint-to-institution pipeline -- CCPA enforcement for most violations runs through the CPPA/Attorney General only (Section 1798.155 administrative fines); an individual consumer has a private right of action ONLY for the narrow unencrypted-breach scenario of Section 1798.150, and Section 1798.150(c) expressly states this cause of action 'shall not be based on violations of any other section' and 'nothing in this title shall be interpreted to serve as the basis for a private right of action under any other law' -- meaning for the large majority of CCPA violations, an aggrieved consumer has NO individual enforcement pathway of any kind, not even a regulator-complaint route structured for individual grievances the way DPDP's S.13/Board pipeline is.",
    "No equivalent",
    "No equivalent",
    "Build the mandatory internal-grievance function as genuine first-line dispute resolution infrastructure (not a formality) since DPDP, unlike GDPR, gives Data Principals no way to bypass it -- and do not assume a DPDP-style Board-escalation safety net exists for CCPA purposes; for most CCPA violation types there is no individual escalation path to design for at all, only regulator-driven enforcement risk to manage.",
    "A genuinely three-way structural divergence rather than a simple strictness comparison: GDPR maximises individual optionality (three parallel/cumulative avenues, no exhaustion precondition, and a direct-to-court option bypassing the regulator entirely); DPDP channels every individual dispute through a mandatory single pipeline (internal grievance, then Board, then Tribunal) with no direct-to-court option built into the individual-rights chapter itself; CCPA gives most individuals no direct pathway at all outside the narrow breach-specific private right of action, relying almost entirely on public (CPPA/AG) enforcement. None of the three designs is a strictness variant of another -- they reflect three different theories of who should drive enforcement (the individual via courts, the individual via an administrative pipeline, or the regulator alone).",
    "Assuming DPDP's Board is a rough equivalent of a GDPR supervisory authority that a Data Principal can approach in parallel with (rather than only after exhausting) internal remedies -- S.13(3)'s mandatory-exhaustion requirement is a hard sequencing precondition, not an optional first step, and building an intake process that lets principals skip straight to Board-style escalation misreads the statute's actual sequencing.")

add("GR2", CAT, "COMPLETE — Session 2",
    "Section 32, read with Schedule Item 6",
    "The Board may accept a VOLUNTARY UNDERTAKING from any person in relation to any matter connected with a contravention of the Act, on such terms as may be prescribed; where a proceeding under S.28 (Board procedure/inquiry) has been instituted, an accepted undertaking may include a further undertaking to publicise the contravention/undertaking. A breach of the undertaking's own terms is a SEPARATELY penalisable violation under the Schedule (Item 6: penalty 'up to the extent applicable for the breach in respect of which the proceedings under section 28 were instituted').",
    "Article 40 (codes of conduct) is the closest adjacent GDPR concept, but it is a drafted, INDUSTRY/ASSOCIATION-level instrument (not an individual, case-specific settlement) developed proactively and approved by a supervisory authority -- GDPR's text has no equivalent to a Board accepting an individual entity's case-specific voluntary undertaking as a way of resolving or forestalling enforcement",
    "N/A",
    "No directly equivalent named statutory mechanism located -- CPPA/AG settlements occur in practice but were not found framed as a distinct, named 'voluntary undertaking' statutory tool with its own dedicated Schedule-penalty consequence for breach",
    "No equivalent",
    "No equivalent",
    "Treat a Board-accepted S.32 voluntary undertaking as a binding, separately enforceable instrument in its own right (with its own Schedule Item 6 penalty exposure for breach) rather than as an informal or purely reputational commitment -- it functions closer to a consent-order/settlement mechanism than to a code-of-conduct membership commitment.",
    "A second genuinely DPDP-specific institutional tool in this category (alongside the mandatory-exhaustion pipeline at GR1): S.32's voluntary-undertaking mechanism functions more like a US regulatory consent-decree/consent-order practice than anything named in the GDPR or CCPA texts reviewed -- GDPR's nearest concept (Art 40 codes of conduct) is a proactive, sector-wide instrument rather than a reactive, case-specific settlement tool, and neither CCPA statute section reviewed names an equivalent case-specific undertaking mechanism with its own dedicated breach-penalty consequence.",
    "Treating a S.32 undertaking as a purely informal, non-binding goodwill gesture with no independent enforcement consequence -- Schedule Item 6 makes a breach of the undertaking's own terms separately penalisable, tied to the same S.28 proceeding, so failing to treat the undertaking's specific commitments as hard compliance deliverables carries real, distinct financial exposure beyond the underlying contravention it was meant to resolve.")

# ============================================================
# CATEGORY 15 — ACCOUNTABILITY AND GOVERNANCE (DPO / general)
# ============================================================
CAT = "15. Accountability and governance (DPO)"

add("AC1", CAT, "COMPLETE — Session 2",
    "Section 8(9), read with DPDP Rules 2025 Rule 9",
    "Every Data Fiduciary (not only SDFs) must publish, in the prescribed manner, the business contact information of EITHER a Data Protection Officer, IF APPLICABLE, OR a person who is able to answer on the Fiduciary's behalf the Data Principal's questions about her personal data's processing -- meaning a DPO is genuinely OPTIONAL for an ordinary Data Fiduciary, with a generic contactable-person fallback; only an SDF faces a MANDATORY DPO appointment (S.10(2)(a), Row SDF2).",
    "Article 37(1)(a)-(c)",
    "GDPR's mandatory-DPO trigger is based entirely on the NATURE of the processing (public-authority status, large-scale systematic monitoring, or large-scale special-category processing) and applies to any qualifying controller/processor regardless of size or any government designation -- materially more organisations are DPO-MANDATED under GDPR's self-executing criteria than under DPDP, where the DPO mandate is gated entirely behind the separate, discretionary SDF-designation event (Row SDF1).",
    "No DPO-equivalent role, mandatory or optional, is named anywhere in the CCPA/CPRA sections reviewed",
    "Partial overlap",
    "No equivalent",
    "Do not assume 'we have no DPO' is DPDP-sufficient merely because the organisation is not (yet) an SDF -- S.8(9)/Rule 9 still requires SOME named, contactable person to be published and reachable for every Data Fiduciary; and separately assess GDPR Art 37 exposure independently, since a materially large set of ordinary (non-SDF) DPDP Data Fiduciaries could still be GDPR-DPO-mandated on the nature of their processing alone.",
    "This row generalises the SDF2 finding to the more common real-world scenario -- most Data Fiduciaries will never be notified as an SDF, so for the great majority of organisations, DPDP simply has NO mandatory-DPO concept at all, only the lighter S.8(9)/Rule-9 named-contact-person fallback. This is a genuinely different governance floor from GDPR's, where DPO-mandatory status turns on processing characteristics any organisation (however small) can trigger on its own. A useful, honest Attack-1 answer: for the median company that is GDPR-DPO-mandated but never becomes a DPDP SDF, DPDP's accountability-governance floor is a lighter build than GDPR's, not a heavier one -- another data point against the reflexive 'DPDP = GDPR-plus' assumption.",
    "Assuming an organisation's existing GDPR-mandated DPO automatically satisfies DPDP's accountability-governance requirements -- it typically over-satisfies the S.8(9)/Rule 9 named-contact-person floor for an ordinary Data Fiduciary, but if that same organisation is later notified as an SDF, the GDPR DPO role must additionally be re-tested against S.10(2)(a)'s SPECIFIC requirements (India residency, direct responsibility to the Board/governing body, formal point-of-contact role for the statutory grievance mechanism) -- a GDPR DPO appointment does not automatically satisfy those India-specific structural requirements.")

add("AC2", CAT, "COMPLETE — Session 2",
    "Section 8(4)",
    "A Data Fiduciary must implement 'appropriate technical and organisational measures to ensure effective observance' of the Act and Rules -- an omnibus, outcome-focused compliance-programme duty. The provision requires the measures to EXIST and be effective; it does not, on its face, separately require the Fiduciary to be able to DEMONSTRATE or document that observance on an ongoing, evidentiary basis.",
    "Article 5(2) + Article 24(1)",
    "GDPR's accountability principle (Art 5(2)) requires the controller to be able to DEMONSTRATE compliance with all the data-protection principles, and Article 24(1) makes this explicit and operational: the controller 'shall implement appropriate technical and organisational measures to ensure and TO BE ABLE TO DEMONSTRATE that processing is performed in accordance with this Regulation' -- an express documentation/evidentiary-trail requirement layered on top of the substantive-measures requirement.",
    "No single omnibus accountability principle of this kind was located; CCPA's closest analogues are narrower and threshold-triggered -- the Article 9 cybersecurity-audit documentation-retention duty (Section 7122(g), five years) and the Article 10 risk-assessment documentation/retention duty (Section 7155(c), also broadly five years) apply only to the specific high-risk processing activities each Article covers, not as a universal documentation mandate for all processing",
    "Partial overlap",
    "No equivalent",
    "Build and retain the demonstrability/documentation evidence trail (records of the specific measures implemented, review dates, responsible owners) as if S.8(4) contained GDPR Art 24(1)'s explicit 'and to be able to demonstrate' language, even though DPDP's text does not use it -- a Board inquiry under S.27/28 will still expect to see evidence, and building only to the substantive-measures half of S.8(4) risks having nothing to show if asked to prove compliance rather than merely assert it.",
    "A subtle but real textual gap worth having precise: GDPR's accountability principle is unusual for making DEMONSTRABILITY an express, freestanding legal requirement in its own right (Art 5(2)'s 'and be able to demonstrate compliance' language, reinforced by Art 24(1)) -- meaning under GDPR, having good security/privacy measures that are NOT documented and evidenced is, on the statute's own terms, itself a form of non-compliance. DPDP's S.8(4) requires the measures to be effective but does not use equivalent explicit demonstrability language; the evidentiary-trail expectation has to be inferred from the Board's practical inquiry/audit powers (S.27/28) rather than being stated as its own principle the way GDPR states it. CCPA's documentation duties exist only for the narrower high-risk-processing subset covered by Articles 9-10, not as a universal principle either.",
    "Building a compliance programme that genuinely implements strong technical/organisational measures but keeps little or no ongoing documentation of WHEN, HOW, and BY WHOM those measures were implemented and reviewed -- this may be defensible against a literalist reading of S.8(4) alone, but it directly fails GDPR's explicit Art 5(2)/24(1) demonstrability requirement for the same organisation, and would leave the Fiduciary with little to show a Board inquiry beyond its own assertions.")

# ============================================================
# DPDP COMMENCEMENT STATUS -- computed automatically per row
# ============================================================
# CRITICAL FINDING from the Session 2 adversarial pass (verified against
# the actual commencement notification, not memory): the DPDP ACT ITSELF
# -- not only the Rules -- commences in three staggered tranches under
# S.1(2), per Notification G.S.R. 843(E) dated 13 November 2025 (the same
# date the Rules were notified under G.S.R. 846(E)):
#
#   TRANCHE 1 (in force from 13 Nov 2025, i.e. already live):
#     Act:   S.1(2), S.2 (definitions), S.18-26 (Data Protection Board
#            establishment/composition/powers), S.35, S.38-43, S.44(1)/(3).
#     Rules: Rules 1, 2, 17-21.
#   TRANCHE 2 (commences 13 Nov 2026 -- ~7 weeks after this build date):
#     Act:   S.6(9) only, S.27(1)(d) only.
#     Rules: Rule 4 (Consent Manager registration/obligations).
#   TRANCHE 3 (commences 13 May 2027 -- ~8 months after this build date):
#     Act:   S.3-5, S.6 (all other subsections), S.7-17 (the ENTIRE
#            substantive obligations/rights chapters -- grounds for
#            processing, notice, consent mechanics, purpose limitation,
#            general obligations incl. security/breach/retention, children,
#            Significant Data Fiduciary, all Data Principal rights,
#            duties, cross-border transfer, exemptions), S.27 (other than
#            (1)(d)), S.28-34, S.36-37, S.44(2).
#     Rules: Rules 3, 5-16, 22, 23.
#
# PRACTICAL CONSEQUENCE: as of this matrix's build date (22 Sep 2026),
# virtually every DPDP obligation this matrix analyses is NOT YET LIVE
# LAW -- only the Data Protection Board's institutional existence (S.18-26)
# and the Act's definitions/procedural scaffolding are currently operative.
# The matrix deliberately analyses the Act AS ENACTED (the law a compliance
# programme must build toward), because that is the only version worth
# building to -- but every row states plainly whether the cited provision
# is live today, and the README states this Tranche-3 date as the single
# most important caveat in the whole project. See SESSION_2_NOTES.md for
# the verification trail (three independent sources cross-checked against
# the notification text itself).
import re

ACT_TRANCHE_1 = set([1, 2, 18, 19, 20, 21, 22, 23, 24, 25, 26, 35, 38, 39, 40, 41, 42, 43])
RULE_TRANCHE_1 = set([1, 2, 17, 18, 19, 20, 21])
RULE_TRANCHE_2 = set([4])
# Everything else cited in this matrix (Act S.3-17, 27-34, 36-37, 44(2);
# Rules 3, 5-16, 22, 23) defaults to Tranche 3. Section 44 and Section 27
# are handled generically (Tranche 3) since no row in this matrix cites
# S.44(1)/(3) or S.27(1)(d) alone/in isolation -- if a future row did,
# it would need a row_id-keyed override added to STATUS_OVERRIDES below.

STATUS_TEXT = {
    1: "IN FORCE (since 13 Nov 2025, per G.S.R. 843(E)/846(E))",
    2: "NOT YET IN FORCE -- commences 13 Nov 2026 (G.S.R. 843(E), Tranche 2 / Rule 1(3))",
    3: "NOT YET IN FORCE -- commences 13 May 2027 (G.S.R. 843(E), Tranche 3 / Rule 1(4))",
}

def commencement_status(dpdp_cite):
    section_nums, rule_nums = [], []
    for start, end in re.findall(r"Sections?\s+(\d+)\s*(?:(?:-|–|to)\s*(\d+))?", dpdp_cite):
        start = int(start)
        end = int(end) if end else start
        section_nums.extend(range(start, end + 1))
    for n in re.findall(r"Rule\s+(\d+)", dpdp_cite):
        rule_nums.append(int(n))

    if not section_nums and not rule_nums:
        return "N/A -- no Act section or Rule number parsed from this citation; verify manually"

    tranches = []
    for s in section_nums:
        tranches.append(1 if s in ACT_TRANCHE_1 else 3)
    for r in rule_nums:
        if r in RULE_TRANCHE_1:
            tranches.append(1)
        elif r in RULE_TRANCHE_2:
            tranches.append(2)
        else:
            tranches.append(3)
    return STATUS_TEXT[max(tranches)]

# Row-specific supplementary notes appended to the computed status where
# the citation spans more than one tranche and the SEQUENCING itself is
# part of the finding (not just "not yet in force").
STATUS_OVERRIDES = {
    "C6": (" | NOTE: this row's citation spans two tranches -- Rule 4 and "
           "S.6(9) (Consent Manager registration mechanics) commence "
           "earlier, 13 Nov 2026, but the underlying S.6(7)-(8) right for "
           "a Data Principal to give/manage/withdraw consent THROUGH a "
           "Consent Manager does not itself become live until 13 May 2027 "
           "-- so a registered Consent Manager could theoretically exist "
           "from Nov 2026 with no live statutory consent-routing duty for "
           "~6 more months."),
    "GR1": (" | NOTE: the Data Protection Board (S.18-26) is already "
            "institutionally constituted and operational (Tranche 1) -- "
            "but the individual grievance right it would adjudicate "
            "(S.13(3)) and the Tribunal appeal pathway (S.29-32) are both "
            "Tranche 3. Today the regulator exists but has no live "
            "individual-complaint jurisdiction under this Act to exercise."),
}

for r in rows:
    row_id, dpdp_cite = r[0], r[3]
    status = commencement_status(dpdp_cite)
    status += STATUS_OVERRIDES.get(row_id, "")
    r.insert(4, status)

# ============================================================
# Build DataFrame, write CSV + XLSX
# ============================================================
df = pd.DataFrame(rows, columns=COLUMNS)

csv_path = "../matrix/compliance_matrix.csv"
xlsx_path = "../matrix/compliance_matrix.xlsx"

df.to_csv(csv_path, index=False)

with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Matrix")
    ws = writer.sheets["Matrix"]
    from openpyxl.utils import get_column_letter
    from openpyxl.styles import Alignment, Font, PatternFill

    widths = {
        "A": 10, "B": 28, "C": 20, "D": 30, "E": 38, "F": 55, "G": 22, "H": 55,
        "I": 40, "J": 16, "K": 16, "L": 45, "M": 65, "N": 55,
    }
    for col, w in widths.items():
        ws.column_dimensions[col].width = w

    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="1F4E78")
        cell.alignment = Alignment(wrap_text=True, vertical="top")

    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[row[0].row].height = 120

    ws.freeze_panes = "A2"

print(f"Wrote {len(df)} rows to {csv_path} and {xlsx_path}")
print(df["Status"].value_counts())
