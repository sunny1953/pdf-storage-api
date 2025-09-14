from motor.motor_asyncio import AsyncIOMotorClient
from schema import DATABASE_NAME, PDFS_COLLECTION
import os

# MongoDB connection - use environment variable for security
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://its4eminence1:Bharadwaj11042004@sunny.of8x3cx.mongodb.net/?retryWrites=true&w=majority&appName=Sunny&ssl=true&ssl_cert_reqs=CERT_NONE")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]
pdfs_collection = db[PDFS_COLLECTION]

# Test connection
async def test_connection():
    try:
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return True
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return False
