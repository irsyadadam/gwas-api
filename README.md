![hello](https://img.shields.io/badge/Author-Irsyad-blue) 
![GitHub last commit](https://img.shields.io/github/last-commit/irsyadadam/gwas-api)
![GitHub](https://img.shields.io/github/license/irsyadadam/gwas-api)
![Build](https://img.shields.io/badge/build-passing-green)
# GWAS Catalog API Wrapper

The parameters of this wrapper class are an empty directory that constains a single query file from https://www.ebi.ac.uk/gwas/downloads/summary-statistics.
The instance will then extract all available files corresponding to that query file and place it into the respective directory.


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
usage: main.py [-h] [--folder FOLDER]

download all the gwas files given a gwas query from gwas catalog

optional arguments:
  -h, --help     show this help message and exit
  --folder FOLDER  folder to go through and see query file, should only have a csv in it
```

Example Usage:

The following command will search for the <code>heart/</code> folder for a query file, and download all of the gwas files associated with the term "heart". This will only happen if the query file is searched with the term "heart".

```
python3 DOWNLOAD_GWAS.py --folder heart
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