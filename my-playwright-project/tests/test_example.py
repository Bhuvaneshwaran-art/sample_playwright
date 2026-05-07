import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://payv2.dev.adaptivegroups.asia/")
    page.get_by_role("textbox", name="Type Your Company Code").fill("Sidco")
    page.get_by_role("textbox", name="Type Your User Name").fill("Naveen")
    page.get_by_role("textbox", name="Type Your Password").fill("Adaptive*123")
    page.locator("input[value='Log In']").click()
    page.wait_for_timeout(5000)
    page.goto("https://payv2.dev.adaptivegroups.asia/Company")
    page.get_by_title("Details").click()
    page.get_by_role("button", name="Organization Chart").click()
    page.locator("#structure-dropdown").select_option("false")
    page.wait_for_timeout(5000)
    page.locator("#structure-dropdown").select_option("hierarchy")
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Collapse").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Expand").click()
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
