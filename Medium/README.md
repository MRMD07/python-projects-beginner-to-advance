# Medium Difficulty Problems

This directory contains real-world problems solved using Python. These challenges follow a **systemic approach** to ensure deep understanding.

## Our Approach
We utilize the **Program Development Life Cycle (PDLC)** for every solution.

### How to use this repository:
1. **Attempt:** Read the problem and try to solve it independently.
2. **Compare:** Read the provided solution and compare it with yours.
   - *Hint:* If you're stuck feel free to check the source code
3. **Contribute:** If your code is more efficient, send a **pull request** I’d love to review it

# Problem 1 Cinema Analytics & Collaborative Filtering Engine
First we break it down it into requirements so we know what to expect
## 🎯 Project Objectives & Requirements

1. **Simulate Sparse Real-World Data**: Generate a $100 \times 20$ user-movie matrix (ratings 1–5) and randomly inject `np.nan` values into 25% of the data to simulate unwatched movies.
2. **Statistical Analysis**: Calculate global movie statistics (mean and standard deviation) while ignoring missing values to identify the most "controversial" film.
3. **Targeted Behavioral Profiling**: Filter and isolate specific user demographics (e.g., "Sci-Fi Fans") based on multi-dimensional slicing criteria.
4. **User Similarity Modeling**: Implement the geometric **Euclidean Distance Formula** to find the user most architecturally similar to a target user profile.
5. **Predictive Recommendation**: Extract high-value content ($>3$ rating) watched by the similar user that remains unwatched (`NaN`) by the target user.
