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

    # Navigate to Company
    page.goto("https://payv2.dev.adaptivegroups.asia/Company")
    page.wait_for_selector("[title='Details']", state="visible")
    page.locator("[title='Details']").click()
    page.get_by_role("button", name="Organization Chart").click()

    # Interact with dropdown
    page.locator("#structure-dropdown").select_option("false")
    page.wait_for_load_state("networkidle")
    page.locator("#structure-dropdown").select_option("hierarchy")
    page.wait_for_load_state("networkidle")

    # Button interactions
    page.get_by_role("button", name="Reset").click()
    page.get_by_role("button", name="Collapse").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Expand").click()
    page.wait_for_load_state("networkidle")
