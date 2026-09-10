import random
import re
from typing import List, Dict, Optional
# Import the loading function from the local module
from .load_data import load_data

# class MyMan:
#     def __init__(self, quote, target, date):
#         self.quote = quote
#         self.target = target
#         self.date = date

#     # Overriding the __str__ method
#     def __str__(self):
#         return f"'{self.quote}' -- directed at {self.target} on {self.date}"

def is_string_an_int(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False

def format_myman_output(record: Dict) -> str:
    """
    Formats the sampled record dictionary into the final display string format.
    Format: My man [quote].\t -- about [target] on [date]
    """
    quote = record['quote']
    target = record['target']
    date_obj = record['date_obj']

    # Date normalization for clean output
    date_output = date_obj
    if isinstance(date_obj, str):
        # Clean up the date string for display consistency
        date_output = date_obj.split(' ')[0]

    return f"{quote}.\n\t -- about {target} on {date_output}\n"
    
def myman(ind: Optional[str] = None,
          target: Optional[str] = None,
          verbose: Optional[bool] = False) -> str:
    """
    Randomly samples a single post (skeet) from the loaded dataset,
    optionally filtering by a target keyword.

    Args:
        int: Optional index, or regex pattern string to match 'post' field
        target: Optional regex pattern string to filter records by the 'target' field.

    Returns:
        A dictionary representing the sampled record, or None if no records are found.
    """
    # 1. Load all data first
    data = load_data(verbose=verbose)
    if not data:
        return None

    records_to_sample = data
    
    # 2. Filter if a target is specified
    if target:
        if (verbose):
            print(f"Filtering records by target regex: {target}")
        filtered_records: List[Dict] = []
        for record in data:
            # Use regex search to check if the target keyword exists
            if record['target'] and record['target'].strip():
                try:
                    # Use re.search for robust regex matching
                    if re.search(target, record['target'], re.IGNORECASE):
                        filtered_records.append(record)
                except re.error as e:
                    print(f"Error in regex pattern '{target}': {e}")
                    return None

        if not filtered_records:
            if (verbose):
                print("No records found matching the target.")
            return ""

        records_to_sample = filtered_records

    # 3.1 Index by position or match
    if ind:
        if (verbose):
            print(f"Indexing records by '{ind}'")
        matched_records: List[Dict] = []

        if is_string_an_int(ind):
            i = int(ind) - 1
            matched_records = records_to_sample[i]
        else:
            for record in records_to_sample:
                # Use regex search to check if the 'ind' pattern matches
                if record['quote'] and record['quote'].strip():
                    try:
                        # Use re.search for robust regex matching
                        if re.search(ind, record['quote'], re.IGNORECASE):
                            matched_records.append(record)
                    except re.error as e:
                        print(f"Error in regex pattern '{ind}': {e}")
                        return None

            if not matched_records:
                if (verbose):
                    print("No records found matching the pattern.")
                return ""
            else:
                # sample down to one
                matched_records = random.choice(matched_records)

        records_to_sample = matched_records

    # 3.2 Or sample the record
    else:
        records_to_sample = random.choice(records_to_sample)
        if (verbose):
            print("Successfully sampled a record.")

    if not records_to_sample:
        if (verbose):
            print("No records found matching the criteria.")
        return ""

    return format_myman_output(records_to_sample)

# Example usage when running this script directly
if __name__ == "__main__":
    # Test 1: Sample a random record
    print("\n--- Testing random sample (no target) ---")
    sample_no_target = myman()
    if sample_no_target:
        print("Sampled Record:", sample_no_target)
    
    # Test 2: Sample by a specific target (e.g., 'crypto')
    print("\n--- Testing targeted sample (target=crypto) ---")
    sample_target = myman(target="crypto")
    if sample_target:
        print("Sampled Record:", sample_target)
