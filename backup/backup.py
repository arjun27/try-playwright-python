from playwright.sync_api import Page

def test_bing_is_working(page: Page):
    page.goto('https://bing.com')
    page.click('text=Images')
    assert 'bing.com/images' in page.url