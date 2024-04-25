import pandas as pd
import subprocess
import sys
from datetime import datetime
import os

def check_waf(url):
    try:
        result = subprocess.run(['wafw00f', url], capture_output=True, text=True)
        if "No WAF detected" in result.stdout:
            return "No"
        elif "is behind" in result.stdout:
            return "Yes"
        else:
            return "Error"
    except Exception as e:
        return "Error"

def process_urls(csv_path, output_dir):
    # Load the CSV file
    data = pd.read_csv(csv_path)
    if 'WAF' not in data.columns:
        data['WAF'] = None  # Add a WAF column if it doesn't exist

    # Check each URL for WAF
    for index, row in data.iterrows():
        print(f"Checking URL: {row['URL']}")
        waf_status = check_waf(row['URL'])
        data.at[index, 'WAF'] = waf_status

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the updated CSV with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(output_dir, f'verified_waf_list_{timestamp}.csv')
    data.to_csv(output_file, index=False)
    print(f"Updated CSV file saved to {output_file}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.waf_checker <path_to_csv>")
        sys.exit(1)
    
    csv_file_path = sys.argv[1]
    output_directory = 'data/waf_verified'
    process_urls(csv_file_path, output_directory)
