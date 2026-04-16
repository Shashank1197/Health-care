# healthcare_analysis.py

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Load the dataset
file_path = 'healthcare_dataset.csv'  # Make sure the CSV is in the same folder
df = pd.read_csv(file_path)

# Set seaborn style
sns.set(style="whitegrid")

# Create a figure to hold multiple subplots
fig, axes = plt.subplots(3, 2, figsize=(18, 18))
fig.suptitle('Healthcare Dataset Analysis', fontsize=22, fontweight='bold')

# 1. Age distribution
sns.histplot(df['Age'], bins=30, kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Age Distribution')

# 2. Gender distribution
gender_counts = df['Gender'].value_counts()
axes[0, 1].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140,
               colors=['lightcoral', 'lightskyblue'])
axes[0, 1].set_title('Gender Distribution')

# 3. Top 10 Medical Conditions
top_conditions = df['Medical Condition'].value_counts().head(10)
sns.barplot(x=top_conditions.values, y=top_conditions.index, ax=axes[1, 0], palette='viridis')
axes[1, 0].set_title('Top 10 Medical Conditions')

# 4. Average Billing Amount per Condition
avg_billing = df.groupby('Medical Condition')['Billing Amount'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=avg_billing.values, y=avg_billing.index, ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Average Billing Amount per Condition')

# 5. Admission Type Counts
admission_counts = df['Admission Type'].value_counts()
sns.barplot(x=admission_counts.index, y=admission_counts.values, ax=axes[2, 0], palette='pastel')
axes[2, 0].set_title('Admission Types')

# 6. Test Results Distribution
test_results_counts = df['Test Results'].value_counts()
sns.barplot(x=test_results_counts.index, y=test_results_counts.values, ax=axes[2, 1], palette='Set2')
axes[2, 1].set_title('Test Results Distribution')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure
output_path = 'healthcare_analysis_output.png'
plt.savefig(output_path)
print(f"Analysis complete. Output saved as {output_path}") 
