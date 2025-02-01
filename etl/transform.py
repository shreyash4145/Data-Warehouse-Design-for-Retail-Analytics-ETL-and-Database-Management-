import pandas as pd

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transform data: Clean, filter, and aggregate.
    """
    #Remove null values
    data = data.dropna()

   #Convert date column to datetime
    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"])

    #Aggregate sales by product
    transformed_data = data.groupby("product_id").agg({"sales": "sum"}).reset_index()

    return transformed_data

if __name__ == "__main__":
    from extract import extract_data
    data = extract_data("path/to/data.csv")
    transformed_data = transform_data(data)
    print(transformed_data.head())