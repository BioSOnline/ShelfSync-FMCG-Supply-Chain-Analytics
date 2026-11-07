# ShelfSync Power BI Dashboard Wireframes & UX Design Specification

## Executive Design System
- **Design Philosophy**: Modern, high-density executive cockpit tailored for FMCG Supply Chain Directors, Logistics Heads, and Key Account Managers.
- **Color Palette**:
  - Primary Dark / Background: `#0F172A` (Slate Dark) / Card Containers: `#1E293B`
  - Text & Accents: Crisp White `#F8FAFC`, Subdued Slate `#94A3B8`
  - Performance Green (Compliant): `#10B981` (Emerald)
  - Warning Amber (At Risk): `#F59E0B` (Amber)
  - Critical Red (SLA Breach / Bleed): `#EF4444` (Coral Red)
  - Metric Accent Blue: `#38BDF8` (Sky Blue)
- **Canvas Resolution**: 16:9 widescreen standard (1920 x 1080 px or 1280 x 720 px).
- **Navigation Bar**: Persistent left-side vertical navigation rail (collapsed / expanded states).

---

## Page Architecture Overview

| Page # | Page Name | Primary Target Persona | Primary Business Purpose |
|---|---|---|---|
| **P1** | **Executive OTIF Command Center** | COO, VP Supply Chain | Big picture health, OTIF gap, financial bleed, regional overview |
| **P2** | **Customer & Channel SLA Scorecard** | Head of Key Accounts, Sales Ops | Retail partner SLA compliance, penalty exposure, churn warning |
| **P3** | **Warehouse & Logistics Diagnostics** | Logistics Director, Plant Managers | Facility bottlenecks, carrier delays, root-cause Pareto analysis |
| **P4** | **SKU Health & Demand Forecasting** | S&OP Director, Inventory Planners | Forecast bias, WAPE, stockout culprits, high-velocity SKU risk |

---

## Detailed Page Wireframes & Visual Layouts

### Page 1: Executive OTIF Command Center

```
+---------------------------------------------------------------------------------------------------------+
| [LOGO] ShelfSync Supply Chain Cockpit  | Filters: [Year-Qtr v] [Region v] [Channel v] [Warehouse v]     |
+---------------------------------------------------------------------------------------------------------+
|  KPI CARD 1         |  KPI CARD 2         |  KPI CARD 3         |  KPI CARD 4         |  KPI CARD 5     |
|  OTIF %             |  On-Time (OT) %     |  In-Full (IF) %     |  Volume Fill Rate   |  Financial Bleed|
|  39.2%              |  76.7%              |  51.5%              |  95.7%              |  $614,088       |
|  Target: 91.8% [RED]|  Target: 95.0%      |  Target: 96.0%      |  "Fill Rate Myth"   |  Lost: $420K    |
|  Gap: -52.6% pts    |  -18.3% pts         |  -44.5% pts         |  Vol looks healthy! |  Pen: $194K     |
+---------------------------------------------------------------------------------------------------------+
|  CHART 1: OTIF Trend vs Target (Line & Clustered Column)   |  CHART 2: Financial Bleed Breakdown        |
|  - Columns: Gross Sales ($M) & Delivered Sales ($M)        |  - Donut Chart:                             |
|  - Line 1: Actual OTIF % (Red line)                        |    * Lost Sales Due to Stockout (68.4%)     |
|  - Line 2: Contractual Target SLA % (Dotted Grey)          |    * Contractual SLA Penalties (31.6%)     |
|                                                            |  - Callout: 6.31% of Gross Sales Lost!     |
+---------------------------------------------------------------------------------------------------------+
|  CHART 3: Regional Performance Matrix (Heatmap / Bar)       |  CHART 4: Delay vs Stockout Top Drivers    |
|  - West: 39.5% OTIF | $165K Bleed                          |  - Horizontal Stacked Bar:                  |
|  - North: 29.1% OTIF (CRITICAL)| $144K Bleed               |    1. Carrier Transport Breakdown (27.3%)   |
|  - South: 42.2% OTIF | $128K Bleed                          |    2. WH Dispatch Backlog (22.7%)           |
|  - Central: 45.6% OTIF | $112K Bleed                       |    3. Documentation / E-Way Bill (18.0%)    |
|  - East: 38.6% OTIF | $65K Bleed                           |    4. Retailer Dock Congestion (15.0%)      |
+---------------------------------------------------------------------------------------------------------+
```

#### Visual Configuration for Page 1:
1. **Top KPI Ribbon**: Use the new `Card (new)` visual with accent bars and conditional font colors driven by `[OTIF KPI Status Color]`. Highlight the contrast between **Volume Fill Rate (95.7%)** and **Order OTIF (39.2%)** to educate leadership on the "Fill Rate Illusion".
2. **Monthly Trend Visual**: `Line and Clustered Column Chart`.
   - X-Axis: `dim_date[Month_Year]`
   - Column Y-Axis: `[Gross Sales USD]`, `[Delivered Sales USD]`
   - Line Y-Axis: `[OTIF %]`, `[Customer Target OTIF %]`
3. **Regional Decomposition**: Decomposition Tree or Filled Map showing drill-down from `Region` -> `Warehouse` -> `Customer Channel`.

---

### Page 2: Customer & Channel SLA Scorecard

```
+---------------------------------------------------------------------------------------------------------+
| [Back to Exec] Channel & Retail Partner SLA Compliance Scorecard                                        |
+---------------------------------------------------------------------------------------------------------+
|  CHANNEL PERFORMANCE CARDS:                                                                             |
|  [Hypermarkets]          [Quick Commerce]         [Supermarkets]         [Cash & Carry]  [E-Commerce]   |
|  OTIF: 41.1% (Tgt: 91%)  OTIF: 37.5% (Tgt: 95%)   OTIF: 40.5% (Tgt: 90%)  OTIF: 33.3%     OTIF: 35.5%   |
|  Penalties: $55.6K       Penalties: $68.3K [!]    Penalties: $25.7K       Pen: $17.1K     Pen: $20.8K   |
+---------------------------------------------------------------------------------------------------------+
|  CUSTOMER COMPLIANCE & PENALTY MATRIX (Interactive Table / Matrix Visual with Data Bars)               |
|  Customer Name         Channel         Orders   OT %    IF %   OTIF %  Target  Gap %    Penalties Lost $ |
|  ------------------------------------------------------------------------------------------------------ |
|  ZeptoGo Rapid         Quick Commerce   279     72.0%   54.8%  39.4%   96.0%   -56.6%   $24,623   $36.5K |
|  UrbanBasket Express   Quick Commerce   281     71.5%   58.0%  41.6%   95.0%   -53.4%   $21,859   $27.9K |
|  QuickDrop Grocery     Quick Commerce   245     56.7%   48.2%  30.6%   95.0%   -64.4%   $21,785   $28.9K |
|  MetroMart Superstores Hypermarket      292     84.6%   47.6%  40.4%   92.0%   -51.6%   $14,948   $31.2K |
|  PrimePantry Hyper     Hypermarket      250     81.2%   48.8%  38.0%   92.0%   -54.0%   $12,215   $24.5K |
|  Reliance Bazaar       Hypermarket      249     83.9%   53.8%  43.4%   92.0%   -48.6%   $11,765   $22.2K |
+---------------------------------------------------------------------------------------------------------+
|  SCATTER PLOT: Customer Relationship Risk Zone             |  SLA GAP DISTRIBUTION BY CHANNEL           |
|  - X-Axis: OTIF Compliance Gap % (Negative = Worse)        |  - Clustered Bar:                          |
|  - Y-Axis: Total Penalty Incurred ($ USD)                  |    Compares Actual OTIF vs Target OTIF     |
|  - Bubble Size: Total Gross Order Value                    |    Highlights Quick Commerce 57.8 pt gap   |
|  - Quadrant 1 (Top-Left): "HIGH FINANCIAL THREAT"          |                                            |
+---------------------------------------------------------------------------------------------------------+
```

#### Visual Configuration for Page 2:
- **Interactive Scatter Plot**: Reveals the most dangerous customers who are both low in OTIF compliance and charge high penalty percentages (e.g., Quick Commerce accounts like `ZeptoGo Rapid` and `QuickDrop Grocery`).
- **Matrix Visual**: Add conditional formatting icons (Red Circle for OTIF < 80%, Amber for 80-90%, Green Check for >=90%). Add Data Bars on `Penalties` and `Lost $`.

---

### Page 3: Warehouse & Logistics Diagnostics

```
+---------------------------------------------------------------------------------------------------------+
| [Back to Exec] Operational Choke Points & Distribution Network Bottlenecks                              |
+---------------------------------------------------------------------------------------------------------+
|  WAREHOUSE COMPARISON TILES                                                                             |
|  WH-NORTH-01 (Gurugram)   WH-WEST-01 (Bhiwandi)   WH-CENTRAL-01 (Nagpur)  WH-SOUTH-01/02 (BLR/Chennai)  |
|  OT: 59.2% [BOTTLENECK]   OT: 80.7%               OT: 84.1% [BENCHMARK]   OT: 81.3%                     |
|  Variance: +0.69 Days     Variance: +0.31 Days    Variance: +0.27 Days    Variance: +0.31 Days          |
|  Penalties: $51,466       Penalties: $39,541      Penalties: $39,528      Penalties: $53,967            |
+---------------------------------------------------------------------------------------------------------+
|  CHART 1: Dispatch Delay Root Causes (Pareto Analysis)     |  CHART 2: Day of Week Order Arrival Lag    |
|  - Bar: Frequency % of Delay Reason                        |  - Column Chart: Avg Lead Time Delay Days   |
|  - Line: Cumulative Impact % (80/20 Rule)                  |    * Monday: 0.18 days delay                |
|    1. Carrier Transport Breakdown (27.3%)                  |    * Tuesday: 0.21 days delay               |
|    2. Warehouse Dispatch Backlog (22.7%)                   |    * Thursday: 0.42 days delay [Peak]       |
|    3. Documentation / E-Way Bill Hold (18.0%)              |    * Friday: 0.49 days delay [Peak Weekend] |
|    4. Dock Congestion at Retailer (15.0%)                  |                                            |
+---------------------------------------------------------------------------------------------------------+
|  CHART 3: Warehouse Lead Time Distribution (Box / Violin)  |  CHART 4: Short Delivery Root Causes       |
|  - Promised Lead Time vs Actual Turnaround                 |  - Production Batch Under-Run (34.7%)      |
|  - Demonstrates Gurugram facility 2-day manual backlog     |  - Regional DC Stockout (32.0%)            |
|                                                            |  - Damaged in Transit/Handling (23.9%)     |
+---------------------------------------------------------------------------------------------------------+
```

#### Visual Configuration for Page 3:
- **Pareto Chart**: Uses a Clustered Column & Line Chart for delay reasons with cumulative percentage curve to pinpoint the exact 2 causes contributing to 50% of all delays (Transport Breakdown + Warehouse Backlog).
- **Day of Week Analysis**: Demonstrates the classic retail "Weekend Surge Trap"—orders placed on Thursday/Friday overwhelm logistics fleets.

---

### Page 4: SKU Health & Demand Forecasting

```
+---------------------------------------------------------------------------------------------------------+
| [Back to Exec] SKU-Level Availability, Velocity & Demand Forecasting Error                              |
+---------------------------------------------------------------------------------------------------------+
|  CATEGORY SCORECARDS                                                                                    |
|  [Dairy & Perishables]     [Beverages]              [Personal Care]         [Packaged Foods / Home]     |
|  Line IF%: 73.9% [WORST]   Line IF%: 88.1%          Line IF%: 85.6%         Line IF%: 86.0%             |
|  Lost Sales: $141,290      Lost Sales: $63,297      Lost Sales: $96,921     Lost Sales: $118,754        |
|  WAPE: 13.0% (Bias: +9.0%) WAPE: 13.1% (Bias: +8.9%) WAPE: 8.5%              WAPE: 8.5%                  |
+---------------------------------------------------------------------------------------------------------+
|  CHART 1: High-Risk SKU Stockout Watchlist (Trellis / Matrix)| CHART 2: Demand Forecast Error vs Actuals|
|  Product Name                 Category     Short Qty  Lost $ | - Monthly Trend Line:                     |
|  ----------------------------------------------------------- |   * Actual Market Demand (Units)         |
|  DairyFresh Greek Yogurt 400g Dairy        12,450     $26.1K |   * S&OP Forecast (Units)                |
|  PureMilk UHT Toned 1L        Dairy        11,200     $84.0K |   * Highlight Q2 Summer Demand Surge Gap |
|  PureGlow Face Wash 200ml     Personal      6,840     $26.7K |                                          |
|  CrispBite Potato Chips 150g  Foods        12,800     $17.9K |                                          |
|  AquaPure Spring Water 1L     Beverages     3,200     $15.4K |                                          |
+---------------------------------------------------------------------------------------------------------+
|  CHART 3: Storage Type Vulnerability                       |  CHART 4: Stockout Reason Breakdown         |
|  - Bar Chart comparing Cold Storage vs Ambient:            |  - Bar Chart:                               |
|    * Cold Storage: Line In-Full = 74.2%                    |    * Production Capacity Constraints (34.7%)|
|    * Ambient: Line In-Full = 86.8%                         |    * RDC Buffer Stock Depletion (32.0%)     |
|    * Conclusion: Refrigerated logistics bottleneck        |    * FEFO Expiry (Dairy specific - 9.5%)    |
+---------------------------------------------------------------------------------------------------------+
```

---

## 4. Interactive UX Features & Bookmarks

1. **"The Fill Rate Illusion" Toggle Bookmark**:
   - Button 1: *Executive View (OTIF %)* -> Visualizes customer-facing reality (39.2% success).
   - Button 2: *Operations View (Volume Fill Rate %)* -> Shows 95.7% aggregate tonnage.
   - Purpose: Directs leadership to understand why retail partners are angry despite operations claiming "we shipped 96% of volume".
2. **Drill-Through Target**:
   - Right-click any customer row -> Drill through to `Customer Deep Dive` page showing order-by-order history, penalty invoices, and SKU fulfillment lines.
3. **Dynamic Parameter Slicer**:
   - What-If Parameter: `Target OTIF Improvement (+5%, +10%, +15%)` -> Calculates recovered revenue and eliminated penalties in real time.
