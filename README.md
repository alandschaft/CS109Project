## Clinical Trials Analysis

Web Site: http://alandschaft.github.io/CS109Project/

### CS109Project

The repository of the final project for the course "CS109 Data Science" at Harvard:

http://cs109.github.io/2015/

### The problem

Information overloading is a common problem when searching for clinical trials. The current search engines available for clinical trials, such as https://clinicaltrials.gov/ , produce too many results that are often not relevant. Because the volume of medical information included in each clinical trial description is high, sorting through them to find suitable trials takes too much time. 

### The Data

Our dataset is a collection of clinical trial descriptions automatically downloaded from clinicaltrials.org web site, using a standard full-text search query. We used two queries in this project: „Seizure“ – that returned more than 1300 results and „Diabetes Type 2“ that returned 7290 search results. 

### Our Goal

Our goal is to develop a prototype for an interactive information retrieval web application. The application shall be proactive and present to the user a set of medical tags that will help the user to filter the long list of results and narrow it to a small set of trials that are highly relevant.


### Technological Highlights


* We used not only standard natural language processing but also 2 well known Medical NLP frameworks:
  * MedEx 
  * MetaMap
* We used Information  retrieval techniques to develop a prototype for an interactive search service and optimize it.
* We developed and deployed as web application with a  usable user interface that facilitates the interactive search.


### Sources

#### IPython notebooks

* **ClinicalTrials_0_Documentation.ipynb** - Plot distribution of inclusion and exclusion criteria
* **ClinicalTrials_1_extract_criteria.ipynb** - automatically query and download data from clinicaltrials.gov, Extract inclusion and exclusion criteria, tag, lemmatize, ngrammize and filter.
* **ClinicalTrials_2_metamap.ipynb** - UMLS documentation, CUIs extraction with MetaMap
* **ClinicalTrials_3_metamap_terms_stats.ipynb** - Plot ditribution of UMLS Semantic Types in the data
* ClinicalTrials_4_clustering.ipynb - Some experiments with clinical trials clustering. We did not pursue this direction further.
* **ClinicalTrials_5_medex.ipynb** - Drug-related data extraction using MedEx
* **ClinicalTrials_6_merge_tags.ipynb** - Merging MetaMap & MedEx datasets
* **ClinicalTrials_7_tag_statistics.ipynb** - Plot MedEx and MetaMap tag frequencies
* **ClinicalTrials_8_optimize_search_algorithm.ipynb** - Monte Carlo simulation of test cases for the web service. Calibration parameters for the web service


