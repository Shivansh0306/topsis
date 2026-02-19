import sys
import pandas as pd
import numpy as np
import os

def topsis(inputFileName, weights, impacts, resultFileName):
    try:
        # Check if file exists
        if not os.path.exists(inputFileName):
            print("Error: File not found.")
            return

        # Read the input file
        try:
            df = pd.read_csv(inputFileName)
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        # Check if contain three or more columns
        if len(df.columns) < 3:
            print("Error: Input file must contain three or more columns.")
            return

        # Check for non-numeric values (from 2nd to last columns)
        try:
            df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric)
        except ValueError:
            print("Error: From 2nd to last columns must contain numeric values only.")
            return

        # Validation of weights and impacts
        weights = [float(w) for w in weights.split(',')]
        impacts = impacts.split(',')

        # Check if number of weights, impacts and columns are same
        if len(weights) != len(impacts) or len(weights) != len(df.columns) - 1:
            print("Error: Number of weights, impacts and columns must be same.")
            return

        # Check if impacts are + or -
        if not all(i in ['+', '-'] for i in impacts):
            print("Error: Impacts must be either + or -.")
            return

        # Topsis Implementation
        # 1. Vector Normalization
        # Creating a copy for calculations
        dataset = df.iloc[:, 1:].values
        dataset = dataset.astype(float) # Ensure float type for calculations
        rows, cols = dataset.shape

        normalized_matrix = dataset / np.sqrt((dataset**2).sum(axis=0))

        # 2. Weighted Normalization
        weighted_matrix = normalized_matrix * weights

        # 3. Ideal Best and Ideal Worst
        ideal_best = []
        ideal_worst = []

        for i in range(cols):
            if impacts[i] == '+':
                ideal_best.append(max(weighted_matrix[:, i]))
                ideal_worst.append(min(weighted_matrix[:, i]))
            else:
                ideal_best.append(min(weighted_matrix[:, i]))
                ideal_worst.append(max(weighted_matrix[:, i]))

        # 4. Euclidean Distance
        S_plus = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
        S_minus = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))

        # 5. Performance Score
        # Avoid division by zero
        score = S_minus / (S_plus + S_minus)

        # 6. Rank
        df['Topsis Score'] = score
        df['Rank'] = df['Topsis Score'].rank(ascending=False, method='max')

        # Formatting Output
        df.to_csv(resultFileName, index=False)
        print(f"Success: Result saved to {resultFileName}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        print('Example: python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv')
    else:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == "__main__":
    main()
