import pandas as pd

#extract data from csv
customers = pd.read_csv("../data_resources/customers.csv")
products = pd.read_csv("../data_resources/products.csv")
orders = pd.read_csv("../data_resources/orders.csv")

customers['name'] = customers['name'].str.title()
customers['city'] = customers['city'].str.title()
customers['join_date'] = pd.to_datetime(customers['join_date'])

orders['order_date']= pd.to_datetime(orders['order_date'])

orders['avg_price_per_item']=orders['total_amount']/orders['quantity']

orders = orders.merge(products[['product_id','category']],on='product_id',how='left')


print('customers : \n',customers.head())
print('products: \n',products.head())
print('orders : \n',orders.head())

#load into bigquery
from google.cloud import bigquery

client = bigquery.Client(project='first-project-477503')


customer_table = "first-project-477503.Ecommerce_data.customers"
product_table = "first-project-477503.Ecommerce_data.products"
orders_table = "first-project-477503.Ecommerce_data.orders"

#load dataframes into bigquery
client.load_table_from_dataframe(customers,customer_table).result()
client.load_table_from_dataframe(products,product_table).result()
client.load_table_from_dataframe(orders,orders_table).result()

print("data loaded successfully into bigquery")