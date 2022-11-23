import build.firebase_config as fc

storage = fc.firebase.storage()
url = storage.child('video_upload/video_2022-11-23_12h06m05s.mp4').get_url(None).s

print(url)
