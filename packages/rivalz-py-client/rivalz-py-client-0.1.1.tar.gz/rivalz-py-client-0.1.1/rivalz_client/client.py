import requests
import base64
import os

RIVALZ_API_URL = "https://be.rivalz.ai/api-v1"


class RivalzClient:
    def __init__(self, secret: str = ''):
        self.secret = secret or os.getenv('SECRET_TOKEN')

    def upload_file(self, file_path: str):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': f'Bearer {self.secret}'
            }
            res = requests.post(f"{RIVALZ_API_URL}/ipfs/upload-file", files=files, headers=headers)
            res.raise_for_status()  # Raise an error for bad status codes
            upload_hash = res.json()['data']['uploadHash']
            return self.get_ipfs_hash(upload_hash)

    def upload_passport(self, file_path: str):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            headers = {
                'Authorization': f'Bearer {self.secret}'
            }
            res = requests.post(f"{RIVALZ_API_URL}/ipfs/upload-passport-image", files=files, headers=headers)
            res.raise_for_status()  # Raise an error for bad status codes
            upload_hash = res.json()['data']['uploadHash']
            return self.get_ipfs_hash(upload_hash)

    def download_file(self, ipfs_hash: str, save_path: str):
        headers = {
            'Authorization': f'Bearer {self.secret}'
        }
        res = requests.get(f"{RIVALZ_API_URL}/ipfs/download-file/{ipfs_hash}", headers=headers)
        res.raise_for_status()  # Raise an error for bad status codes
        data = res.json()['data']
        file_data = base64.b64decode(data['file'])
        file_name = data['name']
        os.makedirs(save_path, exist_ok=True)
        file_path = os.path.join(save_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(file_data)
        return f'File downloaded successfully, check the save path: {file_path}'

    def delete_file(self, ipfs_hash: str):
        headers = {
            'Authorization': f'Bearer {self.secret}'
        }
        res = requests.post(f"{RIVALZ_API_URL}/ipfs/delete-file/{ipfs_hash}", headers=headers)
        res.raise_for_status()  # Raise an error for bad status codes
        return res.json()

    def get_ipfs_hash(self, upload_hash: str):
        headers = {
            'Authorization': f'Bearer {self.secret}'
        }
        while True:
            res = requests.get(f"{RIVALZ_API_URL}/upload-history/{upload_hash}", headers=headers)
            res.raise_for_status()  # Raise an error for bad status codes
            upload_info = res.json()['data']
            if upload_info:
                return upload_info