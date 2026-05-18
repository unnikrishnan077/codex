from playwright.async_api import async_playwright


async def fetch_page_title(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        title = await page.title()
        await browser.close()
        return title
