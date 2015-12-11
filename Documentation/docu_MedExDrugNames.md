# One Active Ingredient, Many Drug Names

When a substance is first discovered, it is given a chemical name (eg. 5-amino-2-hydroxybenzoic acid) which describes its molecular structure. When a drug is approved by the FDA in the United States, it is assigned an official generic name and a proprietary brand name to be used exclusively by the company that requested approval for the drug. Ater the drug patent expires, other companies can manufacture and market the same drug by its generic name or create a new brand name. It is also possible for a patent drug produced by the a company to have multiple names in different countries. 

For example, an anti-diabetic drug has a global generic name "Acarbose". It is also known by the brand name "Prandase" in Canada, "Precose" in America, and "Glucobay" in Europe and China, all manufactured and sold by Bayer Pharmaceuticals. These 4 names refers to the same drug.

When these 4 different names are processed by MedEx, they are all listed as "Acarbose" in the generic name field of MedEx processed output. Our analysis shows the "Seizure" clinical trials dataset refers to drugs by their generic names much more often than brand names.




MedEx also identifies the RxNorm CUI for the corresponding generic drug ingredients. It also identifies UMLS CUI code, however; in practice we found MedEx has a much higher probablity of identifying the RxNorm CUI.


### References:

* Xu H, Stenner SP, Doan S, Johnson KB, Waitman LR, Denny JC. MedEx: a medication information extraction system for clinical narratives. J Am Med Inform Assoc. 2010 Jan-Feb;17(1):19–24.

* Xu H, Jiang M, Oetjens M, et al. Facilitating pharmacogenetic studies using electronic health records and natural-language processing: a case study of warfarin. J Am Med Inform Assoc. 2011 Jul-Aug;18(4):387–391.

* Jiang M, Wu Y, Shah A, Priyanka P, Denny JC, Xu H. Extracting and standardizing medication information in clinical text – the MedEx-UIMA system. AMIA Summits on Translational Science Proceedings. 2014;2014:37-42.

* "Generic Drugs" (http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/SmallBusinessAssistance/ucm127615.pdf), Center for Drug Evaluation and Research, U.S. Food and Drug Administration.