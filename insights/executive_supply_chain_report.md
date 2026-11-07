# ShelfSync FMCG Supply Chain Diagnostic Report: The OTIF Crisis

**Prepared for:** Operating Committee, Chief Supply Chain Officer (CSCO), VP of Modern Trade  
**Domain:** Fast-Moving Consumer Goods (FMCG)  
**Reporting Period:** Calendar 2024 through Q1 2025  
**Data Scope:** 3,800 Orders | 15,166 Order Lines | 20 Key Retail Customers | 6 Regional Hubs | 28 Core SKUs  

---

## 1. Executive Summary: The "Fill Rate Illusion"

ShelfSync FMCG achieved **$9.73 Million in Gross Purchase Orders** over the 15-month analysis window. On the surface, internal logistics operations reported an aggregate **Volume Fill Rate of 95.73%**, leading internal teams to believe supply chain operations were performing smoothly.

However, modern retail trade (Hypermarkets, Supermarkets, and Quick Commerce) does not evaluate suppliers by aggregate tonnage. They evaluate performance on **OTIF: On-Time In-Full delivery at the purchase order level**. 

The customer-facing reality is a full-blown operational crisis:
- **Contractual SLA Target:** $\ge 92.00\%$ OTIF across modern retail accounts.
- **Actual OTIF Delivered:** **39.18%** (a catastrophic **52.6 percentage point shortfall**).
- **On-Time (OT) %:** **76.66%** (1 in 4 shipments arrives late).
- **In-Full (IF) %:** **51.47%** (nearly 1 in 2 orders has missing SKUs or short shipments).

```
+-----------------------------------------------------------------------------------------+
|                                 THE SERVICE LEVEL GAP                                   |
|                                                                                         |
|   Volume Fill Rate (What Operations Sees):   [█████████████████████████████████] 95.7%  |
|   Target SLA (What Retailers Expect):        [██████████████████████████████░░░] 92.0%  |
|   On-Time (OT) Performance:                  [██████████████████████░░░░░░░░░░░] 76.7%  |
|   In-Full (IF) Performance:                  [███████████████░░░░░░░░░░░░░░░░░░] 51.5%  |
|   Actual OTIF Delivered (Customer Reality):  [███████████░░░░░░░░░░░░░░░░░░░░░░] 39.2%  |
+-----------------------------------------------------------------------------------------+
```

### The Financial Bleed: $614,087.58 (6.31% of Gross Revenue)
This fulfillment collapse has directly destroyed bottom-line profitability through two concurrent drains:
1. **$420,261.80 in Lost Sales (Stockouts & Cancellations):** Retailers reject backorders or permanently cancel unfilled quantities. Direct competitor brands fill the empty shelf space.
2. **$193,825.78 in Contractual SLA Penalties:** Modern trade agreements impose strict 2.0% to 5.0% penalties on failed delivery orders. These are deducted straight from cash receivables (chargebacks).

---

## 2. Deep-Dive Diagnostic: Where and Why the Supply Chain is Failing

### Finding 1: The North Regional Choke Point (WH-North-01)
Regional analysis reveals a severe operational disparity across ShelfSync's distribution network:

| Warehouse | Hub Location | Region | Orders Fulfilled | OT % | IF % | OTIF % | Avg Variance (Days) | SLA Penalties Incurred |
|---|---|---|---|---|---|---|---|---|
| **WH-CENTRAL-01** | Nagpur Transit Hub | Central | 926 | **84.13%** | 54.64% | **45.57%** | +0.27 days | $39,528.49 |
| **WH-SOUTH-02** | Sriperumbudur Depot | South | 494 | **83.81%** | 51.42% | **42.51%** | +0.25 days | $27,789.81 |
| **WH-EAST-01** | Dankuni DC | East | 264 | **81.44%** | 48.86% | **38.64%** | +0.30 days | $9,322.91 |
| **WH-WEST-01** | Bhiwandi Central | West | 731 | **80.71%** | 49.52% | **39.53%** | +0.31 days | $39,540.73 |
| **WH-SOUTH-01** | Hosakote Logistics | South | 489 | **78.73%** | 52.35% | **41.92%** | +0.37 days | $26,177.59 |
| **WH-NORTH-01** | Gurugram North | North | 896 | **59.15%** | 50.11% | **29.13%** | **+0.69 days** | **$51,466.25** |

**Root Cause Analysis:**
- Gurugram North Gateway (`WH-NORTH-01`) is an unautomated facility operating at 114% of rated throughput capacity.
- The average order turnaround is delayed by **+0.69 days (over 16 hours of dispatch lag)** due to manual pallet consolidation, dock congestion, and delayed E-Way Bill documentation.
- Consequently, On-Time delivery dropped to **59.15%**, making it the single largest contributor to customer penalties ($51.5K).

---

### Finding 2: The Quick Commerce SLA Trap
Modern retail channels operate with vastly different commercial expectations:

| Customer Channel | Orders | Actual OTIF % | SLA Target % | SLA Gap (% pts) | Penalty Rate | Total Penalties ($) | Total Lost Sales ($) |
|---|---|---|---|---|---|---|---|
| **Quick Commerce** | 805 | **37.52%** | **95.35%** | **-57.83%** | **5.0%** | **$68,267.30** | $93,369.30 |
| **Hypermarket** | 1,179 | **41.14%** | **91.42%** | **-50.29%** | **3.0%** | **$55,599.90** | $125,847.20 |
| **Supermarket** | 731 | **40.49%** | **89.82%** | **-49.33%** | **2.5%** | **$25,665.12** | $78,650.30 |
| **E-Commerce** | 327 | **35.47%** | **93.51%** | **-58.03%** | **4.0%** | **$20,814.45** | $36,983.30 |
| **Wholesale / Cash & Carry** | 474 | **33.33%** | **88.00%** | **-54.67%** | **2.0%** | **$17,125.62** | $56,696.40 |
| **Convenience Store** | 284 | **46.48%** | **85.00%** | **-38.52%** | **1.5%** | **$6,353.39** | $28,715.30 |

**Critical Strategic Finding:**
- Quick Commerce (`ZeptoGo Rapid`, `UrbanBasket Express`, `QuickDrop Grocery`) accounts for **only 21.2% of order volume, but generates 35.2% of all financial penalties** ($68.3K).
- Why? Quick Commerce demands ultra-compressed lead times (24 to 48 hours). When ShelfSync's average turnaround is 3.1 days, these orders fail by default, triggering severe 5.0% contractual chargebacks.

---

### Finding 3: Perishability & Summer Cold-Chain Collapse in Dairy
Looking at line item fulfillment across the 5 FMCG product categories:

| Product Category | Total Lines | Line OT % | Line IF % | Line OTIF % | Line Fill Rate % | Lost Sales ($ USD) |
|---|---|---|---|---|---|---|
| **Beverages** | 3,324 | 77.26% | 88.12% | 68.11% | 96.94% | $63,296.50 |
| **Dairy & Perishables** | 2,689 | 77.28% | **73.93%** | **57.05%** | **93.29%** | **$141,290.20** |
| **Home Care** | 2,695 | 76.55% | 85.68% | 65.71% | 95.91% | $73,590.00 |
| **Packaged Foods** | 3,648 | 75.47% | 86.02% | 64.45% | 96.11% | $45,164.30 |
| **Personal Care** | 2,810 | 76.87% | 85.59% | 65.44% | 96.21% | $96,920.80 |

**Root Cause Analysis:**
- **Dairy & Perishables is the single greatest revenue bleeder**, accounting for **$141,290 in lost sales (33.6% of the company total)**.
- While ambient goods had an In-Full rate of ~86%, Dairy collapsed to **73.93%**.
- Key drivers: Short shelf-life (21-60 days) resulted in 9.5% of short shipments being rejected at receiving bays due to FEFO (First-Expired, First-Out) violations.
- Furthermore, during the Q2 summer heatwave (April - June 2024), cold-chain transport capacity broke down, leading to massive spoiled batches and DC stockouts.

---

### Finding 4: Demand Forecasting Bias (The Bullwhip Catalyst)
Analyzing the S&OP Demand Planning records across categories:

| Category | Actual Demand Units | S&OP Forecast Units | Sum of Errors | WAPE % | Forecast Bias % |
|---|---|---|---|---|---|
| **Beverages** | 1,006,111 | 916,469 | +89,642 | **13.13%** | **+8.91% (Underforecast)** |
| **Dairy & Perishables** | 915,754 | 833,368 | +82,386 | **13.04%** | **+9.00% (Underforecast)** |
| **Home Care** | 736,875 | 720,112 | +16,763 | 8.49% | +2.27% |
| **Packaged Foods** | 968,925 | 946,647 | +22,278 | 8.48% | +2.30% |
| **Personal Care** | 841,279 | 823,000 | +18,279 | 8.47% | +2.17% |

**Root Cause Analysis:**
- Demand forecasting algorithms exhibit a **severe negative bias (underforecasting) of +9.0% on fast-moving seasonal categories** (Beverages and Dairy).
- Plant production schedules relied on these under-estimated forecasts. When summer retail demand surged, Regional DCs ran completely dry within the first week of the month, triggering **34.7% Production Batch Under-Runs** and **32.0% Regional DC Stockouts**.

---

### Finding 5: Delay & Shortage Root-Cause Pareto Analysis

#### Why Are Shipments Late? (33.3% Late Orders)
1. **Carrier Transport Breakdown (27.28%):** Contracted 3PL fleet reliability is poor on inter-state routes; vehicles lack GPS telemetry.
2. **Warehouse Dispatch Backlog (22.66%):** Pick-and-pack bottlenecks at non-automated hubs (`WH-North-01` and `WH-East-01`).
3. **Documentation & E-Way Bill Hold (18.04%):** Manual tax invoice and E-way bill generation causing 4-8 hour gate dispatch holds.
4. **Dock Congestion at Retailer Receiving Bays (14.99%):** Retailers lack advance shipping notices (ASN), leading to 6-hour truck turnaround delays at supermarket docks.
5. **Weather & Route Diversions (17.02%):** Seasonal monsoon and fog disruptions.

#### Why Are Orders Short? (48.5% Incomplete Orders)
1. **Production Batch Under-Run (34.71%):** Manufacturing plant lines constrained on top 5 SKUs.
2. **Regional DC Stockout (31.96%):** Inventory misallocation between Central hub and regional depots.
3. **Transit & Bay Handling Damage (23.86%):** Poor secondary carton packaging integrity during pallet handling.
4. **FEFO Expiry Rejection (9.47%):** Perishable dairy stock arriving at retailer with less than 70% remaining shelf life.
