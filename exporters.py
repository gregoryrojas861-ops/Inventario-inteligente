import pandas as pd
from io import BytesIO

def dataframe_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Reporte")
    return output.getvalue()

def dataframe_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")
