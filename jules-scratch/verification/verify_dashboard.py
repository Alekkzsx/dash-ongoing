from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Go to the local web server
        page.goto('http://localhost:8000/dashboard.html')

        # Wait for the auth screen to be visible
        page.wait_for_selector('#auth-screen')

        # Take a screenshot
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

if __name__ == '__main__':
    run()
