import argparse
import io
from typing import Optional

import google.auth
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

load_dotenv()


def get_service(service_name: str, version: str):
    credentials, project = google.auth.default()
    return build(service_name, version, credentials=credentials)


def read_google_doc(doc_id: str) -> str:
    drive_service = get_service('drive', 'v3')

    try:
        file_metadata = drive_service.files().get(fileId=doc_id).execute()
        mime_type = file_metadata.get('mimeType')
    except:
        mime_type = 'application/vnd.google-apps.document'

    if mime_type == 'application/vnd.google-apps.document':
        docs_service = get_service('docs', 'v1')
        document = docs_service.documents().get(documentId=doc_id).execute()
        doc_content = document.get('body').get('content')

        return ''.join(
            text_run['textRun']['content']
            for element in doc_content if 'paragraph' in element
            for text_run in element['paragraph']['elements']
            if 'textRun' in text_run
        )

    request = drive_service.files().get_media(fileId=doc_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)
    content = fh.read().decode('utf-8')

    return content


def botrun_google_docs_reader(doc_id: Optional[str] = '1uV4gjH3yTfvXweXn8nXhQ7Tx2nBm1fPl9WNpWzo2H3w') -> str:
    try:
        return read_google_doc(doc_id)
    except Exception as e:
        return f"Error reading document: {e}"


def main():
    parser = argparse.ArgumentParser(description='下載並讀取 Google Doc, txt, json 或 csv 檔案內容.')
    parser.add_argument('--doc_id', type=str, default='1uV4gjH3yTfvXweXn8nXhQ7Tx2nBm1fPl9WNpWzo2H3w',
                        help='Google 文件或 Drive 檔案 ID')
    args = parser.parse_args()

    content = botrun_google_docs_reader(args.doc_id)
    print("讀取 Google Drive 檔案內容:")
    print(content)


if __name__ == "__main__":
    main()
