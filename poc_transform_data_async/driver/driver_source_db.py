from sqlalchemy import text
from . import DriverDB


class DriverSourceDB(DriverDB):
    def __init__(self, path=None):
        self._path = path
        super(DriverSourceDB, self).__init__()

    async def get_data_from(self, table):
        statement = text("SELECT * FROM %s LIMIT 20" % table)
        conn = await self.get_connection()
        data = await conn.execute(statement)
        yield data

    @staticmethod
    async def deserialize(data):
        """
         Deserialize data from ProxyResult
         :param data generator object, each elements is
         a async_generator with fetchall() method implemented.

         :return generator with calculated elements fetched
        """

        return (
            await proxy_result.fetchall()
            for async_generators in data
            async for proxy_result in async_generators
        )
