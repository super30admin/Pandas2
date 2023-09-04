import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
  df = employees.loc[employees['name'].str.startswith('M') | (employees['employee_id']%2==0),'salary']=0
  df=employees[['employee_id', 'salary']].rename(columns={'salary': 'bonus'}).sort_values('employee_id')
  return df