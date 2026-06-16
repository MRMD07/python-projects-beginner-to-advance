import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("social_sectors1.csv")

revised_budget = data['revised_2025_26']
budget_25 = data["budget_2025_26"]
budget_26 = data["budget_2026_27"]

variance = ((revised_budget-budget_25)/budget_25) * 100

yoy_growth = ((budget_26-revised_budget)/revised_budget)*100

sustainable_budget = budget_26/11751000


labels = data['sub_classification']

plt.figure(figsize=(12, 6))
plt.barh(labels, variance, color='skyblue', edgecolor='black')
plt.axvline(0, color='red', linestyle='--', linewidth=1)
plt.title("Budget Variance % (Revised 2025-26 vs Original Budget 2025-26)", fontweight='bold')
plt.xlabel("Variance Percentage (%)")
plt.ylabel("Sub-Classification Line Item")
plt.tight_layout()
plt.show()  # <-- WHEN THIS WINDOW OPENS, CLOSE IT TO SEEN THE NEXT CHART
