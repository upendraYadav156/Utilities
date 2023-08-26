from pyspark.sql import SparkSession
#pip install pyspark    
if __name__ == "__main__":
    spark=SparkSession.builder().appName("Spark_SQL_5_Save To Hive").enableHiveSupport().getOrCreate();
    spark.sparkContext().conf().set("spark.sql.warehouse.dir", "/user/hive/metastore/");
    spark.sparkContext().conf().set("hive.metastore.uris", "hrift://hadoop.spark:9083");
    spark.sql("show tables").show()
    
    
    
    
    SparkSession spark=SparkSession.builder().appName("Spark_SQL_5_Save To Hive").enableHiveSupport().getOrCreate();
    spark.sparkContext().conf().set("spark.sql.warehouse.dir", "/user/hive/metastore/");
    spark.sparkContext().conf().set("hive.metastore.uris", "hrift://hadoop.spark:9083");
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    root@f6fd0efde090:/usr/local/bin# cat hiveconnector.py
from pyspark.sql import SparkSession
#pip install pyspark
if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .config("spark.sql.uris", "thrift://hadoop.spark:9083") \
        .config("spark.sql.warehouse.dir", "/user/hive/metastore/")\
        .enableHiveSupport() \
        .getOrCreate()
    spark.sql("show tables").show()
root@f6fd0efde090:/usr/local/bin#