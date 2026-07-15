import dlt

@dlt.table
def transform_data():
    return spark.range(10)