from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("AZURE_ENDPOINT")
key = os.getenv("AZURE_KEY")

# Debug check
print("Endpoint:", endpoint)

if not endpoint:
    raise ValueError("AZURE_ENDPOINT not found in .env file")

if not key:
    raise ValueError("AZURE_KEY not found in .env file")

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

def extract_text(file_path):

    with open(file_path, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-read",
            body=f
        )

        result = poller.result()

    return result.content