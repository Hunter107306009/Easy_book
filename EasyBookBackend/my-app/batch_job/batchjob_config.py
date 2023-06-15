import yaml
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

file_path = os.path.abspath("./my-app/batch_job/db_config.yml")
with open(file_path, "r", encoding="utf-8") as db_f:
    db_config = yaml.safe_load(db_f)

account = db_config["database"]["account"]
password = db_config["database"]["password"]
address = db_config["database"]["address"]
database = db_config["database"]["database"]


engine = create_engine(
    f"mysql+pymysql://{account}:{password}@{address}/{database}?charset=utf8"
)
Base = declarative_base()
Base.metadata.bind = engine
