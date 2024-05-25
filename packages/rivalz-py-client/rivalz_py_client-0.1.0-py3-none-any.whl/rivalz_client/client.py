import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

RIVALZ_API_URL = "https://be.rivalz.ai/api-v1/ipfs"

class RivalzClient:
    def __init__(self, secret=None):
        self.secret = secret or os.getenv('SECRET_TOKEN')

    def upload_file(self, file_path):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': f'Bearer {self.secret}'
            }
            response = requests.post(f'{RIVALZ_API_URL}/upload-file', files=files, headers=headers)
        return response.json()

    def upload_passport(self, file_path):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': f'Bearer {self.secret}'
            }
            response = requests.post(f'{RIVALZ_API_URL}/upload-passport-image', files=files, headers=headers)
        return response.json()

    def download_file(self, ipfs_hash, save_path):
        headers = {
            'Authorization': f'Bearer {self.secret}'
        }
        response = requests.get(f'{RIVALZ_API_URL}/download-file/{ipfs_hash}', headers=headers)
        response_data = response.json().get('data', {})
        file_data = response_data.get('file')
        file_name = response_data.get('name')

        if file_data and file_name:
            file_bytes = base64.b64decode(file_data)
            file_path = os.path.join(save_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(file_bytes)
            return 'File downloaded successfully, check the save path'
        else:
            return 'Failed to download file'

    def delete_file(self, ipfs_hash):
        headers = {
            'Authorization': f'Bearer {self.secret}'
        }
        response = requests.post(f'{RIVALZ_API_URL}/delete-file/{ipfs_hash}', headers=headers)
        return response.json()