from typing import Optional, List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
import gridfs
from bson import ObjectId

async def find_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Any]:
    print(f"Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing find_one query with filter: {filter}")
        result = await collection.find_one(filter)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()


async def find_all(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[List[Dict]]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing find_all query with filter: {filter}")
        cursor = collection.find(filter)
        result = await cursor.to_list(length=None)
        print(f"result: {result}")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def insert_one(mongodb_uri: str, database_name: str, collection_name: str, document: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing insert_one query with document: {document}")
        result = await collection.insert_one(document)
        return {"inserted_id": result.inserted_id}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def insert_many(mongodb_uri: str, database_name: str, collection_name: str, documents: List[Dict]) -> Optional[List]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing insert_many query with documents: {documents}")
        result = await collection.insert_many(documents)
        print(f"ids of the inserted documents: {result.inserted_ids}")
        return {"inserted_ids": result.inserted_ids}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def update_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict, update: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing update_one query with filter: {filter} and update: {update}")
        result = await collection.update_one(filter, update)
        result_dict = result.raw_result
        print(f"result: {result_dict}")
        return result_dict
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def update_many(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict, update: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing update_many query with filter: {filter} and update: {update}")
        result = await collection.update_many(filter, update)
        result_dict = result.raw_result
        print(f"result: {result_dict}")
        return result_dict
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def delete_one(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing delete_one query with filter: {filter}")
        result = await collection.delete_one(filter)
        result_dict = result.raw_result
        print(f"Query result: {result_dict}")
        return result_dict
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def delete_many(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing delete_many query with filter: {filter}")
        result = await collection.delete_many(filter)
        result_dict = result.raw_result
        print(f"Query result: {result_dict}")
        return result_dict
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def count(mongodb_uri: str, database_name: str, collection_name: str, filter: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing count query with filter: {filter}")
        result = await collection.count_documents(filter)
        print(f"Query result: {result}")
        return {"count": result}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def drop(mongodb_uri: str, database_name: str, collection_name: str) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    db = client[database_name]

    try:
        print(f"Executing drop query with collection name: {collection_name}")
        result = await db.drop_collection(collection_name)
        print(f"Query result: {result}")
        return {"dropped": collection_name}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def drop_database(mongodb_uri: str, database_name: str) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)

    try:
        print(f"Executing drop_database query with database name: {database_name}")
        result = await client.drop_database(database_name)
        print(f"Query result: {result}")
        return {"dropped": database_name}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def create_index(mongodb_uri: str, database_name: str, collection_name: str, index: Dict) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing create_index query with index: {index}")
        result = await collection.create_index(index)
        print(f"Query result: {result}")
        return {"index": result}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def drop_index(mongodb_uri: str, database_name: str, collection_name: str, index_name: str) -> Optional[Dict]:
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]

    try:
        print(f"Executing drop_index query with index name: {index_name}")
        result = await collection.drop_index(index_name)
        print(f"Query result: {result}")
        return {"dropped_index": index_name}
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def download_file(mongodb_uri: str, database_name: str, id: str):
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    fs = gridfs.AsyncIOMotorGridFSBucket(client[database_name])

    try:
        file = await fs.open_download_stream(ObjectId(id))
        with open(f'{id}', 'wb') as f:
            content = await file.read()
            f.write(content)
        return id
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()

async def random_value(mongodb_uri: str, database_name: str, collection_name: str, key_name: str):
    print("Connecting to MongoDB server...")
    client = AsyncIOMotorClient(mongodb_uri)
    collection = client[database_name][collection_name]
    
    try:
        document = await collection.aggregate([{"$sample": {"size": 1}}]).to_list(length=1)
        return document[0][key_name] if document else None
    except Exception as e:
        raise Exception(f"An error occurred while querying the MongoDB collection: {str(e)}")
    finally:
        client.close()
