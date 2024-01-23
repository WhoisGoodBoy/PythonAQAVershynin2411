from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bson
uri = "mongodb+srv://Primat:d2z76ctb@cluster0.v1o4bs7.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

weather_db = client.get_database('sample_weatherdata')
data_collection = weather_db.get_collection('data')
print(data_collection)
collection_of_data_samples = data_collection.find_raw_batches()
#for datasample in collection_of_data_samples:
#    print(bson.decode_all(datasample))
result = data_collection.find_one(filter={'type':"FM-13"})
print(result)
value_to_insert = data_collection.insert_one({'Definitely not a city that falls onto weather related collapses':'Kyiv'})
print(value_to_insert)
check_if_value_inserted = data_collection.find_one(value_to_insert.inserted_id)
print(check_if_value_inserted)