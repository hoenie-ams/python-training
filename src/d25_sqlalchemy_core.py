"""
Demo database connections
"""
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/crm.db")
# engine = create_engine("postgres+psycopg2://user:password@localhost:5432/crm")

print(engine.table_names())

with engine.connect() as connection:
    result = connection.execute("SELECT * FROM clients LIMIT 5")
    for row in result:
        print(row)


# 1. Read all data from a table
df = pd.read_sql("clients", engine)

# 2. Select data of interest
budapest = pd.read_sql('SELECT * FROM clients WHERE city = "Budapest" LIMIT 5', engine)

print(budapest)
