""".. py:module:: pdfcheck.tests.font

Test fonts"""

import re
import statistics
from typing import Type
import warnings

import pytest

import pdfcheck.core


@pytest.fixture(scope="function")
def allowed_fonts() -> dict:
    """
    This fixture provides the set of allowed font faces and sizes (page 1)
    """
    return {
        # key is font name; value is font size in points
        "Arial": 10,
        "Century": 11,
        "Garamond": 12,
        "Georgia": 11,
        "Sans Serif": 10,
        "Tahoma": 10,
        "Times New Roman": 12,
        "TimesNewRoman": 12,
        "Verdana": 10,
    }


def test_font(pdf_document, allowed_fonts):
    """
    Test fonts in all pages in document (page 1)

        The Graduate College requires that students use one of the TrueType fonts listed
        below. You should retain the same font and font size throughout your document
        (preliminary, main text, back matter pages); the only exception is endnotes and
        footnotes which may be in a smaller point size.

        Arial               10pt
        Century             11pt
        Garamond            12pt
        *Georgia            11pt
        Sans Serif          10pt
        Tahoma              10pt
        *Times New Roman    12pt
        **TimesNewRoman     12pt
        *Verdana            10pt

        *These fonts are designed for easy screen readability and are highly recommended.

        **TimesNewRoman (with no spaces between words) differs from the traditional font.
        Although it is acceptable to use, your manuscript should not switch between
        TimesNewRoman and Times New Roman as there are distinct differences between
        the two fonts.

    Filenames for fonts are not direct matches for plain-English versions of
    those fonts, so verifying fonts is imprecise.
    """

    # collect all text spans in the document
    doc_spans = list()
    for page in pdf_document:
        page_spans = pdfcheck.core.Page(page=page).text_spans
        doc_spans.extend(page_spans)

    # extract the font for each text span
    fonts = map(lambda x: x["font"], doc_spans)
    # use mode to determine the main font being used in the document;
    # ideally only one, approved font is used in the document
    main_font = statistics.mode(fonts)

    # font file names will not correspond exactly to the font name
    # so look for a rough match
    #
    # key is font name; value is regex to match font name
    font_name_matcher = dict(
        map(
            # anything can come before or after the name
            # spaces in name are optional
            lambda x: (
                x,
                re.compile(r".*" + x.replace(" ", r"\s?") + r".*", re.IGNORECASE),
            ),
            allowed_fonts.keys(),
        )
    )

    approved_font = None
    for font_name in font_name_matcher:
        if re.match(font_name_matcher[font_name], main_font.replace(" ", "")):
            approved_font = font_name
            break

    if approved_font is None:
        message = (
            f"It looks like the main font in the document ({main_font}) "
            "is not in the list of approved fonts: "
            + ", ".join(sorted(allowed_fonts.keys()))
        )
        warnings.warn(message, UserWarning)

    # TODO: identify specific locations of incorrect fonts (i.e., fonts
    # that do not match the main font)

    if approved_font is None:
        message = (
            f"Main font ({main_font}) is not in the list of approved fonts, "
            "so unable to test font size"
        )
        warnings.warn(message, UserWarning)
    else:
        # TODO: identify specific locations of incorrect font sizes
        approved_font_size = allowed_fonts[approved_font]
        for span in doc_spans:
            if span["size"] != approved_font_size:
                message = (
                    f"Font size should be {approved_font_size}, "
                    "but in at least one place, font size is "
                    + str(round(span["size"], 2))
                )
                warnings.warn(message, UserWarning)
                break
