from sqlalchemy import create_engine
from sqlalchemy_aio import ASYNCIO_STRATEGY


PATH = 'db_data.db'


class DriverDB:

	def __init__(self, path=PATH):
		self._path = path
		self._engine = create_engine("sqlite:///%s" % path, strategy=ASYNCIO_STRATEGY)

	async def get_connection(self):
		return await self._engine.connect()	

	async def test_connection(self):
		yield self._engine.table_names()

	async def get_table_names(self):
		self._engine.table_names()