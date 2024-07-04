import requests
import json
import xmltodict
from pymongo import MongoClient


url = "https://sahmeto.com/crypto-sitemap.xml"


response = requests.get(url)

if response.status_code == 200:
   
    xml_data = response.content.decode('utf-8')

    
    data_dict = xmltodict.parse(xml_data)

    
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sahmeto']
    collection = db['coinmap']


    for url in data_dict['urlset']['url']:
        coin_name = url['loc'].split('/')[-1]
        url['name'] = coin_name
        collection.insert_one(url)

    print("Data successfully saved to MongoDB.")
else:
    print("Error loading xml data:", response.status_code)
