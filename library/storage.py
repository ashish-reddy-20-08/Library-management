import json
import os
import logging

# storage class to store the data in the json file 

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            logging.info(f"Storage file not found: {self.filename}. Creating a new one.")
            return []
        with open(self.filename, 'r') as file:
            logging.info(f"Loading data from storage file: {self.filename}")
            return json.load(file)

    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Data saved to storage file: {self.filename}")
