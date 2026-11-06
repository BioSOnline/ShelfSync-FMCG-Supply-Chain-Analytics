"""
ShelfSync FMCG Supply Chain Dataset Generator
Generates realistic, interconnected FMCG supply chain datasets with embedded operational bottlenecks,
SLA variances, regional disruptions, and demand forecast errors for Power BI analytics.
"""

import os
import random
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set random seeds for reproducibility
np.random.seed(42)
random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. DIM_CUSTOMERS
# -------------------------------------------------------------
customers_data = [
    {"Customer_ID": "CUST-101", "Customer_Name": "MetroMart Superstores", "Channel": "Hypermarket", "City": "Mumbai", "Region": "West", "SLA_Target_OTIF": 0.92, "Payment_Terms": "Net 45", "Penalty_Rate_Pct": 0.03},
    {"Customer_ID": "CUST-102", "Customer_Name": "FreshFleet Retail", "Channel": "Supermarket", "City": "Pune", "Region": "West", "SLA_Target_OTIF": 0.90, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-103", "Customer_Name": "UrbanBasket Express", "Channel": "Quick Commerce", "City": "Bengaluru", "Region": "South", "SLA_Target_OTIF": 0.95, "Payment_Terms": "Net 15", "Penalty_Rate_Pct": 0.05},
    {"Customer_ID": "CUST-104", "Customer_Name": "Apex Wholesale Club", "Channel": "Wholesale / Cash & Carry", "City": "Delhi NCR", "Region": "North", "SLA_Target_OTIF": 0.88, "Payment_Terms": "Net 60", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-105", "Customer_Name": "PrimePantry Hyper", "Channel": "Hypermarket", "City": "Hyderabad", "Region": "South", "SLA_Target_OTIF": 0.92, "Payment_Terms": "Net 45", "Penalty_Rate_Pct": 0.03},
    {"Customer_ID": "CUST-106", "Customer_Name": "QuickDrop Grocery", "Channel": "Quick Commerce", "City": "Delhi NCR", "Region": "North", "SLA_Target_OTIF": 0.95, "Payment_Terms": "Net 15", "Penalty_Rate_Pct": 0.05},
    {"Customer_ID": "CUST-107", "Customer_Name": "GreenLeaf Grocers", "Channel": "Supermarket", "City": "Chennai", "Region": "South", "SLA_Target_OTIF": 0.90, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.025},
    {"Customer_ID": "CUST-108", "Customer_Name": "Reliance Bazaar", "Channel": "Hypermarket", "City": "Ahmedabad", "Region": "West", "SLA_Target_OTIF": 0.92, "Payment_Terms": "Net 45", "Penalty_Rate_Pct": 0.03},
    {"Customer_ID": "CUST-109", "Customer_Name": "CityCorner Mart", "Channel": "Convenience Store", "City": "Kolkata", "Region": "East", "SLA_Target_OTIF": 0.85, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.015},
    {"Customer_ID": "CUST-110", "Customer_Name": "OmniCart Online", "Channel": "E-Commerce", "City": "Bengaluru", "Region": "South", "SLA_Target_OTIF": 0.94, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.04},
    {"Customer_ID": "CUST-111", "Customer_Name": "Spence Valley Super", "Channel": "Supermarket", "City": "Kolkata", "Region": "East", "SLA_Target_OTIF": 0.90, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-112", "Customer_Name": "Vanguard Bulk Mart", "Channel": "Wholesale / Cash & Carry", "City": "Jaipur", "Region": "North", "SLA_Target_OTIF": 0.88, "Payment_Terms": "Net 60", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-113", "Customer_Name": "Nectar Food & Mart", "Channel": "Supermarket", "City": "Chandigarh", "Region": "North", "SLA_Target_OTIF": 0.90, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-114", "Customer_Name": "DailyNeeds Express", "Channel": "Convenience Store", "City": "Lucknow", "Region": "Central", "SLA_Target_OTIF": 0.85, "Payment_Terms": "Net 15", "Penalty_Rate_Pct": 0.015},
    {"Customer_ID": "CUST-115", "Customer_Name": "Summit Retail Chain", "Channel": "Hypermarket", "City": "Indore", "Region": "Central", "SLA_Target_OTIF": 0.91, "Payment_Terms": "Net 45", "Penalty_Rate_Pct": 0.03},
    {"Customer_ID": "CUST-116", "Customer_Name": "ZeptoGo Rapid", "Channel": "Quick Commerce", "City": "Mumbai", "Region": "West", "SLA_Target_OTIF": 0.96, "Payment_Terms": "Net 15", "Penalty_Rate_Pct": 0.05},
    {"Customer_ID": "CUST-117", "Customer_Name": "Eastern Superstores", "Channel": "Hypermarket", "City": "Bhubaneswar", "Region": "East", "SLA_Target_OTIF": 0.90, "Payment_Terms": "Net 45", "Penalty_Rate_Pct": 0.025},
    {"Customer_ID": "CUST-118", "Customer_Name": "Southern Comforts Mart", "Channel": "Supermarket", "City": "Kochi", "Region": "South", "SLA_Target_OTIF": 0.89, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-119", "Customer_Name": "National Pantry Logistics", "Channel": "Wholesale / Cash & Carry", "City": "Nagpur", "Region": "Central", "SLA_Target_OTIF": 0.88, "Payment_Terms": "Net 60", "Penalty_Rate_Pct": 0.02},
    {"Customer_ID": "CUST-120", "Customer_Name": "BlinkShip Digital", "Channel": "E-Commerce", "City": "Delhi NCR", "Region": "North", "SLA_Target_OTIF": 0.93, "Payment_Terms": "Net 30", "Penalty_Rate_Pct": 0.035}
]
df_customers = pd.DataFrame(customers_data)
df_customers.to_csv(os.path.join(DATA_DIR, "dim_customers.csv"), index=False)
print("Saved dim_customers.csv with", len(df_customers), "records.")

# -------------------------------------------------------------
# 2. DIM_WAREHOUSES
# -------------------------------------------------------------
warehouses_data = [
    {"Warehouse_ID": "WH-WEST-01", "Warehouse_Name": "Bhiwandi Central Mega Hub", "City": "Mumbai / Bhiwandi", "Region": "West", "Capacity_SqFt": 350000, "Automated_Sorting": True, "Avg_Dispatch_SLA_Days": 1},
    {"Warehouse_ID": "WH-NORTH-01", "Warehouse_Name": "Gurugram North Gateway", "City": "Delhi NCR / Gurugram", "Region": "North", "Capacity_SqFt": 280000, "Automated_Sorting": False, "Avg_Dispatch_SLA_Days": 2}, # Known bottleneck
    {"Warehouse_ID": "WH-SOUTH-01", "Warehouse_Name": "Hosakote Logistics Park", "City": "Bengaluru", "Region": "South", "Capacity_SqFt": 300000, "Automated_Sorting": True, "Avg_Dispatch_SLA_Days": 1},
    {"Warehouse_ID": "WH-EAST-01", "Warehouse_Name": "Dankuni Distribution Center", "City": "Kolkata", "Region": "East", "Capacity_SqFt": 180000, "Automated_Sorting": False, "Avg_Dispatch_SLA_Days": 2},
    {"Warehouse_ID": "WH-CENTRAL-01", "Warehouse_Name": "Nagpur Transit Hub", "City": "Nagpur", "Region": "Central", "Capacity_SqFt": 220000, "Automated_Sorting": True, "Avg_Dispatch_SLA_Days": 1},
    {"Warehouse_ID": "WH-SOUTH-02", "Warehouse_Name": "Sriperumbudur Depot", "City": "Chennai", "Region": "South", "Capacity_SqFt": 200000, "Automated_Sorting": True, "Avg_Dispatch_SLA_Days": 1}
]
df_warehouses = pd.DataFrame(warehouses_data)
df_warehouses.to_csv(os.path.join(DATA_DIR, "dim_warehouses.csv"), index=False)
print("Saved dim_warehouses.csv with", len(df_warehouses), "records.")

# -------------------------------------------------------------
# 3. DIM_PRODUCTS
# -------------------------------------------------------------
products_data = [
    # Dairy & Perishables (High stockout & short shelf-life risk)
    {"Product_ID": "PRD-DRY-01", "Product_Name": "DairyFresh Greek Yogurt 400g", "Category": "Dairy & Perishables", "Sub_Category": "Yogurt & Curd", "Unit_Cost_USD": 1.20, "Unit_Price_USD": 2.10, "Shelf_Life_Days": 21, "Storage_Type": "Cold Storage", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-DRY-02", "Product_Name": "DairyFresh Salted Butter 500g", "Category": "Dairy & Perishables", "Sub_Category": "Butter & Spreads", "Unit_Cost_USD": 2.50, "Unit_Price_USD": 4.00, "Shelf_Life_Days": 90, "Storage_Type": "Cold Storage", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-DRY-03", "Product_Name": "PureMilk UHT Toned 1L (Pack of 6)", "Category": "Dairy & Perishables", "Sub_Category": "Milk & Cream", "Unit_Cost_USD": 4.80, "Unit_Price_USD": 7.50, "Shelf_Life_Days": 180, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-DRY-04", "Product_Name": "DairyFresh Artisan Cheese Block 250g", "Category": "Dairy & Perishables", "Sub_Category": "Cheese", "Unit_Cost_USD": 3.10, "Unit_Price_USD": 5.80, "Shelf_Life_Days": 60, "Storage_Type": "Cold Storage", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-DRY-05", "Product_Name": "ProPro Protein Smoothie 330ml", "Category": "Dairy & Perishables", "Sub_Category": "Yogurt & Curd", "Unit_Cost_USD": 1.40, "Unit_Price_USD": 2.60, "Shelf_Life_Days": 30, "Storage_Type": "Cold Storage", "Velocity": "Fast-Moving"},

    # Packaged Foods & Snacks
    {"Product_ID": "PRD-FOD-01", "Product_Name": "CrispBite Potato Chips Sea Salt 150g", "Category": "Packaged Foods", "Sub_Category": "Snacks & Chips", "Unit_Cost_USD": 0.65, "Unit_Price_USD": 1.40, "Shelf_Life_Days": 180, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-FOD-02", "Product_Name": "CrispBite Nacho Cheese Delite 200g", "Category": "Packaged Foods", "Sub_Category": "Snacks & Chips", "Unit_Cost_USD": 0.85, "Unit_Price_USD": 1.80, "Shelf_Life_Days": 180, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-FOD-03", "Product_Name": "GoldenGrain Rolled Oats 1kg", "Category": "Packaged Foods", "Sub_Category": "Breakfast Cereals", "Unit_Cost_USD": 1.90, "Unit_Price_USD": 3.40, "Shelf_Life_Days": 365, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-FOD-04", "Product_Name": "SunHarvest Choco Crunch Cereal 500g", "Category": "Packaged Foods", "Sub_Category": "Breakfast Cereals", "Unit_Cost_USD": 1.60, "Unit_Price_USD": 2.90, "Shelf_Life_Days": 270, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-FOD-05", "Product_Name": "RomaClassic Pasta Penne 500g", "Category": "Packaged Foods", "Sub_Category": "Staples & Pasta", "Unit_Cost_USD": 0.70, "Unit_Price_USD": 1.50, "Shelf_Life_Days": 540, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-FOD-06", "Product_Name": "GourmetBlend Organic Honey 500g", "Category": "Packaged Foods", "Sub_Category": "Spreads & Condiments", "Unit_Cost_USD": 3.20, "Unit_Price_USD": 6.20, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Slow-Moving"},
    {"Product_ID": "PRD-FOD-07", "Product_Name": "NutriBake Almond Cookies 300g", "Category": "Packaged Foods", "Sub_Category": "Biscuits & Bakery", "Unit_Cost_USD": 1.10, "Unit_Price_USD": 2.20, "Shelf_Life_Days": 120, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},

    # Beverages
    {"Product_ID": "PRD-BEV-01", "Product_Name": "AquaPure Spring Water 1L (Pack of 12)", "Category": "Beverages", "Sub_Category": "Bottled Water", "Unit_Cost_USD": 2.40, "Unit_Price_USD": 4.80, "Shelf_Life_Days": 365, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-BEV-02", "Product_Name": "CitrusBurst Real Orange Juice 1L", "Category": "Beverages", "Sub_Category": "Fruit Juices", "Unit_Cost_USD": 1.30, "Unit_Price_USD": 2.50, "Shelf_Life_Days": 120, "Storage_Type": "Cold Storage", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-BEV-03", "Product_Name": "VitalSpark Electrolyte Lime 500ml", "Category": "Beverages", "Sub_Category": "Energy & Sports", "Unit_Cost_USD": 0.75, "Unit_Price_USD": 1.60, "Shelf_Life_Days": 240, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-BEV-04", "Product_Name": "ZenLeaf Green Tea Bags (Box of 50)", "Category": "Beverages", "Sub_Category": "Tea & Coffee", "Unit_Cost_USD": 2.10, "Unit_Price_USD": 4.20, "Shelf_Life_Days": 540, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-BEV-05", "Product_Name": "VelvetRoast Premium Dark Roast Coffee 200g", "Category": "Beverages", "Sub_Category": "Tea & Coffee", "Unit_Cost_USD": 4.00, "Unit_Price_USD": 7.90, "Shelf_Life_Days": 365, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-BEV-06", "Product_Name": "SparklingFizz Zero Cola 330ml Can (Pack of 6)", "Category": "Beverages", "Sub_Category": "Carbonated Drinks", "Unit_Cost_USD": 2.00, "Unit_Price_USD": 3.80, "Shelf_Life_Days": 270, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},

    # Personal Care
    {"Product_ID": "PRD-PER-01", "Product_Name": "PureGlow Foaming Face Wash 200ml", "Category": "Personal Care", "Sub_Category": "Skincare", "Unit_Cost_USD": 1.80, "Unit_Price_USD": 3.90, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-PER-02", "Product_Name": "SilkyStrands Argan Oil Shampoo 400ml", "Category": "Personal Care", "Sub_Category": "Haircare", "Unit_Cost_USD": 2.50, "Unit_Price_USD": 5.20, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-PER-03", "Product_Name": "SilkyStrands Repair Conditioner 350ml", "Category": "Personal Care", "Sub_Category": "Haircare", "Unit_Cost_USD": 2.40, "Unit_Price_USD": 5.00, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-PER-04", "Product_Name": "DermaShield Ultra Sunscreen SPF50 100g", "Category": "Personal Care", "Sub_Category": "Skincare", "Unit_Cost_USD": 3.80, "Unit_Price_USD": 8.50, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-PER-05", "Product_Name": "HerbalFresh Charcoal Toothpaste 150g", "Category": "Personal Care", "Sub_Category": "Oral Care", "Unit_Cost_USD": 0.90, "Unit_Price_USD": 2.10, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},

    # Home & Hygiene Care
    {"Product_ID": "PRD-HMC-01", "Product_Name": "SparkleWash Liquid Detergent 2L", "Category": "Home Care", "Sub_Category": "Laundry", "Unit_Cost_USD": 3.20, "Unit_Price_USD": 6.80, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-HMC-02", "Product_Name": "SparkleWash Fabric Softener 1L", "Category": "Home Care", "Sub_Category": "Laundry", "Unit_Cost_USD": 1.80, "Unit_Price_USD": 3.60, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"},
    {"Product_ID": "PRD-HMC-03", "Product_Name": "ShieldMax Disinfectant Floor Cleaner 1L", "Category": "Home Care", "Sub_Category": "Surface Cleaners", "Unit_Cost_USD": 1.10, "Unit_Price_USD": 2.40, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-HMC-04", "Product_Name": "GleamKitchen Anti-Grease Dish Gel 750ml", "Category": "Home Care", "Sub_Category": "Dishwashing", "Unit_Cost_USD": 0.95, "Unit_Price_USD": 2.00, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Fast-Moving"},
    {"Product_ID": "PRD-HMC-05", "Product_Name": "AromaMist Lavender Air Freshener 300ml", "Category": "Home Care", "Sub_Category": "Air Care", "Unit_Cost_USD": 1.40, "Unit_Price_USD": 3.10, "Shelf_Life_Days": 720, "Storage_Type": "Ambient", "Velocity": "Medium-Moving"}
]
df_products = pd.DataFrame(products_data)
df_products.to_csv(os.path.join(DATA_DIR, "dim_products.csv"), index=False)
print("Saved dim_products.csv with", len(df_products), "records.")

# -------------------------------------------------------------
# 4. DIM_DATE (Calendar 2024 to Q1 2025)
# -------------------------------------------------------------
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 3, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq="D")

date_records = []
for d in date_range:
    date_records.append({
        "Date": d.strftime("%Y-%m-%d"),
        "Year": d.year,
        "Quarter": f"Q{d.quarter}",
        "Year_Quarter": f"{d.year}-Q{d.quarter}",
        "Month": d.month,
        "Month_Name": d.strftime("%B"),
        "Month_Year": d.strftime("%b %Y"),
        "Month_Sort": d.year * 100 + d.month,
        "Week_Number": d.isocalendar()[1],
        "Day_Of_Month": d.day,
        "Day_Of_Week": d.strftime("%A"),
        "Day_Of_Week_Num": d.isoweekday(),
        "Is_Weekend": 1 if d.isoweekday() in [6, 7] else 0
    })
df_date = pd.DataFrame(date_records)
df_date.to_csv(os.path.join(DATA_DIR, "dim_date.csv"), index=False)
print("Saved dim_date.csv with", len(df_date), "records.")

# -------------------------------------------------------------
# 5. GENERATE FACT_ORDERS & FACT_ORDER_LINES
# -------------------------------------------------------------
print("Generating orders and order line transactions...")

# Mapping customer region to warehouse
region_warehouse_map = {
    "West": ["WH-WEST-01", "WH-CENTRAL-01"],
    "North": ["WH-NORTH-01"],
    "South": ["WH-SOUTH-01", "WH-SOUTH-02"],
    "East": ["WH-EAST-01", "WH-CENTRAL-01"],
    "Central": ["WH-CENTRAL-01", "WH-WEST-01"]
}

# Reason codes for delays and stockouts
delay_reasons = [
    "Carrier Transport Breakdown",
    "Warehouse Dispatch Backlog",
    "Adverse Weather / Route Diversion",
    "Dock Congestion at Retailer",
    "Documentation / E-Way Bill Hold",
    "None"
]

short_reasons = [
    "Production Batch Under-Run",
    "Regional DC Stockout",
    "Damaged in Handling",
    "FEFO Expiry Rejection",
    "None"
]

order_records = []
line_records = []

order_counter = 10001
line_counter = 50001

# Pre-compute product weights and price lookup
prod_lookup = {row["Product_ID"]: row for row in products_data}
cust_lookup = {row["Customer_ID"]: row for row in customers_data}

# Generate 3,800 orders over 15 months (averaging ~250 orders/month, ~4 lines/order -> ~15,000+ line items)
num_orders = 3800
order_dates = random.choices(date_range[date_range <= datetime(2025, 3, 25)], k=num_orders)

for o_idx, o_date in enumerate(order_dates):
    order_id = f"ORD-{order_counter}"
    order_counter += 1

    # Customer selection (Hypermarkets and Quick commerce order more frequently)
    cust_weights = [
        1.5 if c["Channel"] == "Hypermarket" 
        else 1.8 if c["Channel"] == "Quick Commerce" 
        else 1.0 for c in customers_data
    ]
    customer = random.choices(customers_data, weights=cust_weights, k=1)[0]
    cust_id = customer["Customer_ID"]
    channel = customer["Channel"]
    cust_region = customer["Region"]

    # Select Warehouse based on customer region
    assigned_wh = random.choice(region_warehouse_map[cust_region])

    # Lead time agreement based on channel:
    # Quick commerce: 1-2 days
    # Supermarket / Hypermarket: 2-3 days
    # Wholesale: 4-5 days
    if channel == "Quick Commerce":
        sla_days = random.choice([1, 2])
    elif channel in ["Hypermarket", "Supermarket"]:
        sla_days = random.choice([2, 3])
    else:
        sla_days = random.choice([3, 4, 5])

    promised_date = o_date + timedelta(days=sla_days)

    # Operational condition injection:
    # 1. WH-NORTH-01 has systemic dispatch delays (adds 1-3 days late 45% of the time)
    # 2. Thursday/Friday orders experience carrier congestion (adds 1-2 days 35% of the time)
    # 3. Summer peak (Apr-Jun 2024) cold chain delays for Dairy
    is_wh_north = (assigned_wh == "WH-NORTH-01")
    is_weekend_order = (o_date.isoweekday() in [4, 5]) # Thu, Fri
    is_summer_peak = (o_date.month in [4, 5, 6] and o_date.year == 2024)

    # Determine delivery performance for the order
    # Base on-time probability: 82%
    ot_prob = 0.84
    if is_wh_north:
        ot_prob -= 0.22 # drops to ~62%
    if is_weekend_order:
        ot_prob -= 0.08
    if channel == "Quick Commerce" and sla_days == 1:
        ot_prob -= 0.07

    is_on_time = (random.random() < ot_prob)

    if is_on_time:
        # Delivered on time or early
        early_offset = -1 if (random.random() < 0.12 and sla_days > 1) else 0
        actual_delivery_date = promised_date + timedelta(days=early_offset)
        delay_days = max(0, (actual_delivery_date - promised_date).days)
        delay_reason = "None"
    else:
        # Delayed
        delay_added = random.choices([1, 2, 3, 4], weights=[0.55, 0.28, 0.12, 0.05], k=1)[0]
        actual_delivery_date = promised_date + timedelta(days=delay_added)
        delay_days = delay_added
        if is_wh_north and random.random() < 0.55:
            delay_reason = "Warehouse Dispatch Backlog"
        elif is_weekend_order and random.random() < 0.45:
            delay_reason = "Carrier Transport Breakdown"
        else:
            delay_reason = random.choice([
                "Carrier Transport Breakdown",
                "Dock Congestion at Retailer",
                "Adverse Weather / Route Diversion",
                "Documentation / E-Way Bill Hold"
            ])

    # Number of line items in order
    num_lines = random.randint(2, 6)
    selected_products = random.sample(products_data, k=num_lines)

    order_gross_value = 0.0
    order_delivered_value = 0.0
    order_lines_in_full = 0
    order_penalty_amount = 0.0

    for prod in selected_products:
        line_id = f"LIN-{line_counter}"
        line_counter += 1

        p_id = prod["Product_ID"]
        p_category = prod["Category"]
        unit_price = prod["Unit_Price_USD"]
        unit_cost = prod["Unit_Cost_USD"]

        # Order quantity (Fast moving items have higher order volume)
        if prod["Velocity"] == "Fast-Moving":
            order_qty = random.choice([50, 100, 150, 200, 300, 500])
        elif prod["Velocity"] == "Medium-Moving":
            order_qty = random.choice([30, 50, 80, 120, 150])
        else:
            order_qty = random.choice([15, 25, 40, 60])

        # In-Full Delivery logic:
        # Base in-full prob: 88%
        if_prob = 0.88
        if p_category == "Dairy & Perishables":
            if_prob -= 0.14 # Dairy has frequent short supplies
            if is_summer_peak:
                if_prob -= 0.10
        elif p_id in ["PRD-FOD-01", "PRD-PER-01", "PRD-HMC-01"]:
            # Top sellers with batch capacity bottlenecks
            if_prob -= 0.12

        is_line_in_full = (random.random() < if_prob)

        if is_line_in_full:
            delivered_qty = order_qty
            damaged_qty = 0
            short_qty = 0
            short_reason = "None"
            order_lines_in_full += 1
        else:
            # Short delivery (delivering 60% to 90% of ordered qty)
            fill_pct = random.choice([0.50, 0.65, 0.75, 0.80, 0.85, 0.90])
            delivered_qty = int(order_qty * fill_pct)
            short_qty = order_qty - delivered_qty
            damaged_qty = random.choice([0, 0, 0, 2, 5]) if delivered_qty > 50 else 0
            if p_category == "Dairy & Perishables":
                short_reason = random.choice(["Regional DC Stockout", "FEFO Expiry Rejection", "Production Batch Under-Run"])
            else:
                short_reason = random.choice(["Regional DC Stockout", "Production Batch Under-Run", "Damaged in Handling"])

        line_ordered_val = round(order_qty * unit_price, 2)
        line_delivered_val = round(delivered_qty * unit_price, 2)
        lost_sales_val = round(short_qty * unit_price, 2)

        order_gross_value += line_ordered_val
        order_delivered_value += line_delivered_val

        # Line-level OTIF
        line_is_ot = 1 if is_on_time else 0
        line_is_if = 1 if is_line_in_full else 0
        line_is_otif = 1 if (line_is_ot == 1 and line_is_if == 1) else 0

        line_records.append({
            "Order_Line_ID": line_id,
            "Order_ID": order_id,
            "Product_ID": p_id,
            "Ordered_Qty": order_qty,
            "Delivered_Qty": delivered_qty,
            "Short_Qty": short_qty,
            "Damaged_Qty": damaged_qty,
            "Unit_Price_USD": unit_price,
            "Unit_Cost_USD": unit_cost,
            "Line_Ordered_Value_USD": line_ordered_val,
            "Line_Delivered_Value_USD": line_delivered_val,
            "Lost_Sales_Value_USD": lost_sales_val,
            "Is_Line_On_Time": line_is_ot,
            "Is_Line_In_Full": line_is_if,
            "Is_Line_OTIF": line_is_otif,
            "Short_Reason": short_reason
        })

    # Order-level flags
    order_is_ot = 1 if is_on_time else 0
    order_is_if = 1 if (order_lines_in_full == num_lines) else 0
    order_is_otif = 1 if (order_is_ot == 1 and order_is_if == 1) else 0

    # Contractual penalty calculation if OTIF failed
    penalty_rate = customer["Penalty_Rate_Pct"]
    if order_is_otif == 0:
        # Penalty applied to gross order value
        order_penalty_amount = round(order_gross_value * penalty_rate, 2)
    else:
        order_penalty_amount = 0.0

    order_records.append({
        "Order_ID": order_id,
        "Customer_ID": cust_id,
        "Warehouse_ID": assigned_wh,
        "Order_Date": o_date.strftime("%Y-%m-%d"),
        "Promised_Delivery_Date": promised_date.strftime("%Y-%m-%d"),
        "Actual_Delivery_Date": actual_delivery_date.strftime("%Y-%m-%d"),
        "Planned_Lead_Time_Days": sla_days,
        "Actual_Lead_Time_Days": (actual_delivery_date - o_date).days,
        "Lead_Time_Variance_Days": delay_days,
        "Total_Order_Lines": num_lines,
        "Total_Lines_In_Full": order_lines_in_full,
        "Order_Gross_Value_USD": round(order_gross_value, 2),
        "Order_Delivered_Value_USD": round(order_delivered_value, 2),
        "Order_Lost_Sales_USD": round(order_gross_value - order_delivered_value, 2),
        "Penalty_Amount_USD": order_penalty_amount,
        "Is_Order_On_Time": order_is_ot,
        "Is_Order_In_Full": order_is_if,
        "Is_Order_OTIF": order_is_otif,
        "Primary_Delay_Reason": delay_reason
    })

df_orders = pd.DataFrame(order_records)
df_orders.to_csv(os.path.join(DATA_DIR, "fact_orders.csv"), index=False)
print("Saved fact_orders.csv with", len(df_orders), "orders.")

df_order_lines = pd.DataFrame(line_records)
df_order_lines.to_csv(os.path.join(DATA_DIR, "fact_order_lines.csv"), index=False)
print("Saved fact_order_lines.csv with", len(df_order_lines), "order lines.")

# -------------------------------------------------------------
# 6. GENERATE FACT_FORECAST_ACCURACY
# -------------------------------------------------------------
print("Generating monthly demand forecast vs actuals...")
forecast_records = []
monthly_periods = pd.period_range(start="2024-01", end="2025-03", freq="M")

for period in monthly_periods:
    month_str = period.strftime("%Y-%m")
    is_q2_summer = period.month in [4, 5, 6]
    is_festive_q4 = period.month in [10, 11, 12]

    for prod in products_data:
        p_id = prod["Product_ID"]
        p_cat = prod["Category"]

        for cust in customers_data:
            c_id = cust["Customer_ID"]

            # Base monthly expected volume
            base_vol = 400 if prod["Velocity"] == "Fast-Moving" else 180 if prod["Velocity"] == "Medium-Moving" else 80
            if cust["Channel"] == "Hypermarket":
                base_vol *= 2.2
            elif cust["Channel"] == "Quick Commerce":
                base_vol *= 1.8

            # Seasonality spikes
            multiplier = 1.0
            if p_cat in ["Beverages", "Dairy & Perishables"] and is_q2_summer:
                multiplier = 1.45 # Demand surge
            elif is_festive_q4:
                multiplier = 1.30

            actual_demand = int(base_vol * multiplier * np.random.uniform(0.85, 1.25))

            # Forecast error injection (Forecasting model underestimates surges)
            if is_q2_summer and p_cat in ["Beverages", "Dairy & Perishables"]:
                # Under-forecasted by 20-35% (Causes stockouts!)
                forecasted_demand = int(actual_demand * np.random.uniform(0.68, 0.82))
            elif is_festive_q4:
                forecasted_demand = int(actual_demand * np.random.uniform(0.78, 0.95))
            else:
                forecasted_demand = int(actual_demand * np.random.uniform(0.88, 1.15))

            forecast_error = actual_demand - forecasted_demand
            abs_error = abs(forecast_error)

            forecast_records.append({
                "Month_Year": month_str,
                "Customer_ID": c_id,
                "Product_ID": p_id,
                "Forecast_Qty": forecasted_demand,
                "Actual_Demand_Qty": actual_demand,
                "Forecast_Error_Qty": forecast_error,
                "Abs_Forecast_Error_Qty": abs_error
            })

df_forecast = pd.DataFrame(forecast_records)
df_forecast.to_csv(os.path.join(DATA_DIR, "fact_forecast_accuracy.csv"), index=False)
print("Saved fact_forecast_accuracy.csv with", len(df_forecast), "records.")

print("\n--- Summary Statistics of Generated Data ---")
total_orders = len(df_orders)
ot_orders = df_orders["Is_Order_On_Time"].sum()
if_orders = df_orders["Is_Order_In_Full"].sum()
otif_orders = df_orders["Is_Order_OTIF"].sum()

print(f"Total Orders: {total_orders:,}")
print(f"Total Gross Sales: ${df_orders['Order_Gross_Value_USD'].sum():,.2f}")
print(f"Total Delivered Sales: ${df_orders['Order_Delivered_Value_USD'].sum():,.2f}")
print(f"Total Lost Sales: ${df_orders['Order_Lost_Sales_USD'].sum():,.2f}")
print(f"Total Penalties Incurred: ${df_orders['Penalty_Amount_USD'].sum():,.2f}")
print(f"Overall On-Time (OT) %: {ot_orders / total_orders * 100:.2f}%")
print(f"Overall In-Full (IF) %: {if_orders / total_orders * 100:.2f}%")
print(f"Overall OTIF %: {otif_orders / total_orders * 100:.2f}% (Industry SLA Target: >=92.00%)")
