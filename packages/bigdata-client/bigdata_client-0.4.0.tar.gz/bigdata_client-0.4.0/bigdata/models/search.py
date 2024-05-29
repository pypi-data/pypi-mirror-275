from typing import Optional, Union

from pydantic import BaseModel, Field

from bigdata.enum_utils import StrEnum

OLDEST_RECORDS = 2000


class ExpressionOperation(StrEnum):
    IN = "in"
    ALL = "all"
    GREATER_THAN = "greater-than"
    LOWER_THAN = "lower-than"
    BETWEEN = "between"


class ExpressionTypes(StrEnum):
    AND = "and"
    OR = "or"
    NOT = "not"
    KEYWORD = "keyword"
    SIMILARITY = "similarity"
    ENTITY = "entity"
    SOURCE = "source"
    TOPIC = "rp_topic"
    LANGUAGE = "language"
    WATCHLIST = "watchlist"
    DATE = "date"
    CONTENT_TYPE = "content_type"
    SENTIMENT = "sentiment"
    SECTION_METADATA = "section_metadata"
    DOCUMENT_TYPE = "document_type"
    REPORTING_PERIOD = "reporting_period"
    DOCUMENT = "document"


class FiscalQuarterValidator(BaseModel):
    value: int = Field(ge=1, le=4)

    def get_string(self):
        return f"FQ{self.value}"


class FiscalYearValidator(BaseModel):
    value: int = Field(ge=OLDEST_RECORDS)

    def get_string(self):
        return f"{self.value}FY"


class Expression(BaseModel):
    type: ExpressionTypes
    value: Union[list[Union[str, float, "Expression"]], str, float, "Expression"]
    operation: Optional[ExpressionOperation] = None

    @classmethod
    def new(cls, etype: ExpressionTypes, values: Optional[list[str]]) -> "Expression":
        if not values:
            return None
        return cls(type=etype, operation=ExpressionOperation.IN, value=values)


class DocumentType(StrEnum):
    ALL = "all"
    FILINGS = "filings"
    TRANSCRIPTS = "transcripts"
    NEWS = "news"
    FILES = "files"


class SortBy(StrEnum):
    """Defines the order of the search results"""

    RELEVANCE = "relevance"
    DATE = "date"


class Ranking(StrEnum):
    STABLE = "stable"
    EXPERIMENTAL = "experimental"
    SIMILARITY = "similarity"


class SearchChain(StrEnum):
    DEDUPLICATION = "deduplication"
    ENRICHER = "enricher"  # NO LONGER USED
    DEFAULT = "default"  # NO LONGER USED?
    CLUSTERING = "clustering"


class SearchPagination(BaseModel):
    limit: int = Field(default=100, gt=0, lt=1001)
    cursor: int = Field(default=1, gt=0)


class SearchSharePermission(StrEnum):
    READ = "read"
    UNDEFINED = "undefined"
