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

inflation_target = 8.2  # Official Government Inflation Target
nominal_yoy = ((budget_26 - revised_budget) / revised_budget) * 100

plt.figure(figsize=(14, 7))


filtered_indices = [i for i in range(len(labels)) if i not in [6, 9]]
plot_labels = labels.iloc[filtered_indices]
plot_growth = nominal_yoy.iloc[filtered_indices]

# Green if it beats inflation, coral if it's a real-term spending cut
colors = ['g' if x >= inflation_target else 'coral' for x in plot_growth]

plt.barh(plot_labels, plot_growth, color=colors, edgecolor='black', height=0.6)
plt.axvline(inflation_target, color='red', linestyle='--', linewidth=2, 
            label=f'Official Inflation Target ({inflation_target}%)')

plt.title("FY2026-27 New Budget Allocation Growth vs. 8.2% Inflation Target\n(Sectors in Orange are facing Real-Term Funding Slashes)", 
          fontsize=12, fontweight='bold', pad=15)
plt.xlabel("Nominal Year-on-Year Growth Rate (%)")
plt.ylabel("Budgetary Line Item")
plt.legend(loc='lower right')
plt.grid(axis='x', linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()  # <-- CLOSE THIS WINDOW TO SEE THE FINAL MACRO CHART