#to pull from the api
import requests

#to parse data
import pandas as pd
import numpy as np
import ast

#iteration tracking
from tqdm import tqdm

#downloading
#import wget


class download_gwas_summary_stats:
    def __init__(self, index: str):
        self.index = self.parse_index(index)
        #TODO: get an iterator that iterates through the list and then calls def extract_gwas for everything in the list
        #IMPLEMENT IT IN self.index

    #MAIN FUNCTION
    def extract_gwas(self, GWAS_ID) -> None:
        """
        grabs .tsv summary statistics associated with gwas id

        ARGS:
            GWAS_ID is the gwas id of the research
        
        RETURNS: 
            None
        """

        #get the url
        endpoint = self.find_endpoint(GWAS_ID) + "/"

        url = 'http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/' + endpoint

        #check the response
        response = requests.get(url=url)

        #if response.code == 200:

        #get the link using def extract_link
        #TODO: ERROR HEREEEE, GO TO LINE 63 TO SEARCH FOR THE CASE HAT ENDPOINT IS A RANGE
        link = url + "/" + self.extract_link(response)
        
        print(link)
        #TODO: WGET IS SLOOWWWWWW (~2 hours to download)
        #wget.download(link)

    
    def extract_link(self, response: requests.Response) -> str:
        """
        extracts the link from a response from def extract_gwas

        ARGS: 
            response is the http response object

        RETURNS:
            string associated with the link in the response object
        """

        
        #TODO: 
        # - if endpoint is a range, look throught the range
        # - if endpoint is single number, just go to the endpoint and extract 
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
        df = pd.read_csv("gwas_catalog_index/index.csv", header = 0)

        #get the index
        ID = int(GWAS_ID[4:])

        endpoint = ""

        #iterate through the id range column
        for i in range(len(df["id_range"])):

            range_ids = ast.literal_eval(df["id_range"][i])
            # CASE1: if the id is in the range column, and range column only has 1 variable
            if len(range_ids) == 1 and range_ids[0] == ID:  
                endpoint = df["endpoints"][i]
                print("%s endpoint found" % GWAS_ID)
                break

            #CASE2 : if id is in between the range, and range column has 2 values
            elif range_ids[0] <= ID <= range_ids[1]:
                endpoint = df["endpoints"][i]
                print("%s endpoint found" % GWAS_ID)
                break
        
        if not endpoint:
            print("WARNING: %s endpoint not found" % GWAS_ID)

        return endpoint

        
    


