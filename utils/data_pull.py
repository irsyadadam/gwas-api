#to pull from the api
import requests

#to parse data
import pandas as pd
import numpy as np
import ast
import logging

#iteration tracking
from tqdm import tqdm


#downloading
#import wget


"""
Process Hierarchy:
1) on class creation, iterate_through is called, which iterates through gwas id index
2) for every line in gwas id index, self.extract_gwas is called
3) in extract_gwas, find_endpoint is used to extract the endpoint in the BASE FTP SERVER
    - find_endpoint iterates through the index of GWAS Catalog and returns the endpoint in the form of a range of GWAS IDs 
      or a single GWAS ID, whichever is nested in the FTP server
4) extract_gwas then goes though and finds the download link of .tsv file hosting the summary statistics

"""

class download_gwas_summary_stats:
    def __init__(self, index: str, logger):
        self.logger = logger
        self.index = self.iterate_through(index)

    def iterate_through(self, index) -> None:
        self.logger.info("relevant GWAS_ID statistics found")
        with open(index) as f:
            for i in tqdm(f.readlines(), desc = "downloading summary statistics"):
                self.extract_gwas(i)

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
        endpoint = self.find_endpoint(GWAS_ID)
            
        summary_stats_link = ""

        #if endpointis a range of endpoints
        if len(endpoint) > len(GWAS_ID):
            url = 'http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/' + endpoint + "/" + GWAS_ID + "/"
            response = requests.get(url=url)
            if response.status_code == "200":
                summary_stats_link = url + self.extract_link(response)
                self.logger.warning("%s summary statistics found" % GWAS_ID)
            else:
                self.logger.warning("%s summary statistics not available in ftp" % GWAS_ID)


        #else if single gwas id endpoint
        elif endpoint == GWAS_ID:
            url = 'http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/' + endpoint + "/"
            response = requests.get(url=url)
            if response.status_code == "200":
                self.logger.warning("%s summary statistics found" % GWAS_ID)
                summary_stats_link = url + self.extract_link(response)
            else:
                self.logger.warning("%s summary statistics not available in ftp" % GWAS_ID)


        if (summary_stats_link):
            print("final link", summary_stats_link)


        #TODO: WGET IS SLOOWWWWWW (~2 hours to download)
        #wget.download(link)

    @classmethod
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
                break

            #CASE2 : if id is in between the range, and range column has 2 values
            elif len(range_ids) > 1 and range_ids[0] <= ID <= range_ids[1]:
                endpoint = df["endpoints"][i]
                break

        return endpoint

        
    


