import datetime
from dataclasses import dataclass

from bigdata.api.search import ChunkedDocumentResponse
from bigdata.models.document import (
    DocType,
    DocumentChunk,
    DocumentSentence,
    DocumentSentenceEntity,
    DocumentSource,
)


@dataclass
class Document:
    """A document object"""

    id: str
    headline: str
    sentiment: float
    document_type: DocType
    source: DocumentSource
    timestamp: datetime.datetime
    chunks: list[DocumentChunk]
    language: str

    @classmethod
    def from_response(cls, response: ChunkedDocumentResponse) -> "Document":
        source = DocumentSource(
            key=response.source_key,
            name=response.source_name,
            rank=response.source_rank,
        )
        chunks = [
            DocumentChunk(
                text=s.text,
                chunk=s.cnum,
                entities=[
                    DocumentSentenceEntity(e.key, e.start, e.end, e.queryType)
                    for e in s.entities
                ],
                sentences=[DocumentSentence(e.pnum, e.snum) for e in s.sentences],
                relevance=s.relevance,
                sentiment=s.sentiment / 100.0,
            )
            for s in response.chunks
        ]
        document = cls(
            id=response.id,
            headline=response.headline,
            sentiment=response.sentiment / 100.0,
            document_type=response.doc_type,
            source=source,
            timestamp=response.timestamp,
            chunks=chunks,
            language=response.language,
        )
        return document

    def __str__(self) -> str:
        """
        Returns a string representation of the document.
        """
        chunks_repr = "\n".join(f"* {chunk.text}" for chunk in self.chunks)
        return (
            f"Document ID:  {self.id}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Doc type:  {self.document_type.value}\n"
            f"Source:    {self.source.name} ({self.source.rank})\n"
            f"Title:     {self.headline}\n"
            f"Language:  {self.language}\n"
            f"Sentiment: {self.sentiment}\n"
            f"Sentence matches:\n{chunks_repr}"
        )
