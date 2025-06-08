import requests
from pyDataverse.api import NativeApi, DataAccessApi
import zipfile
import os

cm4ai_doi = "doi:10.18130/V3/DXWOS5"
base_url = "https://dataverse.lib.virginia.edu"
target_filename = "cm4ai_chromatin_mda-mb-468_untreated_apms_0.1_alpha.zip"
output_dir = "data/raw"

os.makedirs(output_dir, exist_ok=True)

api = NativeApi(base_url)

print("Downloading data set (this may take a while)...")
cm4ai_dataset = api.get_dataset(cm4ai_doi)
files = cm4ai_dataset.json()['data']['latestVersion']['files']

file_id = None
for file in files:
    if file['dataFile']['filename'] == target_filename:
        file_id = file['dataFile']['id']
        break

# Download the file
if file_id:
    download_url = f"{base_url}/api/access/datafile/{file_id}"
    filename = target_filename
    output_path = os.path.join(output_dir,filename)
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {target_filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
else:
    print("Target file not found in dataset.")

print("Extracing archives...")
for filename in os.listdir(output_dir):
    if filename.endswith('.zip'):
        zip_path = os.path.join(output_dir, filename)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.infolist():
                if not member.is_dir():
                    member.filename = os.path.basename(member.filename)
                    zip_ref.extract(member, output_dir)
        os.remove(zip_path)

print(f"Complete! AP-MS data extracted to: {output_dir}")
