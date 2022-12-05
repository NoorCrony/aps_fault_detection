import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATAFILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    # read csv file
    df = pd.read_csv(DATAFILE_PATH)
    print(df.shape)

    # convert df to JSON format, so that we can dump into MongoDB
    df.reset_index(drop=True, inplace=True)
    print(df.head())
    json_records = list(json.loads(df.T.to_json()).values())
    print(json_records[0])

    # insert json records to mongoDB
    # client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)

