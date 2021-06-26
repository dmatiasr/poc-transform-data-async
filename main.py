#
# The purpose of this script is load data from Remote database 
# transform with async method and store data-transformed in another 
# database
#
import asyncio

from sqlalchemy_aio import ASYNCIO_STRATEGY
from sqlalchemy import create_engine, text

from poc_transform_data_async.extract import extract, TABLES
from poc_transform_data_async.driver.driver_source_db import DriverSourceDB


async def main():
	await extract()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())


