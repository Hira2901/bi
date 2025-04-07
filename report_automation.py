import pandas as pd
from sqlalchemy import create_engine
from openpyxl import Workbook

# Connect to database
engine = create_engine('sqlite:///sales.db')  # Example DB
df = pd.read_sql('SELECT * FROM sales_data', engine)

# Clean and summarize data
df['Date'] = pd.to_datetime(df['Date'])
summary = df.groupby(df['Date'].dt.week)['Revenue'].sum()

# Export to Excel
with pd.ExcelWriter('weekly_report.xlsx', engine='openpyxl') as writer:
    summary.to_excel(writer, sheet_name='Summary')
