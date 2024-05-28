from pymongo import MongoClient
import yaml
class MongoModel:
    connection_uri = ""
    db_name = ""
    db_client = ""
    def init_by_conf(self,conf_path:str) -> None:
        with open(conf_path,'r') as f:
            configs = yaml.load(f,Loader=yaml.FullLoader)
        self.connection_uri = configs['mongo']['uri']
        self.db_name = configs['mongo']['defaul']
    def get_database(self):
        # 提供 mongodb atlas url 以使用 pymongo 将 python 连接到 mongodb
        CONNECTION_STRING = self.connection_uri
        
        # 使用 MongoClient 创建连接。您可以导入 MongoClient 或者使用 pymongo.MongoClient
        client = MongoClient(CONNECTION_STRING)

        # 为我们的示例创建数据库（我们将在整个教程中使用相同的数据库
        return client[self.db_name]