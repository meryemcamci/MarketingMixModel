import pandas as pd

def load_marketing_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Basic sanity checks
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date").reset_index(drop=True)
    return df

def make_weekly(df, date_col="date", agg_map=None):
    """Ensure weekly frequency & forward-fill/missing handling."""
    if agg_map is None:
        agg_map = {col: "sum" for col in df.columns if col != date_col}
    df = df.copy()
    df = df.set_index(date_col).resample("W-MON").agg(agg_map).reset_index()
    return df
