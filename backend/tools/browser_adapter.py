from playwright.sync_api import sync_playwright


class BrowserAdapter:
    def search(self, query: str) -> str:
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.set_extra_http_headers({"User-Agent": "Mozilla/5.0"})
                page.goto("https://www.google.com", wait_until="domcontentloaded")
                page.fill("textarea[name='q']", query)
                page.keyboard.press("Enter")
                page.wait_for_timeout(2000)
                page.wait_for_selector("h3", timeout=10000)

                titles = page.locator("h3").all_text_contents()
                top_five_titles = [title.strip() for title in titles[:5] if title.strip()]
                top_titles = top_five_titles[:3]
                browser.close()

                if not top_titles:
                    return f"[ADAPTER MOCK] Search results for: {query}"

                return " | ".join(
                    f"{index}. {title}" for index, title in enumerate(top_titles, start=1)
                )
        except Exception as exception:
            print("[ADAPTER ERROR]", exception)
            return f"[ADAPTER MOCK] Search results for: {query}"
