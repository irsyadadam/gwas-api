#to pull from the api
import requests

#to parse data
import pandas as pd
import numpy as np

#iteration tracking
from tqdm import tqdm

import argparse
import os
import warnings

warnings.filterwarnings("ignore")
from utils.gwas_list_extractor import extracted_lists
from utils.data_pull import download_gwas_summary_stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="download all the gwas files given a gwas query grom gwas catalog")
    parser.add_argument("--query", type=str, help="query to extract relevant gwas ids", default="")
    args = parser.parse_args()

    #check if proper parameters
    assert type(args.query) == str

    extractor = extracted_lists(args.query)
    gwas_lists = extractor.gwas_list

    #write new folder
    folder_name = "query_" + args.query
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    #add the list to the new folder
    file_name = folder_name + "/gwas_id_list.txt"
    with open(file_name, 'w') as file:
        file.write('\n'.join(gwas_lists))

    print("file saved to:", folder_name)
    print("gwas_id list saved to:", file_name)

    print("\n-------------------------------------\n")
    print("downloading gwas files in", folder_name)

    index_file = "gwas_catalog_index/index.txt"
    downloader = download_gwas_summary_stats(index_file)
