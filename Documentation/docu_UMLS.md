
# Unified Medical Language System (UMLS)

Unified Medical Language System (UMLS) is a complex collection of terms, concepts and relationships retrieved from standard classification. UMLS has been designed by the National Library of Medicine (NLM) in order to facilitate the developers or computer systems to understand the meanings of these terms, concepts and relationships. 

UMLS is comprised of three main components; Metathesaurus consisted of concepts and inter-concept relationships; Semantic Network based on semantic types and semantic network relationships; Lexical resources based on Lexical tools and SPECIALIST LEXICON. Many synonymous terms are clustered into a concept which is followed by choosing one preferred term. This term is then added to Metathesaurus in order to understand the intended meaning of every term in each source vocabulary. Another purpose is to link all the same meaning terms from all the source vocabularies. CUI consists of the letter C and seven digits, for example CUI for headache and adrenal gland diseases is C0018681 and C0001621 respectively.  (Bodenreider, et al., 2004)

The semantic network of the UMLS is an abstraction network consisted of 135 broad high level categories called semantic types and 54 relationships. These semantic types are hierarchically organized in two categories of semantic types; *Entity* and *Event*. One or more semantic types are assigned to every concept in the UMLS. The set of the assigned concepts of the UMLS is the extent of a semantic type. Some concepts are assigned one while other are assigned two or more, therefore, it is possible that the some semantic types contain concepts having various kinds of semantics. (Friedman & Fan, 2008)

For instance, the two concepts **peptide hormone** and **peptide cyclic** receive the semantic type of **_protein_**, **_peptide_** and **_amino acid._** Similarly, **_"Sign or Symptom"_** would cover *angina pectoris, vomiting, insomnia* and *muscle cramp.* For example, the ‘animal’ is a concept that receives semantic type ‘organism’ similarly; *‘enzyme’* receives the semantic type **_Biologically Active substance.’_** More examples of semantic types include ‘Amphibian’ ‘Gene’, ‘Mental Process’ and ‘Laboratory procedure’. Semantic types are assigned at the most specific level available in the Metathesaurus. A relationship between two semantic types can possibly lead to a link between two concepts. (Bathesda, 2009)

UMLS concepts are located in hierarchical relationships of source vocabularies and these relationships are described in one graph with multiple paths rather than multiple trees. This process is conducted using lexical knowledge, semantic pre-processing and UMLS editors. The Semantic types, as broad categories, are assigned to Metathesaurus editors independent of the hierarchical relationships in which these concepts are located. Comprehensive research has been conducted in order to regroup the semantic types into broader classes and to audit the semantic network classifications. The main purpose is to reclassify the UMLS concepts into many broad classes that will prove to be helpful for biomedical text mining tasks. (Bodenreider, 2004)


###References:

Bethesda (MD)., 2009. Semantic Network. UMLS reference Manual , Volume Chapter 5.
Bodenreider, O., 2004. The Unified Medical Language System (UMLS): integrated biomedical terminology. Oxford Journals , 32(1), pp. D267-D270.
Bodenreider, O., Willis, J. & Hole, W., 2004. The Unified Medical Language System; what is it and how to use it?, s.l.: National Library Medicine; Medinfo.
Friedman, C. Fan, J., 2008. Semantic Reclassification of the UMLS concepts. Oxford Journals Bioinformatics , 24(17), pp. 1971-1973.

