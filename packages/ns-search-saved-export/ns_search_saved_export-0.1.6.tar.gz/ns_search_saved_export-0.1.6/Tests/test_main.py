from ns_search_saved_export.ns_search_saved_export import NsSearchSavedExport

api = NsSearchSavedExport(
    url = 'https://5469654.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=3472&deploy=1',
    consumer_key = '6bf7afb708cd34d17d64c19ee74a305e9aa476b85ce7a0143feafd3e841c195a',
    consumer_secret = '029be94e829b9dbd17e33257bc3416739da4aeaa4974169673e34bbee8668037',
    token_key = '2d726b31b7a05d11bbdc517e470cf53310613c9f474f50ac3e348d8a2e6e3d8a',
    token_secret = '6a842ba5f1e13dd56e9cef9a88f7bb05e498973de1942e540ea8554050c3fc44',
    realm = '5469654'
)
    
# Send request
payload = {'searchID': 'customsearch_mc_iges_producto'}

response = api.send_request(payload)

# Extract data
data = api.extract_data(response)

# Save data to Excel
api.save_to_excel(data, 'data.xlsx', 'Sheet1')

# Save data to CSV
api.save_to_csv(data, 'data.csv')

# Save data to TXT
api.save_to_txt(data, 'data.txt')


