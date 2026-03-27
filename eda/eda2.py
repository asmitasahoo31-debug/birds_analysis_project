import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_bird_dataset_final.csv")



# BUSINESS INSIGHT:
# Balanced dataset → reliable comparison between habitats

# -------------------------------

# BUSINESS INSIGHT:
# Common species dominate → easier monitoring, but rare species need focus



# BUSINESS INSIGHT:
# Temperature influences bird behavior → climate monitoring neede

# BUSINESS INSIGHT:
# Humidity affects bird activity and visibility


# BUSINESS INSIGHT:
# Birds observed mostly nearby → habitat proximity important



# BUSINESS INSIGHT:
# Majority ground-level → habitat protection is critical

# -------------------------------


# BUSINESS INSIGHT:
# Observation bias may exist → improve survey techniques




# -------------------------------
# 15. YEARLY TREND
# -------------------------------
df.groupby("Year")["Scientific_Name"].count().plot()
plt.title("Yearly Observation Trend")
plt.show()

# BUSINESS INSIGHT:
# Track biodiversity changes over time