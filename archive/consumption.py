import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv(r"D:\LEARN BROGRAMMING ALL\archive\Coffee_domestic_consumption.csv")
print(df.head())
print(df.shape)

# 2. Q1: Which country consumes the most coffee?
top = df.sort_values("Total_domestic_consumption", ascending=False)
print(top[["Country", "Total_domestic_consumption"]].head(5))

top5 = top.head(5)
plt.bar(top5["Country"], top5["Total_domestic_consumption"])
plt.title("Top 5 coffee consuming countries")
plt.ylabel("Total domestic consumption")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# 3. Q2: Which coffee type is consumed the most?
by_type = df.groupby("Coffee type")["Total_domestic_consumption"].sum()
print(by_type)

by_type.plot(kind="bar")
plt.title("Consumption by coffee type")
plt.ylabel("Total domestic consumption")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4. Q3: How does world consumption change over time?
year_cols = df.columns[2:-1]
world = df[year_cols].sum()
print(world)

world.plot(kind="line")
plt.title("World coffee consumption by year")
plt.ylabel("Consumption")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()