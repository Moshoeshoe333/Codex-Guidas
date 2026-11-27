# DEF-2026-003 — Raw scan content is retained in AsyncStorage

- **State:** Investigating
- **Severity:** S4 (source-level privacy/security observation; user impact and exploitability not established)
- **Date detected:** 2026-11-27
- **Last updated:** 2026-11-27
- **Owning project/repository:** SoulSyncMobile — `Moshoeshoe333/SOULSYNCMOBILE`
- **Affected branch/ref:** `main`
- **Affected full commit SHA:** `1f50bd3387c61d51868140ec3776b94150a2d4c6` (rechecked 2026-11-27)
- **Owner:** SoulSyncMobile project maintainer (to be assigned)
- **Related issue/PR/CI run/log:** None; no exploitation, device extraction or user impact is claimed
- **Related lessons:** CG-002, CG-011, CG-026 and CG-052
- **Reporter/source:** Codex-Guidas source review prompted by 2026-11-27 AI mathematics and cryptographic security review

## 1. Summary

At the inspected application baseline, the scan hook places the complete supplied message text into each `IncidentLog`, and the storage manager serialises the incident collection to React Native AsyncStorage. React Native documents AsyncStorage as an unencrypted key-value store. The application source inspected here does not encrypt the incident payload before writing it.

This creates a potential privacy/security exposure if users scan messages containing OTPs, passwords, banking details, personal identifiers, token-bearing URLs or other sensitive information. No actual sensitive message, data extraction, unauthorised access or production impact was observed.

## 2. Expected behaviour

The owning project must define an explicit data-classification and retention contract for scanned input. Sensitive message content should not be retained inadvertently or by default. If raw-content retention is genuinely required, the project must approve an appropriate storage, key-management, access, deletion, backup and recovery design before implementation.

The current `SECURITY.md` advises that passwords, authentication tokens, banking credentials, ID numbers and sensitive personal data must not be included in logs or reports. The project owner must clarify how that rule applies to the persistent incident ledger, which currently stores the entire scanned input.

## 3. Observed behaviour

At application baseline `1f50bd3387c61d51868140ec3776b94150a2d4c6`:

1. `src/hooks/useGuardianState.ts` builds an incident using `input: { text: textInput, source }`.
2. The hook passes the complete incident array to `storageManager.saveIncidentLogs(nextIncidents)`.
3. `src/storage/storageManager.ts` calls `AsyncStorage.setItem(INCIDENTS_KEY, JSON.stringify(logs))` without application-level payload encryption in this path.
4. `src/types/index.ts` defines `ScanInput.text` as a string and embeds `ScanInput` in `IncidentLog`.
5. The hook's `exportLedgerAsJSON` function serialises the full incident records, including their input text, if called.

Relevant source blobs are recorded in E-001 through E-004 below. React Native's official security documentation identifies AsyncStorage as unencrypted and advises against its use for secrets. OWASP separately identifies sensitive unencrypted data in private app storage as a mobile storage weakness.

The fact that an app API uses unencrypted storage does not establish that other ordinary applications can read the data; operating-system sandboxing and device-level encryption are separate protections. It does establish that this application code does not apply its own cryptographic protection to the incident payload before persisting it.

## 4. Impact and scope

- **Actual impact:** None established. No real user data, extraction, unauthorised access, breach or user report was inspected.
- **Potential impact:** If scanned content contains secrets or personal/financial information, that material may remain in the app's persistent local storage and could be exposed in a compromised device/app, an accessible backup or another storage-disclosure scenario.
- **Affected users/data/components:** Potentially any user who scans and retains sensitive message content; incident ledger, in-memory incident state and JSON export method.
- **Scope known or unknown:** The source data flow is identified at the stated commit. Physical device behaviour, backup configuration, platform-level protection, installed-build status, user retention expectations and real-world data exposure remain unknown.
- **Workaround / containment:** No tested workaround is established in this record. Until the owner decides the policy, avoid scanning real credentials, OTPs, banking secrets or other highly sensitive material in development builds; use synthetic examples for testing.

## 5. Evidence ledger

| Evidence ID | Type | Exact ref (commit/run/log) | Observation | Limitation |
|---|---|---|---|---|
| E-001 | Source | `SOULSYNCMOBILE` `src/hooks/useGuardianState.ts`, blob `db52b38fd4c9f8909f33df78c8e2752e18993fe2`, app commit `1f50bd3387c61d51868140ec3776b94150a2d4c6` | Incident object includes the full `textInput` value | Source inspection; no device run |
| E-002 | Source | `SOULSYNCMOBILE` `src/storage/storageManager.ts`, blob `17859deeb96a9fb87353151014ca3982e5668c62` at same app commit | Incident collection is serialised and written through AsyncStorage without payload encryption in this code path | Source inspection does not determine OS-level encryption or actual backup exposure |
| E-003 | Contract | `SOULSYNCMOBILE` `src/types/index.ts`, blob `204074d2ff8198c1e7036133f53d0a709062b0cf` at same app commit | `IncidentLog.input` contains `ScanInput`; `ScanInput.text` is a string | Type definition does not determine sensitivity or retention intent |
| E-004 | Policy | `SOULSYNCMOBILE` `SECURITY.md`, blob `8cc466afdec075fa5990076d643ca8fdcc31d53d` at same app commit | Advises not to include credentials and sensitive personal/financial information in logs/reports | Does not explicitly define incident-ledger retention |
| E-005 | Framework documentation | [React Native Security](https://reactnative.dev/docs/security) | Official documentation describes AsyncStorage as an unencrypted key-value store and advises against using it for secrets | General framework guidance; does not prove this app has been compromised |
| E-006 | Security standard | [OWASP MASVS-STORAGE](https://mas.owasp.org/MASVS/05-MASVS-STORAGE/) and [MASWE-0001](https://mas.owasp.org/MASWE/MASVS-STORAGE/MASWE-0001/) | Sensitive local data must be protected; unencrypted private storage is a recognised weakness when sensitive data is involved | Applicability/severity depends on data classification and threat model |
| E-007 | Source | `SOULSYNCMOBILE` `src/hooks/useGuardianState.ts`, same blob as E-001 | `exportLedgerAsJSON` serialises the full incident records if called | No UI call site or external export event is established by this finding |

## 6. Root-cause analysis

- **Status:** Suspected data-protection/retention contract gap; source data flow confirmed.
- **Hypothesis:** The application has not yet established whether original scanned content is required to be retained, for how long, or under what protection. The implementation currently persists raw text in a store that React Native documents as unencrypted.
- **Evidence supporting:** E-001 through E-006.
- **Evidence contradicting:** No evidence inspected establishes that the application has already exposed data; OS sandboxing and device encryption may add protections not visible in this code path.
- **Discriminating work still needed:** Owner review of intended product behaviour and data-classification contract; synthetic persistence/backup/export tests; platform-specific device assessment where approved.

Do not call this a confirmed breach, exploit or root cause for a real-world incident. The source behaviour is observed; impact and threat applicability need triage.

## 7. Similarity search

- **Search terms:** raw SMS retention; sensitive local data; AsyncStorage; unencrypted private storage; mobile data minimisation; secret redaction; data retention
- **Lesson IDs searched:** CG-002, CG-011, CG-026, CG-052
- **Prior defect IDs:** DEF-2026-001 and DEF-2026-002 concern storage hydration and multi-key consistency; they are not the same security/privacy issue.
- **Similarity result:** Related to evidence and storage boundaries, but a separate data-classification and confidentiality concern. Do not combine it with the multi-write atomicity defect.

## 8. Corrective action

None authorised or implemented. First obtain the project owner's decision on:
- whether raw input needs to be retained at all;
- whether retention is opt-in or default;
- the allowed data categories and redaction policy;
- retention duration and deletion semantics;
- the encrypted-storage and key-management requirements if retention remains necessary;
- backup, export, crash/log and recovery behaviour.

Do not select SecureStore, SQLite, an encrypted database, Rust, a custom cipher or any migration solely from this finding.

## 9. Preventive and detective controls

**Proposed, not implemented:**
- Default to not persisting raw message text unless a documented product need and explicit owner approval justify it.
- Minimise stored data to derived indicators, policy outcome and necessary metadata, with a documented false-positive/false-negative and retention analysis.
- Define synthetic redaction tests for dummy OTPs, tokens, account numbers and identity-like values.
- Check persisted bytes, exports, logs, crash reports, screenshots, backups and deletion.
- If raw retention is approved, use a vetted platform-supported encryption design with keys separated from ciphertext and documented rotation, recovery and loss behaviour.
- Test key unavailability, corrupted records, device restore and user-requested deletion without silently falling back to plaintext.

## 10. Regression and acceptance evidence

| Check | Command / procedure | Environment | Exact commit | Expected | Actual | Evidence link |
|---|---|---|---|---|---|---|
| P-01 | Synthetic sentinel scan; inspect persisted storage bytes | Not run | Target SHA above | Stored content matches approved minimisation/encryption policy; no prohibited sentinel remains in plaintext | Not run | Pending |
| P-02 | Exercise ledger export with synthetic secret markers | Not run | Target SHA above | Export follows approved redaction/consent policy | Not run | Pending |
| P-03 | Inspect backup, logs, crash output and app-switcher/screenshot leakage | Not run | Target SHA above | No unintended sensitive-content disclosure | Not run | Pending |
| P-04 | Verify retention expiry and clear-history deletion, including restart | Not run | Target SHA above | Data is deleted according to the approved policy and not silently restored | Not run | Pending |

## 11. Residual risk and follow-up

The project owner has not yet approved the raw-input retention and protection contract. No device extraction, app backup, compromised-device or actual user-data test has been performed. Severity remains S4 pending impact and threat-model assessment; re-triage if the app is handling real sensitive user input or a credible exposure scenario is demonstrated.

## 12. Closure decision

- **Decision:** Keep open / Investigating
- **Approver/authority:** SoulSyncMobile project owner
- **Acceptance criteria met:** No
- **Reason:** Data classification, retention, protection requirements and platform evidence are unresolved.
- **Closure evidence:** None

## 13. Record propagation and synchronization

- **Canonical DEF record path:** `11-defect-intelligence/DEF-2026-003-raw-scan-content-retained-in-asyncstorage.md`
- **Defect README register updated:** Yes — commit `45efb9da1a4ce23ca0f2e1041925417757ead169`
- **Chronological ledger follow-up added or linked:** CG-052 added in commit `14a081dd2249e6a44de589d4e99a34ff7d8723df`; no defect-specific chronology note is needed yet
- **Upstream source/run rechecked directly:** Yes — GitHub source blobs re-fetched for app baseline `1f50bd3387c61d51868140ec3776b94150a2d4c6`; React Native and OWASP guidance reviewed
- **Exact tested commit and current project HEAD distinguished:** Yes; source check only, not test evidence
- **Historical statements dated or qualified:** Yes
- **Related links checked:** Yes — research note and defect-register entry read back
- **Atomic change / commit identity:** Detailed DEF created in `4df8ca60212a6a83b8b8e530b83453d70e4b0053`; register/lesson propagation followed in separate commits. These are linked documentation updates, not a single atomic multi-file commit.

## 14. Reusable lesson

Existing CG-011, CG-026 and CG-052 provide relevant boundaries. CG-052 is a broader crypto-agility lesson; it does not itself verify this project's local data storage. This record may inform a privacy-by-design lesson after owner triage and project-specific verification.
