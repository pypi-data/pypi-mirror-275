# filename: google_doc_downloader.py
import argparse

import google.auth
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()


def botrun_google_doc_reader(doc_id: str) -> str:
    credentials, project = google.auth.default()
    service = build('docs', 'v1', credentials=credentials)
    document = service.documents().get(documentId=doc_id).execute()
    doc_content = document.get('body').get('content')

    text = ''
    for element in doc_content:
        if 'paragraph' in element:
            for text_run in element['paragraph']['elements']:
                if 'textRun' in text_run:
                    text += text_run['textRun']['content']

    return text


def main():
    parser = argparse.ArgumentParser(description='Download Google Doc and read content.')
    parser.add_argument('--doc_id', type=str, default='1uV4gjH3yTfvXweXn8nXhQ7Tx2nBm1fPl9WNpWzo2H3w',
                        help='Google Doc ID')
    args = parser.parse_args()
    print("botrun_google_doc_reader.py, args.doc_id:", args.doc_id)
    print(botrun_google_doc_reader(args.doc_id))


if __name__ == "__main__":
    main()
