import re
from prompts import get_prompts
from utils import chat_completion
from rich.console import Console

console = Console()

# Process input text using the prompts and obtain responses from OpenAI
def process_input(input_text, prompts):
    responses = []
    for i, prompt in enumerate(prompts, 1):
        messages = [{"role": "user", "content": f"{prompt}\n\nInput text:\n{input_text}"}]
        console.print(f"[italic yellow]Processing Prompt {i}...[/]")
        response = chat_completion(messages)
        if response:
            responses.append(response)
            console.print(f"\n[bold magenta]Response {i}:[/]")
            console.print(response)
            console.print("\n" + "-"*50 + "\n")
        else:
            console.print(f"[bold red]Prompt {i} processing failed[/]")
    return responses

# Extract sample data from the response based on predefined fields
def extract_sample_data(response_sample, pmid):
    data_dict = {field: "" for field in sample_fields}
    data_dict["PMID"] = pmid
    lines_sample = response_sample.splitlines()
    
    for line in lines_sample:
        match = re.match(r'\s*\d+\.\s+([^0-9].*?)\s{2,}(.*)', line.strip())
        if match:
            field, value = match.groups()
            if "Data Type" in field:
                data_dict["Data Type"] = value
            elif "Date Range in the Development Set" in field:
                data_dict["Date Range"] = value
            elif "Date Range in the Validation Set" in field:
                data_dict["Date Range (Validation)"] = value
            elif "Median Follow-up Time" in field:
                data_dict["Median Follow-up Time"] = value
            elif "Mean Follow-up Time" in field:
                data_dict["Mean Follow-up Time"] = value
            elif "Data Sources" in field:
                data_dict["Data Sources"] = value
            elif "Sample Characteristics" in field:
                data_dict["Sample Characteristics"] = value
            elif "Number of Cases in the Development Set" in field:
                data_dict["Number of Cases (Development)"] = value
            elif "Number of Controls in the Development Set" in field:
                data_dict["Number of Controls (Development)"] = value
            elif "Number of Cases in the Validation Set" in field:
                data_dict["Number of Cases (Validation)"] = value
            elif "Number of Controls in the Validation Set" in field:
                data_dict["Number of Controls (Validation)"] = value
            elif "Number of Female Participants (Development)" in field:
                data_dict["Female Participants (Development)"] = value
            elif "Number of Female Participants (Validation)" in field:
                data_dict["Female Participants (Validation)"] = value
            elif "Number of Male Participants (Development)" in field:
                data_dict["Male Participants (Development)"] = value
            elif "Number of Male Participants (Validation)" in field:
                data_dict["Male Participants (Validation)"] = value
            elif "Age Range (Development)" in field:
                data_dict["Age Range (Development)"] = value
            elif "Age Range (Validation)" in field:
                data_dict["Age Range (Validation)"] = value
            elif "Average Age and Standard Deviation (Development)" in field:
                data_dict["Avg. Age ± SD (Development)"] = value
            elif "Average Age and Standard Deviation (Validation)" in field:
                data_dict["Avg. Age ± SD (Validation)"] = value
            elif "Median Age (Development)" in field:
                data_dict["Median Age (Development)"] = value
            elif "Median Age (Validation)" in field:
                data_dict["Median Age (Validation)"] = value
            elif "Racial/Ethnic Composition (Development)" in field:
                data_dict["Racial/Ethnic Composition (Development)"] = value
            elif "Racial/Ethnic Composition (Validation)" in field:
                data_dict["Racial/Ethnic Composition (Validation)"] = value

    return data_dict

# Extract model data from the response based on predefined fields
def extract_model_data(response_model, pmid):
    model_data = {field: "" for field in model_fields}
    model_data["PMID"] = pmid
    lines_model = response_model.splitlines()
    
    for line in lines_model:
        match = re.match(r'\s*\d+\.\s+([^0-9].*?)\s{2,}(.*)', line.strip())
        if match:
            field, value = match.groups()
            if "Model Name" in field:
                model_data["Model Name"] = value
            elif "Disease Name" in field:
                model_data["Disease Name"] = value
            elif "Model Type" in field:
                model_data["Model Type"] = value
            elif "Model Stage" in field:
                model_data["Model Stage"] = value
            elif "External Validation" in field:
                model_data["External Validation"] = value
            elif "Prediction Variables" in field:
                model_data["Prediction Variables"] = value
            elif "AUC Values (Development)" in field:
                model_data["AUC Values (Development)"] = value
            elif "AUC Values (Validation)" in field:
                model_data["AUC Values (Validation)"] = value
            elif "C-index Values (Development)" in field:
                model_data["C-index Values (Development)"] = value
            elif "C-index Values (Validation)" in field:
                model_data["C-index Values (Validation)"] = value
            elif "Accuracy (Development)" in field:
                model_data["Accuracy (Development)"] = value
            elif "Accuracy (Validation)" in field:
                model_data["Accuracy (Validation)"] = value
            elif "Calibration Values (Development)" in field:
                model_data["Calibration Values (Development)"] = value
            elif "Calibration Values (Validation)" in field:
                model_data["Calibration Values (Validation)"] = value
            elif "Clinical Utility Values" in field:
                model_data["Clinical Utility Values"] = value
            elif "Nomogram Application" in field:
                model_data["Nomogram Application"] = value
            elif "Use of TRIPOD Guidelines" in field:
                model_data["Use of TRIPOD Guidelines"] = value

    return model_data
