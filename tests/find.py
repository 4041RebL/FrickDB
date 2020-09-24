import FrickDB

client = FrickDB.Client()

# Get collection.
col = client.get_col("new_collection")

# return one document which satisfies provided query
col.find_one({"_id":1})

# returns all the documents which satsify the provided query
col.find_many({"address": "geez"})

# returns all the documents in a collection
col.find_all()