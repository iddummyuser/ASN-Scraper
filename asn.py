import asyncio
from pyppeteer import launch


async def bgpasnbrowser(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://bgp.he.net/{}#_prefixes'.format(keyword))
    await page.waitForNavigation()
    results = await page.evaluate('''() => {
    const tableRows = Array.from(document.querySelectorAll('#prefixes table tbody tr'));
    const resultColumn = tableRows.map(row => {
        const resultCell = row.querySelector('td:first-child');
        return resultCell.innerText.trim();
    });
    return resultColumn;
    }''');
    await browser.close()
    return results
   

async def bgpsearchbrowser(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://bgp.he.net/')
    await page.type('#search_search', keyword)
    await page.click('input[name="commit"]')
    await page.waitForNavigation()
    results = await page.evaluate('''() => {
    const tableRows = Array.from(document.querySelectorAll('#search table tbody tr'));
    const resultColumn = tableRows.map(row => {
        const resultCell = row.querySelector('td:first-child');
        return resultCell.innerText.trim();
    });
    return resultColumn;
    }''');        
    await browser.close()
    return results

async def main(orgname):
    alldata = await bgpsearchbrowser(orgname)
    ips = []
    for i in alldata:
        if ":" not in i:
            if "." in i:
                ips.extend(extract_ips(i))
            elif i.startswith("AS"):
                ipsubnet = await bgpasnbrowser(i)
                for j in ipsubnet:
                    ips.extend(extract_ips(j))
    with open('ips.txt', 'w') as file:
        for item in list(set(ips)):
            file.write(str(item) + '\n')

asyncio.run(main("orgname"))



