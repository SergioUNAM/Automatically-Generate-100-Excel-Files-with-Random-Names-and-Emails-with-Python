
# Automatically Generate 100 Excel Files with Random Names and Emails with Python

## Overview
This Python script generates 100 Excel files, each containing randomly generated names, emails, and ages. It uses the `Faker` library to create fake data, and `pandas` to save the data into Excel files. Each file is named uniquely with a timestamp.

## Prerequisites
- Python 3.x
- `faker` library
- `pandas` library

## Installation
To install the required libraries, run:
```bash
pip install faker pandas
```

## Script Description

### Logging Configuration
The script configures logging to provide information about the script’s execution, including successes and errors.

### Function: `generate_fake_data(num_entries)`
This function generates fake data using the Faker library.

**Parameters:**
- `num_entries` (int): Number of fake data entries to generate.

**Returns:**
- `dict`: A dictionary containing lists of fake names, emails, and ages.

### Function: `save_to_excel(data, filename)`
This function saves the generated fake data to an Excel file.

**Parameters:**
- `data` (dict): The data to save.
- `filename` (str): The name of the Excel file.

### Main Function
The `main()` function generates fake data and saves it to 100 Excel files. Each file contains a random number of entries (between 1 and 100). The filenames include a timestamp to ensure uniqueness.

## Usage
To run the script, execute the following command in your terminal:
```bash
python script_name.py
```

## Example Output
The script generates files with names in the following format:
```
fake_data_1_20230803_123456.xlsx
fake_data_2_20230803_123457.xlsx
...
fake_data_100_20230803_124556.xlsx
```

## Error Handling
The script includes error handling to log any issues that occur during the file-saving process.

## Conclusion
This script is a useful tool for generating large amounts of test data quickly and efficiently. It can be easily modified to generate different types of data or to save the data in other formats.
