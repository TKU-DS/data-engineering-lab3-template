import time
import random
import csv
import os
import statistics
from collections import deque

# ==========================================
# Data Engineering - Lab 3: Anomaly Detection & Edge Robustness
# ==========================================
# Objective: Protect the data pipeline from impulse noise (point anomalies)
# using Robust Statistics (Sliding Window + Median Absolute Deviation).

RAW_DATA_FILE = "raw_noisy_data.csv"
CLEAN_DATA_FILE = "clean_filtered_data.csv"
TOTAL_SAMPLES = 500
WINDOW_SIZE = 10  # We keep the last 10 samples in memory
MAD_THRESHOLD = 3.0 # Reject points that are 3 MADs away from the median

def unstable_sensor_stream(num_samples):
    """
    Simulates a sensor that normally outputs values around 25.0,
    but occasionally suffers from massive electronic interference (Flash Crashes/Spikes).
    """
    for i in range(num_samples):
        # 10% chance of a massive anomaly
        if random.random() < 0.10:
            yield random.choice([0.0, 100.0]) # Impulse noise
        else:
            yield 25.0 + random.uniform(-1.0, 1.0) # Normal reading

def process_without_filter():
    """[Poor Architecture] Saves everything directly to disk. (GIGO)"""
    print(f"\n[*] Processing {TOTAL_SAMPLES} samples WITHOUT filtering...")
    sensor = unstable_sensor_stream(TOTAL_SAMPLES)
    
    anomalies_recorded = 0
    with open(RAW_DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for value in sensor:
            writer.writerow([value])
            if value > 50.0 or value < 10.0:
                anomalies_recorded += 1
                
    print(f"    -> Warning: {anomalies_recorded} anomalies written to database!")


def process_with_mad_filter():
    """
    [Good Architecture] Uses a sliding window and Robust Statistics (MAD)
    to reject anomalies in real-time before they reach the database.
    """
    print(f"\n[*] Processing {TOTAL_SAMPLES} samples WITH MAD Filter...")
    sensor = unstable_sensor_stream(TOTAL_SAMPLES)
    
    # deque with maxlen acts as an automatic sliding window O(W) memory
    window = deque(maxlen=WINDOW_SIZE)
    anomalies_rejected = 0
    
    with open(CLEAN_DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        for value in sensor:
            # If the window isn't full yet, just add the value and write it
            if len(window) < WINDOW_SIZE:
                window.append(value)
                writer.writerow([value])
                continue
                
            # TODO 1: Calculate the 'current_median' of the values in the 'window'
            # Hint: Use statistics.median()
            
            
            # TODO 2: Calculate the Absolute Deviations for each item in the window
            # deviations = [abs(x - current_median) for x in window]
            
            
            # TODO 3: Calculate the Median Absolute Deviation (MAD)
            # Hint: It's the median of the 'deviations' list. Add 0.001 to avoid division by zero later.
            # mad = ... + 0.001
            
            
            # TODO 4: Calculate the deviation of the new 'value' from the 'current_median'
            # diff = abs(value - current_median)
            
            
            # TODO 5: Reject or Accept the value based on the MAD_THRESHOLD
            # if (diff / mad) > MAD_THRESHOLD:
            #     anomalies_rejected += 1
            #     # Do not append to window, do not write to file (Reject)
            # else:
            #     # Append to window, write to file (Accept)
            
            pass # Remove this pass when you implement the logic
            
    print(f"    -> Success: {anomalies_rejected} anomalies successfully blocked!")

if __name__ == "__main__":
    print("=== Edge Pipeline: Robustness & Anomaly Detection ===")
    
    process_without_filter()
    process_with_mad_filter()
    
    print("\n===========================================")
    print("Experiment completed. Please check the difference between the two CSV files.")
