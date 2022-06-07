#to pull from the api
import requests

#to parse data
import pandas as pd
import numpy as np

#unpack the response
import json


class extracted_lists:
    """
    data type that extracts the list from a query
    
    """
    def __init__(self, query):
        self.endpoint = "https://www.ebi.ac.uk/gwas/api/search?q="
        self.gwas_list = self.response_query(query)


    def extract_queries(self, query : str) -> str:
        """
        extracts all gwas ids associated with a term
        endpoint: https://www.ebi.ac.uk/gwas/api/search
        params: q is the query

        ex)
        https://www.ebi.ac.uk/gwas/api/search?q=heart

        ARGS:
            term is the query term
        
        RETURNS: 
            None
        """
        #get the url
        print("\n-------------------------------------\n")
        url = self.endpoint + query
        print("extracting query:", url)

        #check the response
        try:
            response = requests.get(url=url)
            print("success")
        except:
            print("invalid request: ", response.status_code)
            exit()
        print("\n-------------------------------------\n")
        #response is one huge dictionary full of responses
        return response.text

    def response_query(self, query: str) -> json:
        """
        extracts all the gwas ids that are associated with the query

        ARGS:
            query is the query string

        RETURNS:
            a list of gwas ids associated with the query
        
        """
        #get response
        response = json.loads(self.extract_queries(query))["response"]
        print("num of hits:", response["numFound"])


        #want to use this data only
        hits_data = response["docs"]

        #go through and extract all gwas ids
        gwas_ids = []
        for hit in hits_data:
            #we only want gwas ids
            if hit["id"].isnumeric():
                gwas_ids.append(hit["accessionId"])

        print("num of gwas ids:", len(gwas_ids))
        return gwas_ids

    