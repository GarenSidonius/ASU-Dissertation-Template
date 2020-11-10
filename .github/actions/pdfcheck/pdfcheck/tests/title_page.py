""".. py:module:: pdfcheck.tests.title_page

Test content and formatting in title page"""

import datetime
import re
import warnings

import pytest
from titlecase import titlecase

import pdfcheck.titlepage


@pytest.fixture(scope="function")
def title_page(pdf_document):
    """
    This fixture provides the title page as a
    :py:class:`pdfcheck.titlepage.TitlePage`
    """
    return pdfcheck.titlepage.TitlePage(page=pdf_document.loadPage(page_id=0))


def test_title(title_page):
    """
    Test that the title is capitalized correctly.
    """
    title = title_page.title.one_line()
    assert titlecase(title), "Title is titlecase"


def test_by(title_page):
    """
    Test that the title is followed by exactly "by".
    """
    assert title_page.by.one_line() == "by", 'The word "by" is correct'


def test_author(title_page):
    """
    Test that the author is provided.
    """
    assert title_page.title.one_line(), "Author is provided"


def test_description(title_page):
    """
    Test that the description matches

        A [Dissertation] Presented in Partial Fulfillment
        of the Requirements for the Degree
        [Doctor of Philosophy]

    where "Dissertation" can also be "Thesis" and "Doctor of Philosophy" is
    unconstrained due to the variety of degrees offered by Arizona State University.

    """
    if len(title_page.description.text_blocks) == 1:
        description = title_page.description.text_blocks[0].text
    else:
        description = "".join(map(lambda x: x.text, title_page.description.text_blocks))

    regex = "\n".join(
        [
            "^A (?:Dissertation|Thesis) Presented in Partial Fulfillment",
            "of the Requirements for the Degree",
            "(.*?)",
        ]
    )

    assert re.match(regex, description), "Description is valid"


def test_approval_by(title_page):
    """
    Test that the approval by text matches

        Approved [Month] [Year] by the
        Graduate Supervisory Committee:

    where "Month" is the capitalized, full month name (e.g., April)
    and "Year" is the four-digit year (e.g., 2020)
    """

    text = title_page.approval_by.text_blocks[0].text.rstrip()

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    regex = r"\n".join(
        [
            r"^Approved (?P<month>\w{1,})\s(?P<year>\d{4}) by the",
            r"Graduate Supervisory Committee:$",
        ]
    )
    p = re.compile(regex)
    m = p.search(text)

    assert m.group(0) == text, "Approval by string is valid"
    assert m.group("month") in months, "Approval by month is valid"
    assert int(m.group("year")) >= 2020, "Approval by year is valid"


def test_committee(title_page):
    """
    Test that the list of committee members handles the "Chair" and
    "Co-Chair designations correctly"

    Currently no test for the numbers of committee members (minimum or maximum)
    """

    # Collect all committee members into a single text string,
    # separated by new line characters
    text = "\n".join(map(lambda x: x.text, title_page.committee.text_blocks))

    # there may be double line returns given how the lines were joined above
    # get committee members in a list
    members = text.splitlines()

    # rough match to detect whether chair or co-chair
    p_chair = re.compile(r"Chair$", re.IGNORECASE)
    p_cochair = re.compile(r"Co-?Chair$", re.IGNORECASE)

    # check whether there is just one chair or co-chairs
    if p_chair.search(members[0]):
        has_chair = True
    else:
        has_chair = False

    # exact match for correct output; use these in tests
    p_chair = re.compile(r", Chair$")
    p_cochair = re.compile(r"Co-?Chair$")

    if has_chair:
        # first member is always the chair
        assert p_chair.search(members[0]), "First member is noted as chair"
        # none of the remaining members are chairs or co-chairs
        for member in members[1:]:
            assert not p_chair.search(member), "Other member is not noted as chair"
            assert not p_cochair.search(member), "Other member is not noted as co-chair"
    else:
        # first and second members are co-chairs
        assert p_cochair.search(members[0]), "First member is noted as co-chair"
        assert p_cochair.search(members[1]), "Second member is noted as co-chair"
        # none of the remaining members are chairs or co-chairs
        for member in members[2:]:
            assert not p_chair.search(member), "Other member is not noted as chair"
            assert not p_cochair.search(member), "Other member is not noted as co-chair"


def test_university(title_page):
    """
    Test that the university line is exactly "ARIZONA STATE UNIVERSITY".
    """
    expected = "ARIZONA STATE UNIVERSITY"
    assert (
        title_page.university.one_line() == expected
    ), f'The university on the title page is "{expected}"'


def test_date(title_page):
    """
    Test that the graduation date matches

        [Month] [Year]

    where "Month" can be "May", "August", or "December"
    and "Year" is the four-digit year (e.g., 2020)
    """

    text = title_page.date.one_line()

    months = [
        "May",
        "August",
        "December",
    ]

    p = re.compile(r"^(?P<month>\w{1,})\s(?P<year>\d{4})$")
    m = p.search(text)

    assert m.group(0) == text, "Graduation date string is valid"
    assert m.group("month") in months, "Graduation month is valid"
    grad_year = int(m.group("year"))
    assert grad_year >= 2020, "Graduation year is valid"

    this_year = datetime.date.today().year
    if grad_year != this_year:
        message = (
            f"The graduation year ({grad_year}) does not match "
            f"the current year ({this_year})"
        )
        warnings.warn(message, UserWarning)


def test_horizontal_alignment(title_page):
    """
    Test that all text blocks are centered.
    """
    assert title_page.is_horizontally_centered(), "Content is centered"


def test_vertical_alignment(title_page):
    """
    Test vertical spacing between blocks.

    The title, "by" text, and author are double spaced.
    Then, there are five single-spaced line returns to the description text.
    The "approved by" text and commitee members taken together should appear
    halfway between the description text and the university name.
    The university name and date are double spaced (page 5).
    """
    pass
