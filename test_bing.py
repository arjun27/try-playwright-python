from playwright.sync_api import BrowserContext

def test_bing_is_working(context: BrowserContext):
    page = context.newPage()
    page.setContent('<a href="https://bing.com" target="_blank">link</a>')
    
    with page.expect_popup() as popup_event:
        page.click('text=link')
    
    popup = popup_event.value
    assert 'bing.com' in popup.url
    popup.bringToFront()
