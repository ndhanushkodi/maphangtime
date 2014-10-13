import json
from pprint import pprint
json_data=open('events.json')

data = json.load(json_data)
#pprint(data)

longitude_list=[]
latitude_list=[]
name_list = []
location_list = []
list_all_events = [['Lat', 'Long', 'Name']]

length = len(data)
for i in range(length):
	name = data[i]['name']
	longitude = data[i]['lng']
	latitude = data[i]['lat']
	location = data[i]["location"]

	list_location_event = [float(latitude),float(longitude),name]
	list_all_events.append(list_location_event)
	list_as_json = json.dumps(list_all_events)
	#name_list.append(name)
	#longitude_list.append(longitude)
	#latitude_list.append(latitude)
	#location_list.append(location)

	#events_dictionary = dict(zip(longitude_list,latitude_list,name_list))

data_file = open('list_of_all_location_name.txt','w')
data_file.write(str(list_as_json))
data_file.close()
#pprint(list_all_events)
