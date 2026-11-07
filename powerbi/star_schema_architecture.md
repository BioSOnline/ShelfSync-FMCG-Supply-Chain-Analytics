# ShelfSync Power BI Data Architecture & Star Schema Specification

## 1. Architectural Overview
The ShelfSync FMCG Supply Chain Analytics model is built using an optimized **Star Schema** with Kimball modeling best practices. It minimizes bi-directional cross-filtering, eliminates snowflake overhead, and ensures sub-second DAX calculation latency on tabular engines.

```
                    +--------------------+
                    |     dim_date       |
                    +--------------------+
                              |
                +-------------+-------------+
                | 1:*                       | 1:*
                v                           v
+-----------------------+           +--------------------------+
|      fact_orders      |<-- 1:* ---|     fact_order_lines     |
+-----------------------+           +--------------------------+
      ^          ^                               |
  1:* |      1:* |                               | 1:*
      |          |                               v
+-----------+  +----------------+        +--------------------+
| dim_cust  |  | dim_warehouses |        |    dim_products    |
+-----------+  +----------------+        +--------------------+
      |                                          |
      | 1:*                                  1:* |
      +-------------------+  +-------------------+
                          v  v
              +--------------------------+
              |  fact_forecast_accuracy  |
              +--------------------------+
```

---

## 2. Table Schemas & Data Dictionary

### A. Fact Tables

#### `fact_orders` (Grain: One row per customer order)
| Column Name | Data Type | Key Type | Description |
|---|---|---|---|
| `Order_ID` | String (Text) | Primary Key | Unique order identifier (e.g. `ORD-10001`) |
| `Customer_ID` | String (Text) | Foreign Key | References `dim_customers.Customer_ID` |
| `Warehouse_ID` | String (Text) | Foreign Key | References `dim_warehouses.Warehouse_ID` |
| `Order_Date` | Date | Foreign Key | Active relationship to `dim_date.Date` |
| `Promised_Delivery_Date` | Date | Foreign Key | Inactive relationship to `dim_date.Date` |
| `Actual_Delivery_Date` | Date | Foreign Key | Inactive relationship to `dim_date.Date` |
| `Planned_Lead_Time_Days`| Integer | Metric | Contractual lead time in days (1 to 5 days) |
| `Actual_Lead_Time_Days` | Integer | Metric | Days elapsed between order date and delivery date |
| `Lead_Time_Variance_Days`| Integer | Metric | Max(0, Actual Delivery - Promised Delivery) |
| `Total_Order_Lines` | Integer | Metric | Count of line items in order |
| `Total_Lines_In_Full` | Integer | Metric | Count of line items delivered 100% in full |
| `Order_Gross_Value_USD` | Decimal | Metric | Total promised/ordered revenue in USD |
| `Order_Delivered_Value_USD`| Decimal | Metric | Actual delivered revenue in USD |
| `Order_Lost_Sales_USD` | Decimal | Metric | Gross Value - Delivered Value |
| `Penalty_Amount_USD` | Decimal | Metric | Contractual penalty levied if OTIF = 0 |
| `Is_Order_On_Time` | Integer (0/1) | Flag | 1 if delivered on or before Promised Date |
| `Is_Order_In_Full` | Integer (0/1) | Flag | 1 if all lines delivered in full |
| `Is_Order_OTIF` | Integer (0/1) | Flag | 1 if On-Time = 1 AND In-Full = 1 |
| `Primary_Delay_Reason` | String (Text) | Dimension | Root cause reason code for order delivery delay |

#### `fact_order_lines` (Grain: One row per SKU line item within an order)
| Column Name | Data Type | Key Type | Description |
|---|---|---|---|
| `Order_Line_ID` | String (Text) | Primary Key | Unique line identifier (e.g. `LIN-50001`) |
| `Order_ID` | String (Text) | Foreign Key | References `fact_orders.Order_ID` |
| `Product_ID` | String (Text) | Foreign Key | References `dim_products.Product_ID` |
| `Ordered_Qty` | Integer | Metric | Number of units ordered by retail customer |
| `Delivered_Qty` | Integer | Metric | Number of units actually fulfilled and accepted |
| `Short_Qty` | Integer | Metric | Ordered Qty - Delivered Qty |
| `Damaged_Qty` | Integer | Metric | Units rejected at receiving bay due to damage |
| `Unit_Price_USD` | Decimal | Dimension | Retail billing price per unit |
| `Unit_Cost_USD` | Decimal | Dimension | Unit cost of production / procurement |
| `Line_Ordered_Value_USD`| Decimal | Metric | Ordered Qty * Unit Price |
| `Line_Delivered_Value_USD`| Decimal| Metric | Delivered Qty * Unit Price |
| `Lost_Sales_Value_USD` | Decimal | Metric | Short Qty * Unit Price |
| `Is_Line_On_Time` | Integer (0/1) | Flag | Inherited from order dispatch performance |
| `Is_Line_In_Full` | Integer (0/1) | Flag | 1 if Delivered Qty == Ordered Qty |
| `Is_Line_OTIF` | Integer (0/1) | Flag | 1 if Line On Time == 1 AND Line In Full == 1 |
| `Short_Reason` | String (Text) | Dimension | Root cause for SKU short delivery |

#### `fact_forecast_accuracy` (Grain: Monthly forecast vs actuals per Product per Customer)
| Column Name | Data Type | Key Type | Description |
|---|---|---|---|
| `Month_Year` | String (YYYY-MM)| Foreign Key | Relates to Month period |
| `Customer_ID` | String (Text) | Foreign Key | References `dim_customers.Customer_ID` |
| `Product_ID` | String (Text) | Foreign Key | References `dim_products.Product_ID` |
| `Forecast_Qty` | Integer | Metric | Projected demand units by S&OP team |
| `Actual_Demand_Qty` | Integer | Metric | True market/customer order demand units |
| `Forecast_Error_Qty` | Integer | Metric | Actual Demand - Forecasted Qty |
| `Abs_Forecast_Error_Qty`| Integer | Metric | \|Actual Demand - Forecasted Qty\| |

---

### B. Dimension Tables

#### `dim_customers`
| Column Name | Data Type | Description |
|---|---|---|
| `Customer_ID` | Text (PK) | Unique retailer ID (e.g. `CUST-101`) |
| `Customer_Name` | Text | Retailer name (e.g. `MetroMart Superstores`) |
| `Channel` | Text | Channel (Hypermarket, Supermarket, Quick Commerce, Wholesale, E-Commerce) |
| `City` | Text | Primary headquarters / DC city |
| `Region` | Text | Geographic region (North, South, East, West, Central) |
| `SLA_Target_OTIF` | Decimal | Contractual OTIF target (e.g. 0.92 for 92%) |
| `Payment_Terms` | Text | Commercial terms (Net 15, Net 30, Net 45, Net 60) |
| `Penalty_Rate_Pct` | Decimal | Financial penalty % applied on failed orders (1.5% to 5.0%) |

#### `dim_products`
| Column Name | Data Type | Description |
|---|---|---|
| `Product_ID` | Text (PK) | SKU code (e.g. `PRD-DRY-01`) |
| `Product_Name` | Text | Full brand SKU title |
| `Category` | Text | Category (Dairy & Perishables, Packaged Foods, Beverages, Personal Care, Home Care) |
| `Sub_Category` | Text | Sub-category (e.g. Snacks & Chips, Dairy & Curd, Skincare) |
| `Unit_Cost_USD` | Decimal | Cost of goods sold (COGS) |
| `Unit_Price_USD` | Decimal | Standard list wholesale price |
| `Shelf_Life_Days` | Integer | Usable shelf life (21 days for yogurt to 720 for home care) |
| `Storage_Type` | Text | Storage regime: `Cold Storage` vs `Ambient` |
| `Velocity` | Text | ABC Velocity classification: `Fast-Moving`, `Medium-Moving`, `Slow-Moving` |

#### `dim_warehouses`
| Column Name | Data Type | Description |
|---|---|---|
| `Warehouse_ID` | Text (PK) | Warehouse identifier (e.g. `WH-NORTH-01`) |
| `Warehouse_Name`| Text | Facility name |
| `City` | Text | Facility city |
| `Region` | Text | Operating region |
| `Capacity_SqFt` | Integer | Warehouse floor space |
| `Automated_Sorting`| Boolean | True if facility has automated sorters/conveyors |
| `Avg_Dispatch_SLA_Days`| Integer | Internal target turnaround dispatch time |

#### `dim_date`
Standard date dimension spanning 2024-01-01 to 2025-03-31 with hierarchical attributes: `Year`, `Quarter`, `Month`, `Month_Name`, `Month_Year`, `Week_Number`, `Day_Of_Week`, and `Is_Weekend`.

---

## 3. Power BI Relationship Setup Guide

1. **`dim_customers` [Customer_ID]** `1` ──── `*` **`fact_orders` [Customer_ID]** (Single Direction)
2. **`dim_warehouses` [Warehouse_ID]** `1` ──── `*` **`fact_orders` [Warehouse_ID]** (Single Direction)
3. **`dim_date` [Date]** `1` ──── `*` **`fact_orders` [Order_Date]** (**Active**, Single Direction)
4. **`dim_date` [Date]** `1` ──── `*` **`fact_orders` [Promised_Delivery_Date]** (*Inactive*, Single Direction)
5. **`dim_date` [Date]** `1` ──── `*` **`fact_orders` [Actual_Delivery_Date]** (*Inactive*, Single Direction)
6. **`fact_orders` [Order_ID]** `1` ──── `*` **`fact_order_lines` [Order_ID]** (Single Direction)
7. **`dim_products` [Product_ID]** `1` ──── `*` **`fact_order_lines` [Product_ID]** (Single Direction)
8. **`dim_customers` [Customer_ID]** `1` ──── `*` **`fact_forecast_accuracy` [Customer_ID]** (Single Direction)
9. **`dim_products` [Product_ID]** `1` ──── `*` **`fact_forecast_accuracy` [Product_ID]** (Single Direction)
