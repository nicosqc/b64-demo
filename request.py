import base64
import requests
import json

# URL to get the base64 string
url = "http://127.0.0.1:5000/getpdf"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()
    
    # Retrieve the base64 string from the response
    base64_string = response_json['pdf_base64']
    
    # Decode the base64 string
    binary_data = base64.b64decode(base64_string)

    # Define the file path and name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = f"{timestamp}.pdf"

    # Write the binary data to a file
    with open(file_path, 'wb') as file:
        file.write(binary_data)

    print(f"File saved as {file_path}")
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
