from sqlalchemy import text
from . import DriverDB


class DriverSourceDB(DriverDB):
    def __init__(self, path=None):
        self._path = path
        super(DriverSourceDB, self).__init__()

    async def get_data_from(self, table, left_condition=None, right_condition=None):
        statement = text("SELECT * FROM %s LIMIT 15" % table)
        conn = await self.get_connection()
        data = await conn.execute(statement)
        yield data