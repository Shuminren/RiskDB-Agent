import openai
from rich.console import Console
from config import API_KEY, MODEL  # Import API_KEY and MODEL from config.py

console = Console()

# Function to call OpenAI API and get a response
def chat_completion(messages):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            api_key=API_KEY  # Use the API_KEY imported from config
        )
        return response.choices[0].message.content
    except Exception as e:
        console.print(f"[bold red]API request failed: {str(e)}[/]")
        return None

# Function to read PMIDs from a text file
def read_pmid_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pmids = [line.strip() for line in file if line.strip()]
        return pmids
    except FileNotFoundError:
        console.print(f"[bold red]Error: File {file_path} not found.[/]")
        return []
    except Exception as e:
        console.print(f"[bold red]Error reading {file_path}: {str(e)}[/]")
        return []
