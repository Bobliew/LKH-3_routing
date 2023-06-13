from pyspark.sql import SparkSession

# 创建SparkSession
spark = SparkSession.builder.appName("TSP Par File Generation").getOrCreate()

# 定义要处理的数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 将数据转换为Spark RDD
data_rdd = spark.sparkContext.parallelize(data)

# 定义要调用的函数
def call_main(x):
    from generate_tsp_par_file import main
    return main(x)

# 在RDD上使用map操作调用函数
result_rdd = data_rdd.map(call_main)

# 收集结果并打印
result = result_rdd.collect()
print(result)

# 关闭SparkSession
spark.stop()
