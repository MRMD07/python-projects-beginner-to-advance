# 📊 Medium Level Projects

Welcome to the Medium level! You've mastered the basics—now let's tackle real-world problems using data analysis, statistics, and more sophisticated programming techniques.

## 📚 What You'll Learn

At this level, you'll develop skills in:
- **Data Analysis**: Working with datasets using NumPy and Pandas
- **Statistical Concepts**: Mean, standard deviation, variance, similarity metrics
- **Data Visualization**: Creating charts and plots with Matplotlib
- **Algorithm Implementation**: Building recommendation systems and predictive models
- **Real-World Problem Solving**: Approaching business problems systematically
- **PDLC Methodology**: Program Development Life Cycle for structured solutions

## 🎯 Prerequisites

Before starting Medium level, ensure you're comfortable with:
- ✅ Functions and modules
- ✅ Lists and basic data structures
- ✅ Loops and conditional logic
- ✅ Basic Python syntax and problem-solving
- ✅ Reading and understanding existing code

## 📚 Required Libraries

Install these before starting:
```bash
pip install numpy pandas matplotlib
```

## 🎯 How to Use This Repository

### **Our Systematic Approach - PDLC Method**

We follow the **Program Development Life Cycle** for every project:

1. **Attempt**: Read the problem and try solving it independently
2. **Compare**: Check the provided solution against yours
3. **Learn**: Identify what was different and why
4. **Contribute**: If you find a more efficient approach, submit a pull request!

---

## 📋 Projects Overview

| # | Project Name | Focus Area | Real-World Application | Difficulty | Libraries |
|---|---|---|---|---|---|
| 1 | **Cinema Analytics & Collaborative Filtering** | Data Analysis & Recommendations | Recommendation Systems | ⭐⭐ | NumPy |
| 2 | **Budget Analysis & Visualization** | Financial Analysis & Visualization | Government Budget Planning | ⭐⭐ | Pandas, Matplotlib |

---

## 🎬 Project 1: Cinema Analytics & Collaborative Filtering Engine

### **Real-World Context**
Streaming platforms like Netflix and YouTube need to recommend movies to users. This project teaches you the fundamental concepts behind these recommendation engines using **Collaborative Filtering** and **Euclidean Distance**.

### **Business Problem**
A cinema platform has:
- 100 users who have rated 20 movies (1-5 stars)
- 25% of ratings are missing (users haven't watched every movie)
- Need to find which movies to recommend to users based on similar users' preferences

### **🎯 Project Objectives & Requirements**

1. **Simulate Sparse Real-World Data**: Generate a 100×20 user-movie matrix (ratings 1–5) and randomly inject `np.nan` values into 25% of the data to simulate unwatched movies.

2. **Statistical Analysis**: Calculate global movie statistics (mean and standard deviation) while ignoring missing values to identify the most "controversial" film.

3. **Targeted Behavioral Profiling**: Filter and isolate specific user demographics (e.g., "Sci-Fi Fans") based on multi-dimensional slicing criteria.

4. **User Similarity Modeling**: Implement the geometric **Euclidean Distance Formula** to find the user most architecturally similar to a target user profile.

5. **Predictive Recommendation**: Extract high-value content (>3 rating) watched by the similar user that remains unwatched (`NaN`) by the target user.

### **📁 Files**
📄 [`Cinema_analytics.py`](./Cinema_analytics.py)

### **How to Run**
```bash
python Cinema_analytics.py
```

### **Expected Output**
```
The most controversial movie is  <index_of_movie>
<array_of_scifi_fan_indices>
The user similar to user 1 is  <index_of_similar_user>
The movie recommended to user 1 is movie number <recommended_movie_indices>
```

### **Concepts & Learning Objectives**

#### **1. Sparse Data Handling**
Real datasets are incomplete. Users don't watch all movies, sensors miss readings, etc.
```python
mask = np.random.choice([True, False], size=ratings.shape, p=[0.25, 0.75])
ratings[mask] = np.nan  # 25% missing data
```

#### **2. Working with Missing Values (NaN)**
Use `np.nanmean()`, `np.nanstd()`, `np.nansum()` instead of regular functions.
```python
mean_ratings = np.nanmean(ratings, axis=0)  # Mean per movie, ignoring NaN
```

#### **3. Statistical Analysis - Finding "Controversial" Content**
Higher standard deviation = more divisive content (some love it, some hate it)
```python
stdv = np.nanstd(ratings, axis=0)  # Std dev per movie
index = np.nanargmax(stdv)  # Movie with highest disagreement
```

#### **4. User Segmentation**
Filter users by behavior (e.g., identify Sci-Fi fans by high ratings in Sci-Fi movies)
```python
scifi_fan = np.where(np.nanmean(ratings[:,:10], axis=1) > 4)
```

#### **5. Euclidean Distance for Similarity**
Measures how "close" two users are in preference space.
```python
difference = np.sqrt(np.nansum((np.square((rest_users - user_1))), axis=1))
similar_user = np.nanargmin(difference)
```

#### **6. Collaborative Filtering Recommendation**
Recommend movies liked by similar users but unwatched by target user
```python
recommendation = np.where((similar_user > 3) & (np.isnan(user_1)))
```

### **Challenge Questions**

1. **Data Science**: Why is standard deviation a good measure of controversy? What would you use to measure agreement instead?

2. **Algorithm Design**: The Euclidean Distance treats all genres equally. How would you weight Sci-Fi movies more heavily?

3. **Performance**: With 1 million users and 10,000 movies, how would you optimize the similarity calculation?

4. **Real-World Application**: What happens if a user has only watched 1 movie? Is their similarity score reliable?

5. **Enhancement**: Can you recommend multiple movies instead of just one?

### **Key Insights**

- 🔍 **Why NaN Matters**: Ignoring NaN is crucial; regular `np.mean()` would return NaN
- 📐 **Euclidean Distance**: The most common similarity metric, but alternatives exist (Cosine Similarity, Pearson Correlation)
- 💡 **Cold Start Problem**: New users with few ratings are hard to match—real systems use content-based filtering too
- 🎬 **Real Platforms**: Netflix uses more sophisticated matrix factorization techniques (SVD, gradient descent)

---

## 💰 Project 2: Budget Analysis & Visualization

### **Real-World Context**
Governments allocate billions in budgets. Analysts need to understand budget changes, compare actual vs. planned spending, and visualize allocation trends. This project uses real government budget data.

### **Business Problem**
A government needs to:
- Compare revised budget vs. original budget for different sectors
- Analyze year-over-year growth against inflation targets
- Visualize how much each sector receives
- Identify which sectors are facing real-term funding cuts

### **🎯 Project Objectives**

1. **Budget Variance Analysis**: Calculate the percentage change from original to revised budget
2. **Inflation Adjustment**: Compare YoY growth against official inflation targets
3. **Visualization**: Create multiple chart types to show trends
4. **Impact Analysis**: Identify sectors receiving less funding than inflation

### **📁 Files**
📄 [`budgepk_26-27/analysis.py`](./budgepk_26-27/analysis.py)
📄 [`budgepk_26-27/social_sectors1.csv`](./budgepk_26-27/social_sectors1.csv)

### **How to Run**
```bash
cd budgepk_26-27
python analysis.py
```

**Note**: The script displays charts sequentially. Close each chart window to see the next one.

### **Expected Output**
Three visualizations will appear:
1. **Budget Variance Chart**: Horizontal bar chart showing percentage changes
2. **YoY Growth vs. Inflation**: Compares growth against 8.2% inflation target
3. **Macro Budget Allocation**: Shows spending on interest payments, defense, and social services

### **Concepts & Learning Objectives**

#### **1. Pandas Data Loading & Manipulation**
```python
data = pd.read_csv("social_sectors1.csv")
revised_budget = data['revised_2025_26']
```

#### **2. Financial Calculations**
```python
variance = ((revised_budget - budget_25) / budget_25) * 100
yoy_growth = ((budget_26 - revised_budget) / revised_budget) * 100
```

#### **3. Data Visualization with Matplotlib**
- **Bar Charts**: Compare categories
- **Horizontal Charts**: Good for many categories
- **Reference Lines**: Show inflation targets
- **Color Coding**: Green for growth above inflation, red for cuts

#### **4. Conditional Formatting**
```python
colors = ['g' if x >= inflation_target else 'coral' for x in plot_growth]
```

### **Challenge Questions**

1. **Analysis**: Which sector is facing the biggest real-term cut compared to inflation?

2. **Visualization**: How would you add error bars or confidence intervals to the charts?

3. **Enhancement**: Create a pie chart showing the proportion of total budget for each sector

4. **Prediction**: Using past year data, forecast next year's allocations

5. **Comparison**: Compare budgets across multiple years—which trends do you see?

### **Key Insights**

- 📊 **Nominal vs. Real Growth**: Nominal growth above inflation = real increase in purchasing power
- 💡 **Budget Trade-offs**: If defense gets more, social sectors get less
- 📈 **Visualization Power**: Charts communicate data faster than numbers
- 🎯 **Policy Impact**: Even 1% budget cut in a large sector affects millions

---

## 📖 Key Concepts Explained

### **NumPy - Numerical Computing**
Fast array operations on large datasets
```python
import numpy as np
ratings = np.random.randint(1, 5, (100, 20))  # 100x20 matrix
```

### **Pandas - Data Analysis**
Structured data with CSV/Excel support
```python
import pandas as pd
data = pd.read_csv("file.csv")
```

### **Matplotlib - Visualization**
Create professional charts and plots
```python
import matplotlib.pyplot as plt
plt.barh(labels, values)
plt.show()
```

### **Euclidean Distance**
Geometric distance between two points: `√((x₁-x₂)² + (y₁-y₂)²)`

### **Standard Deviation**
Measure of how spread out data is from the mean

### **Variance**
Percentage change: `((new - old) / old) * 100`

---

## ✅ Tips for Success

1. **Read the Data First**: Use `print(data.head())` to understand your dataset
2. **Handle Missing Values**: Always check for NaN values before calculations
3. **Document Calculations**: Comment your formulas so you remember them later
4. **Visualize Early**: Create charts to spot patterns before deep analysis
5. **Test with Small Data**: Debug algorithms on small datasets first
6. **Compare Results**: Always sanity-check your numbers against raw data

---

## 🎓 Common Medium-Level Mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting NaN handling | Use `np.nanmean()` not `np.mean()` |
| Wrong axis parameter | `axis=0` for column operations, `axis=1` for row operations |
| Shape mismatch | Check array/dataframe shapes with `.shape` |
| Not importing libraries | Always `import numpy`, `import pandas`, `import matplotlib.pyplot` |
| Off-by-one in slicing | Remember Python slicing is `[start:end)` (end is exclusive) |
| Modifying original data | Use `.copy()` if you want to preserve original |

---

## 📚 Resources

- **NumPy Documentation**: https://numpy.org/doc/
  - Useful: `nanmean()`, `nansum()`, `sqrt()`, `argmax()`, `where()`
- **Pandas Documentation**: https://pandas.pydata.org/docs/
  - Useful: `read_csv()`, `iloc[]`, `loc[]`, filtering
- **Matplotlib Guide**: https://matplotlib.org/stable/users/index.html
  - Useful: `bar()`, `barh()`, `plot()`, `show()`
- **Statistics Concepts**: Khan Academy (https://www.khanacademy.org/)

---

## 🏆 When to Move to Advance Level

You're ready for Advance level when you:
- ✅ Can handle missing data confidently
- ✅ Understand statistical concepts (mean, std, variance)
- ✅ Can create multiple visualizations
- ✅ Can implement algorithms from pseudocode
- ✅ Can optimize code for performance
- ✅ Can debug complex data issues

---

## 💡 Next Steps

1. ✅ Complete both projects
2. 🔄 Modify projects: Add new metrics, new visualizations, new datasets
3. 📊 Use different datasets: Find CSV files online and practice analysis
4. 🚀 Move to **[Advance Level](../Advance/README.md)** when ready

---

## 🤝 Contributing

Found a better algorithm? Optimized the visualization? Have a new project?
1. Fork the repository
2. Make your improvements
3. Submit a pull request with clear documentation

Happy Analyzing! 📈🎉
