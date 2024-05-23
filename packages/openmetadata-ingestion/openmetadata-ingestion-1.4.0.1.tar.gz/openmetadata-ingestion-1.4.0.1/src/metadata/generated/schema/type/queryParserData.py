# generated by datamodel-codegen:
#   filename:  type/queryParserData.json
#   timestamp: 2024-05-23T06:46:22+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class ParsedData(BaseModel):
    tables: List[str] = Field(..., description='List of tables used in query')
    databaseName: Optional[str] = Field(
        None, description='Database associated with the table in the query'
    )
    joins: Optional[Dict[str, Any]] = Field(
        None,
        description='Maps each parsed table name of a query to the join information',
    )
    sql: str = Field(..., description='SQL query')
    query_type: Optional[str] = Field(None, description='SQL query type')
    exclude_usage: Optional[bool] = Field(
        None,
        description='Flag to check if query is to be excluded while processing usage',
    )
    serviceName: str = Field(
        ..., description='Name that identifies this database service.'
    )
    userName: Optional[str] = Field(
        None, description='Name of the user that executed the SQL query'
    )
    date: Optional[str] = Field(None, description='Date of execution of SQL query')
    databaseSchema: Optional[str] = Field(
        None, description='Database schema of the associated with query'
    )
    duration: Optional[float] = Field(
        None, description='How long did the query took to run in milliseconds.'
    )


class QueryParserData(BaseModel):
    class Config:
        extra = Extra.forbid

    parsedData: Optional[List[ParsedData]] = None
