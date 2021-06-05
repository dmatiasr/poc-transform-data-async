#
# The purpose of this script is load data from Remote database 
# transform with async method and store data-transformed in another 
# database
#

from poc_transform_data_async.driver import DriverDB


def main():
	origin_db = DriverDB()
	print(origin_db.test_connection())


if __name__ == '__main__':
	main()



