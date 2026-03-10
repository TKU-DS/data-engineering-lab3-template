import time
import random
import csv
import os

# ==========================================
# Data Engineering - Lab 2: Data Acquisition & Downsampling
# ==========================================
# Objective: Handle high-frequency data streams without overwhelming memory or I/O.
# Task: Implement a chunk-averaging downsampler to reduce data volume by 99%.

RAW_DATA_FILE = "raw_sensor_data.csv"
PROCESSED_DATA_FILE = "downsampled_data.csv"
TOTAL_SAMPLES = 100000  # Simulate 100,000 high-frequency sensor readings
DOWNSAMPLE_RATE = 100   # Compress every 100 samples into 1

def high_frequency_sensor_stream(num_samples):
    """
    Simulates an Edge sensor (e.g., 1000 Hz vibration sensor).
    Uses 'yield' to act as a Generator, keeping memory footprint at O(1).
    """
    for _ in range(num_samples):
        # Simulate a baseline signal of 5.0 with high-frequency random noise
        reading = 5.0 + random.uniform(-2.0, 2.0)
        yield reading

def process_raw_stream():
    """Reads the stream and writes everything directly to disk (Heavy I/O)."""
    print(f"[*] Processing {TOTAL_SAMPLES} RAW samples...")
    sensor = high_frequency_sensor_stream(TOTAL_SAMPLES)
    
    with open(RAW_DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for value in sensor:
            writer.writerow([value])
            
    raw_size = os.path.getsize(RAW_DATA_FILE) / 1024
    print(f"    -> Raw Data File Size: {raw_size:.2f} KB")


def process_and_downsample_stream():
    """
    Reads the stream, applies chunk-averaging, and writes the reduced data.
    """
    print(f"\n[*] Processing and DOWNSAMPLING (Rate: {DOWNSAMPLE_RATE}:1)...")
    sensor = high_frequency_sensor_stream(TOTAL_SAMPLES)
    
    with open(PROCESSED_DATA_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        buffer = []
        # TODO 1: Iterate through the 'sensor' generator
        for value in sensor:
            
            # TODO 2: Append the 'value' to the 'buffer'
            buffer.append(value)
            
            # TODO 3: Check if the buffer length has reached the DOWNSAMPLE_RATE
            if len(buffer) == DOWNSAMPLE_RATE:
                
                # TODO 4: Calculate the average of the buffer
                average_val = sum(buffer) / len(buffer)
                
                # Write the averaged value to disk and clear the buffer
                writer.writerow([average_val])
                buffer.clear()
                
    processed_size = os.path.getsize(PROCESSED_DATA_FILE) / 1024
    print(f"    -> Downsampled File Size: {processed_size:.2f} KB")


if __name__ == "__main__":
    print("=== Edge Pipeline: Data Acquisition & Filtering ===")
    
    start_time = time.time()
    process_raw_stream()
    raw_duration = time.time() - start_time
    print(f"    -> Raw Processing Time: {raw_duration:.4f} sec")
    
    start_time = time.time()
    process_and_downsample_stream()
    downsample_duration = time.time() - start_time
    print(f"    -> Downsample Processing Time: {downsample_duration:.4f} sec")
    
    print("\n===========================================")
    print("Experiment completed! Observe the massive reduction in file size.")
