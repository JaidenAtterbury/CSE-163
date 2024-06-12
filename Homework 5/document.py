"""
Jaiden Atterbury
CSE 163 AD
04/29/23

Implements the class Document and its corresponding methods. These methods
include the initiializer __init__ which takes a path to a document and
initializes the document data, a method term_frequency that returns the
tf of a given normalized word in the Document, a method get_path that returns
the path of the file that the Document represents, a method get_words that
returns a list of the unique normalized words in the Document, and lastly a
method __str__ which returns a string representation of the Document.
"""

from cse163_utils import normalize_token


class Document:
    """
    Represents the data in a single web page and includes methods to compute
    term frequency of the document.
    """

    def __init__(self, file_path: str) -> None:
        """
        Takes in a string file_path which represents a path to a document and
        initializes the document data. Works for empty and non-empty files.
        """
        # Initialize the first two fields:
        self._file_path: str = file_path
        self._word_count: int = 0

        # Find the normalized words and corresponding word count and increment
        # the total word count for each word in the given path:
        word_count = {}
        with open(self._file_path) as f:
            lines = f.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    norm_word = normalize_token(word)
                    if norm_word not in word_count:
                        word_count[norm_word] = 0
                    word_count[norm_word] += 1
                    self._word_count += 1

        # Initialze the last field by mapping each normalized word to its
        # given term frequency:
        self._tf_dict: dict[str, float] = {word: count/self._word_count for
                                           word, count in word_count.items()}

    def term_frequency(self, term: str) -> float:
        """
        Returns the term frequency of a given string term, if the term does
        not appear in the Document returns zero. Otherwise returns the term
        frequency of the term computed as: tf(term, document) = count of
        the term in the document / count of words in the document. Casing and
        punctuation don't matter as all terms will be normalized by
        lowercasing text and ignoring punctuation.
        """
        # Normalize the given term:
        normalized_term = normalize_token(term)

        # If the term is not in the Document return zero, if it is return the
        # corresponding term frequency of the given term:
        if normalized_term not in self._tf_dict.keys():
            return 0
        else:
            return self._tf_dict[normalized_term]

    def get_path(self) -> str:
        """
        Returns the path of the file that the Document represents.
        """
        return self._file_path

    def get_words(self) -> list[str]:
        """
        Returns a list of the unique, normalized words in the Document.
        """
        return list(self._tf_dict.keys())

    def __str__(self) -> str:
        """
        Returns a sting representation of the Document in the following
        format: "Document({doc_path}, words: {num_words}), Where doc_path
        is the path of the Document and where num_words is the total number
        of words in the Document.
        """
        return f'Document({self._file_path}, words: {self._word_count})'
