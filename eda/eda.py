import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_bird_dataset_final.csv")

# -------------------------------
# BASIC INFO
# -------------------------------
print("Shape:", df.shape)
print("Columns:", df.columns)

# -------------------------------
# 1. TOTAL SPECIES
# -------------------------------
total_species = df["Scientific_Name"].nunique()
print("Total Species:", total_species)

# -------------------------------
# 2. SPECIES BY HABITAT
# -------------------------------
species_habitat = df.groupby("Habitat")["Scientific_Name"].nunique()

species_habitat.plot(kind='bar')
plt.title("Species Diversity by Habitat")
plt.ylabel("Unique Species")
plt.show()

# BUSINESS INSIGHT:
# Forest areas have higher biodiversity → prioritize conservation

# -------------------------------
# 3. OBSERVATION COUNT
# -------------------------------
df["Habitat"].value_counts().plot(kind='bar')
plt.title("Observation Distribution")
plt.show()

# BUSINESS INSIGHT:
# Balanced dataset → reliable comparison between habitats

# -------------------------------
# 4. TOP 10 SPECIES
# -------------------------------
df["Common_Name"].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Bird Species")
plt.show()

# BUSINESS INSIGHT:
# Common species dominate → easier monitoring, but rare species need focus

# -------------------------------
# 5. MONTHLY ACTIVITY
# -------------------------------
df.groupby(["Month","Habitat"])["Scientific_Name"].count().unstack().plot()
plt.title("Monthly Bird Activity")
plt.show()

# BUSINESS INSIGHT:
# Seasonal trends → useful for eco-tourism and conservation planning

# -------------------------------
# 6. TEMPERATURE IMPACT
# -------------------------------
df.groupby("Habitat")["Temperature"].mean().plot(kind='bar')
plt.title("Average Temperature by Habitat")
plt.show()

# BUSINESS INSIGHT:
# Temperature influences bird behavior → climate monitoring needed

# -------------------------------
# 7. HUMIDITY IMPACT
# -------------------------------
df.groupby("Habitat")["Humidity"].mean().plot(kind='bar')
plt.title("Humidity by Habitat")
plt.show()

# BUSINESS INSIGHT:
# Humidity affects bird activity and visibility

# -------------------------------
# 8. DISTANCE ANALYSIS
# -------------------------------
df["Distance"].value_counts().head(10).plot(kind='bar')
plt.title("Distance Distribution")
plt.show()

# BUSINESS INSIGHT:
# Birds observed mostly nearby → habitat proximity important

# -------------------------------
# 9. FLYOVER ANALYSIS
# -------------------------------
df["Flyover_Observed"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Flyover Behavior")
plt.show()

# BUSINESS INSIGHT:
# Majority ground-level → habitat protection is critical

# -------------------------------
# 10. SEX DISTRIBUTION
# -------------------------------
df["Sex"].value_counts().plot(kind='bar')
plt.title("Sex Distribution")
plt.show()

# BUSINESS INSIGHT:
# Observation bias may exist → improve survey techniques

# -------------------------------
# 11. LOCATION HOTSPOTS
# -------------------------------
df.groupby("Admin_Unit")["Scientific_Name"].count().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top Locations (Hotspots)")
plt.show()

# BUSINESS INSIGHT:
# Identify key biodiversity zones → prioritize protection

# -------------------------------
# 12. ID METHOD
# -------------------------------
df["ID_Method"].value_counts().plot(kind='bar')
plt.title("Identification Method")
plt.show()

# BUSINESS INSIGHT:
# Some methods more effective → standardize data collection

# -------------------------------
# 13. DISTURBANCE IMPACT
# -------------------------------
df["Disturbance"].value_counts().head(5).plot(kind='bar')
plt.title("Disturbance Impact")
plt.show()

# BUSINESS INSIGHT:
# Human/environment disturbance affects bird activity

# -------------------------------
# 14. RARE SPECIES
# -------------------------------
rare_species = df["Common_Name"].value_counts().tail(10)
print("Rare Species:\n", rare_species)

# BUSINESS INSIGHT:
# Rare species need conservation focus

# -------------------------------
# 15. YEARLY TREND
# -------------------------------
df.groupby("Year")["Scientific_Name"].count().plot()
plt.title("Yearly Observation Trend")
plt.show()

# BUSINESS INSIGHT:
# Track biodiversity changes over time