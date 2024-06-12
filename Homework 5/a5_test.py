"""
Jaiden Atterbury
CSE 163 AD
04/29/23

Tests the functions for Search. In particular, tests the functions in
docuement.py and search_engine.py.
"""

from cse163_utils import assert_equals
from search_engine import SearchEngine
from document import Document
import math as m


# Define your test functions here!
def test_document() -> None:
    """
    Tests the implementation of the Document class located in document.py.
    """
    # Create the documents pertaining to the created files:
    doc1 = Document("/home/a5_test_files/test_file_1")
    doc2 = Document("/home/a5_test_files/test_file_2")
    doc3 = Document("/home/a5_test_files/test_file_3")

    print("testing document.py:")

    # Testing term_frequency:
    print("Testing term_frequency:")

    # Test a word not in the document:
    assert_equals(0, doc1.term_frequency('hi!'))

    # Test a singular word:
    assert_equals(1/8, doc1.term_frequency('ThiS'))

    # Test a frequent word:
    assert_equals(2/8, doc1.term_frequency('assiGnment'))

    print("Passed all tests!")

    # Testing get_path:
    print("Testing get_path:")

    # Test file 1:
    assert_equals("/home/a5_test_files/test_file_1", doc1.get_path())

    # Test file 2:
    assert_equals("/home/a5_test_files/test_file_2", doc2.get_path())

    # Test file 3:
    assert_equals("/home/a5_test_files/test_file_3", doc3.get_path())

    print("Passed all tests!")

    # Testing get_words:
    print("Testing get_words:")

    # Test file 1:
    assert_equals(['this', 'assignment', 'takes', 'a', 'long', 'time',
                  'fulfilling'], doc1.get_words())

    # Test file 2:
    assert_equals(['time', 'is', 'just', 'a', 'construct', 'it', 'entirely',
                  'meaningless', 'i', 'remember', 'the', 'forgot'],
                  doc2.get_words())

    # Test file 3:
    assert_equals(['meaningless', 'time'], doc3.get_words())

    print("Passed all tests!")

    # Testing __str__:
    print("Testing __str__")

    # Test file 1:
    assert_equals("Document(/home/a5_test_files/test_file_1, words: 8)",
                  str(doc1))

    # Test file 2:
    assert_equals("Document(/home/a5_test_files/test_file_2, words: 16)",
                  str(doc2))

    # Test file 3:
    assert_equals("Document(/home/a5_test_files/test_file_3, words: 4)",
                  str(doc3))

    print("Passed all tests!")

    print("document.py testing complete!")


def test_search_engine() -> None:
    """
    Tests the implementation of the SearchEngine class located in
    search_engine.py.
    """
    # Get the directory name and SearchEngine for testing:
    dir_name = "/home/a5_test_files/"
    test_engine = SearchEngine(dir_name)

    print("Testing search_engine.py:")

    # Testing _calculate_idf:
    print("Testing _calculate_idf:")

    # Test file 1:
    assert_equals(m.log(3 / 3), test_engine._calculate_idf('time'))

    # Test file 2:
    assert_equals(m.log(3 / 2), test_engine._calculate_idf('meaningless!'))

    # Test file 3:
    assert_equals(m.log(3 / 1), test_engine._calculate_idf('CONSTRUCT'))

    print("All tests passed!")

    # Testing __str__:
    print("Testing __str__:")

    # Test for test_engine:
    assert_equals("SearchEngine(/home/a5_test_files/, size: 3)",
                  str(test_engine))

    print("All tests passed!")

    # Testing search:
    print("Testing search:")

    # Single word query tests:
    print("Testing single word queries:")

    # Test empty query case:
    assert_equals([], test_engine.search("Watermelon"))

    # Test word only in one file:
    assert_equals(["/home/a5_test_files/test_file_2"],
                  test_engine.search("CONSTRUCT"))

    # Test frequent word:
    assert_equals(["/home/a5_test_files/test_file_3",
                  "/home/a5_test_files/test_file_2"],
                  test_engine.search("Meaningless!"))

    # Multiple word query tests:
    print("Testing multiple word queries:")

    # Test empty query case:
    assert_equals([], test_engine.search("hello there!"))

    # Test single document case:
    assert_equals(["/home/a5_test_files/test_file_1"],
                  test_engine.search("long fulfILling"))

    # Test multi document case:
    assert_equals(["/home/a5_test_files/test_file_3",
                  "/home/a5_test_files/test_file_2",
                   "/home/a5_test_files/test_file_1"],
                  test_engine.search("I remember a meaningless"))

    print("All tests passed!")

    print("search_engine testing complete!")


def main():
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
