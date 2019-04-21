import requests
import json

# PDB fetching in JSON format
# https://www.rcsb.org/pages/webservices/rest-fetch
r = requests.get('https://www.rcsb.org/pdb/json/describePDB?structureId='+'5pti')
print(r.json())