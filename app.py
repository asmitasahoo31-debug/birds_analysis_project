import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Bird Insights Dashboard", layout="wide")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_bird_dataset_final.csv")
    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.title("🔎 Filters")

habitat = st.sidebar.multiselect(
    "Select Habitat",
    df["Habitat"].dropna().unique(),
    default=df["Habitat"].dropna().unique()
)

month = st.sidebar.multiselect(
    "Select Month",
    sorted(df["Month"].dropna().unique()),
    default=sorted(df["Month"].dropna().unique())
)

df = df[(df["Habitat"].isin(habitat)) & (df["Month"].isin(month))]

# -----------------------------
# TITLE
# -----------------------------
st.title("🌿 Bird Insights Dashboard")

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Observations", len(df))
col2.metric("🐦 Total Species", df["Scientific_Name"].nunique())
col3.metric("🌡 Avg Temperature", round(df["Temperature"].mean(), 2))

st.markdown("---")

# -----------------------------
# 1. Species Diversity
# -----------------------------
species_df = df.groupby("Habitat")["Scientific_Name"].nunique().reset_index()

fig1 = px.bar(
    species_df,
    x="Habitat",
    y="Scientific_Name",
    color="Habitat",
    title="Species Diversity by Habitat"
)
st.plotly_chart(fig1, use_container_width=True)

st.info("🌍 Forest habitats show higher biodiversity → prioritize conservation.")

# -----------------------------
# 2. Top Species
# -----------------------------
top_species = df["Common_Name"].value_counts().head(10).reset_index()
top_species.columns = ["Common_Name", "Count"]

fig2 = px.bar(
    top_species,
    x="Common_Name",
    y="Count",
    color="Count",
    title="Top 10 Bird Species"
)
st.plotly_chart(fig2, use_container_width=True)

st.info("🐦 Few species dominate → rare species need attention.")

# -----------------------------
# 3. Monthly Trend
# -----------------------------
monthly = df.groupby(["Month", "Habitat"]).size().reset_index(name="Count")

fig3 = px.line(
    monthly,
    x="Month",
    y="Count",
    color="Habitat",
    markers=True,
    title="Monthly Bird Activity"
)
st.plotly_chart(fig3, use_container_width=True)

st.info("📅 Bird activity varies seasonally.")

# -----------------------------
# 4. Temperature
# -----------------------------
temp_df = df.groupby("Habitat")["Temperature"].mean().reset_index()

fig4 = px.bar(
    temp_df,
    x="Habitat",
    y="Temperature",
    color="Habitat",
    title="Temperature Impact"
)
st.plotly_chart(fig4, use_container_width=True)

st.info("🌦 Temperature influences bird behavior.")

# -----------------------------
# 5. Humidity
# -----------------------------
hum_df = df.groupby("Habitat")["Humidity"].mean().reset_index()

fig5 = px.bar(
    hum_df,
    x="Habitat",
    y="Humidity",
    color="Habitat",
    title="Humidity Impact"
)
st.plotly_chart(fig5, use_container_width=True)

st.info("💧 Humidity affects bird activity.")

# -----------------------------
# 6. Distance Distribution (FIXED)
# -----------------------------
distance_df = df["Distance"].value_counts().reset_index()
distance_df.columns = ["Distance", "Count"]

fig6 = px.bar(
    distance_df,
    x="Distance",
    y="Count",
    color="Count",
    title="Distance Distribution"
)
st.plotly_chart(fig6, use_container_width=True)

st.info("📍 Most birds observed nearby.")

# -----------------------------
# 7. Flyover
# -----------------------------
fig7 = px.pie(
    df,
    names="Flyover_Observed",
    title="Flyover Behavior"
)
st.plotly_chart(fig7, use_container_width=True)

st.info("✈️ Most birds are local (not flyovers).")

# -----------------------------
# 8. Sex Distribution (FIXED)
# -----------------------------
sex_df = df["Sex"].value_counts().reset_index()
sex_df.columns = ["Sex", "Count"]

fig8 = px.bar(
    sex_df,
    x="Sex",
    y="Count",
    color="Count",
    title="Sex Distribution"
)
st.plotly_chart(fig8, use_container_width=True)

st.info("⚖️ Possible observation bias.")

# -----------------------------
# 9. Hotspots
# -----------------------------
hotspots = df.groupby("Admin_Unit").size().reset_index(name="Count")

fig9 = px.bar(
    hotspots.sort_values("Count", ascending=False).head(10),
    x="Admin_Unit",
    y="Count",
    color="Count",
    title="Top Biodiversity Locations"
)
st.plotly_chart(fig9, use_container_width=True)

st.info("📍 Certain locations are biodiversity hotspots.")

# -----------------------------
# FINAL INSIGHTS
# -----------------------------
st.markdown("---")
st.subheader("📌 Final Business Insights")

st.success("""
✔ Forest areas have higher biodiversity  
✔ Seasonal patterns influence bird activity  
✔ Environmental factors affect behavior  
✔ Rare species need conservation focus  
✔ Certain locations act as biodiversity hotspots  
""")

# -----------------------------
# DATA TABLE
# -----------------------------
st.subheader("📋 Dataset Preview")
st.dataframe(df.head(100))