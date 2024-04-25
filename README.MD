# WAF Checker Project

## Overview

The WAF Checker Project is a Python-based tool designed to determine if websites are protected by Web Application Firewalls (WAF). It uses Wafw00f to check URLs listed in a CSV file and writes the results to another CSV file in a timestamped format, indicating whether each URL is behind a WAF.

## Directory Structure

```plaintext
waf_checker/
│
├── src/
│   ├── __init__.py         # Makes src a Python package
│   ├── waf_checker.py      # Main Python script for WAF checking
│
├── data/
│   ├── urls.csv            # CSV file containing URLs to check
│   ├── waf_verified/       # Directory where output CSV files are saved
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── launch.sh               # Script to set up environment and run the project
```

## Requirements

- Python 3.6 or newer
- Pip (Python package installer)
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone [repository-url] waf_checker
   cd waf_checker
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Input CSV:**
   - Ensure that `data/urls.csv` is populated with the URLs you wish to check.

## Running the Project

To run the project, execute the `launch.sh` script:

```bash
./launch.sh
```

This script will:
- Activate the Python virtual environment.
- Install any required dependencies.
- Run the `waf_checker.py` script to check URLs from `data/urls.csv`.
- Save the results in `data/waf_verified/` with a timestamp in the filename.

## Output

The results will be output to the `data/waf_verified/` directory. Each output file is named in the format `verified_waf_list_YYYYMMDDHHMMSS.csv`, where `YYYYMMDDHHMMSS` is the timestamp of when the script was run.

## Troubleshooting

- **Virtual Environment Not Creating Properly:** Ensure that you have the `python3-venv` package installed on your system.
- **Script Permissions:** If the `launch.sh` script fails to execute, run `chmod +x launch.sh` to make sure it has executable permissions.
- **Python or Pip Not Found:** Verify that Python and Pip are correctly installed and that Python is added to your system’s PATH.

## Contributing

Contributions to this project are welcome! To contribute, please fork the repository, make your changes, and submit a pull request.

---

Make sure to replace `[repository-url]` with the actual URL of your GitHub repository. This `README.md` file provides clear and concise instructions for setting up and running the project, and it outlines the structure and purpose of the project components, making it easier for new users or contributors to get started.



