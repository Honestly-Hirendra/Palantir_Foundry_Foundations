# Architecture Documentation
## Palantir Foundry Foundations — Hirendra Basantani

---

## System Overview

This program covers four distinct Foundry workstreams, each using a different dataset and Foundry capability layer. Together they demonstrate end-to-end platform proficiency.

---

## Workstream 1: Manufacturing Quality Analysis (Contour — Step 2)

**Dataset:** Parts & Equipment (2,176 rows, 5 plants)

**Data Flow:**
```
parts (2,176 rows) ──┐
                     ├── Parts-Equipment Join (on equipment_id)
equipment ───────────┘
                          └── Avg_Purity (window function)
                               └── Inspection Alert Histogram
                               └── Count of Parts by Plant
                               └── Count of Parts by Equipment & Avg Purity
```

**Key Insight:** EQUIP002 processes the highest volume (942 parts) with avg purity 0.89. 61% of all inspections are high-alert, indicating quality control pressure across the fleet.

---

## Workstream 2: Insurance Claims Pipeline (Code Repositories — Step 4)

**Dataset:** Claims & Policies

**Transform Logic:**
```
claims_raw → clean date (strip ###) → filter is_accepted==True
policies ──────────────────────────► left join on policy_id
                                          └── groupBy(line_of_business)
                                               └── avg(claim_value) → claims
```

---

## Workstream 3: Aviation Ontology & Workshop App (Steps 5-6)

**Dataset:** Flight Alerts (183,999 objects)

**Ontology Structure:**
```
[OFT] Flight
    └── linked to ──► (Hirendra) Flight Alerts
                        ├── Properties (27): Alert Title, Flight Alert ID,
                        │   Airline Route ID, Alert Reason, Arrival Delay,
                        │   Cancellation Reason, Carrier Delay, Cancelled...
                        └── Action: Assign Root Cause (write-back enabled)
```

---

## Workstream 4: RAG Pipeline + AIP Logic (Steps 7-8)

**Dataset:** Research Articles (PDF)

**Full Pipeline DAG:**
```
Articles (PDF)
    └── Process PDFs (5 cols)
         └── Extract Chunk (6 cols)
              └── Create Chunk ID (7 cols)
                   └── Data Modification (10 cols)
                        └── Use LLM (11 cols)
                             ├── Get Entities (13 cols)
                             │    └── Deduplicate → Hirendra_Entities [deployed]
                             └── Embedded Chunks (12 cols)
                                  └── Hirendra_Chunks [deployed]
```

**AIP Logic Function:**
```
Input: askQuestion
    └── Semantic Search on Hirendra Chunks
         └── Format chunks as string context
              └── Use LLM (grounded generation)
                   └── Output: AI Response
```
