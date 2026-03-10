# Lab 3: Data Quality & Anomaly Detection

## 📌 Objective
In the real world, edge sensors degrade, suffer from electromagnetic interference, or experience sudden "flash crashes" in their readings. If we allow this corrupted data to enter our pipeline, downstream AI models will produce confident but incorrect predictions (Garbage In, Garbage Out).

This lab demonstrates **Robust Statistics** on streaming data. You will implement a Sliding Window and use the **Median Absolute Deviation (MAD)** algorithm to detect and reject point anomalies in real-time, preventing them from corrupting the edge database.

## 🛠️ Environment Setup
1. Launch your **GitHub Codespaces** from this repository.
2. Open the `lab3_anomaly_detection.py` file.

## 🚀 Instructions
1. Review the `unstable_sensor_stream()` function. Notice it occasionally fires massive outliers (0.0 or 100.0) simulating hardware spikes.
2. We use `collections.deque(maxlen=WINDOW_SIZE)` to create an $\mathcal{O}(W)$ sliding window.
3. Locate `TODO 1` to `TODO 5` inside `process_with_mad_filter()`.
4. Implement the MAD logic:
    * Find the median of the current window.
    * Find the absolute difference of each point from that median.
    * The MAD is the median of those differences.
    * If the incoming `value` is more than $3 \times \text{MAD}$ away from the current median, **reject it** (do not save it, do not add it to the window).
5. Run the script in the terminal:

    ```bash
    python lab3_anomaly_detection.py
    ```

6. Open `raw_noisy_data.csv` and `clean_filtered_data.csv` in your editor to visually verify that the spikes were removed.

## 🧠 Reflection Questions
1. **The Flaw of Averages**: Why didn't we just use the Mean and Standard Deviation (Z-score) to detect anomalies? What happens to the Mean if a massive outlier enters the sliding window?
2. **Pipeline Resilience**: In our code, when we detect an anomaly, we drop it entirely. In a real-world factory monitoring system, is it always safe to just silently drop anomalies? How might you improve this architecture? (e.g., logging the drops).

## ✅ Submission Guidelines
1. Ensure your filter successfully blocks the anomalies without crashing.
2. Commit your changes:

    ```bash
    git add lab3_anomaly_detection.py
    git commit -m "Complete Lab 3 MAD anomaly filter"
    ```

3. Push the code:

    ```bash
    git push origin main
    ```
