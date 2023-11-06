import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

def bgpsearch(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(options=chrome_options)  

    driver.get('https://bgp.he.net/')
    
    search_box = driver.find_element(By.NAME, "search[search]")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search table tbody tr td:first-child')))
    
    page_content = driver.page_source
    driver.quit()
    return page_content

def main(orgname, output_filename):
    page_content = bgpsearch(orgname)
    soup = BeautifulSoup(page_content, 'html.parser')
    
    results = soup.select('#search table tbody tr td:first-child')
    
    as_numbers = []  
    
    for result_cell in results:
        result = result_cell.get_text().strip()
        if ":" not in result and not result.startswith("AS"):
            as_numbers.append(result)  
    
    if output_filename:
        with open(output_filename, "w") as output_file:
            for as_number in as_numbers:
                output_file.write(as_number + "\n")
    
    return as_numbers  

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search BGP information for an organization.")
    parser.add_argument("orgname", type=str, help="Organization name to search for")
    parser.add_argument("-o", "--output", type=str, help="Output file to save results")
    args = parser.parse_args()    
    as_numbers = main(args.orgname, args.output)
    
    print(f"IP for {args.orgname}:")
    for as_number in as_numbers:
        print(as_number)
    
    time.sleep(3)
