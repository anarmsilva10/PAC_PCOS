import pandas as pd

def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    # Drop unnecessary columns
    df.drop(columns=["Sl. No","Patient File No.","Unnamed: 44"], inplace=True)

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill missing numeric values with median
    df.fillna(df.median(numeric_only=True), inplace=True)

    return df
