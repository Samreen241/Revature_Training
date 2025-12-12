import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("cleaned_streaming_titles.csv")

# Define output folder relative to project root
output_dir = os.path.join(os.getcwd(), "output", "plots")
os.makedirs(output_dir, exist_ok=True)  # Create folder if it doesn't exist

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'axes.titlesize': 16, 'axes.labelsize': 12})

# Ensure release_year is numeric and create content_age
df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce")
df["content_age"] = 2025 - df["release_year"]

# Helper function to save plots
def save_plot(fig, filename):
    path = os.path.join(output_dir, filename)
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)

# 1. Content count by platform
fig = plt.figure()
platform_counts = df["platform"].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values, hue=platform_counts.index, palette="Set2", legend=False)
plt.title("Content Count by Platform")
plt.xlabel("Platform")
plt.ylabel("Number of Titles")
plt.tight_layout()
save_plot(fig, "content_count_by_platform.png")

# 2. Content added per year
fig = plt.figure()
yearly = df["year_added"].value_counts().sort_index()
sns.lineplot(x=yearly.index, y=yearly.values, marker="o", color="teal")
for x, y in zip(yearly.index, yearly.values):
    plt.text(x, y + 5, str(y), ha='center')
plt.title("Content Added Per Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.tight_layout()
save_plot(fig, "content_added_per_year.png")

# 3. Top 10 countries by content count
fig = plt.figure()
top_countries = df["country"].value_counts().head(10)
sns.barplot(y=top_countries.index, x=top_countries.values, hue=top_countries.index, palette="coolwarm", legend=False)
plt.title("Top 10 Countries by Content Count")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
save_plot(fig, "top_10_countries.png")

# 4. Rating distribution
fig = plt.figure()
rating_counts = df["rating"].value_counts().head(10)
sns.barplot(y=rating_counts.index, x=rating_counts.values, hue=rating_counts.index, palette="muted", legend=False)
plt.title("Rating Distribution")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()
save_plot(fig, "rating_distribution.png")

# 5. Content age distribution
fig = plt.figure()
sns.histplot(df["content_age"].dropna(), bins=20, kde=True, color="skyblue")
plt.title("Content Age Distribution")
plt.xlabel("Years Since Release")
plt.ylabel("Frequency")
plt.tight_layout()
save_plot(fig, "content_age_distribution.png")

print(f"✔ All visualizations saved successfully in {output_dir}/")
