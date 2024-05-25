#!/usr/bin/env python3

import subprocess
import sys

COUNT_SCRIPT_COMMAND= './count.py'
TEST_FILE = 'test.txt'


def run_wc(filename, flag):
    """Run the wc command and return its output."""
    result = subprocess.run(['wc', flag, filename], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running wc: {result.stderr}")
        sys.exit(1)
    return result.stdout.split()

def run_custom_count(filename, flag):
    """Run the custom count command and return its output."""
    result = subprocess.run([COUNT_SCRIPT_COMMAND, flag, filename], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running custom count: {result.stderr}")
        sys.exit(1)
    return result.stdout.strip().split()

def main():
    test_file = TEST_FILE
    flags = ['-c', '-l', '-w', '-m']
    all_passed = True

    for flag in flags:
        wc_output = run_wc(test_file, flag)
        custom_output = run_custom_count(test_file, flag)

        if wc_output != custom_output:
            print(f"Test failed for flag {flag}")
            all_passed = False

    if all_passed:
        print("All test cases passed")
    else:
        print("Some tests failed")

if __name__ == '__main__':
    main()
