
from pymongo import MongoClient
import pandas as pd


#_____________________________________Sourced by xiewenqian
#MongoDB 연결 이거 굳이?
def _connect_mongo(host, port, username, password, db):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

#MongoDB 읽기
def read_mongo(db, collection, query={}, host='localhost', port = 27017, username=None, password=None, no_id=True)
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    #Delete the _id
    if no_id and '_id' in df:
        del df['_id']

    return df

if __name__ == '__main__':
    df = read_mongo('db_test', 'db_collection', {}, '172.168.203.174', 10800)
    df.to_csv('', index=False)

client = MongoClient('125.140.110.217:27017', username='guest', password = 'keti', authSource='guest')
