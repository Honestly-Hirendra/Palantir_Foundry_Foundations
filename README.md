# Palantir Foundry Foundations — Hirendra Basantani

![Palantir Foundry](https://img.shields.io/badge/Palantir-Foundry-0a0a0f?style=for-the-badge&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![AIP](https://img.shields.io/badge/AIP_Logic-LLM_Powered-1a1aff?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG_Pipeline-Knowledge_Graph-ff3c00?style=for-the-badge)
![Status](https://img.shields.io/badge/All_8_Steps-Completed-28a745?style=for-the-badge)

> End-to-end Palantir Foundry portfolio — manufacturing inspection analytics, production PySpark pipelines, aviation ontology with 183,999 objects, Workshop application, and a full RAG pipeline powered by AIP Logic. Completed as part of the **Analyticore Foundry Foundations Entry Program**.

---

## What Makes This Work Stand Out

- ★ Built a **complete end-to-end RAG AI system**: PDF ingestion → LLM entity extraction → Knowledge Graph → AIP Agent → interactive Q&A application
- ★ Mastered **Contour's visual-to-code translation** — every board operation mapped to reproducible PySpark logic
- ★ Modelled a **manufacturing inspection ontology** with custom object types, relationships, and action types
- ★ Created production-grade pipelines in both **low-code (Pipeline Builder) and full-code (Code Repositories)**
- ★ Delivered a **live Workshop application** powered by the Ontology for real-time operational decision-making
- ★ Demonstrated the rarest skill in the program: **connecting ALL layers of Foundry into a single coherent workflow**

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        PALANTIR FOUNDRY — FULL STACK                            │
├──────────────┬──────────────────┬──────────────────┬──────────────────────────┤
│  INGEST      │  TRANSFORM       │  SEMANTIC LAYER  │  APPLICATIONS            │
├──────────────┼──────────────────┼──────────────────┼──────────────────────────┤
│              │                  │                  │                          │
│  Raw PDFs    │  Pipeline Builder│  Ontology        │  Workshop App            │
│  Sensor data │  Code Repos      │  (Equipment,     │  (tables, charts,        │
│  Inspection  │  (PySpark)       │   Plant,         │   search, actions)       │
│  records     │  Contour         │   Inspection,    │                          │
│              │  (visual)        │   Flight Alerts, │  AIP Logic Function      │
│              │                  │   Chunks,        │  (semantic search        │
│              │                  │   Entities)      │   + LLM answer)          │
│              │                  │                  │                          │
│              │         ↓        │        ↓         │          ↓               │
│              │  OPERATIONAL INTELLIGENCE (inspect right equipment, AI-supported)│
└─────────────────────────────────────────────────────────────────────────────────┘
```

**RAG Pipeline DAG (Step 8 capstone):**
```
Articles (PDF)
    └── Process PDFs (5 cols)
         └── Extract Chunk (6 cols)
              └── Create Chunk ID (7 cols)
                   └── Data Modification (10 cols)
                        └── Use LLM (11 cols)
                             ├── Get Entities (13 cols)
                             │    └── Deduplicate → Hirendra_Entities [deployed]
                             │    └── Get Join Table → Joined Table [deployed]
                             └── Embedded Chunks (12 cols)
                                  └── Hirendra_Chunks [deployed]
```

**AIP Logic Function:**
```
Input: askQuestion
    └── Semantic Search on Hirendra Chunks
         └── Format retrieved chunks as string context
              └── Use LLM (grounded generation — zero hallucination)
                   └── Output: AI Response
```

---

## Six-Course Overview

| Course | Focus Area | Key Outcome |
|--------|-----------|-------------|
| 1 — Contour: Deep Dive Data Analysis | Visual transformation, cleaning, joining, derived columns & dashboards | Manufacturing inspection dashboard with window functions |
| 2 — Pipeline Builder: First Pipeline | Low-code/no-code Spark pipelines; branching, scheduling, validation | Production data flow with incremental compute |
| 3 — Code Repositories: First Transforms | PySpark transforms, joins, aggregations, Data Lineage, Job Tracker | Engineering-grade insurance claims pipeline |
| 4 — Ontology: Deep Dive | Semantic object model; object types, relationships, actions | 183,999 aviation flight alert objects with write-back actions |
| 5 — Workshop: First Application | Ontology-powered interactive app with tables, charts, search, actions | Live manufacturing inspection app for operational decisions |
| 6 — AIP Speedrun: First E2E Workflow | LLM batch processing, Knowledge Graph, AIP Agent, Q&A app | Full RAG pipeline with knowledge-graph-grounded answers |

---

## Step-by-Step Breakdown

### Step 1 — Environment Setup
Set up Palantir AIP Developer trial workspace via the official developer portal. Configured project namespace and verified environment readiness.

### Step 2 — Data Exploration and Analysis in Contour

**Dataset:** Manufacturing parts & equipment (2,176 rows, 5 plants — EQUIP001–005)

Built a multi-step Contour analysis pipeline:
- Loaded raw datasets, reviewed structure and quality with summary statistics
- Renamed/dropped columns, standardized values, converted data types (string → date/numeric)
- Joined `parts` with `equipment` on `equipment_id`
- Derived `Avg_Purity` column: `AVG(part_purity) OVER (PARTITION BY equipment_id)`
- Generated `Inspection_Alert` flags with conditional logic (high/medium/low)
- Built Histogram, Pivot Table, and Average Purity Chart → assembled into unified Dashboard

**Key findings:**
- **1,331 high-alert** inspections (61% of total) — quality control pressure fleet-wide
- EQUIP002 highest purity avg (0.89) with highest volume (942 parts)
- EQUIP005 lowest avg purity (0.82) — potential maintenance priority

**Contour → Code translation:**

| Contour Board | Equivalent PySpark/SQL |
|---|---|
| Filter Board | `df.filter(condition)` / `WHERE` clause |
| Join Board | `df.join(other, on='key', how='left')` |
| Expression Board | `df.withColumn('new_col', expression)` |
| Aggregate Board | `df.groupBy().agg(sum, mean, count_distinct)` |
| Pivot Board | `df.groupBy().pivot().agg()` |

### Step 3 — Building Your First Pipeline
Built a production-grade pipeline in Pipeline Builder connecting raw datasets through materialized transformations. Configured branching, build schedules, and data validation steps for downstream consumption.

### Step 4 — Transforming Data with Code Repositories

**Dataset:** Insurance claims & policies

Replicated all Contour logic in production PySpark. The core transform:

```python
from pyspark.sql import functions as F
from pyspark.sql import types as T
from transforms.api import transform_df, Input, Output

@transform_df(
    Output("/Hirendra_project-829831/Learning (Hirendra)/Code Repo Training/Prepared/claims"),
    claims_df=Input("ri.foundry.main.dataset.3bbe6bea-9476-4ce2-a470-1af7b9d2f145"),
    policies_df=Input("ri.foundry.main.dataset.63c4572e-1126-45dc-bf1a-b5555d871bc0"),
)
def compute(claims_df, policies_df):
    # 1. Clean malformed date column — strip '###' artifacts
    claims = claims_df.withColumn(
        "date", F.regexp_replace("date", "###", "").cast(T.DateType())
    )
    # 2. Keep only accepted claims
    claims = claims.filter(F.col("is_accepted") == True)
    # 3. Enrich with policy metadata
    claims = claims.join(policies_df, on="policy_id", how="left")
    # 4. Aggregate: average claim value per line of business
    return claims.groupBy("line_of_business").agg(
        F.avg("claim_value").alias("avg_claim_cost")
    )
```

Used Data Lineage to trace field origins and Job Tracker to monitor pipeline performance.

### Step 5 — Creating Your First Ontology

**Dataset:** Aviation flight alerts (183,999 objects)

Designed a semantic object model:

| Field | Value |
|---|---|
| Object type | (Hirendra) Flight Alerts |
| API name | `HirendraFlightAlerts` |
| Total objects | **183,999 indexed** |
| Properties | 27 (Alert Title, Flight Alert ID, Airline Route ID, Arrival Delay, Cancellation Reason, Carrier Delay...) |
| Link type | `[OFT] Flight` → `(Hirendra) Flight Alerts` |
| Action type | **Assign Root Cause** (write-back to ontology) |

> *The Ontology is not just a data model — it is the operational vocabulary of an entire organization. When equipment, plants, and inspections are modelled as first-class objects with relationships and actions, every application and AI agent shares the same ground truth.*

### Step 6 — End-to-End Application (Workshop)

Built a Workshop application with 21 modules backed by the Flight Alerts ontology:
- Full Object View — individual alert investigation
- Panel Object View — Object Instance and Object Set browsing
- Action-enabled interface: users can **Assign Root Cause** directly from the app, writing decisions back to the ontology as auditable events

### Step 7 — AIP End-to-End Workflow

Built an **AIP Logic function** for knowledge-graph-grounded Q&A:

```
Input: askQuestion (string)
  └─► Semantic Search on Hirendra Chunks
       └─► Format retrieved chunks as string context
            └─► Use LLM (context-grounded — zero hallucination)
                 └─► Output: AI-generated answer
```

The AIP Agent retrieves answers from structured Ontology objects, not open-ended LLM memory — eliminating hallucination for operational use.

### Step 8 — Exploration and Extension (RAG Capstone)

Built the complete **Retrieval-Augmented Generation pipeline** as the program capstone:

- Semantic chunking of PDF content with unique chunk IDs
- LLM-based named entity extraction across all chunks
- Entity deduplication and join to produce a clean knowledge graph
- **30+ entity nodes** visible in the knowledge graph visualization
- Workshop Q&A application: "Ask A Question" → semantic retrieval → LLM answer grounded in graph
- "Filter in Books" UI — scope search to specific source documents

---

## Foundry Capability Coverage

| Capability | Tool | Step |
|---|---|---|
| Visual data exploration | Contour | 2 |
| No-code pipeline orchestration | Pipeline Builder | 3 |
| Production transforms | Code Repositories (PySpark) | 4 |
| Semantic data modeling | Ontology Manager | 5 |
| Operational application | Workshop (21 modules) | 6 |
| LLM-powered workflows | AIP Logic | 7 |
| RAG + entity extraction + knowledge graph | Pipeline + AIP + Workshop | 8 |

---

## Key Transferable Skills

| Skill Category | Competency Demonstrated |
|---|---|
| Data Engineering | PySpark transforms, joins, aggregations, incremental compute, pipeline scheduling |
| Data Analysis | Visual transformation in Contour, expression language, summary statistics |
| Semantic Modelling | Ontology design — object types, relationships, actions, operational vocabulary |
| AI/ML Engineering | LLM entity extraction, RAG pipeline, AIP Agent, Knowledge Graph |
| Application Development | Workshop app — tables, charts, search, link types, action capture |
| Data Governance | Data lineage tracing, job tracking, branching, unit test gating |

---

## Repository Structure

```
palantir-foundry-foundations/
├── README.md
├── pipeline-code/
│   └── claims_transform.py          # Production PySpark transform (Step 4)
├── docs/
│   └── architecture.md              # Full data flow documentation
├── ontology-design/
│   └── flight-alerts-schema.md      # Object types, properties, relationships
├── screenshots/                     # Foundry UI screenshots (add yours here)
│   └── README.md                    # Screenshot index
└── resources/
    └── program-structure.md         # 6-course program overview
```

---

## Program Context

Completed as part of the **Palantir Foundry Foundations Entry Program** prepared by Sainath Palla at [Analyticore](https://analyticorex.com) — an independent training and evaluation initiative, not affiliated with Palantir.

> *"Only a small fraction of applicants complete this program end to end. The depth required filters for consistency and independent problem-solving."*

---

## Author

**Hirendra Basantani**  
[LinkedIn](https://linkedin.com/in/) · [GitHub](https://github.com/)

---

## Portfolio Showcase

An interactive HTML portfolio page for this project is available at [`palantir_showcase.html`](./palantir_showcase.html) — open in any browser for the full visual presentation.
