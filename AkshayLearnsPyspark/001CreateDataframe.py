# Databricks notebook source
from pyspark.sql.types import *

# COMMAND ----------

spark.createDataFrame([('Alex',1),('Sara',21)]).show()

# COMMAND ----------

dict_data =[{'Name':'Alex', 'Age':10},
       {'Name':'Sara', 'Age':20},
       {'Name':'John', 'Age':30},
       {'Name':'Conor', 'Age':40}
       ]      

# COMMAND ----------

struct = StructType([
                        StructField('Name', StringType(), True),
                        StructField('Age', StringType(), True)
                    ])

# COMMAND ----------

spark.createDataFrame(data=dict_data, schema=struct).show()

# COMMAND ----------

df = spark.createDataFrame(data=dict_data, schema=struct) 

# COMMAND ----------

display(df)

# COMMAND ----------

schema_ddl=DataType.fromDDL("name string NOT NULL, age int")
data=[('Alex',10),('Sara',20),('John',30),(None,40)]

# COMMAND ----------

try:
    df_ddl = spark.createDataFrame(data=data, schema=schema_ddl) 
    display(df_ddl)
except Exception as e :
    print(e)

# COMMAND ----------

try:
    df_ddl = spark.createDataFrame(data=data, schema=schema_ddl) 
    display(df_ddl)
except Exception as e :
    print(e)
