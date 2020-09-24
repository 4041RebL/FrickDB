import FrickDB

client = FrickDB.Client()

# Get collection.
col = client.get_col("new_collection")

# Update one document, provide query as first arg and updated doc as second
col.update_one({"_id":"single_insert"}, {"address":"updated data"})

# Update all documents, takes one argument only
col.update_all({"new_key":"some value"})

# Update multiple documents, provide query as first arg and updated doc as second
col.update_many({"new_key":"some value"}, {"address":"geez"})
