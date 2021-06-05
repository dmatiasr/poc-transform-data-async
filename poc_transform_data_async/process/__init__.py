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


def process_data():
    origin = DriverSourceDB()
    for table in TABLES:
        data = origin.get_data_from(table)
