import pandas as pd
order = 10100

status = 'Shipped'

sql = """SELECT  * from orders where orderNumber = ?
         and status = ? order by orderNumber"""
df1 = pd.read_sql_query(sql, cnx, params=[order, status])
