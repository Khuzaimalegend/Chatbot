
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    url = "http://127.0.0.1:5000"
    print(f"Navigating to {url}...")
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_timeout(2000) # Wait for animations to settle
    page.screenshot(path="jules-scratch/verification/high_impact_ui.png")
    print("Screenshot taken.")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
