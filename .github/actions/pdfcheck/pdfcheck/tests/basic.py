""".. py:module:: pdfcheck.tests.basic

Basic tests"""

import pytest


def test_annotations(pdf_document):
    """
    Test that there are no annotations.
    """
    for page in pdf_document:
        annotations = list(page.annots())
        assert not annotations, "Document has no annotations"
