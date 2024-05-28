import re
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from typing_extensions import Self

from python_text_cleaning.character_mappings.text_cleaning import (
    TEXT_CLEANERS,
    NeStr,
    TextCleaner,
)


class Casing(Enum):
    LOWER = "LOWER"
    UPPER = "UPPER"
    original = "ORIGINAL"

    def _to_dict(self, skip_keys: list[str] | None = None) -> dict[str, str]:
        obj = self
        module = obj.__class__.__module__
        _target_ = f"{module}.{obj.__class__.__name__}"
        # TODO: WTF? why _target_ and _id_ stuff here?
        d = {"_target_": _target_, "value": self.value, "_id_": str(id(self))}
        skip_keys = skip_keys if skip_keys is not None else []
        return {k: v for k, v in d.items() if k not in skip_keys}

    def apply(self, text: str) -> str:
        if self in CASING_FUNS.keys():
            fun = CASING_FUNS[self](text)
        else:  # noqa: RET505
            msg = "unknown Casing"
            raise AssertionError(msg)
        return fun

    @classmethod
    def create(cls, value: str | dict[str, str]) -> Self:
        if isinstance(value, dict):
            value = value["value"]
        elif value.startswith("Casing."):
            value = value.split(".")[1]
        return cls(value)


CASING_FUNS: dict[Casing, Callable[[str], str]] = {
    Casing.UPPER: lambda s: s.upper(),
    Casing.LOWER: lambda s: s.lower(),
    Casing.original: lambda s: s,
}


Letters = NeStr


def upper_lower_text(text: str, casing: Casing = Casing.original) -> str:
    # first upper than check if in vocab actually makes sense for ß, cause "ß".upper()==SS
    return casing.apply(text)


#
# def casing_vocab_filtering(
#     text: str, vocab_letters: list[str], casing: Casing = Casing.original
# ) -> str:
#     return filter_by_lettervocab(casing.apply(text), vocab_letters)


@dataclass
class VocabCasingAwareTextCleaner(TextCleaner):
    casing: str | dict[str, str] | Casing
    text_cleaner_name: str
    letter_vocab: Letters

    @property
    def name(self) -> NeStr:
        assert isinstance(self.casing, Casing)
        return f"{self.casing.name}-{self.text_cleaner_name}"

    def __post_init__(self) -> None:
        if isinstance(self.casing, str):
            self.casing = Casing(self.casing)
        elif isinstance(
            self.casing, dict  # noqa: COM812
        ):  # TODO: somehow Casing gets not deserialized properly!
            self.casing = Casing.create(self.casing["value"])

    def __call__(self, text: str) -> str:
        assert isinstance(self.casing, Casing)
        text = clean_and_filter_text(
            text=text,
            vocab_letters=self.letter_vocab,
            text_cleaner=TEXT_CLEANERS[self.text_cleaner_name],
            casing=self.casing,
        )
        assert "  " not in text, f"{text=}"
        return text


def clean_and_filter_text(
    text: str,
    vocab_letters: str,
    text_cleaner: str | TextCleaner,
    casing: Casing,
) -> str:
    if isinstance(text_cleaner, str):
        text_cleaner = TEXT_CLEANERS[text_cleaner]
    text = clean_upper_lower_text(text, text_cleaner, casing)
    text = filter_by_lettervocab(text, list(vocab_letters))
    return re.sub(
        r"\s\s+",
        " ",
        text,
    )  # \s\s+ -> see jiwer RemoveMultipleSpaces transform


def filter_by_lettervocab(text: str, vocab_letters: list[str]) -> str:
    return "".join([c for c in text if c in vocab_letters or c == " "]).strip(" ")


def clean_upper_lower_text(
    text: str,
    text_cleaner: TextCleaner,
    casing: Casing = Casing.original,
) -> str:
    text = text_cleaner(text).strip(" ")
    return casing.apply(text)


def determine_casing(letter_vocab: Letters) -> Casing:
    more_than_half_is_upper = (
        sum([1 if c.upper() == c else 0 for c in letter_vocab]) > len(letter_vocab) / 2
    )
    return Casing.UPPER if more_than_half_is_upper else Casing.LOWER


if __name__ == "__main__":
    print(Casing.LOWER)  # noqa: T201
