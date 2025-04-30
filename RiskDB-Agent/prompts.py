# Define prompts used for extracting data
def get_prompts():
    prompt1 = """
You are a medical research assistant specializing in the study of disease risk prediction models. You provide answers related to medical data analysis, statistical modeling, and other technical issues to help users solve research problems. 

[input text]

Please analyze the above text and extract detailed information related to the study design and its key parameters. Specifically, extract the following elements.
1.	Data Type: Specify whether the data used in the model is prospective, retrospective, or sourced from public databases, etc.
2.	Date Range: Specify the dates of the collected participant data for model development and model validation, including the start and end dates.
3.	Follow-up Time: Specify the follow-up time of the primary cohort, if applicable.
4.	Data Sources: Extract details about the primary data source, such as the institution, database, or registry where the data was collected.
5.	Sample Characteristics: Indicate whether the included samples underwent specific surgeries, treatments, or were in a particular condition (e.g., pregnancy, smoking, or a specific disease state).
6.	Sample Sizes: Extract the sample sizes for the development set and validation set, if mentioned.
7.	Case and Control Numbers: What are the numbers of cases and controls in the development set? What are the numbers of cases and controls in the validation set?
8.	Participant Statistics: Extract demographic information about participants in the development and validation stages, including:
(1)	The number of female participants in the development and validation stages.
(2)	The number of male participants in the development and validation stages.
(3)	The age range of participants in the development and validation stages.
(4)	The average age and standard deviation of participants in the development and validation stages.
(5)	The median age of participants in the development and validation stages.
9.	The racial or ethnic composition of participants in the development and validation stages.
acial or ethnic composition of participants in the development and validation stages.
    """
    prompt2 = """
Continue extracting the following details related to the prediction model from the research. If the paper constructs or evaluates multiple models, please extract the following information for all models.
1.	Disease Name: Specify the disease for which the model is applied.
2.	Model Type: Identify the type of prediction model used (e.g., regression, random forests, deep learning).
3.	Model Development or Validation: Indicate whether the study developed a new model or validated an existing one.
4.	External Validation: State whether external validation was performed.
5.	Prediction Variables: List the variables used in the prediction model.
6.	Report the AUC values, including confidence intervals, for the development stage.
7.	Report the AUC values, including confidence intervals, for the validation stage.
8.	Report the C-index values, including confidence intervals, for the development stage.
9.	Report the C-index values, including confidence intervals, for the validation stage.
10.	Report accuracy values, including confidence intervals, for the development stage.
11.	Report accuracy values, including confidence intervals, for the validation stage.
12.	Report calibration values for the development stage.
13.	Report calibration values for the external validation stage.
14.	Clinical Utility Values: Describe any reported clinical utility values (e.g., net benefit), if provided.
15.	Nomogram Development: Indicate whether a nomogram was constructed based on the model.
16.	Use of TRIPOD Guidelines: State whether the study followed the TRIPOD guidelines and provide details, if applicable.
    """
    prompt3 = """
Please format the extracted information into two columns: one column for the field and one column for the value, ensuring that each field corresponds to only one value. Use the following fields to create the table. Remember, only 23 fields is needed in this table.
1.	Data Type: e.g., prospective data, Retrospective data.
2.	Date Range in the Development Set: e.g., 1992–2008（No months and days information needed）
3.	Date Range in the Validation Set: e.g., 1992–2008（No months and days information needed）
4.	Median Follow-up Time (Years): e.g., 2.95 years (IQR: 1.71–4.83).
5.	Mean Follow-up Time (Years): e.g., 2.95 years (IQR: 1.71–4.83).
6.	Data Sources: e.g., the Kaiser Permanente Washington Breast Cancer Surveillance Consortium (BCSC) registry, the GEO database, the Cancer Screening Program in Urban China (CanSPUC) conducted in Henan Province.
7.	Sample Characteristics: e.g., Pregnant women, ever-smokers.
8.	Number of Cases in the Development Set: e.g., 5,323.
9.	Number of Controls in the Development Set: e.g., 5,323.
10.	Number of Cases in the Validation Set: e.g., 5,323.
11.	Number of Controls in the Validation Set: e.g., 5,323.
12.	Number of Female Participants (Development): e.g., 86 (23%).
13.	Number of Female Participants (Validation): e.g., 86 (23%).
14.	Number of Male Participants (Development): e.g., 545 (40%).
15.	Number of Male Participants (Validation): e.g., 545 (40%).
16.	Age Range (Development): e.g., 22–60.
17.	Age Range (Validation): e.g., 22–60.
18.	Average Age and Standard Deviation (Development): e.g., 74.2 years (SD = 8.2).
19.	Average Age and Standard Deviation (Validation): e.g., 74.2 years (SD = 8.2).
20.	Median Age (Development): e.g., 45.
21.	Median Age (Validation): e.g., 45.
22.	Racial/Ethnic Composition (Development): e.g., White: 80.4%, Asian: 8.8%, Black: 3.9%, Other or multiple races: 5.3%, Unknown: 1.5%.
23.	Racial/Ethnic Composition (Validation): e.g., White: 80.4%, Asian: 8.8%, Black: 3.9%, Other or multiple races: 5.3%, Unknown: 1.5%.
    """
    prompt4 = """
Please extract and format the following information for the models in the study. Organize the data into a two-column or multi-column table, with one column for the field name (e.g., Model Name, Disease Name, etc.) and the remaining columns for values. Each column corresponds to one model's values. If there are multiple models, a multi-column table is needed. The required fields are below.
1.	Model Name: e.g., Tyrer-Cuzick Model, LiFeCRC Score.
2.	Disease Name: e.g., lung cancer.
3.	Model Type: e.g., regression, random forest, support vector machine.
4.	Model Stage: Choose Development or Validation.
5.	External Validation: Yes or No.
6.	Prediction Variables: e.g., age, gender, education, smoking status, blood pressure medication, prevalent stroke.
7.	AUC Values (Development): e.g., 0.767 (95% CI: 0.749–0.786).
8.	AUC Values (Validation): e.g., 0.767 (95% CI: 0.749–0.786).
9.	C-index Values (Development): e.g., 0.767 (95% CI: 0.749–0.786).
10.	C-index Values (Validation): e.g., 0.767 (95% CI: 0.749–0.786).
11.	Accuracy (Development): e.g., 74.8% (95% CI: 71.30% - 78.30%).
12.	Accuracy (Validation): e.g., 74.8% (95% CI: 71.30% - 78.30%).
13.	Calibration Values (Development): e.g., Hosmer-Lemeshow (HL) test p-value = 0.428; O/E ratio ranged from 0.79 to 1.22.
14.	Calibration Values (Validation): e.g., Hosmer-Lemeshow (HL) test p-value = 0.428; O/E ratio ranged from 0.79 to 1.22, or a brief description.
15.	Clinical Utility Values: A brief description.
16.	Nomogram Application: Indicate whether a nomogram was constructed, answer Yes or No.
17.	Use of TRIPOD Guidelines: answer Yes or No.
    """
    return [prompt1, prompt2, prompt3, prompt4]
