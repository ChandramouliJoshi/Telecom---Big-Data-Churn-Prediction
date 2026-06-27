from ..config.paths import RAW_CSV_PATH
from ..config.spark_config import create_spark_session

spark = create_spark_session()

df = spark.read.csv(
    str(RAW_CSV_PATH),
    header=True,
    inferSchema=True
)

df.show(5)

df.printSchema()

print("Rows:", df.count())
print("Columns:", len(df.columns))

spark.stop()

