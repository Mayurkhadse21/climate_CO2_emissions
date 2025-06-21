# Step 1: Load and preview full dataset

import pandas as pd

# Load the full dataset
df = pd.read_csv("full_climate_co2_emissions_data.csv")

# Preview first few rows
df.head()

# Step 2: Global CO₂ Emissions Over Time (1960–2023)

import matplotlib.pyplot as plt
import seaborn as sns

# Group by year for global total
global_emissions = df.groupby("Year")["CO2 Emissions (Mt)"].sum()

# Plotting
plt.figure(figsize=(12,6))
sns.lineplot(x=global_emissions.index, y=global_emissions.values)
plt.title("🌍 Global CO₂ Emissions (1960–2023)")
plt.xlabel("Year")
plt.ylabel("Total Emissions (Million Tonnes)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 3: Top 10 Emitters in the Most Recent Year

latest_year = df["Year"].max()

top_emitters = df[df["Year"] == latest_year].sort_values(by="CO2 Emissions (Mt)", ascending=False)

# Bar plot
plt.figure(figsize=(10,5))
sns.barplot(data=top_emitters.head(10), x="CO2 Emissions (Mt)", y="Country", palette="Reds_r")
plt.title(f"🔝 Top 10 CO₂ Emitters in {latest_year}")
plt.xlabel("Emissions (Million Tonnes)")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# Step 4: Emissions per Capita – Compare Countries

# Filter to key countries
countries_to_compare = ["India", "USA", "China"]
filtered = df[df["Country"].isin(countries_to_compare)]

# Line plot
plt.figure(figsize=(12,6))
sns.lineplot(data=filtered, x="Year", y="CO2 per Capita", hue="Country")
plt.title("📈 CO₂ Emissions per Capita Over Time")
plt.xlabel("Year")
plt.ylabel("CO₂ per Capita (Tonnes/person)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Emissions vs Population Trend

# Group globally by year
trend_df = df.groupby("Year").agg({
    "CO2 Emissions (Mt)": "sum",
    "Population": "sum"
}).reset_index()

# Calculate global CO2 per capita
trend_df["CO2 per Capita"] = trend_df["CO2 Emissions (Mt)"] / (trend_df["Population"] / 1_000_000)

# Plot emissions vs population
plt.figure(figsize=(12, 6))
sns.lineplot(x="Year", y="CO2 Emissions (Mt)", data=trend_df, label="Total CO₂ Emissions", color="red")
sns.lineplot(x="Year", y="Population", data=trend_df, label="Total Population", color="blue")
plt.title("🌍 Global CO₂ Emissions vs Population")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Global Summary KPIs (Latest Year)

latest_year = df["Year"].max()
latest_data = df[df["Year"] == latest_year]

total_emissions = latest_data["CO2 Emissions (Mt)"].sum()
total_population = latest_data["Population"].sum()
avg_per_capita = total_emissions / (total_population / 1_000_000)

print(f"🌍 Summary for {latest_year}:")
print(f"• Total CO₂ Emissions: {total_emissions:,.2f} million tonnes")
print(f"• Total Population: {total_population:,.0f}")
print(f"• Global CO₂ per Capita: {avg_per_capita:.2f} tonnes/person")


# Exporting the Summary for using in Power BI

# Save the per-year trend
trend_df.to_csv("global_trend_summary.csv", index=False)

# Save the country-wise latest snapshot
latest_data.to_csv("countrywise_emissions_latest_year.csv", index=False)