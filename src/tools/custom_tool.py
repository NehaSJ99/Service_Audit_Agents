from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import pandas as pd
import os

# Define input schema for the tool
class CSVReaderToolInput(BaseModel):
    query: str = Field(..., description="Keyword or column name to search in the support CSV")

# Define the tool
class CSVReaderTool(BaseTool):
    name: str = "CSV Reader Tool"
    description: str = (
        "Reads the support_tickets_data.csv file and returns relevant rows or column data based on the query."
    )
    args_schema: Type[BaseModel] = CSVReaderToolInput

    def _run(self, query: str) -> str:
        file_path = "data/support_tickets_data.csv"
        if not os.path.exists(file_path):
            return f" File not found at {file_path}"

        df = pd.read_csv(file_path)

        # Check if query is a column name
        if query in df.columns:
            return df[query].dropna().head(5).to_string(index=False)

        # Else search within all cell values
        matches = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        return matches.head(5).to_string(index=False) if not matches.empty else "No matching rows found."
        
# Instantiate and expose the tool
csv_tool = CSVReaderTool()

