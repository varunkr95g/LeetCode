spark practice:


import org.apache.spark.sql.{Encoders, Row, SparkSession}
import org.apache.spark.sql.types.{ArrayType, DataType, DataTypes, DoubleType, IntegerType, MapType, StringType, StructField, StructType}
import org.apache.spark.sql.functions.{col, from_json, struct, when}

import spark.implicits._

val sparkSession = org.apache.spark.sql.SparkSession.builder.master("local").appName("Spark_Practice").getOrCreate;

val simpleData = Seq(Row(1,"abc",23),
    Row(2,"xyz",34),
    Row(3,"pqr",45)
  )
  
   val simpleSchema = StructType(Array(
    StructField("id",IntegerType,true),
    StructField("name",StringType,true),
    StructField("age",IntegerType,true)
    ))
    
    val mainDF = sparkSession.createDataFrame(spark.sparkContext.parallelize(simpleData),simpleSchema)
    
    mainDF.printSchema()
    mainDF.show()


val simpleData_2 = Seq(Row(1,23),
    Row(2,34),
    Row(1,45)
  )


 val simpleSchema_2 = StructType(Array(
    StructField("dept",IntegerType,true),
StructField("age",IntegerType,true)
    ))  
    
 val mainDF = sparkSession.createDataFrame(spark.sparkContext.parallelize(simpleData_2),simpleSchema_2)
    
    mainDF.printSchema()
    mainDF.show()   

mainDF.groupBy("dept").sum("age").show()
    
