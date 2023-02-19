import firebase_admin
from firebase_admin import db, firestore
import pandas as pd


# initialize sdk
cred_obj = firebase_admin.credentials.Certificate('/Users/tobysavage/Documents/CU Boulder/Senior Year/Spring 2022/Capstone II/OfferChief/Code/offerchief-firebase-adminsdk-fqr9i-cbbe6b104d.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://offerchief-default-rtdb.firebaseio.com/'})

# initialize firestore instance
firestore_db = firestore.client()

# add data - test
# firestore_db.collection(u'homes').add({'address':{'city':'Del Mar', 'postal_code:':92014, 'state':'CA', 'street':'24th Street', 'street_number':145}, 'baths_full': 3, 'beds': 4, 'building_size':'1854', 'garage':2, 'lot_size':0.25, 'predicted_purchase_price': 2500000, 'prop_type':'single_family', 'purchase_price':2350000, 'year_built':2005})

# read computer/organized data fro csv file
df = pd.read_csv ('properties_listings.csv')

# add data to firebase database
for i in range(len(df)):
    if i%5 == 0: # testing moniterization 
        print(i)
    firestore_db.collection(u'property_listings').add({'address':str(df.iloc[i]['addr']), 'city':df.iloc[i]['city'], 'state':df.iloc[i]['state'],\
        'zip':int(df.iloc[i]['postal_code']), 'baths_full':int(df.iloc[i]['baths_full']), 'beds':int(df.iloc[i]['beds']), 'building_size':int(df.iloc[i]['building_size']), \
        'lot_size':int(df.iloc[i]['lot_size']), 'predicted_purchase_price':int(df.iloc[i]['predicted_purchase_price']), 'prop_type':df.iloc[i]['prop_type'],\
        'listing_price':int(df.iloc[i]['listing_price'])})

