import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.
    """
    return pd.read_csv(file_path)

# Example usage
if __name__ == "__main__":
    data = extract_data("data/raw/sales_data.csv")
    print(data.head())