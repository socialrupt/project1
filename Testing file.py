import pandas as pd

df = pd.read_csv("members0.csv")
Line_Target = len(df) // 3
print(Line_Target)
