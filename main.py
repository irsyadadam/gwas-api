#to pull from the api
from fileinput import filename
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

import logging
from datetime import datetime

from utils.gwas_list_extractor import extracted_lists
from utils.data_pull import download_gwas_summary_stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="download all the gwas files given a gwas query from gwas catalog")
    parser.add_argument("--query", type=str, help="query to extract relevant gwas ids", default="")
    args = parser.parse_args()

    #check if proper parameters
    assert type(args.query) == str

    print("starting gwas catalog api wrapper")
    extractor = extracted_lists(args.query)
    gwas_lists = extractor.gwas_list

    folder_name = "query_" + args.query
    file_name = folder_name + "/gwas_id_list.txt"

    #if folder doenst exist, write to it
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    #if folder exists, do not write again
    if not os.path.exists(file_name):
        #add the list to the new folder
        with open(file_name, 'w') as file:
            file.write('\n'.join(gwas_lists))
        print("gwas_id list saved to:", file_name)

    print("gwas_id list found:", file_name)

    print("\n-------------------------------------\n")

    print("download gwas files in %s?" % file_name)
    val = input("y/n: ")

    if val in ["y", "Y", "yes", "Yes", "YES"]:
        print("\nbeginning download to %s" % folder_name)

        date = datetime.now().strftime("_%H_%M_%d_%m_%Y")
        log_name = folder_name + "/" + folder_name + date + ".log"
        print("log file %s \n" % log_name)
        logging.basicConfig(filename = log_name, format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()

        downloader = download_gwas_summary_stats(file_name, logger)


    elif val in ["n", "N", "no", "NO", "No"]:
        print("download cancelled. finishing")
        exit()

    else:
        print("invalid statement. exiting")
        exit()

