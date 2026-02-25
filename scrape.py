from playwright.sync_api import sync_playwright

def scrape_quotes():
    with sync_playwright() as p:
        # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        result = 0
        for index in range(69, 79):
            page.goto(f"https://sanand0.github.io/tdsdata/js_table/?seed={index}")
            quotes = page.query_selector("#table")
            values = quotes.inner_text()
            values = values.split("\n")
            for value in values:
                value = value.split("\t")
                for id in value:
                    result = result + int(id)      

        print("FINAL TOTAL:", result)

        browser.close()

if __name__ == "__main__":
    scrape_quotes()
