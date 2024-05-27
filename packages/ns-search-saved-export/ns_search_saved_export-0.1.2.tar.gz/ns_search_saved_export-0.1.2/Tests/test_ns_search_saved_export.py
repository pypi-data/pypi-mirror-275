import unittest
from unittest.mock import patch, Mock
from search_saved_export.ns_search_saved_export import NsSearchSavedExport

class TestNetSuiteAPI(unittest.TestCase):
    
    def setUp(self):
        self.api = NsSearchSavedExport(
           # pass
        )
        
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
