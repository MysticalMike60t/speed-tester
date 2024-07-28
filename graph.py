import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_data(filename='network_speeds.csv'):
    timestamps, download_speeds, upload_speeds, pings = [], [], [], []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestamps.append(datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S.%fZ'))
            download_speeds.append(float(row[1]) / 1e6)  # Convert to Mbps
            upload_speeds.append(float(row[2]) / 1e6)    # Convert to Mbps
            pings.append(float(row[3]))
    return timestamps, download_speeds, upload_speeds, pings

def plot_data(timestamps, download_speeds, upload_speeds, pings):
    plt.figure(figsize=(10, 6))
    
    # Plot download and upload speeds
    plt.plot(timestamps, download_speeds, label='Download Speed (Mbps)', color='blue')
    plt.plot(timestamps, upload_speeds, label='Upload Speed (Mbps)', color='green')
    
    # Process ping values
    processed_pings = []
    for i, ping in enumerate(pings):
        if ping > 150:
            processed_pings.append(150)
            plt.annotate(
                '>',
                xy=(timestamps[i], 150),
                xytext=(timestamps[i], 150 + 5),
                ha='center',
                color='red'
            )
        else:
            processed_pings.append(ping)
    
    # Plot ping values as a line
    plt.plot(timestamps, processed_pings, label='Ping (ms)', color='red', linestyle='dashed')

    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.title('Network Speeds Over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    timestamps, download_speeds, upload_speeds, pings = read_data()
    plot_data(timestamps, download_speeds, upload_speeds, pings)
