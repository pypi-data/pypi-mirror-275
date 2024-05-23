PET dataset reader
######################


A structured interface to interact with the `PET-dataset`_ hosted on huggingface.

.. _PET-dataset: https://huggingface.co/datasets/patriziobellan/PET



Created by `Patrizio Bellan`_.

.. _Patrizio Bellan: https://pdi.fbk.eu/bellan/

=================

Interacting with the data hosted on HuggingFace could be difficult since the data has a strict format. 
For example, getting the list of PET activities of a PET document requires a user to create a custom script that scans the dataset, extracts the words and their NER tags, and combines them. 
In addition, documents are stored in the different, non-always continuous samples in the HuggingFace dataset. Thus, conducting experiments with the `PET Dataset <https://huggingface.co/datasets/patriziobellan/PET>`_ could become a time-intensive operation. 
To alleviate such difficulties, we developed the *PET dataset reader*, a Python package that makes the interaction with the dataset easy.
This package is composed of three different modules: **TokenClassification** module, **RelationExtraction** module, and **ProcessInformation** module.

TokenClassification Module
****************************************

This module is composed of a Python class that allows users to extract structured information at the token levels.
This class has specific methods to get all the PET elements of a specific category. We briefly introduce the principal methods implemented in this module.

#. **GetDocumentNames**  This method returns a list of the document names of the dataset.

#. **GetDocumentText**  This method returns the textual description of a document.

#. **GetTokens**  This method returns the text of a sentence in the form of a list of words of a given sentence ID.

#. **GetNerTagLabels**  This method provides the list of NER tags of a sentence, document, or entire dataset. Since the NER tags are stored as numbers in the dataset, we created specific methods to convert the number into a textual tag. For example, the method \emph{GetPrefixAndLabel} returns the NER marker (B, I, or O) and the tag text (e.g., Activity) of a specific NER tag number.

#. **Statistics**  This method provides the statistics about the PET elements annotated.

In addition, specific methods were implemented to get the list of elements of a given category. For example, the method \emph{GetActivity} returns all the \PETactivity of a specific document or the entire dataset. Similarly, the method \emph{GetActivityData} returns the \PETactivitydata.


RelationExtraction Module
****************************************

This module is composed of a Python class that allows users to extract structured information about the PET relations annotated in the dataset, e.g., *PET Uses* relation.
This class has specific methods to get all the PET relations of a specific category. We briefly introduce the principal methods implemented in this module.

#. **GetNerLabels** This method returns the NER tag IDs of a given document.

#. **GetRelations**  This method provides a list of PET relations of a given document.

#. **GetSentencesWithIdsAndNerTagLabels** This method provides a user with a list of sentences composed of word tokens and the corresponding NER tags. 

#. **Statistics**  This method provides the statistics about the PET relations.


ProcessInformation Module
****************************************
This module contains the methods developed to obtain a structured representation of a document in the form of a graph, e.g., in the form of a Directly Follows Graph.
The module has six main methods:

#. **GetRawActivityLabels** returns the activity labels (PET activity + PET Acitity Data) as their are annotated in the text.


#. **GetDFG** returns the directlyfollows graph representation of the annotations of a document. This graph is composed of behavioral elements only.

#. **GetKG_DFGActivityData** provides the DFG representation of a document enhanced with the \PETactivitydata elements.

#. **GetKG_DFGPerformsActors** provides the DFG graph representation of a document enhanced with the \actorperformer information.

#. **GetPerformsActors** returns a graph representation of the DFG graph of a document enhanced with \actorperformer relations.

#. **GetKnowledgeGraph** returns a graph representation of a document representing the information about the behavioral elements, the activity data elements, and the actor performer elements.



How to Load the PET dataset 
*********************************************

**Token-classification task**

.. code-block:: python
    
    from datasets import load_dataset
    
    modelhub_dataset = load_dataset("patriziobellan/PET", name='token-classification')


**Relations-extraction task**

.. code-block:: python

    from datasets import load_dataset 

    modelhub_dataset = load_dataset("patriziobellan/PET", name='relations-extraction')
..
