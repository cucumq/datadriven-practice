import pyspark
from pyspark.sql.windows import Window
import pyspark.sql.functions as F

w = (
  Window.partitionBy('svc_name')
  .orderBy('checked')
  .rowsBetween(-6,0)  
  )

df = svc_health
  .withColumn('rolling_avg', F.avg('latency').over(w))
  .select('svc_name','checked','latency','rolling_avg')



df
