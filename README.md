# Lab 2: Data Acquisition & Downsampling

## 📌 Objective
In Edge AI, sensors (like vibration monitors or microphones) often generate high-frequency data (e.g., 1000+ readings per second). Saving all this raw data to disk will quickly exhaust the device's storage and bandwidth.

This lab demonstrates **Downsampling**. You will implement a Chunk Averaging filter to compress the data stream on-the-fly, retaining the core signal features while discarding high-frequency noise and reducing the storage footprint by 99%.

## 🛠️ Environment Setup
1. Launch your **GitHub Codespaces** from this repository.
2. Open the `lab2_data_acquisition.py` file.

## 🚀 Instructions
1. Review the `high_frequency_sensor_stream()` function. Notice the use of the `yield` keyword. This makes it a **Generator**, allowing us to process infinite streams without running out of RAM.
2. Locate the `TODO 1` to `TODO 4` markers inside the `process_and_downsample_stream()` function.
3. Implement the logic to collect samples into a buffer, average them when the buffer is full, write the result, and clear the buffer.
4. Run the script in the terminal:

    ```bash
    python lab2_data_acquisition.py
    ```

5. Compare the output file sizes and processing times printed in the terminal. 

## 🧠 Reflection Questions
1. **The Signal Loss**: By averaging 100 samples into 1, we save 99% of storage. But what kind of physical events might we miss by doing this? (Hint: Think about extremely short, sudden impacts on a machine).
2. **Memory Footprint**: Why did we use `yield` instead of returning a massive Python `list` containing all 100,000 samples at once?

## ✅ Submission Guidelines
1. Ensure your script calculates the averages correctly and runs without errors.
2. Commit your changes:

    ```bash
    git add lab2_data_acquisition.py
    git commit -m "Complete Lab 2 downsampling logic"
    ```

3. Push the code:

    ```bash
    git push origin main
    ```
