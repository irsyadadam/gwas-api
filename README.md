![hello](https://img.shields.io/badge/Author-Irsyad-blue) 
![GitHub last commit](https://img.shields.io/github/last-commit/irsyadadam/gwas-api)
![GitHub](https://img.shields.io/github/license/irsyadadam/gwas-api)
![Build](https://img.shields.io/badge/build-passing-green)
# GWAS Catalog API Wrapper

Wrapper Class takes in a query string and creates a directory that will host all summary statistics of all potential GWAS studies associated with that query. 

Object will then extract all GWAS Catalog IDs that are associated with query, and dowload summary statistics in order of the reponses from the endpoint. 



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
## Data Preprocessing

The final GWAS summary statistics should be in the following format:

```
CHR     BP      SNP             P           N
1       717587  rs144155419     0.453345    279949
1       740284  rs61770167      0.921906    282079
1       769223  rs60320384      0.059349    281744
```

-------