import pandas as pd

df = pd.read_csv(r"C:\Users\pedro.rrocha\Downloads\funcionarios.csv")

df_qualitativas = df[["salario", "lucro"]]


