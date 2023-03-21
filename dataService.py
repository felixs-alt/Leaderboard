import firebase_admin
from firebase_admin import firestore

# Application Default credentials are automatically created.
app = firebase_admin.initialize_app()
db = firestore.client()


docs = db.collection(u'users').where(u'clicks')
print(docs)
