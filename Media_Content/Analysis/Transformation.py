import pandas as pd

# === Step 1: Load the Combined Cleaned Dataset ===
combined = pd.read_csv("../Data_Resources/combined_media_titles.csv")

# === Step 2: Handle Duplicates ===
combined = combined.drop_duplicates(subset=['title', 'platform']).reset_index(drop=True)

# === Step 3: Extract Year and Month from 'date_added' ===
combined['date_added'] = pd.to_datetime(combined['date_added'], errors='coerce')
combined['year_added'] = combined['date_added'].dt.year
combined['month_added'] = combined['date_added'].dt.month_name()

# === Step 4: Simplify Genre Column ===
combined['main_genre'] = combined['genre'].apply(lambda x: x.split(',')[0] if isinstance(x, str) else None)

# === Step 5: Add Binary Columns for Analysis ===
combined['is_movie'] = combined['type'].apply(lambda x: 1 if x == 'Movie' else 0)
combined['is_tv'] = combined['type'].apply(lambda x: 1 if x == 'TV' else 0)

# === Step 6: Save Transformed Dataset ===
combined.to_csv("../Data_Resources/combined_transformed.csv", index=False)

# === Step 7: Display Summary ===
print("✅ Transformation Complete!")
print(f"Rows after transformation: {len(combined)}")
print("\nSample transformed data:")
print(combined.head().to_string())
