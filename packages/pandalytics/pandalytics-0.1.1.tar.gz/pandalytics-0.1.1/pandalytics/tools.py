from dotenv import load_dotenv
import anthropic

from pandalytics.shell import PythonShell
from  pandalytics.templates.code_generation_prompt import PREFIX, FORMAT_INSTRUCTIONS, SUFFIX


## abstraction of anthropic
## for re-usability
def anthropic_client(system_prompt: str, user_prompt: str):
    load_dotenv()
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        temperature=0,
        system=system_prompt,
        max_tokens=1024,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return next(
        (block.text for block in message.content if hasattr(block, "text")),
        None,
    )


## function for tool
def pandas_executor(file_path: str, query: str, metadata: str):
    system_prompt = PREFIX + "\n" + FORMAT_INSTRUCTIONS
    user_prompt = SUFFIX.format(metadata=metadata, query=query, file_path=file_path)

    pandas_code = anthropic_client(system_prompt=system_prompt, user_prompt=user_prompt)
    code = pandas_code.strip("`")[6:]

    pandas_shell = PythonShell()
    pandas_shell.execute_code(code=code)

    if pandas_shell.get_error() != "":
        return code, pandas_shell.get_error()

    return code, pandas_shell.get_output()


tool = [
    {
        "name": "pandas_executor",
        "description": "Generate and execute the pandas code",
        "input_schema": {
            "type": "object",
            "properties": {
                "file": {
                    "type": "string",
                    "description": "The file path of csv file containing the data, e.g. records.csv, movies.csv, ratings.csv",
                },
                "query": {
                    "type": "string",
                    "description": "The user query to get the code, e.g. Give me the top 5 countries by sales?",
                },
                "metadata": {
                    "type": "string",
                    "description": "The metadata about the pandas dataframe.",
                },
            },
            "required": ["file_path", "query", "metadata"],
        },
    }
]
