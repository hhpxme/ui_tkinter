import firebase_config
import requests
import json

db = firebase_config.firebase.database()
print(db.get().val())


def get_video_name():
    storage = firebase_config.firebase.storage()
    url = storage.get_url(None)
    r = requests.get(url)
    with open('json_file/link.json', 'wb') as f:
        f.write(r.content)

    # Opening JSON file
    f = open('json_file/link.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    name = []
    # Iterating through the json
    # list
    for i in data['items']:
        s1 = str(i).split(': ')
        s2 = s1[1].split('\'')
        name.append(s2[1])
    name.sort(reverse=True)

    return name

