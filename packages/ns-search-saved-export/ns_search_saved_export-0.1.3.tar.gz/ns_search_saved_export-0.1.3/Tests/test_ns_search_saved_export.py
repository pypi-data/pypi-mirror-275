import unittest
from unittest.mock import patch, Mock
from search_saved_export.ns_search_saved_export import NsSearchSavedExport

class TestNetSuiteAPI(unittest.TestCase):
    
    def setUp(self):
        self.api = NsSearchSavedExport(
            url = 'https://5469654.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=3472&deploy=1',
            consumer_key = '6bf7afb708cd34d17d64c19ee74a305e9aa476b85ce7a0143feafd3e841c195a',
            consumer_secret = '029be94e829b9dbd17e33257bc3416739da4aeaa4974169673e34bbee8668037',
            token_key = '2d726b31b7a05d11bbdc517e470cf53310613c9f474f50ac3e348d8a2e6e3d8a',
            token_secret = '6a842ba5f1e13dd56e9cef9a88f7bb05e498973de1942e540ea8554050c3fc44',
            realm = '5469654'
        )
        payload = {'searchID': 'customsearch_mc_iges_producto'}
        
    @patch('search_saved_export.ns_search_saved_export.requests.post')
    def test_send_request(self, mock_post):
        # Mock the response
        mock_response = Mock()
        expected_json = {"results": [{"values": {"internalid": [{"value": "123"}], "name": "Test"}}]}
        mock_response.json.return_value = expected_json
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response
        
        payload = {"search": "criteria"}
        response = self.api.send_request(payload)
        
        self.assertEqual(response, expected_json)
        mock_post.assert_called_once()
    
    def test_extract_data(self):
        json_data = {"results": [{"values": {"internalid": [{"value": "123"}], "name": "Test"}}]}
        expected_matrix = [['internalid', 'name'], ['123', 'Test']]
        
        result = self.api.extract_data(json_data)
        
        self.assertEqual(result, expected_matrix)

    @patch('pandas.DataFrame.to_excel')
    def test_save_to_excel(self, mock_to_excel):
        matrix = [['Col1', 'Col2'], ['Data1', 'Data2']]
        self.api.save_to_excel(matrix, 'test.xlsx', 'Sheet1')
        mock_to_excel.assert_called_once()

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_csv(self, mock_to_csv):
        matrix = [['Col1', 'Col2'], ['Data1', 'Data2']]
        self.api.save_to_csv(matrix, 'test.csv')
        mock_to_csv.assert_called_once()

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_txt(self, mock_to_csv):
        matrix = [['Col1', 'Col2'], ['Data1', 'Data2']]
        self.api.save_to_txt(matrix, 'test.txt')
        mock_to_csv.assert_called_once_with('test.txt', sep=',', index=False, header=False)

if __name__ == '__main__':
    unittest.main()
