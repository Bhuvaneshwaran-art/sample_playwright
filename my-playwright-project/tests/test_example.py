import pytest
from playwright.sync_api import Page, expect

def test_login(page: Page) -> None:
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    # Login
    page.goto("https://payv2.dev.adaptivegroups.asia/")
    page.get_by_role("textbox", name="Type Your Company Code").fill("Sidco")
    page.get_by_role("textbox", name="Type Your User Name").fill("Naveen")
    page.get_by_role("textbox", name="Type Your Password").fill("Adaptive*123")
    page.locator("input[value='Log In']").click()

    # Wait for login to fully complete — wait for dashboard to appear
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)  # buffer for session to establish

    # Navigate to Company
    page.goto("https://payv2.dev.adaptivegroups.asia/Company")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(3000)  # buffer for dynamic content to render

    # Take screenshot to debug what's on screen
    page.screenshot(path="company_page.png")

    # Wait explicitly for Details to be visible before clicking
    page.wait_for_selector("[title='Details']", state="visible", timeout=60000)
    page.locator("[title='Details']").click()

    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("button", name="Organization Chart").click()

    # Interact with dropdown
    page.wait_for_selector("#structure-dropdown", state="visible")
    page.locator("#structure-dropdown").select_option("false")
    page.wait_for_timeout(3000)
    page.locator("#structure-dropdown").select_option("hierarchy")
    page.wait_for_timeout(3000)

    # Button interactions
    page.wait_for_selector("button:has-text('Reset')", state="visible")
    page.get_by_role("button", name="Reset").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Collapse").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Expand").click()
    page.wait_for_timeout(2000)
