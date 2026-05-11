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

     # Check if Details is inside iframe
    frames = page.frames
    print("\n=== ALL FRAMES ON PAGE ===")
    for frame in frames:
        print(frame.name, frame.url)

    # Try clicking Details inside each frame
    for frame in page.frames:
        try:
            if frame.locator("[title='Details']").count() > 0:
                print(f"\n✅ Found Details in frame: {frame.url}")
                frame.locator("[title='Details']").first.click()
                break
        except Exception as e:
            print(f"Frame error: {e}")
    page.wait_for_timeout(5000)

    # Step 5 — Organization Chart
    try:
                # Option 3 — by input value
                page.locator("input[value='Organization Chart']").click()
    except Exception as e:
                print(f"Frame error: {e}")

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
