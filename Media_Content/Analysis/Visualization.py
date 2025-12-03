import pandas as pd
import matplotlib.pyplot as plt
import os

# === Step 1: Load the Data ===
data = pd.read_csv("../Data_Resources/combined_transformed.csv")

# === Step 2: Create Output Folder (if not exists) ===
output_dir = "../Output_Data"
os.makedirs(output_dir, exist_ok=True)

# === Step 3: Visualization 1 - Content Type Distribution ===
type_count = data['type'].value_counts()
plt.figure(figsize=(6, 4))
type_count.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Content Type Distribution')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "content_type_distribution.png"))
plt.show()

# === Step 4: Visualization 2 - Top 10 Genres ===
top_genres = data['main_genre'].value_counts().head(10)
plt.figure(figsize=(8, 5))
top_genres.plot(kind='barh', color='salmon')
plt.title('Top 10 Genres')
plt.xlabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_10_genres.png"))
plt.show()

# === Step 5: Visualization 3 - Content Added Over the Years ===
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
yearly = data['date_added'].dt.year.value_counts().sort_index()
plt.figure(figsize=(8, 5))
yearly.plot(kind='line', marker='o', color='orange')
plt.title('Content Added Over the Years')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "content_added_over_years.png"))
plt.show()

# === Step 6: Visualization 4 - Platform Distribution ===
platform_count = data['platform'].value_counts()
plt.figure(figsize=(5, 5))
platform_count.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightblue'])
plt.title('Platform Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "platform_distribution.png"))
plt.show()

# === Step 7: Visualization 5- Top 10 Countries Producing Most Content===
top_countries = data['country'].value_counts().head(10)
plt.figure(figsize=(8, 5))
top_countries.plot(kind='bar', color='teal')
plt.title('Top 10 Content Producing Countries')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_10_countries.png"))
plt.show()

# === Step 6: Visualization 6 - Average Rating Distribution ===
rating_count = data['rating'].value_counts()
plt.figure(figsize=(7, 4))
rating_count.plot(kind='bar', color='purple')
plt.title('Content Rating Distribution')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "content_rating_distribution.png"))
plt.show()


print(f"✅ All charts saved successfully in: {os.path.abspath(output_dir)}")
