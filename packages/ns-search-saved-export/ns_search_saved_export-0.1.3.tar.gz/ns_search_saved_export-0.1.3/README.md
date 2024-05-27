# NetSuite SEARCH SAVED EXPORT

This library allows you to interact with saved searches by importing data from saved searches in Excel, CSV, and TXT formats.

## Installation

```python
pip install ns_search_saved_export
```

## Usage

```python
from ns_search_saved_export.ns_search_saved_export import NsSearchSavedExport

# Initialize the API
api = NsSearchSavedExport(
    url='https://your-netsuite-url',
    consumer_key='your_consumer_key',
    consumer_secret='your_consumer_secret',
    token_key='your_token_key',
    token_secret='your_token_secret',
    realm='your_realm'
)

# Send request
payload = {
    "search_id": "1234"  # Replace with your saved search ID
}
response = api.send_request(payload)

# Extract data
data = api.extract_data(response)

# Save data to Excel
api.save_to_excel(data, 'data.xlsx', 'Sheet1')

# Save data to CSV
api.save_to_csv(data, 'data.csv')

# Save data to TXT
api.save_to_txt(data, 'data.txt')

```