import pyspark
import pyspark.sql.functions as F
from pyspark.sql.window import Window

df = transactions
  .filter(F.col('total_amount')>0)
  .withColumn('ym',F.date_format(F.col('transaction_date'),'yyyy-MM'))

df_1 = df.groupBy('ym').agg(F.sum('total_amount').alias('total_amount'))

w = (
  Window.orderBy('ym')
  .rowsBetween(-2,0)
  )

df_2 = df_1.withColumn('rolling_avg', F.avg('total_amount').over(w))
  .drop('total_amount').orderBy('ym')
