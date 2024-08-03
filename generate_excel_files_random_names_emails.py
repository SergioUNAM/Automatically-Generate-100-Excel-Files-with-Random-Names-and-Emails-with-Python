# Automatically Generate 100 Excel Files with Random Names and Emails with Python

from faker import Faker
import pandas as pd
import random
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_fake_data(num_entries):
    """
    Generates a dictionary with fake names, emails and ages.

    Parameters:
        num_entries(int): Number of fake data entries to generate.

    Returns:
        dict: A dictionary with keys: 'name', 'email' and 'age' and corresponding lists of fake data.
    """
    fake = Faker()
    data = {
        "name": [fake.name() for _ in range(num_entries)],
        "email": [fake.email() for _ in range(num_entries)],
        "age": [fake.random_int(min=18, max=80) for _ in range(num_entries)]
    }
    return data

def save_to_excel(data, filename):
    """
    Saves the data to an Excel file.

    Parameters:
        data (dict): The data to save.
        filename (str): The name of the Excel file.
    """
    df = pd.DataFrame(data)
    try:
        df.to_excel(filename, index=False)
        logging.info(f"Data successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Failed to save data to {filename}: {e}")

def main():
    # Generate fake data and save to 100 Excel files
    for i in range(1, 101):
        num_entries = random.randint(1, 100)
        data = generate_fake_data(num_entries)
        
        # Añadir una marca de tiempo al nombre del archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'fake_data_{i}_{timestamp}.xlsx'
        
        save_to_excel(data, filename)

if __name__ == "__main__":
    main()
