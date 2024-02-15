import pandas as pd
import json
from datetime import datetime

with open('D:\Carpeta Proyectos\Python\HojaDe\employees.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['age'] = pd.to_numeric(df['age'], errors='coerce')

df['salary'] = df['salary'].str.replace('\$|,', '', regex=True).astype(float)

df['salary'] = df.apply(lambda row: row['salary'] * 1.1 if row['age'] < 30 else row['salary'], axis=1)

if 'project' in df.columns:
    df = df[(df['age'] < 30) & (df['project'] != 'GRONK')]

current_date = datetime.now()
file_name = f"pagos-empleados-{current_date.strftime('%m-%Y')}.xlsx"

df.to_excel(file_name, index=False)

print(f"Archivo '{file_name}' generado exitosamente con los pagos de los empleados.")