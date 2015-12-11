# MedEx Tag Extraction

We use MedEx to extract **_drug-related data_**. MedEx is an system for extracting medication and signature information from clinical text developed by Hua Xu, Josh Denny, and Min Jiang at Vanderbilt University. We used MedEx-UIMA 1.3, the open source Java implementation of original Python MedEx based on the Unstructured Information Management Architecture (UIMA) framework, for semantic‐based parsing of drug names and signatures in clinical trials data. You can find more information about the MedEx tool at https://sbmi.uth.edu/ccb/resources/medex.htm. (Xu, et al., 2010)

Medicine data is one of the most important types of clinical data in electronic medical records, but it is often recorded in free-text notes. MedEx natural language processing tool exclusively extracts medication-related information. Not only does the MedEx system identifies drug and signature entities, it also codes the data into a standard representation that is easy to use for further processing. 


The following diagram illustrates the 100 most frequent drugs in our "Seizure" dataset:

/Images/medex-top-terms.png.png

