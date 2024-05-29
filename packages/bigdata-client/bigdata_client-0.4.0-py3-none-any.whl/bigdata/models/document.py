from dataclasses import dataclass
from enum import Enum

from bigdata.query_type import QueryType


@dataclass
class DocumentSource:
    """The source of a document"""

    key: str
    name: str
    rank: int


class DocType(Enum):
    """
    The type of the document.
    """

    NEWS = "news"
    FILINGS = "filings"
    TRANSCRIPTS = "transcripts"
    FILES = "files"


@dataclass
class DocumentSentenceEntity:
    """
    A detection instance of an entity in a sentence
    """

    key: str
    start: int
    end: int
    query_type: QueryType


@dataclass
class DocumentSentence:
    paragraph: int
    sentence: int


@dataclass
class DocumentChunk:
    """
    A chunk of text representing a contextual unit within the document
    """

    text: str
    chunk: int
    entities: list[DocumentSentenceEntity]
    sentences: list[DocumentSentence]
    relevance: float
    sentiment: float
