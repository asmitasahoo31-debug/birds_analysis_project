import pandas as pd

# File paths
forest_file = "data/Bird_Monitoring_Data_FOREST.xlsx"
grass_file = "data/Bird_Monitoring_Data_GRASSLAND.xlsx"

# Load Forest Data
forest_excel = pd.ExcelFile(forest_file)
forest_data = {}

for sheet in forest_excel.sheet_names:
    forest_data[sheet] = pd.read_excel(forest_file, sheet_name=sheet)

print("Forest Sheets:", forest_excel.sheet_names)

# Load Grassland Data
grass_excel = pd.ExcelFile(grass_file)
grass_data = {}

for sheet in grass_excel.sheet_names:
    grass_data[sheet] = pd.read_excel(grass_file, sheet_name=sheet)

print("Grassland Sheets:", grass_excel.sheet_names)

# View one sheet
print(forest_data["ANTI"].head())
print(grass_data["ANTI"].head())

print(forest_data["ANTI"].columns)

print(forest_data["ANTI"].shape)

forest_list = []

for sheet, data in forest_data.items():
    data["Admin_Unit"] = sheet   # location name
    data["Habitat"] = "Forest"   # mark habitat
    forest_list.append(data)

forest_df = pd.concat(forest_list, ignore_index=True)

print("Forest combined shape:", forest_df.shape)

grass_list = []

for sheet, data in grass_data.items():
    data["Admin_Unit"] = sheet
    data["Habitat"] = "Grassland"
    grass_list.append(data)

grass_df = pd.concat(grass_list, ignore_index=True)

print("Grassland combined shape:", grass_df.shape)

df = pd.concat([forest_df, grass_df], ignore_index=True)

print("Final dataset shape:", df.shape)
print(df.head())

print(df.columns)
print(df["Habitat"].value_counts())

# 1. Remove missing species
df = df.dropna(subset=["Scientific_Name"])

# 2. Convert date
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# 3. Extract time features
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

# 4. Fill missing values
df["Sex"] = df["Sex"].fillna("Unknown")
df["Flyover_Observed"] = df["Flyover_Observed"].fillna(False)

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Drop unnecessary columns
df = df.drop(columns=["TaxonCode", "Previously_Obs"], errors='ignore')

# 7. Standardize text
df["Location_Type"] = df["Location_Type"].str.strip()

print("Cleaned shape:", df.shape)


df.isnull().sum()
empty_cols = df.columns[df.isnull().all()]
print(empty_cols)
df = df.drop(columns=empty_cols)
threshold = 0.8
df = df.dropna(axis=1, thresh=int((1-threshold)*len(df)))
df.isnull().sum().sort_values(ascending=False)
df["Sex"] = df["Sex"].fillna("Unknown")
df["Flyover_Observed"] = df["Flyover_Observed"].fillna(False)
df["Sky"] = df["Sky"].fillna("Unknown")
df["Wind"] = df["Wind"].fillna("Unknown")
df["Disturbance"] = df["Disturbance"].fillna("No Data")
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].mean())
df["Distance"] = df["Distance"].fillna("Unknown")
print(df.columns[df.columns.duplicated()])
df = df.loc[:, ~df.columns.duplicated()]
print(df.columns)

df = df.drop(columns=["NPSTaxonCode"], errors="ignore")
df.to_csv("cleaned_bird_dataset_final.csv", index=False)