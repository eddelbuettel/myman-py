import csv
import os
from datetime import datetime
from typing import List, Dict, Optional
from importlib import resources

def load_data(verbose: Option[bool] = False) -> List[Dict]:
    """
    Loads the raw 'myman.csv' data using Python's built-in csv module.

    Returns:
        A list of dictionaries, where each dictionary represents a row.
    """
    records: List[Dict] = []
    full_path = resources.files("myman").joinpath("data/myman.csv")
    if verbose:
        print(f"Loading data from: {os.path.abspath(full_path)}")
    
    try:
        with open(full_path, mode='r', newline='', encoding='utf-8') as file:
            # Use DictReader to automatically handle headers
            reader = csv.DictReader(file)
            
            for row in reader:
                # Structure the record for consistency
                record = {
                    'quote': row.get('post', '').strip(),
                    'target': row.get('man', '').strip(),
                    #'date_str': row.get('created', '').strip()
                    # Date handling: Keep date as string initially for consistency, 
                    # but attempt to normalize the format if possible.
                    'date_obj': row.get('created', '').strip()
                }
                records.append(record)
        
        if verbose:
            print(f"Successfully loaded {len(records)} records.")
        return records
        
    except FileNotFoundError:
        print(f"Error: The data file '{csv_file_path}' was not found.")
        return []

if __name__ == "__main__":
    # Example usage when running this script directly
    data = load_data()
    if data:
        print("Data successfully loaded (first record sample):")
        print(data[0])
