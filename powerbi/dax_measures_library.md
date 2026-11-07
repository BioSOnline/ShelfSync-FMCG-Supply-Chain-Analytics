# ShelfSync DAX Measures Library (Production Ready)

This repository contains the complete catalog of DAX measures required for the ShelfSync FMCG Supply Chain Analytics solution in Power BI.
It is best practice to store these measures in a dedicated disconnected table named `_Measures`.

---

## Table of Contents
1. [Base Volume & Financial Measures](#1-base-volume--financial-measures)
2. [FMCG Fulfillment & Service Level Measures (The Core Engine)](#2-fmcg-fulfillment--service-level-measures)
3. [SLA Target, Benchmark & Variance Measures](#3-sla-target-benchmark--variance-measures)
4. [Financial Impact & Penalty Bleed Measures](#4-financial-impact--penalty-bleed-measures)
5. [Logistics & Lead Time Diagnostics](#5-logistics--lead-time-diagnostics)
6. [Demand Forecasting Accuracy & Bias Measures](#6-demand-forecasting-accuracy--bias-measures)
7. [Time Intelligence & MoM Trend Measures](#7-time-intelligence--mom-trend-measures)
8. [Dynamic UI Formatting & KPI Alert Measures](#8-dynamic-ui-formatting--kpi-alert-measures)

---

## 1. Base Volume & Financial Measures

```dax
// Total number of customer purchase orders placed
Total Orders = 
COUNTROWS('fact_orders')

// Total order lines (SKU line transactions)
Total Order Lines = 
COUNTROWS('fact_order_lines')

// Total physical units ordered by retailers
Total Ordered Units = 
SUM('fact_order_lines'[Ordered_Qty])

// Total physical units successfully delivered
Total Delivered Units = 
SUM('fact_order_lines'[Delivered_Qty])

// Total units short-delivered (out of stock / rejected)
Total Short Units = 
SUM('fact_order_lines'[Short_Qty])

// Gross Sales Value based on purchase orders (USD)
Gross Sales USD = 
SUM('fact_orders'[Order_Gross_Value_USD])

// Delivered Sales Value recognized upon completed delivery (USD)
Delivered Sales USD = 
SUM('fact_orders'[Order_Delivered_Value_USD])
```

---

## 2. FMCG Fulfillment & Service Level Measures

> **Key FMCG Insight**: Beware of the **"Fill Rate Illusion"**! 
> Operations teams often report a Volume Fill Rate of ~95%+, while the customer-facing Order OTIF is failing at <40%.

```dax
// Order-Level On-Time Delivery Percentage
On-Time (OT) % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('fact_orders'),
        'fact_orders'[Is_Order_On_Time] = 1
    ),
    [Total Orders],
    0
)

// Order-Level In-Full Delivery Percentage (All order lines fulfilled 100%)
In-Full (IF) % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('fact_orders'),
        'fact_orders'[Is_Order_In_Full] = 1
    ),
    [Total Orders],
    0
)

// Order-Level On-Time In-Full (OTIF) % (The gold standard FMCG SLA metric)
OTIF % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('fact_orders'),
        'fact_orders'[Is_Order_OTIF] = 1
    ),
    [Total Orders],
    0
)

// Line-Level On-Time In-Full (Measures individual SKU performance)
Line OTIF % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('fact_order_lines'),
        'fact_order_lines'[Is_Line_OTIF] = 1
    ),
    [Total Order Lines],
    0
)

// Line Fill Rate (Percentage of SKU lines delivered in full)
Line Fill Rate % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('fact_order_lines'),
        'fact_order_lines'[Is_Line_In_Full] = 1
    ),
    [Total Order Lines],
    0
)

// Volume Fill Rate (Aggregated tonnage/units delivered vs ordered)
Volume Fill Rate % = 
DIVIDE(
    [Total Delivered Units],
    [Total Ordered Units],
    0
)
```

---

## 3. SLA Target, Benchmark & Variance Measures

```dax
// Weighted average contractual OTIF target for active customer filter context
Customer Target OTIF % = 
AVERAGE('dim_customers'[SLA_Target_OTIF])

// Gap between actual OTIF and contractual SLA (Negative = Underperforming)
OTIF Variance Gap % = 
[OTIF %] - [Customer Target OTIF %]

// Number of orders failing OTIF SLA
Failed OTIF Orders = 
CALCULATE(
    COUNTROWS('fact_orders'),
    'fact_orders'[Is_Order_OTIF] = 0
)

// Percentage of failed orders
Failed Orders % = 
DIVIDE([Failed OTIF Orders], [Total Orders], 0)
```

---

## 4. Financial Impact & Penalty Bleed Measures

```dax
// Top-line revenue lost directly due to short-shipped products
Lost Sales Value USD = 
SUM('fact_orders'[Order_Lost_Sales_USD])

// Contractual chargeback penalties levied by modern trade / retail partners
Total Penalties USD = 
SUM('fact_orders'[Penalty_Amount_USD])

// Total direct financial bleed caused by supply chain failure
Total Financial Bleed USD = 
[Lost Sales Value USD] + [Total Penalties USD]

// Financial bleed as a percentage of gross order value
Financial Bleed % of Sales = 
DIVIDE(
    [Total Financial Bleed USD],
    [Gross Sales USD],
    0
)

// Line-item level lost sales value
Line Lost Sales USD = 
SUM('fact_order_lines'[Lost_Sales_Value_USD])
```

---

## 5. Logistics & Lead Time Diagnostics

```dax
// Average planned lead time promised to customers (in days)
Avg Planned Lead Time Days = 
AVERAGE('fact_orders'[Planned_Lead_Time_Days])

// Average actual turnaround cycle time (in days)
Avg Actual Lead Time Days = 
AVERAGE('fact_orders'[Actual_Lead_Time_Days])

// Average dispatch/transit delay in days beyond promised date
Avg Delivery Delay Days = 
AVERAGE('fact_orders'[Lead_Time_Variance_Days])

// Total count of late delivery orders
Delayed Orders Count = 
CALCULATE(
    COUNTROWS('fact_orders'),
    'fact_orders'[Is_Order_On_Time] = 0
)

// Late Delivery Rate
Late Delivery Rate % = 
DIVIDE([Delayed Orders Count], [Total Orders], 0)
```

---

## 6. Demand Forecasting Accuracy & Bias Measures

```dax
// Total actual customer demand units
Actual Demand Units = 
SUM('fact_forecast_accuracy'[Actual_Demand_Qty])

// Total forecasted demand projected by S&OP / planning team
Forecasted Demand Units = 
SUM('fact_forecast_accuracy'[Forecast_Qty])

// Total absolute forecast deviation
Total Absolute Error Units = 
SUM('fact_forecast_accuracy'[Abs_Forecast_Error_Qty])

// Weighted Absolute Percentage Error (WAPE) - Industry standard for FMCG
WAPE % = 
DIVIDE(
    [Total Absolute Error Units],
    [Actual Demand Units],
    0
)

// Overall Forecast Accuracy % (1 - WAPE)
Forecast Accuracy % = 
MAX(0, 1 - [WAPE %])

// Forecast Bias % (Positive = Underforecasting / Stockout Risk; Negative = Overforecasting / Cash Trap)
Forecast Bias % = 
DIVIDE(
    SUM('fact_forecast_accuracy'[Forecast_Error_Qty]),
    [Actual Demand Units],
    0
)
```

---

## 7. Time Intelligence & MoM Trend Measures

```dax
// OTIF % in previous calendar month
OTIF % Prior Month = 
CALCULATE(
    [OTIF %],
    PREVIOUSMONTH('dim_date'[Date])
)

// Month-over-Month change in OTIF % (in percentage points)
OTIF % MoM Delta = 
IF(
    ISBLANK([OTIF % Prior Month]),
    BLANK(),
    [OTIF %] - [OTIF % Prior Month]
)

// Penalties incurred in previous month
Penalties Prior Month = 
CALCULATE(
    [Total Penalties USD],
    PREVIOUSMONTH('dim_date'[Date])
)

// Month-over-Month growth in penalty cost
Penalties MoM % Growth = 
DIVIDE(
    [Total Penalties USD] - [Penalties Prior Month],
    [Penalties Prior Month],
    0
)
```

---

## 8. Dynamic UI Formatting & KPI Alert Measures

```dax
// Dynamic Hex Color for OTIF SLA Compliance
OTIF KPI Status Color = 
SWITCH(
    TRUE(),
    [OTIF %] >= [Customer Target OTIF %], "#107C41",  // Forest Green (Target Met)
    [OTIF %] >= [Customer Target OTIF %] - 0.05, "#FFB900", // Amber (Near Target)
    "#D83B01" // Crimson Red (Critical Violation)
)

// KPI Callout Icon
OTIF KPI Icon = 
SWITCH(
    TRUE(),
    [OTIF %] >= [Customer Target OTIF %], "🟢 SLA Met",
    [OTIF %] >= [Customer Target OTIF %] - 0.05, "🟡 At Risk",
    "🔴 SLA Breached"
)

// Dynamic Card Subtitle for Executive Overview
Executive Summary Subtitle = 
"OTIF is currently at " & FORMAT([OTIF %], "0.0%") & 
" vs Target of " & FORMAT([Customer Target OTIF %], "0.0%") & 
" | Financial Bleed: $" & FORMAT([Total Financial Bleed USD], "#,##0")
```
