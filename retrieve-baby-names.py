# Databricks notebook source
import requests

response = requests.get('http://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv')
csvfile = response.content.decode('utf-8')
dbutils.fs.put("/Volumes/quickstart_catalog_vkm_external/tpch/myvolume/baby/babynames.csv", csvfile, True)


