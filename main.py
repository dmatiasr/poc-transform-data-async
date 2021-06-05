#
# The purpose of this script is load data from Remote database 
# transform with async method and store data-transformed in another 
# database
#

from poc_transform_data_async.process import process_data, TABLES
from poc_transform_data_async.driver.driver_source_db import DriverSourceDB


def main():

	db = DriverSourceDB()
	results = []
	for table in TABLES:
		data = db.get_data_from(table)
		results.append(data)

	for elems in results:
		for row in elems:
			print(row)



if __name__ == '__main__':
	main()



