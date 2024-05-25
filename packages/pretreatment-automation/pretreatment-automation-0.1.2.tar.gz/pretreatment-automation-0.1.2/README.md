# Pretreatment Automation

Pretreatment Automation is a Python library for automatically preprocessing datasets. It provides functionalities such as removing outliers, handling missing values, and unifying data formats.

## Features

- Remove outliers from your data
- Handle missing values with specified thresholds
- Unify data formats for consistent analysis

## Installation

You can install Pretreatment Automation from PyPI:

```sh
pip install pretreatment-automation

## Usage

### Example Usage

```python
import pandas as pd
from Pretreatment_automation import PretreatmentAutomation

# Load data from a CSV file
file_path = 'sample_data.csv'
processor = PretreatmentAutomation(file_path=file_path)

# Process the data
processed_df = processor.process(outliers=False, missing=True, format=True, missing_threshold=0.2, fill_value=50000)

print(processed_df)
```

### Sample Data

Save the following data into a file named `sample_data.csv`:

```csv
name,age,income,city
Alice,25,50000,New York
Bob,32,60000,Los Angeles
Charlie,22,,Chicago
David,35,55000,New York
Edward,29,70000,San Francisco
```

## License

This project is licensed under the MIT License.