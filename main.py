import speedtest
import csv
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def measure_speed():
    logging.info("Measuring Speed...")
    try:
        logging.info("Testing Speed...")
        s = speedtest.Speedtest()
        logging.info("Testing Download Speed...")
        s.download()
        logging.info("Testing Upload Speed...")
        s.upload()
        result = s.results.dict()
        logging.info(f"Results of scan: {result}")
        return result
    except speedtest.ConfigRetrievalError as e:
        logging.error(f"Configuration retrieval error: {e}")
    except speedtest.SpeedtestException as e:
        logging.error(f"Speedtest error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    return None

def save_data(data, filename='network_speeds.csv'):
    logging.info("Saving Data...")
    if data is not None:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            logging.info("Writing data...")
            writer.writerow([data['timestamp'], data['download'], data['upload'], data['ping']])
            logging.info(f"Wrote data: {data['timestamp'], data['download'], data['upload'], data['ping']}")
    else:
        logging.warning("No data to save (possibly no connection)")

if __name__ == "__main__":
    while True:
        sleep_duration = 1
        logging.info("Starting measure speed process...")
        speed_data = measure_speed()
        if speed_data is None:
            logging.error("No internet connection or unable to retrieve data")
            speed_data = {
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'download': 0,
                'upload': 0,
                'ping': 0
            }
        logging.info("Measured Speed")
        logging.info("Starting save data process...")
        save_data(speed_data)
        logging.info("Saved data")
        logging.info(f"Sleeping for {sleep_duration} seconds...")
        logging.info("------------------------------")
        time.sleep(sleep_duration)
        logging.info("Starting New Scan...")
