**RiskDB-LLM**

Welcome to RiskDB-LLM! This is a tool designed for building domain-specific biomedical databases, particularly tailored for processing literature data. With this tool, you can easily create and update your own biomedical database, making it especially suitable for handling large-scale literature data.

**Usage Steps**

1. **Configure PMID List**  
   Before using RiskDB-Agent, you first need to prepare a list of PMIDs. Ensure that the PMID list is saved in the `PMID.txt` format.  

   **Example format of PMID.txt:**  
   ```
   23456789
   34567890
   ```  
   Each PMID should be on a separate line, with no extra spaces or characters.

2. **Obtain ChatGPT-4o API**  
   This tool relies on the ChatGPT-4o API to enable automated data processing. You need to acquire and configure your API key.  
   - Visit OpenAI and register or log into your account.  
   - Obtain the ChatGPT-4o API key and store it in a secure location.  
   - Configure your API key in the tool’s configuration file.

3. **Configure and Run**  
   After preparing `PMID.txt` and configuring the ChatGPT-4o API key, open a command-line terminal and navigate to the RiskDB-Agent folder.  
   Run the following command to start using RiskDB-Agent:  
   ```
   python main.py
   ```

4. **Functionality Description**  
   After running `main.py`, the tool will retrieve publicly accessible biomedical literature from PubMed based on the PMID list and automatically process the text data.

5. **Output Results**  
   The tool will save the generated data in the local directory.
