from pubmed_fetcher import setup_driver, fetch_pubmed_data, fetch_pmc_full_text
from data_extractor import extract_sample_data, extract_model_data, process_input
from utils import read_pmid_from_txt, chat_completion
from config import API_KEY, MODEL  # Import API_KEY and MODEL from config.py
import csv
from rich.console import Console

# Configuration
console = Console()

def main():
    console.print("[bold green]Welcome to the Disease Risk Prediction Model Analysis Tool[/]")
    txt_file = 'PMID.TXT'
    pmids = read_pmid_from_txt(txt_file)
    if not pmids:
        console.print("[bold red]Failed to read PMID[/]")
        return

    with open('literature_data.csv', 'a', newline='', encoding='utf-8') as literature_csv, \
         open('sample_data.csv', 'a', newline='', encoding='utf-8') as sample_csv, \
         open('model_information.csv', 'a', newline='', encoding='utf-8') as model_csv:
        
        literature_writer = csv.DictWriter(literature_csv, fieldnames=literature_fields)
        sample_writer = csv.DictWriter(sample_csv, fieldnames=sample_fields)
        model_writer = csv.DictWriter(model_csv, fieldnames=model_fields)
        
        if literature_csv.tell() == 0:
            literature_writer.writeheader()
        if sample_csv.tell() == 0:
            sample_writer.writeheader()
        if model_csv.tell() == 0:
            model_writer.writeheader()

        for pmid in pmids:
            console.print(f"[italic yellow]Processing PMID: {pmid}...[/]")
            driver = setup_driver()
            pubmed_data = fetch_pubmed_data(pmid, driver)
            full_text_data = fetch_pmc_full_text(pubmed_data['pmcid'], driver)
            full_text = full_text_data.get('full_text', "")
            
            literature_writer.writerow({
                'PMID': pmid,
                'Title': pubmed_data.get('title', ''),
                'Authors': pubmed_data.get('authors', ''),
                'First Author Last Affiliation Word': pubmed_data.get('first_author_last_affiliation_word', ''),
                'DOI': pubmed_data.get('doi', ''),
                'Keywords': pubmed_data.get('keywords', ''),
                'Journal Name': pubmed_data.get('journal_name', ''),
                'PMCID': pubmed_data.get('pmcid', ''),
                'Full Text': full_text
            })
            
            prompts = get_prompts()
            prompt1_with_fulltext = prompts[0].replace("[input text]", full_text)
            responses = process_input(prompt1_with_fulltext, prompts)
            
            if len(responses) >= 4:
                response_sample = responses[2]  # Prompt 3
                response_model = responses[3]  # Prompt 4
                
                sample_data = extract_sample_data(response_sample, pmid)
                model_data = extract_model_data(response_model, pmid)
                
                sample_writer.writerow(sample_data)
                model_writer.writerow(model_data)
            
            driver.quit()
            print(f"Information related to PMID {pmid} has been saved.")

if __name__ == "__main__":
    main()
