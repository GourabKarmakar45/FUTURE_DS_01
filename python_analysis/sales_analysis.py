import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folder
charts_path = "charts"
os.makedirs(charts_path, exist_ok=True)
# Function to save plots
def save_plot(filename):
    plt.tight_layout()
    plt.savefig(os.path.join(charts_path, filename), dpi=300)
    plt.close()

#Load the sales data
sales_data = "fixed_sales_dataset_200.csv"

try:
    df=pd.read_csv(sales_data)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path name and location.")
    exit()

df = pd.read_csv(sales_data)
print(df.head())


#Data Cleaning
#order date to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors= 'coerce')
print(df.info())
print(df.tail())

#check the missing values
df=df.dropna()
print(df)

#create revenue column
df['Revenue']=df['Quantity']*df['Price']
print(df.head())
#print(df.describe())

print("Data cleaning completed successfully.")


#Basic Information
print("\n**📊Basic information about the dataset.**")
print(df.info())

print("\n📈 Summary Statistics:")
print(df.describe())


#Data Analysis
print("\n Data Analysis:")
#Revenue trend over the time
revenue_trend = df.groupby('Order_Date')['Revenue'].sum()  #means same data ka revenue ko sum karna hai order date ke hisab se
print(revenue_trend)

#chek the top products
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print("\n Top products by revenue: ")
print(top_products)


#Monthly revenue trend
df['Month'] = df['Order_Date'].dt.to_period('M')
monthly_trend = df.groupby('Month')['Revenue'].sum()
print(monthly_trend)

print("\n✅ Analysis Completed!")




#Data Visualization
print("\n**📊 Generated all the charts..**")

#Trend over time visualization
plt.figure()
revenue_trend.plot()
plt.title("Revenue Trend Over the Time")
plt.xlabel("Product ")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
save_plot("revenue_trend.png")
print("Trend over time graph saved successfully.")



#Visualize top 5 selling products
plt.figure()
top_products.head(5).plot(kind='bar')
plt.title("Revenue by Category")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
save_plot("top5_selling_product.png")
print("Top 5 selling product graph saved successfully.")



#  Visualize of Monthly Trend
plt.figure()
monthly_trend.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
save_plot("monthly_trend.png")
print("Monthly trend graph saved successfully.")




print("\n💡 BUSINESS INSIGHTS")

print("\n🏆 Top Product:")
print(top_products.head(1))

print("\n📦 Best Category:")
print(top_products.head(1))

#print("\n🌍 Best Region:")
#print(region_performance.head(1))

print("\n💰 Total Revenue:")
print(df['Revenue'].sum())

# ==========================================
# 📌 8. SAVE RESULTS
# ==========================================

print("\n💾 Saving Reports...")

top_products.to_csv("top_products.csv")
#top_products.to_csv("category_performance.csv")
#region_performance.to_csv("region_performance.csv")
monthly_trend.to_csv("monthly_trend.csv")

print("✅ Files Saved Successfully!")

# ==========================================
# 📌 9. FINAL MESSAGE
# ==========================================

print("\n🎉 PROJECT COMPLETED SUCCESSFULLY!")
print("You have performed a full Business Sales Analysis using Python 🚀")



