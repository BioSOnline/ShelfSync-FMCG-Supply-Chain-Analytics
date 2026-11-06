"""
Diagnostic analytics script to extract granular supply chain insights from generated data.
"""
import pandas as pd
import numpy as np

df_orders = pd.read_csv("data/raw/fact_orders.csv")
df_lines = pd.read_csv("data/raw/fact_order_lines.csv")
df_cust = pd.read_csv("data/raw/dim_customers.csv")
df_prod = pd.read_csv("data/raw/dim_products.csv")
df_wh = pd.read_csv("data/raw/dim_warehouses.csv")
df_fc = pd.read_csv("data/raw/fact_forecast_accuracy.csv")

print("=== 1. OVERALL METRICS ===")
tot_orders = len(df_orders)
ot_pct = df_orders["Is_Order_On_Time"].mean() * 100
if_pct = df_orders["Is_Order_In_Full"].mean() * 100
otif_pct = df_orders["Is_Order_OTIF"].mean() * 100
gross_rev = df_orders["Order_Gross_Value_USD"].sum()
lost_rev = df_orders["Order_Lost_Sales_USD"].sum()
penalties = df_orders["Penalty_Amount_USD"].sum()
total_short_units = df_lines["Short_Qty"].sum()
total_ordered_units = df_lines["Ordered_Qty"].sum()
vol_fill_rate = (df_lines["Delivered_Qty"].sum() / total_ordered_units) * 100

print(f"Total Orders: {tot_orders}")
print(f"OT %: {ot_pct:.2f}% | IF %: {if_pct:.2f}% | OTIF %: {otif_pct:.2f}%")
print(f"Volume Fill Rate: {vol_fill_rate:.2f}%")
print(f"Gross Revenue: ${gross_rev:,.2f}")
print(f"Lost Sales: ${lost_rev:,.2f}")
print(f"Penalties: ${penalties:,.2f}")
print(f"Total Financial Bleed (Lost Sales + Penalties): ${lost_rev + penalties:,.2f} ({(lost_rev + penalties)/gross_rev * 100:.2f}% of Revenue)")

print("\n=== 2. PERFORMANCE BY WAREHOUSE ===")
wh_perf = df_orders.groupby("Warehouse_ID").agg(
    Orders=("Order_ID", "count"),
    OT_Pct=("Is_Order_On_Time", lambda x: x.mean() * 100),
    IF_Pct=("Is_Order_In_Full", lambda x: x.mean() * 100),
    OTIF_Pct=("Is_Order_OTIF", lambda x: x.mean() * 100),
    Avg_Variance_Days=("Lead_Time_Variance_Days", "mean"),
    Penalties=("Penalty_Amount_USD", "sum")
).reset_index().merge(df_wh[["Warehouse_ID", "Warehouse_Name", "Region"]], on="Warehouse_ID")
print(wh_perf.to_string(index=False))

print("\n=== 3. PERFORMANCE BY CUSTOMER CHANNEL ===")
m_orders_cust = df_orders.merge(df_cust, on="Customer_ID")
ch_perf = m_orders_cust.groupby("Channel").agg(
    Orders=("Order_ID", "count"),
    OT_Pct=("Is_Order_On_Time", lambda x: x.mean() * 100),
    IF_Pct=("Is_Order_In_Full", lambda x: x.mean() * 100),
    OTIF_Pct=("Is_Order_OTIF", lambda x: x.mean() * 100),
    Target_OTIF=("SLA_Target_OTIF", lambda x: x.mean() * 100),
    Penalties=("Penalty_Amount_USD", "sum"),
    Lost_Sales=("Order_Lost_Sales_USD", "sum")
).reset_index()
ch_perf["OTIF_Gap"] = ch_perf["OTIF_Pct"] - ch_perf["Target_OTIF"]
print(ch_perf.to_string(index=False))

print("\n=== 4. TOP 5 CUSTOMERS BY PENALTY HIT ===")
top_pen_cust = m_orders_cust.groupby(["Customer_ID", "Customer_Name", "Channel"]).agg(
    Orders=("Order_ID", "count"),
    OTIF_Pct=("Is_Order_OTIF", lambda x: x.mean() * 100),
    Target_OTIF=("SLA_Target_OTIF", lambda x: x.mean() * 100),
    Penalties=("Penalty_Amount_USD", "sum"),
    Lost_Sales=("Order_Lost_Sales_USD", "sum")
).reset_index().sort_values(by="Penalties", ascending=False).head(5)
print(top_pen_cust.to_string(index=False))

print("\n=== 5. PERFORMANCE BY PRODUCT CATEGORY ===")
m_lines_prod = df_lines.merge(df_prod, on="Product_ID")
cat_perf = m_lines_prod.groupby("Category").agg(
    Lines=("Order_Line_ID", "count"),
    Line_OT_Pct=("Is_Line_On_Time", lambda x: x.mean() * 100),
    Line_IF_Pct=("Is_Line_In_Full", lambda x: x.mean() * 100),
    Line_OTIF_Pct=("Is_Line_OTIF", lambda x: x.mean() * 100),
    Ordered_Units=("Ordered_Qty", "sum"),
    Delivered_Units=("Delivered_Qty", "sum"),
    Lost_Sales_USD=("Lost_Sales_Value_USD", "sum")
).reset_index()
cat_perf["Line_Fill_Rate_Pct"] = (cat_perf["Delivered_Units"] / cat_perf["Ordered_Units"]) * 100
print(cat_perf.to_string(index=False))

print("\n=== 6. ROOT CAUSES FOR ORDER DELAYS ===")
delay_df = df_orders[df_orders["Primary_Delay_Reason"] != "None"]
delay_counts = delay_df["Primary_Delay_Reason"].value_counts(normalize=True) * 100
delay_vals = delay_df.groupby("Primary_Delay_Reason")["Order_Gross_Value_USD"].sum()
root_delays = pd.DataFrame({"Pct_Of_Delayed_Orders": delay_counts, "Gross_Value_Affected": delay_vals})
print(root_delays.to_string())

print("\n=== 7. ROOT CAUSES FOR SHORT DELIVERIES ===")
short_df = df_lines[df_lines["Short_Reason"] != "None"]
short_counts = short_df["Short_Reason"].value_counts(normalize=True) * 100
short_lost = short_df.groupby("Short_Reason")["Lost_Sales_Value_USD"].sum()
root_shorts = pd.DataFrame({"Pct_Of_Short_Lines": short_counts, "Lost_Sales_USD": short_lost})
print(root_shorts.to_string())

print("\n=== 8. DEMAND FORECAST ACCURACY (WAPE & BIAS) ===")
m_fc_prod = df_fc.merge(df_prod, on="Product_ID")
fc_by_cat = m_fc_prod.groupby("Category").agg(
    Total_Actual=("Actual_Demand_Qty", "sum"),
    Total_Forecast=("Forecast_Qty", "sum"),
    Sum_Abs_Error=("Abs_Forecast_Error_Qty", "sum"),
    Sum_Error=("Forecast_Error_Qty", "sum")
).reset_index()
fc_by_cat["WAPE_Pct"] = (fc_by_cat["Sum_Abs_Error"] / fc_by_cat["Total_Actual"]) * 100
fc_by_cat["Forecast_Bias_Pct"] = (fc_by_cat["Sum_Error"] / fc_by_cat["Total_Actual"]) * 100 # Positive = Underforecasted
print(fc_by_cat.to_string(index=False))
