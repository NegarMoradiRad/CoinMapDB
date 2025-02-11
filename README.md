#CoinMapDB

This project is a Python-based data pipeline that extracts financial data from **Sahmeto** (XML format) and stores it in a **MongoDB** database.

## Features:
- Extracts **coin mapping data** from Sahmeto and saves it in the `coinmap` collection.
- Ensures efficient data storage in MongoDB.

## How to Run:
1. Install dependencies:
   ```sh
   pip install requests pymongo xmltodict
   
Collection: coinmap
Stores JSON data converted from Sahmeto XML.
Dependencies:
Python 3.x
requests
pymongo
xmltodic
