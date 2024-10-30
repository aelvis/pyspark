import csv
csv_file = "/content/sample_data/california_housing_test.csv"
rdd_csv = sc.textFile(csv_file)
rdd = rdd_csv.map(lambda line: next(csv.reader([line])))
rdd.collect()