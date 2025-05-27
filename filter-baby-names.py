# Databricks notebook source
babynames = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Volumes/quickstart_catalog_vkm_external/tpch/myvolume/baby/babynames.csv")
babynames.createOrReplaceTempView("babynames_table")
years = spark.sql("select distinct(Year) from babynames_table").toPandas()['Year'].tolist()
years.sort()
dbutils.widgets.dropdown("year", "2014", [str(x) for x in years])
display(babynames.filter(babynames.Year == dbutils.widgets.get("year")))