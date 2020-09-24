import FrickDB

client = FrickDB.Client()

# Get collection.
col = client.get_col("new_collection")

# Deletes a collection, only if there are no foreign files in it.
col.drop()