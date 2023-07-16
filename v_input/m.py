import firebase_admin
from firebase_admin import db
import json

cred_object = firebase_admin.credentials.Certificate('key.json')
firebase_admin.initialize_app(cred_object, {
	'databaseURL':'https://twoo-77302-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})
ref = db.reference("/unity_api/test")
a = '{"punch":"a","kick":"a","crouch":"a","moveb":"a","movef":"a","stay":"a","superattack":"a"}'
ref.set(json.loads(a))