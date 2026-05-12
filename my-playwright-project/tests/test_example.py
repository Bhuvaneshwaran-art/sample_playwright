import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(autouse=True)
def clear_cookies(context: BrowserContext):
    context.clear_cookies()
    yield

def get_target_frame(page, selector):
    """Find which frame contains the given selector"""
    # Check main page first
    if page.locator(selector).count() > 0:
        return page
    # Check all frames
    for frame in page.frames:
        try:
            if frame.locator(selector).count() > 0:
                return frame
        except:
            pass
    return None

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

    # Step 3 — Click Details (search in all frames)
    details_frame = get_target_frame(page, "[title='Details']")
    if details_frame:
        print(f"✅ Details found in: {getattr(details_frame, 'url', 'main page')}")
        details_frame.locator("[title='Details']").first.click()
    else:
        raise Exception("❌ Details element not found in any frame")
    page.wait_for_timeout(5000)

    # Step 4 — Click Organization Chart (search in all frames)
    org_frame = get_target_frame(page, "input[value='Organization Chart']")
    if org_frame:
        print(f"✅ Org Chart found in: {getattr(org_frame, 'url', 'main page')}")
        org_frame.locator("input[value='Organization Chart']").click()
    else:
        raise Exception("❌ Organization Chart button not found in any frame")
    page.wait_for_timeout(5000)

    # Step 5 — Find frame containing dropdown
    dropdown_frame = get_target_frame(page, "#structure-dropdown")
    if dropdown_frame:
        print(f"✅ Dropdown found in: {getattr(dropdown_frame, 'url', 'main page')}")
        dropdown_frame.locator("#structure-dropdown").select_option("false")
        page.wait_for_timeout(3000)
        dropdown_frame.locator("#structure-dropdown").select_option("hierarchy")
        page.wait_for_timeout(3000)
    else:
        raise Exception("❌ Dropdown not found in any frame")

    # Step 6 — Find frame containing Reset button
    reset_frame = get_target_frame(page, "button[onclick='resetView()']")
    if reset_frame:
        print(f"✅ Reset found in: {getattr(reset_frame, 'url', 'main page')}")
        reset_frame.locator("button[onclick='resetView()']").click()
        page.wait_for_timeout(2000)
        reset_frame.locator("button[onclick='collapseAll()']").click()
        page.wait_for_timeout(2000)
        reset_frame.locator("button[onclick='expandAll()']").click()
        page.wait_for_timeout(2000)
    else:
        raise Exception("❌ Reset button not found in any frame")

    # Final screenshot
    page.screenshot(path="debug_final.png", full_page=True)
    print("✅ Test completed successfully!")
