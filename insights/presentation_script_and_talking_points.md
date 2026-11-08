# ShelfSync: Project Presentation Script & Executive Talking Points

Use this script when presenting this project in **job interviews, portfolio reviews, or executive management meetings**.

---

## 1. The 60-Second Elevator Pitch
> *"I designed an end-to-end supply chain analytics solution in Power BI for an FMCG manufacturer named **ShelfSync**, which supplies 20 tier-1 modern trade retail accounts like Hypermarkets and Quick Commerce.*  
> *The company was suffering from a hidden operational breakdown known as the **'Fill Rate Illusion'**: internal logistics teams celebrated an aggregate **Volume Fill Rate of 95.7%**, while true customer-facing delivery performance collapsed to **39.2% OTIF (On-Time In-Full)** against an agreed contractual target of **$\ge 92\%$**.*  
> *This service level collapse resulted in **$614,000 in annual financial bleed**—composed of $420K in lost sales due to retail stockouts and $194K in cash chargeback penalties.*  
> *Using Power BI and advanced diagnostic data modeling, I identified three acute bottlenecks: dispatch congestion at the Gurugram regional hub, an unrealistic Quick Commerce fulfillment lead-time model, and summer demand forecasting bias on perishable dairy lines. I then architected a 5-pillar operational transformation playbook delivering a **3.8x ROI ($430K net year-1 cash recovery)**."*

---

## 2. Deep-Dive Q&A: Master These 5 Interview Questions

### Q1: What is the "Fill Rate Illusion" and why does it matter in FMCG?
**Answer:**  
In consumer goods, operations teams often measure **Volume Fill Rate** (total units or tonnage shipped divided by total units ordered). In our case, Volume Fill Rate was 95.7%, which seemed healthy.  
However, modern retailers (like Walmart, MetroMart, or Quick Commerce apps) operate on tight shelf space. If an order has 5 SKUs and 4 arrive on time, but the 5th (e.g., yogurt or shampoo) is missing or delayed, the retailer cannot replenish the shelf.  
At the **Order level**, In-Full fulfillment dropped to **51.5%**, and when combined with On-Time delivery (76.7%), the true **Order OTIF collapsed to 39.2%**. This metric divergence is the classic "Fill Rate Illusion."

---

### Q2: What were the biggest root causes your data uncovered?
**Answer:**  
1. **The Regional Choke Point (Gurugram Hub - `WH-North-01`):**  
   While Central and South hubs had On-Time rates over 81-84%, Gurugram dropped to **59.2%**, running an average dispatch lag of **+0.69 days (over 16 hours)** due to manual pallet sorting and dock congestion. It alone generated **$51.5K in penalties**.
2. **The Quick Commerce SLA Trap:**  
   Quick Commerce accounts (ZeptoGo, UrbanBasket, QuickDrop) carried strict 1-day lead-time expectations with severe 5% penalty clauses. While representing only 21.2% of order volume, they generated **35.2% of all financial penalties ($68,267)**.
3. **Perishable Dairy & Summer Forecasting Bias:**  
   Dairy & Perishables had the lowest Line In-Full rate (**73.9%**) and accounted for **33.6% of lost revenue ($141K)**. S&OP models consistently under-forecasted peak summer demand by **+9.0%**, depleting DC safety stocks within days.

---

### Q3: How did you design the data model in Power BI?
**Answer:**  
I implemented an enterprise **Star Schema (Kimball Methodology)**:
- **4 Dimension Tables:** `dim_customers` (channel, SLA targets, penalty rates), `dim_products` (category, storage regime, velocity), `dim_warehouses` (capacity, automation status), and `dim_date` (hierarchical calendar).
- **3 Fact Tables:** `fact_orders` (order grain with delivery dates and financial penalties), `fact_order_lines` (SKU grain with ordered vs delivered quantities), and `fact_forecast_accuracy` (monthly S&OP forecast vs actual demand).
- All dimension-to-fact relationships are **1-to-Many single-direction**, eliminating bi-directional ambiguity and optimizing VertiPaq compression. Role-playing dates (Order Date vs Promised Date) are handled via DAX `USERELATIONSHIP()`.

---

### Q4: Which key DAX measures did you build?
**Answer:**  
I wrote over 35 DAX measures categorized into:
- **Fulfillment Engines:** `[OT %]`, `[IF %]`, `[OTIF %]`, `[Line Fill Rate %]`, `[Volume Fill Rate %]`.
- **Financial Impact:** `[Lost Sales USD]`, `[Total Penalties USD]`, and `[Total Financial Bleed USD]`.
- **Forecasting:** `[WAPE %]` (Weighted Absolute Percentage Error) and `[Forecast Bias %]` to diagnose supply chain bullwhip effects.

---

### Q5: What were your concrete recommendations and expected business outcomes?
**Answer:**  
I formulated a 5-pillar transformation roadmap with clear ROI:
1. **Gurugram 4-Hour Cross-Docking & Pick-to-Light Sortation:** Slashes turnaround time from 16.5 hrs to 4 hrs.
2. **Dedicated Quick Commerce Dark Pods:** Pre-buffered stock for top-12 high-velocity SKUs to protect against 5% chargebacks.
3. **Automated E-Way Billing API:** Eliminates 6 hours of manual dispatch gate holding.
4. **WMS Automated FEFO Expiry Enforcement:** Prohibits batches with $<75\%$ shelf life from dispatching to modern trade.
5. **Demand Sensing & Kingman Dynamic Safety Buffers:** Dynamically expands stock buffers during summer demand surges.

> **Business Outcome:** Recovers **$580,000 in annual financial bleed** against a $150,000 implementation budget, delivering **3.8x ROI (+$430,000 net year-1 cash benefit)** and elevating OTIF from 39.2% to $\ge 92\%$.
