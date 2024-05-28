import json
import oauth2 as oauth
import requests
import pandas as pd
from .utils import SignatureMethod_HMAC_SHA256

class NsSearchSavedExport:
    def __init__(self, url: str, consumer_key: str, consumer_secret: str, token_key: str, token_secret: str, realm: str, search_id: str = ''):
        """Class constructor

        Args:
            url (str): RESTlet service URL to export saved search
            consumer_key (str): Netsuite integration client key
            consumer_secret (str): Netsuite integration client secret key
            token_key (str): NetSuite Access Key Token
            token_secret (str): NetSuite Access Secret Token
            realm (str): NetSuite domain environment ID. Example: 123456
            searchID (str): search ID of the search saved in NetSuite
        """
        self.url = url
        self.consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
        self.token = oauth.Token(key=token_key, secret=token_secret)
        self.realm = realm
        self.search_id = search_id
        self.payload = {'searchID': search_id}

    def _generate_oauth_params(self):
        """Returns the structured oauth parameters

        Returns:
            dict: Oauth params
        """
        return {
            'oauth_version': '1.0',
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_timestamp': str(oauth.generate_timestamp()),
            'oauth_token': self.token.key,
            'oauth_consumer_key': self.consumer.key,
            'oauth_signature_method': 'HMAC-SHA256'
        }

    def send_request(self):
        """POST request to obtain saved search data

        Returns:
            dict: POST request response
        """
        params = self._generate_oauth_params()
        req = oauth.Request(method='POST', url=self.url, parameters=params)
        signature_method = SignatureMethod_HMAC_SHA256()
        req.sign_request(signature_method, self.consumer, self.token)
        header = req.to_header(self.realm)
        headers = {'Authorization': header['Authorization'].encode('ascii', 'ignore'), 'Content-Type': 'application/json'}
        
        response = requests.post(url=self.url, headers=headers, data=json.dumps(self.payload))
        response.raise_for_status()
        return response.json()

    def extract_data(self, json_data: dict):
        """Structured data obtained from the saved search

        Args:
            json_data (dict): Data obtained in the POST response

        Returns:
            list: List of saved search data
        """
        # Export original JSON data to a JSON file
        with open(self.search_id, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        
        matrix = []
        headers = set()
        for index, data in enumerate(json_data['results']):
            row = []
            values = data['values']
            
            if index == 0:
                headers = list(values.keys())
                matrix.append(headers)
            
            for key in headers:
                value = values.get(key, "")
                if isinstance(value, list) and key == 'internalid':
                    row.append(value[0]['value'])
                elif isinstance(value, list) and value and 'text' in value[0]:
                    row.append(value[0]['text'])
                elif isinstance(value, dict) and 'text' in value:
                    row.append(value['text'])
                else:
                    row.append(value)
            matrix.append(row)
        
        return matrix

    @staticmethod
    def save_to_excel(matrix: list, filename: str, sheet_name: str):
        """Save data in Excel format

        Args:
            matrix (list): Search data
            filename (str): Excel file name
            sheet_name (str): Excel sheet name
        """
        df = pd.DataFrame(matrix[1:], columns=matrix[0])
        df.to_excel(filename, sheet_name=sheet_name, index=False)
        
    @staticmethod
    def save_to_csv(matrix: list, filename: str):
        """Save data in CSV format

        Args:
            matrix (list): Search data
            filename (str): CSV file name
        """
        df = pd.DataFrame(matrix[1:], columns=matrix[0])
        df.to_csv(filename, index=False)

    @staticmethod
    def save_to_txt(matrix: list, filename: str):
        """Save data in TXT format

        Args:
            matrix (list): Search data
            filename (str): TXT file name
        """
        df = pd.DataFrame(matrix[1:], columns=matrix[0])
        df.to_csv(filename, sep=',', index=False, header=False)
