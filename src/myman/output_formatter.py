from typing import Optional, Dict
import random
import re
from .myman import myman

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
        
    return f"My man {quote}.\t -- about {target} on {date_output}"

def run_myman(ind: Optional[str] = None, target: Optional[str] = None) -> str:
    """
    High-level function to execute the full cycle: sample data -> format output.
    """
    # Get the sampled record
    from .myman import myman # Local import for circular dependency protection
    sampled_record = myman(ind=ind, target=target)
    
    if sampled_record:
        # Format and return the final string
        return format_myman_output(sampled_record)
    else:
        return "Could not generate content: Sample failed or data is unavailable."

if __name__ == "__main__":
    # Example usage: generate and print a sample
    print("="*50)
    print("--- Running Python 'myman' Generator ---")
    print("="*50)
    
    # Test 1: General sample
    final_output = run_myman(target=None)
    print(final_output)
    
    # Test 2: Targeted sample (e.g., 'crypto')
    print("\n" + "="*50)
    final_output_crypto = run_myman(target="crypto")
    print(final_output_crypto)
    print("="*50)
