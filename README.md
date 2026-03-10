# Lab 3: Data Quality & Anomaly Detection

## 📌 Objective
In the real world, edge sensors suffer from electromagnetic interference or sudden "flash crashes". If we allow this corrupted data to enter our pipeline, downstream AI models will produce garbage predictions.

This lab demonstrates **Robust Statistics**. You will implement a Sliding Window and use the **Modified Z-Score** to detect and reject point anomalies in real-time, matching the architecture discussed in Lecture 3.

## 🛠️ Environment Setup
1. Launch your **GitHub Codespaces** from this repository.
2. Open the `lab3_anomaly_detection.py` file.

## 🚀 Instructions
1. We use `collections.deque(maxlen=WINDOW_SIZE)` to create an $\mathcal{O}(W)$ sliding window.
2. Locate `TODO 1` to `TODO 5` inside `process_with_mad_filter()`.
3. Implement the exact math from the lecture:
    * Calculate the Median of the window.
    * Calculate the MAD.
    * Calculate the Modified Z-Score: $M = 0.6745 \times (x - \text{median}) / \text{MAD}$
    * If $|M| > 3.5$, **reject the point** (do not add it to the window).
    * If $|M| \le 3.5$, **accept the point** (add it to the window and write to CSV).
4. Run the script:

    ```bash
    python lab3_anomaly_detection.py
    ```

## 🧠 Reflection Questions
1. **The Breakdown Point**: Why is MAD mathematically superior to the Standard Deviation ($\sigma$) for this specific task? What would happen to the threshold if a massive spike entered a standard Z-score calculation?
2. **Safe Appends**: Why is it critical that we only `window.append(value)` *after* we have verified it is not an anomaly? 

## ✅ Submission Guidelines
1. Ensure your filter successfully blocks anomalies.
2. Commit and push your changes to GitHub.
