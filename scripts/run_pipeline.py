"""
Master ETL Pipeline
Runs all ETL scripts and stops if any script fails.
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent

scripts = [
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_performance.py",
    "load_to_sqlite.py"
]

for script in scripts:
    script_path = BASE_DIR / script

    print(f"\n{'='*50}")
    print(f"Running {script}...")
    print(f"{'='*50}")

    result = subprocess.run(
        [sys.executable, str(script_path)]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script} failed!")
        sys.exit(1)

    print(f"{script} completed successfully.")

print("\nPipeline completed successfully.")