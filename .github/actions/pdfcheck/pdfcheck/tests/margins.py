""".. py:module:: pdfcheck.tests.margins

Test page size and spacing attributes"""


from typing import Type
import warnings

import fitz
import pytest

import pdfcheck.core
from pdfcheck.helper import inches_2_points


@pytest.fixture(scope="function")
def paper_size_coordinates() -> Type[pdfcheck.core.BoundingBox]:
    """
    This fixture provides the paper size as bounding box (tuple of four values)
    in points
    """

    # define set of paper sizes
    paper_sizes = {
        "letter": {
            "width": 8.5,
            "length": 11,
        },
    }

    # select paper size
    paper_size = "letter"

    paper_dimensions = paper_sizes[paper_size]

    # units are in points
    paper_size_coordinates = [
        0.0,
        0.0,
        inches_2_points(paper_dimensions["width"]),
        inches_2_points(paper_dimensions["length"]),
    ]
    return pdfcheck.core.BoundingBox.from_rect(paper_size_coordinates)


@pytest.fixture(scope="function")
def margins() -> dict:
    """
    This fixture provides the margins in inches
    """
    return {
        "left": 1.25,
        "right": 1.25,
        "top": 1.00,
        "bottom": 1.00,
    }


def test_paper_size(pdf_document, paper_size_coordinates):
    """
    Test paper size for all pages in document

    There is no stated requirement about paper size in the format manual, but
    these tests assume US letter is required.
    """
    page_number = 1
    for page in pdf_document:

        # this is just a warning for now; depending on use cases, it could
        # become an error in the future
        if page.CropBox != page.MediaBox:
            message = (
                f"Page {page_number} MediaBox does not match CropBox, "
                "so it may appear differently when printed"
            )
            warnings.warn(message, UserWarning)

        # this is just a warning for now; depending on use cases, it could
        # become an error in the future
        if page.CropBoxPosition != fitz.Point(0, 0):
            warnings.warn(f"Page {page_number} is displaced", UserWarning)

        # this is just a warning for now; depending on use cases, it could
        # become an error in the future
        if page.rotation != 0:
            warnings.warn(f"Page {page_number} is rotated", UserWarning)

        obj = pdfcheck.core.Page(page=page)
        assert (
            obj.bounding_box == paper_size_coordinates
        ), f"Page {page_number} has wrong size"

        page_number += 1


def test_margins(pdf_document, margins):
    """
    Test margins (page 1)

        Every page of your document must meet the margin requirements of 1.25
        inches on the left and right, and 1 inch on the top and bottom.
        All materials including appendices, if you choose to include them,
        must meet the margin requirements.

    """
    page_number = 1
    for page in pdf_document:

        obj = pdfcheck.core.Page(page=page)
        page_bounding_box = obj.bounding_box

        # margins are allowed to exceed boundaries by this amount (in points)
        tolerance = 2.5

        # collect each bounding box coordinate into a list
        # (it seems like it will be more efficient to do
        # one `min` or `max` calculation for each type of coordinate
        # than four comparisons for each bounding box to continually
        # update the min/max value for that coordinate)
        coordinates = {
            "left": list(),
            "upper": list(),
            "right": list(),
            "lower": list(),
        }
        for text_block in obj.text_block_collection.text_blocks:
            coordinates["left"].append(text_block.left)
            coordinates["upper"].append(text_block.upper)
            coordinates["right"].append(text_block.right)
            coordinates["lower"].append(text_block.lower)

        min_left_coordinate = page_bounding_box.left + inches_2_points(margins["left"])
        assert (
            min(coordinates["left"]) >= min_left_coordinate - tolerance
        ), f"Some text violates the left margin on page {page_number}"

        min_upper_coordinate = page_bounding_box.upper + inches_2_points(margins["top"])
        assert (
            min(coordinates["upper"]) >= min_upper_coordinate - tolerance
        ), f"Some text violates the top margin on page {page_number}"

        max_right_coordinate = page_bounding_box.right - inches_2_points(
            margins["right"]
        )
        assert (
            max(coordinates["right"]) <= max_right_coordinate + tolerance
        ), f"Some text violates the right margin on page {page_number}"

        # increase tolerance slightly
        tolerance = 4
        max_lower_coordinate = page_bounding_box.lower - inches_2_points(
            margins["bottom"]
        )
        assert (
            max(coordinates["lower"]) <= max_lower_coordinate + tolerance
        ), f"Some text violates the bottom margin on page {page_number}"

        page_number += 1
