from poc_transform_data_async.driver.driver_source_db import DriverSourceDB
TABLES = (
    "user",
    "role_of_rule",
    "iprestrictions",
    "dynamicgroup",
    "hr_of_user",
    "permission_metadata",
    "proxy_of_user"
)


async def extract():
    db = DriverSourceDB()
    results = []
    for table in TABLES:
        data = db.get_data_from(table)
        results.append(data)

    async for elem in data:
        print( await elem.fetchall())


