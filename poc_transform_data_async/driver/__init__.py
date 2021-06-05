from sqlalchemy import create_engine

PATH = 'db_data.db'


class DriverDB:
	def __init__(self, path=PATH):
		self._path = path
		self._engine = create_engine("sqlite:///%s" % path)
		self._conn = self._engine.connect()

	def test_connection(self):
		return self._engine.table_names()