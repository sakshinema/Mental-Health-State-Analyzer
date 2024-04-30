def save_history(user_id,disease_score):
	#user_id = "rahul0405"

	import pymongo
	client = pymongo.MongoClient("mongodb+srv://rahul:rahul@mentalhealthstatusanaly.5wzql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	database = client[user_id]
	collection = database['history']

	import datetime
	time = datetime.datetime.now()
	timestamp = time.timestamp()

	data = {timestamp:disease_score}
	collection.insert_one(data)

	return {"result":"history saved for user {}".format(user_id)}