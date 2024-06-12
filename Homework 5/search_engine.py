"""
Jaiden Atterbury
CSE 163 AD
04/29/23

Implements the class SearchEngine and its corresponding methods. These methods
include the initiializer __init__ which takes a string directory path and
constructs an inverted index associating each term in the corpus to the list
of documents that contain the term, the private method _calculate_idf that
takes in a string term and returns the inverse document frequency of that
term, the method __str__ which returns a string representation of a
SearchEngine object, and lastly a method search which takes in a string query
and returns a list of documents paths sorted in descending order by the tf-idf
statistic.
"""

from cse163_utils import normalize_token
from operator import itemgetter
from document import Document
import math as m
import os


class SearchEngine:
    """
    Represents a corpus of Document objects and includes methods to compute
    and sort Documents by the tf-idf statistic between each Document and a
    given search query.
    """

    def __init__(self, dir_name: str) -> None:
        """
        Takes in a string path to a directory called dir_name and constructs
        an inverted index associating each term in the corpus to the list of
        Documents that contain the term.
        """
        self._dir_name: str = dir_name
        self._num_of_docs: int = 0
        self._inverted_index: dict[str, list[Document]] = {}

        # For each file in the given directory increment the number of
        # Documents, and create a Document object for the given file_name:
        for file_name in os.listdir(dir_name):
            self._num_of_docs += 1
            file_path = os.path.join(dir_name, file_name)
            document = Document(file_path)

            # For each normalized word in the given Document, if the word
            # isn't already in the inverted index, initialize a list for that
            # word. Finally, add the given Document into the list:
            for word in document.get_words():
                if word not in self._inverted_index:
                    self._inverted_index[word] = []
                self._inverted_index[word].append(document)

    def _calculate_idf(self, term: str) -> float:
        """
        Takes in a string called term and returns the inverse document
        frequency of that term. If the term is not in the corpus, return 0.
        Otherwise, returns the idf as follows: idf(term) = ln(total number of
        documents in the corpus / number of documents containing the term).
        """
        # Normalize the given term:
        normalized_term = normalize_token(term)

        # If the term is not in the corpus return zero, if it is return the
        # corresponding inverse document frequency of the given term:
        if normalized_term not in self._inverted_index:
            return 0
        else:
            return m.log(self._num_of_docs /
                         len(self._inverted_index[normalized_term]))

    def __str__(self) -> str:
        """
        Returns a string representation of a SearchEngine object in the format
        "SearchEngine({path}, size: {num_docs})" where path is the path to the
        directory given in the initializer, and where num_docs is the total
        number of unique Documents in the corpus.
        """
        return f'SearchEngine({self._dir_name}, size: {self._num_of_docs})'

    def search(self, query: str) -> list[str]:
        """
        Takes in a string query that contains one or more terms and returns
        a list of document paths sorted in descending order based on the
        tf-idf statistic. If there are no matching documents, returns an empty
        list. The casing and punctuation of any of the terms in the search
        query doesn't matter as all terms will be normalized by lowercasing
        text and ignoring punctuation.
        """
        # Intialize needed data strictures:
        document_dict = {}
        list_of_docs = []

        # For each term in the query, normalize the term, find the idf of the
        # term, and retrieve all of relevant documents.
        for term in query.split():
            normalized_term = normalize_token(term)
            idf = self._calculate_idf(normalized_term)
            if normalized_term in self._inverted_index.keys():
                list_of_docs = self._inverted_index[normalized_term]

            # For each relevant document, if it is not in the document
            # dictionary, add it to the dictionary. Also add the
            # corresponding tf-idf of that word and document.
            for document in list_of_docs:
                if document not in document_dict:
                    document_dict[document] = 0
                tf_idf = document.term_frequency(normalized_term) * idf
                document_dict[document] += tf_idf

        # Retrieve the list of (Document, tf-idf) tuples:
        list_of_items = document_dict.items()

        # Sort this list in descending order depending on the tf-idf value:
        sorted_list = sorted(list_of_items, key=itemgetter(1), reverse=True)

        # Retrieve the list of file_paths in order of relevance:
        return [tup[0].get_path() for tup in sorted_list]
