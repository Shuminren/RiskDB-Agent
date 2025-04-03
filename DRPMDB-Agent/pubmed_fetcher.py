from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Setup the web driver for scraping
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Fetch data from PubMed using the provided PMID
def fetch_pubmed_data(pmid, driver):
    url = f"https://www.ncbi.nlm.nih.gov/pubmed/{pmid}"
    driver.get(url)
    
    data = {'pmid': pmid}
    wait = WebDriverWait(driver, 5)
    
    try:
        data['title'] = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'heading-title'))).text.strip()
    except:
        data['title'] = None

    try:
        authors = driver.find_element(By.CLASS_NAME, 'authors-list').text
        data['authors'] = ', '.join(re.sub(r'\s*\d+', '', authors).split(','))
    except:
        data['authors'] = None

    try:
        affiliation = driver.find_element(By.CLASS_NAME, 'affiliation-link').get_attribute('title')
        data['first_author_last_affiliation_word'] = affiliation.split(',')[-1].strip().split()[-1].rstrip('.')
    except:
        data['first_author_last_affiliation_word'] = None

    try:
        data['doi'] = driver.find_element(By.XPATH, '//a[@data-ga-action="DOI"]').text.strip()
    except:
        data['doi'] = None

    try:
        keywords = driver.find_element(By.XPATH, '//p[strong[contains(text(),"Keywords")]]').text
        data['keywords'] = keywords.replace("Keywords:", "").strip().rstrip('.')
    except:
        data['keywords'] = None

    try:
        data['journal_name'] = driver.find_element(By.XPATH, '//meta[@name="citation_publisher"]').get_attribute('content').strip()
    except:
        data['journal_name'] = None

    try:
        pmcid_element = driver.find_element(By.XPATH, '//a[contains(@href, "pmc.ncbi.nlm.nih.gov/articles/PMC")]')
        pmcid_full = pmcid_element.text.strip()
        data['pmcid'] = pmcid_full.replace("PMCID: ", "").strip()
    except:
        data['pmcid'] = None

    return data

# Fetch the full text from PMC using the provided PMCID
def fetch_pmc_full_text(pmcid, driver):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    driver.get(url)
    
    data = {'pmcid': pmcid}
    wait = WebDriverWait(driver, 30)
    
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_source = driver.page_source
        text_content = re.sub(r'<[^>]+>', '', page_source).strip()
        data['full_text'] = text_content
    except Exception as e:
        data['full_text'] = None
        print(f"Error fetching full text: {str(e)}")
    
    return data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Setup the web driver for scraping
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Fetch data from PubMed using the provided PMID
def fetch_pubmed_data(pmid, driver):
    url = f"https://www.ncbi.nlm.nih.gov/pubmed/{pmid}"
    driver.get(url)
    
    data = {'pmid': pmid}
    wait = WebDriverWait(driver, 5)
    
    try:
        data['title'] = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'heading-title'))).text.strip()
    except:
        data['title'] = None

    try:
        authors = driver.find_element(By.CLASS_NAME, 'authors-list').text
        data['authors'] = ', '.join(re.sub(r'\s*\d+', '', authors).split(','))
    except:
        data['authors'] = None

    try:
        affiliation = driver.find_element(By.CLASS_NAME, 'affiliation-link').get_attribute('title')
        data['first_author_last_affiliation_word'] = affiliation.split(',')[-1].strip().split()[-1].rstrip('.')
    except:
        data['first_author_last_affiliation_word'] = None

    try:
        data['doi'] = driver.find_element(By.XPATH, '//a[@data-ga-action="DOI"]').text.strip()
    except:
        data['doi'] = None

    try:
        keywords = driver.find_element(By.XPATH, '//p[strong[contains(text(),"Keywords")]]').text
        data['keywords'] = keywords.replace("Keywords:", "").strip().rstrip('.')
    except:
        data['keywords'] = None

    try:
        data['journal_name'] = driver.find_element(By.XPATH, '//meta[@name="citation_publisher"]').get_attribute('content').strip()
    except:
        data['journal_name'] = None

    try:
        pmcid_element = driver.find_element(By.XPATH, '//a[contains(@href, "pmc.ncbi.nlm.nih.gov/articles/PMC")]')
        pmcid_full = pmcid_element.text.strip()
        data['pmcid'] = pmcid_full.replace("PMCID: ", "").strip()
    except:
        data['pmcid'] = None

    return data

# Fetch the full text from PMC using the provided PMCID
def fetch_pmc_full_text(pmcid, driver):
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    driver.get(url)
    
    data = {'pmcid': pmcid}
    wait = WebDriverWait(driver, 30)
    
    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_source = driver.page_source
        text_content = re.sub(r'<[^>]+>', '', page_source).strip()
        data['full_text'] = text_content
    except Exception as e:
        data['full_text'] = None
        print(f"Error fetching full text: {str(e)}")
    
    return data
