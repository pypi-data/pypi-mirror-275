import anthropic
from pandalytics.tools import tool, pandas_executor
from dotenv import load_dotenv
import pandas as pd
from io import StringIO
from typing import List

from pandalytics.templates.agent_prompt import (
    PREFIX,
    FORMAT_INSTRUCTIONS,
    SUFFIX,
    TEMPLATE_TOOL_RESPONSE,
)


class Pandalytics:
    """
    Main agent class
    """

    def __init__(self, file: List[str]) -> None:
        ## csv file
        self.file = file

        ## to be implemented
        self.pandas_code = None
        self.code_result = None

    ## private function to extract the dataframe context
    def _extract_data_context(self):
        df = pd.read_csv(self.file)

        info_output = StringIO()
        df.info(buf=info_output)

        # Get the string value
        info_output_string = info_output.getvalue()

        context = (
            "The columns of the dataframe are: {}\n\n"
            "The overall information of the dataframe is:\n{}\n\n"
            "The unique values of the columns are:\n{}"
        ).format(df.columns, info_output_string, df.apply(pd.Series.unique))
        return context

    def query(self, query: str):
        """
        Method to execute the the user query

        Args:
            query (str): A user query
        """
        load_dotenv()

        metadata = self._extract_data_context()

        client = anthropic.Anthropic()
        response = client.beta.tools.messages.create(
            model="claude-3-haiku-20240307",
            temperature=0,
            max_tokens=1024,
            system=PREFIX.format(tool=tool) + "\n" + FORMAT_INSTRUCTIONS,
            tools=tool,
            messages=[
                {
                    "role": "user",
                    "content": SUFFIX.format(
                        query=query, file=self.file, metadata=metadata
                    ),
                }
            ],
        )

        if response.stop_reason == "tool_use":
            tool_use = next(
                block for block in response.content if block.type == "tool_use"
            )
            tool_name = tool_use.name
            tool_input = tool_use.input

        if tool_name == "pandas_executor":
            out = pandas_executor(
                tool_input["file"], tool_input["query"], tool_input["metadata"]
            )
            tool_result = out[1]
            self.pandas_code = out[0]
            self.code_result = tool_result

        result = client.beta.tools.messages.create(
            model="claude-3-haiku-20240307",
            temperature=0,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": SUFFIX.format(
                        query=query, file=self.file, metadata=metadata
                    ),
                },
                {"role": "assistant", "content": response.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": TEMPLATE_TOOL_RESPONSE.format(
                                observation=tool_result
                            ),
                        }
                    ],
                },
            ],
            tools=tool,
        )

        return next(
            (block.text for block in result.content if hasattr(block, "text")),
            None,
        )
