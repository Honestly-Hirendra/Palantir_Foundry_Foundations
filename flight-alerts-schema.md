# Ontology Schema — Flight Alerts
## Palantir Foundry Foundations — Hirendra Basantani

---

## Object Type: (Hirendra) Flight Alerts

| Field | Value |
|---|---|
| API Name | HirendraFlightAlerts |
| Ontology | Hirendra_project Ontology |
| Total Objects | 183,999 |
| Status | Experimental |
| Index Status | Indexed |
| Edits | Enabled |

---

## Properties (27 total)

| Property | Type |
|---|---|
| Alert Title | String (Primary) |
| Flight Alert Id | String (Key) |
| Airline Route Id | String |
| Alert Reason | String |
| Arrival Delay | Double |
| Cancellation Reason | String |
| Cancelled | String |
| Carrier Delay | Double |
| *(+ 19 additional properties)* | |

---

## Link Types

| From | To | Relationship |
|---|---|---|
| [OFT] Flight | (Hirendra) Flight Alerts | Flight has Alerts |

---

## Action Types

| Action | Modifies |
|---|---|
| Assign Root Cause | (Hirendra) Flight Alerts |

---

## Dependents

- Object View: 3 views
- Workshop: 3 applications
  - (Hirendra) Flight Alerts — Full Object View — Overview Tab
  - (Hirendra) Flight Alerts — Panel Object View — Object Instance
  - (Hirendra) Flight Alerts — Panel Object View — Object Set
