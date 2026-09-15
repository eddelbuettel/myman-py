from typing import Optional
from .myman import myman

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
