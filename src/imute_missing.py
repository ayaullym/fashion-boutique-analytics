from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

def impute_customer_rating(df):
    target = "customer_rating"
    train = df[df[target].notna()]
    missing = df[df[target].isna()]

    X_train = train.drop(columns=[target])
    y_train = train[target]
    X_missing = missing.drop(columns=[target])

    preprocess = ColumnTransformer([
        ("num", "passthrough", X_train.select_dtypes(include=["int64", "float64"]).columns),
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         X_train.select_dtypes(include=["object", "bool"]).columns)
    ])

    model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)

    pipe = Pipeline([
        ("preprocess", preprocess),
        ("model", model)
    ])

    pipe.fit(X_train, y_train)
    df.loc[df[target].isna(), target] = pipe.predict(X_missing)

    df[target] = df[target].clip(1, 5).round(1)
    return df
