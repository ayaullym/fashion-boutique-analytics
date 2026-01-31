def clean_return_reason(df):
    df["return_reason"] = df["return_reason"].fillna("Not Returned")
    df.loc[df["is_returned"], "return_reason"] = (
        df.loc[df["is_returned"], "return_reason"].replace("Not Returned", "Unknown")
    )
    return df

def fill_missing_size(df):
    df["size"] = df["size"].fillna("Unknown")
    return df
