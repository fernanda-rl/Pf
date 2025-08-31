from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # altere se usar MongoDB Atlas
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.academia
atletas_collection = database.get_collection("atletas")
