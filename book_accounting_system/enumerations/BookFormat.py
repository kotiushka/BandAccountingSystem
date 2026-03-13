from enum import Enum, StrEnum
from typing import Self


class BookFormat(StrEnum):
    # Physical book formats
    HARDCOVER = "Hardcover"
    A = "A"
    B = "B"

    # Digital formats
    EPUB = "EPUB"
    MOBI = "MOBI"
    PDF = "PDF"

    # Audio formats
    CD_AUDIO = "CD"
    AUDIOBOOK = "Audiobook"

    @classmethod
    def _missing_(cls, value) -> Self | None:
        if isinstance(value, str):
            value = value.strip().lower()
            for member in cls:
                if member.value.lower() == value:
                    return member
        return None
