![hello](https://img.shields.io/badge/Author-Irsyad-blue) 
![GitHub last commit](https://img.shields.io/github/last-commit/irsyadadam/gwas-api)
![GitHub](https://img.shields.io/github/license/irsyadadam/gwas-api)
![Build](https://img.shields.io/badge/build-failed-red)
# GWAS Catalog API Wrapper

Wrapper Class takes in a query string and creates a directory that will host all summary statistics of all potential GWAS studies associated with that query. 

Object will then extract all GWAS Catalogs that are associated with query, and dowload summary statistics in order of the reponses from the endpoint. 



**Project Goals**: 

The goal of this repos is to extract GWAS summary statistics such that the data can be easily streamlined into the sc-DRS pipeline for transcriptomics-genomics integration. 

**Notes**:

HTTP Query Endpoint: 

https://www.ebi.ac.uk/gwas/api/search

HTTP GWAS Summary Statistics Endpoint: 

http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/


----------

## Usage:

Download Dependencies:
```
git clone git@github.com:irsyadadam/gwas-api.git
pip install -r requirements.txt
```

The following are the parameters for the API Wrapper:

```
usage: main.py [-h] [--query QUERY]

download all the gwas files given a gwas query from gwas catalog

optional arguments:
  -h, --help     show this help message and exit
  --query QUERY  query to extract relevant gwas ids
```

Example Usage:

The following command will create a directory names query_heart and download all GWAS summary statistics of GWAS studies correlating to the query "heart".

```
python3 main.py --query heart
```

------------

**TODOs**
1. utils.datapull lines 85 - 87: finish finding proper endpoint given gwas id
2.  utils.datapull line 30: see if endpoint can be accessed properly from master ftp direrctory
3. utils.data_pull line 18: create an iterator to access the gwas id list in a query folder
4. fix the problem with wget slow