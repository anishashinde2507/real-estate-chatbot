"""
Script to generate sample real estate data Excel file.
Run this before starting the backend.
"""

import pandas as pd
import os

# Sample data
data = {
    'Year': [2020, 2021, 2022, 2023, 2024] * 4,
    'Area': ['Wakad'] * 5 + ['Akurdi'] * 5 + ['Aundh'] * 5 + ['Baner'] * 5,
    'Price': [45, 48, 52, 58, 65, 35, 37, 40, 44, 48, 50, 53, 56, 60, 65, 42, 45, 48, 52, 56],
    'Demand': [85, 88, 90, 92, 95, 75, 78, 80, 82, 85, 80, 82, 85, 88, 90, 78, 80, 83, 86, 89],
    'Size': [1200, 1250, 1300, 1400, 1500, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1600, 1150, 1200, 1250, 1350, 1400],
}

df = pd.DataFrame(data)

# Create data directory if not exists
os.makedirs('data', exist_ok=True)

# Save to Excel
output_path = 'data/realestate.xlsx'
df.to_excel(output_path, index=False)

print(f"✓ Excel file created: {output_path}")
print(f"✓ Total records: {len(df)}")
print(f"✓ Areas: {df['Area'].unique().tolist()}")
