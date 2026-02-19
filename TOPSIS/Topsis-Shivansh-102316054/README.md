# Topsis-Shivansh-102316054

A Python package to implement Topsis (Technique for Order of Preference by Similarity to Ideal Solution).

## Installation

```bash
pip install Topsis-Shivansh-102316054
```

## Usage

Run the package from the command line:

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example

```bash
topsis data.csv "1,1,1,1,1" "+,+,+,+,+" result.csv
```

### Parameters

1.  **InputDataFile**: Input CSV file containing the data. structure:
    -   First column: Object/Alternative name (e.g., M1, M2, M3).
    -   Rest columns: Numeric criteria values.
2.  **Weights**: Comma-separated weights for each criterion (e.g., "0.25,0.25,0.25,0.25").
3.  **Impacts**: Comma-separated impacts ('+' for maximize, '-' for minimize) (e.g., "+,+,-,+").
4.  **OutputResultFileName**: Name of the output CSV file to save results.

## License

MIT
