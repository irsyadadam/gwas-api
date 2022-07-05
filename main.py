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
    parser.add_argument("--folder", type=str, help="folder to go through and see query file, should only have a csv in it", default="")
    args = parser.parse_args()

    #check if proper parameters
    assert type(args.folder) == str


    print("starting gwas catalog api wrapper")
    print("folder: ", args.folder)

    folder_name = args.folder

    if os.listdir(folder_name) == []:
        print("query_file not found")
        exit()


    query_file = "%s/%s" % (folder_name, os.listdir(folder_name)[0])
    index = pd.read_csv(query_file)["Study accession"].tolist()

    print("query_file found:", query_file)

    print("\n-------------------------------------\n")

    print("downloading summary statistics in", folder_name)

    date = datetime.now().strftime("_%H_%M_%d_%m_%Y")
    log_name = folder_name + "/" + folder_name + date + ".log"
    print("log file %s \n" % log_name)
    logging.basicConfig(filename = log_name, format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()

    
    downloader = download_gwas_summary_stats(index, logger, folder_name)


