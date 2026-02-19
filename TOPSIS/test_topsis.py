import os
import subprocess
import pandas as pd

def run_test(description, cmd, expected_output_contains=None, expected_file=None):
    print(f"Running Test: {description}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    
    if expected_output_contains:
        if expected_output_contains in output:
            print("  PASSED: Output contains expected string.")
        else:
            print(f"  FAILED: Output does not contain '{expected_output_contains}'.")
            print(f"  Start Output:\n{output}\nEnd Output")
            
    if expected_file:
        if os.path.exists(expected_file):
            print(f"  PASSED: File '{expected_file}' created.")
            # Verify its content (basic check)
            try:
                df = pd.read_csv(expected_file)
                if 'Topsis Score' in df.columns and 'Rank' in df.columns:
                     print("  PASSED: File contains 'Topsis Score' and 'Rank' columns.")
                else:
                     print("  FAILED: File missing required columns.")
            except Exception as e:
                print(f"  FAILED: Could not read created file: {e}")
        else:
            print(f"  FAILED: File '{expected_file}' not created.")
    print("-" * 20)

def main():
    # Test 1: Successful execution
    # Weights: 1,1,1,1,1
    # Impacts: +,+,+,+,+
    run_test(
        "Successful Execution",
        'python topsis.py data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv',
        expected_output_contains="Success: Result saved to result.csv",
        expected_file="result.csv"
    )

    # Test 2: Incorrect number of parameters
    run_test(
        "Incorrect Parameters",
        'python topsis.py data.csv "1,1,1,1,1"',
        expected_output_contains="Usage: python <program.py>"
    )

    # Test 3: File not found
    run_test(
        "File Not Found",
        'python topsis.py non_existent.csv "1,1" "+,+" result.csv',
        expected_output_contains="Error: File not found."
    )

    # Test 4: Mismatched weights/impacts/columns
    # Data has 5 numeric columns, passing 4 weights
    run_test(
        "Mismatched Dimensions",
        'python topsis.py data.csv "1,1,1,1" "+,+,+,+" result.csv',
        expected_output_contains="Error: Number of weights, impacts and columns must be same."
    )

    # Test 5: Invalid impacts
    run_test(
        "Invalid Impacts",
        'python topsis.py data.csv "1,1,1,1,1" "+,+,?,+,+" result.csv',
        expected_output_contains="Error: Impacts must be either + or -."
    )
    
    # Test 6: Verify Ranking Logic (basic check)
    # create a small known file
    with open("test_small.csv", "w") as f:
        f.write("ID,C1,C2\nA,10,10\nB,5,5\nC,1,1\n")
    
    # Run topsis on it. Weights 1,1 Impacts +,+ 
    # A should be rank 1 (best), C rank 3 (worst)
    run_test(
        "Small File Ranking Check",
        'python topsis.py test_small.csv "1,1" "+,+" result_small.csv',
        expected_file="result_small.csv"
    )
    
    if os.path.exists("result_small.csv"):
        df = pd.read_csv("result_small.csv")
        # Check A is rank 1
        rank_a = df.loc[df['ID']=='A', 'Rank'].values[0]
        if rank_a == 1:
             print("  PASSED: Logic check (A is Rank 1).")
        else:
             print(f"  FAILED: Logic check (A should be Rank 1, got {rank_a}).")
             print(df)

if __name__ == "__main__":
    main()
