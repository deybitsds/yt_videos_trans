# -------------- LIBRERIAS
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.documents import Document 
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import concurrent.futures
import re
import json
import jsonlines
import os
import ipynb

from auxiliar_tasks import *

# -main
def main():
    docs = []
    from urls import list_urls
    for link_url in list_urls:
        document = video_procesing(link_url)
        docs.append(document)
    
    file_path = "Doc.jsonl"
    save_to_doc(file_path, docs)
    print()
    print("="*40)
    print("EVERYTHING WENT WELL :). Finished")
    print("="*40)




if __name__ == "__main__":
    main()

