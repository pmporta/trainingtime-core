from sqlalchemy import create_engine
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

engine = create_engine('postgresql://trainingtime:trainingtime00:5432/trainingtimedb')

connection = engine.connect()
result = connection.execute()
for row in result:
    print("")
connection.close()

