import requests

class NetworkResponseIterator:
    def __init__(self, url):
        self.url = url
        self.response_iterator = self._get_response_iterator()

    def _get_response_iterator(self):
        response = requests.get(self.url, stream=True)
        response.raise_for_status()

        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.response_iterator)


# Usage example: Iterating over network responses in real time
url = "https://example.com/big_data_file.txt"
response_iterator = NetworkResponseIterator(url)

for chunk in response_iterator:
    # Process the chunk of data as it arrives
    print("Received chunk:", chunk[:10])  # Print the first 10 characters
