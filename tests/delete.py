import FrickDB

client = FrickDB.Client()

# Get collection.
col = client.get_col("new_collection")

# Deletes a single document which satsify the provided query
col.delete_one({"_id":"single_insert"})

# Deletes multiple documents which satsify the provided query
col.delete_many("address": "geez")

# Deletes all the documents in a collection
col.delete_all()