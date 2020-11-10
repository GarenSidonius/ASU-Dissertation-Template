""".. py:module:: pdfcheck.titlepage

Objects for getting attributes of the title page"""

from functools import cached_property
import re
from typing import Type

import attr

import pdfcheck.core


@attr.s
class TitlePage(pdfcheck.core.Page):
    """
    A class for checking attributes of a title page
    """

    @cached_property
    def title(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for title
        """
        text_blocks = self.text_block_collection.text_blocks

        # the title can take up variable numbers of lines;
        # anything until "by" is the title
        return pdfcheck.core.TextBlockCollection(
            text_blocks=list(text_blocks[0 : self.by.text_blocks[0].index - 1])
        )

    @cached_property
    def by(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for "by"
        """
        match_by = re.compile("^by$", re.IGNORECASE)

        # the title can take up variable numbers of lines
        for text_block in self.text_block_collection.text_blocks:

            # collect the "by" line and exit
            if re.match(match_by, text_block.text):
                return pdfcheck.core.TextBlockCollection(
                    text_blocks=[
                        text_block,
                    ]
                )

    @cached_property
    def author(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for the author
        """
        text_blocks = self.text_block_collection.text_blocks

        # the author should follow "by"
        return pdfcheck.core.TextBlockCollection(
            text_blocks=[
                text_blocks[self.by.text_blocks[-1].index + 1],
            ]
        )

    @cached_property
    def description(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for the description
        """
        text_blocks = self.text_block_collection.text_blocks

        # the description should be three lines following the author
        description_blocks = [
            text_blocks[self.author.text_blocks[0].index + 1],
        ]

        # text boxes can contain multiple lines; lines tend to be followed by "\n"
        # even when the text box contains only one line, so there need to be at
        # least two line returns to indicate that the text box already has all three
        # lines
        if len(re.findall("\n", description_blocks[0].text)) >= 2:
            # in that case, they have already been captured
            pass
        else:
            # otherwise, grab the next two lines as well
            start = description_blocks[0].index + 1
            end = start + 1
            description_blocks.append(text_blocks[start:end])

        return pdfcheck.core.TextBlockCollection(text_blocks=description_blocks)

    @cached_property
    def approval_by(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for the
        approval by information
        """
        text_blocks = self.text_block_collection.text_blocks

        # the approval_by should follow the description
        return pdfcheck.core.TextBlockCollection(
            text_blocks=[
                text_blocks[self.description.text_blocks[-1].index + 1],
            ]
        )

    @cached_property
    def committee(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for committee members
        """
        text_blocks = self.text_block_collection.text_blocks

        # the committee members should follow the approval_by line and take up
        # all the lines up to the university line;
        # there can be different numbers of committee members
        start = self.approval_by.text_blocks[0].index + 1
        end = self.university.text_blocks[0].index - 1
        if start == end:
            return pdfcheck.core.TextBlockCollection(
                text_blocks=[
                    text_blocks[start],
                ]
            )
        else:
            return pdfcheck.core.TextBlockCollection(
                text_blocks=list(text_blocks[start:end])
            )

    @cached_property
    def university(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for the name of the university
        """
        text_blocks = self.text_block_collection.text_blocks

        # the university should be second to last
        return pdfcheck.core.TextBlockCollection(
            text_blocks=[
                text_blocks[-2],
            ]
        )

    @cached_property
    def date(self) -> Type[pdfcheck.core.TextBlockCollection]:
        """
        :py:class:`pdfcheck.core.TextBlockCollection` for the date
        """
        text_blocks = self.text_block_collection.text_blocks

        # the date should be last
        return pdfcheck.core.TextBlockCollection(
            text_blocks=[
                text_blocks[-1],
            ]
        )
