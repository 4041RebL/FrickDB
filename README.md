
# FrickDB
This package creates a wierd json-based database by organising it into folders and subfolders. Its usage is almost similar to PyMongo. The class and methods are listed below.
Check [tests](https://github.com/4041RebL/FrickDB/tree/master/tests) for examples.

### Installing
- For Linux and Mac, use `python3 -m pip install -U FrickDB` to install the package.
- On windows, use `py -3 -m pip install -U FrickDB` to install the package.

### `class` Client:
Represents a client connection that connects to the database.
```py
>>> import FrickDB
>>> client = FrickDB.Client()
```

- #### `method` insert_col(name)
Inserts a collection into the database. Requires one parameter, `name` of the collection to be created.
For example,
```py
>>> col = client.insert_col("collection_name")
```

- #### `method` get_col(col)
Fetches the collection from the database. Requires one parameter, `name` of the collection to be fetched.
For example,
```py
>>> col = client.get_col("collection_name")
```

### `class` Col:
Represents a client connection that connects to the database.
 
- #### `method` insert_one(doc)
Inserts a document into the collection. Requires `doc` parameter as the document to be inserted.
```py
>>> col.insert_one({"_id":1234, "somekey":"somevalue"})
```

- #### `method` insert_many(docs)
Inserts multiple documents into the collection.
For example,
```py
>>> col.insert_many([
	{"_id":1, "somekey1":"somevalue1"}, 
	{"_id":2, "somekey2":"somevalue2"}, 
	{"_id":3, "somekey3":"somevalue3"}, 
	{"_id":4, "somekey4":"somevalue4"}, 
	{"_id":5, "somekey5":"somevalue5"}
])
```

- #### `method`update_one(query, docs)
Updates a document. Requires 2 parameters, `query` and `docs`
Incase of multiple documents satisfying the query, only the first document is updated.
For example,
```py
>>> col.update_one({"_id":1}, {"somevalue1":"newvalue"})
```

- #### `method`update_all(docs)
Updates every document in a collection. Requires 1 parameters `docs`
For example
```py
>>> col.update_all({"newkey":"somenewvalue"})
```

- #### `method`update_many(query, docs)
Updates multiple document. Requires 2 parameters, `query` and `docs`
Incase of multiple documents satisfying the query, all the documents are updated.
For example,
```py
>>> col.update_many({"newkey":"somenewvalue"}, {"newkey":"anothernewvalue"})
```

# Unfinished
```py
	method find_all()
	method find_many(query)
	method find_one(query)
	method delete_one(query)
	method delete_many(query)
	method delete_all()
	method drop()
```
```py
class Sort:
	method by_asc(key)
	method by_desc(key)
```
