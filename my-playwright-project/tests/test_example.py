import pytest
from playwright.sync_api import Page, BrowserContext, expect

@pytest.fixture(autouse=True)
def clear_cookies(context: BrowserContext):
    context.clear_cookies()
    yield

def test_login(page: Page) -> None:
    page.set_default_timeout(60000)
    page.set_default_navigation_timeout(60000)

    # Step 1 — Login
    page.goto("https://payv2.dev.adaptivegroups.asia/")
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("textbox", name="Type Your Company Code").fill("Sidco")
    page.get_by_role("textbox", name="Type Your User Name").fill("Naveen")
    page.get_by_role("textbox", name="Type Your Password").fill("Adaptive*123")
    page.locator("input[value='Log In']").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(5000)

    # Step 2 — Navigate to Company
    page.goto("https://payv2.dev.adaptivegroups.asia/Company")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(5000)

    # Step 3 — Screenshot to verify page loaded
    page.screenshot(path="debug_company.png")

    # Step 4 — Click Details
    page.wait_for_selector("[title='Details']", state="visible")
    page.locator("[title='Details']").click()
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(5000)

    # Step 5 — Organization Chart
    page.get_by_role("button", name="Organization Chart").click()
    page.wait_for_timeout(5000)

    # Step 6 — Dropdown interactions
    page.wait_for_selector("#structure-dropdown", state="visible")
    page.locator("#structure-dropdown").select_option("false")
    page.wait_for_timeout(3000)
    page.locator("#structure-dropdown").select_option("hierarchy")
    page.wait_for_timeout(3000)

    # Step 7 — Button interactions
    page.get_by_role("button", name="Reset").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Collapse").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Expand").click()
    page.wait_for_timeout(2000)
