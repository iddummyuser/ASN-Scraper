# ASN Scraper

This script allows you to scrape IP addresses related to an organization's Autonomous System Number (ASN) using the BGP (Border Gateway Protocol) lookup.

## Prerequisites

Before running the script, make sure you have the following requirements:

- Python 3.x
- `asyncio` library
- `pyppeteer` library

You can install the required libraries using the following command:

```bash
pip install asyncio pyppeteer
```

## Usage
- Clone this repository or copy the script to your local machine.
- Open a terminal or command prompt and navigate to the directory where the script is located.
- Run the script using the following command:
```bash
python asn_scrapper.py
```
## How it works
The script performs the following steps:

- Launches a headless browser using pyppeteer.
- Navigates to the BGP Lookup page on https://bgp.he.net/ to search for the provided organization name.
- Retrieves the relevant ASN data from the search results.
- If the ASN data contains IP subnets, it scrapes the IP addresses associated with each subnet.
- Writes the unique IP addresses to a file named ips.txt in the current directory.
#### Note: Please replace the orgname parameter in the asyncio.run(main("orgname")) line with the desired organization name.

Feel free to modify the code as per your requirements.

For more information on how to use pyppeteer, refer to the official documentation: pyppeteer - https://github.com/pyppeteer/pyppeteer
