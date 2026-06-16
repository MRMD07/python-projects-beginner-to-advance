import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("social_sectors1.csv")

revised_budget = data['revised_2025_26']
budget_25 = data["budget_2025_26"]
budget_26 = data["budget_2026_27"]