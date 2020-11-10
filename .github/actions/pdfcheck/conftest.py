import fitz
import pytest

import os.path

"""
Configuration for PDF tests.
"""


def pytest_addoption(parser):
    parser.addoption(
        "--pdf",
        action="store",
        type=str,
        required=True,
        nargs="+",
        help="absolute path to the PDF that tests will run on (as a list of path parts)",
    )


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.pdf
    if "pdf" in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("pdf", [option_value])


@pytest.fixture(scope="function")
def pdf_document(pdf):
    """
    This fixture opens the PDF document for reading,
    and closes the file when the fixture goes out of scope.
    """
    pdf_path = os.path.join("/", *pdf)

    assert pdf_path
    pdf_document = fitz.open(pdf_path)

    yield pdf_document
    pdf_document.close()
