import requests
from bs4 import BeautifulSoup
import re
import json


        
        
    
    
if __name__ == '__main__':
    response = requests.get('https://feeds.megaphone.fm/hubermanlab')
    if response.status_code == 200:
        master_meta = parse_text(response.text)
        with open('metadata.json', 'w') as json_file:
            json.dump(master_meta, json_file)
        