#to pull from the api
import requests

#to parse data
import pandas as pd
import numpy as np

#iteration tracking
from tqdm import tqdm

#downloading
import wget


class download_gwas_summary_stats:
    def __init__(self, index: str):
        self.index = self.parse_index(index)
        #TODO: get an iterator that iterates through the list and then calls def extract_gwas for everything in the list

    def extract_gwas(self, GWAS_ID) -> None:
        """
        grabs .tsv summary statistics associated with gwas id

        ARGS:
            GWAS_ID is the gwas id of the research
        
        RETURNS: 
            None
        """
        #TODO 1: see if you can access endpoint

        #get the url
        endpoint = self.find_endpoint(GWAS_ID) + "/"

        url = 'http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/' + endpoint

        #check the response
        response = requests.get(url=url)

        #if response.code == 200:

        #get the link using def extract_link
        link = url + "/" + self.extract_link(response)
        
        #TODO: WGET IS SLOOWWWWWW (~2 hours to download)
        wget.download(link)

    
    def extract_link(self, response: requests.Response) -> str:
        """
        extracts the link from a response from def extract_gwas

        ARGS: 
            response is the http response object

        RETURNS:
            string associated with the link in the response object
        """
        txts = response.text

        #iterate through the lines for the file
        #find first occurance of .tsv file
        #get the link
        for i in txts.splitlines():
            if ".tsv" in i:
                start = '>'
                end = '<'
                link = (i.split(start))[1].split(end)[0]
                return link
            

    def find_endpoint(self, GWAS_ID):
        """
        get the endpoint associated with the GWAS_ID
        
        ARGS:
            GWAS_ID is the id

        RETURNS:
            a string that represents the endpoint that hosts the GWAS ID
        """
        example = "GCST007999"
        df = pd.read_csv("gwas_catalog_index/index.csv", header = 0)

        #TODO 1: Iterate through the dataframe, and find corresponding endpoint
        #TODO 2: return endpoint
        #TODO 3: see if you can access the .tsv file

