from pysql_manager import PySql
from pysql_manager.types import StringType, IntegerType
from pysql_manager.functions import col


class User:
    name = StringType(25, default=None)
    age = IntegerType(default=120)

    __table__ = "User"

data = [{"name": None, "age": None}, {"name": "kevin", "age": 24}]
#
pysql = PySql(meta_class=User, username="root", password="password", host="localhost", dbname="appexplorer")
#
# # pysql.insert(data)
# sample_data = pysql.insert(data, update_on_duplicate=["age"])
# print(pysql.fetch_all.unique(col("name")))

# sample_data.fetch_all.show()

print(pysql.fetch_all.is_empty())

# print(sample_data.to_list_dict())


