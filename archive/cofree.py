import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("Coffee_production.csv")
print(df.head())
print(df.shape)

# 2. Q1: Which country produces the most coffee?
top = df.sort_values("Total_production", ascending=False)
print(top[["Country", "Total_production"]].head(5))

top5 = top.head(5)
plt.bar(top5["Country"], top5["Total_production"])
plt.title("Top 5 coffee producers")
plt.ylabel("Total production")
plt.show()

# 3. Q2: Which coffee type has the highest production?
by_type = df.groupby("Coffee type")["Total_production"].sum()
print(by_type)

by_type.plot(kind="bar")
plt.title("Production by coffee type")
plt.ylabel("Total production")
plt.show()

# 4. Q3: How does world production change over time?
year_cols = df.columns[2:-1]
world = df[year_cols].sum()

world.plot(kind="line")
plt.title("World coffee production by year")
plt.ylabel("Production")
plt.xticks(rotation=90)
plt.show()