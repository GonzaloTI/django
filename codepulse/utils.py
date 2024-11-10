from django.http import JsonResponse
import nmap
import requests
import logging
import re
from codepulse.models import ScanResult  

# This essentailly sets up logging to help me enable tracking of information and errors 
logger = logging.getLogger(__name__)

def fetch_url(url):
    try:
        # This attempts to retrieve content from the specified URL
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception
        # This returns the text content of the fetched URL, HTML or similar web content
        return response.text
    except requests.RequestException as e:
        # this Logs any errors encountered during the fetching process
        logger.error(f"Error fetching URL {url}: {e}")
        # this will return None if an error occurs to signify the fetch was unsuccessful
        return None

 # registration of the url in the database for the corresponding user
# print(request.user.id)

 