from playwright.sync_api import Page, expect, Playwright, APIRequestContext
import re

url_api = 'https://restful-booker.herokuapp.com'
#Dungeons & Dragons
url = 'https://geekach.com.ua/nastolnye-igry/rolevye-igry/dungeons-dragon/'

def test_valid_title(page:Page):
    page.goto(url)
    expect(page).to_have_title(re.compile('Dungeons & Dragons'))
    

def test_bypass_pages(page:Page):
    page.goto(url)
    page.locator('xpath=//div[@class="catalogCard-title"]/a[@href="/nabor-krasok-dd-nolzurs-marvelous-pigments-undead-paint-set/"]').click()
    expect(page.locator('xpath=//meta[@itemprop="price"][@content="1295"]')).to_be_hidden()
    expect(page.locator('xpath=//td[@class="product-features__cell"][contains(text(), "75005")]')).to_be_visible()


def test_get(context:APIRequestContext):
    api_request_context = context.request
    all_bookings = api_request_context.get(url_api+'/booking')
    assert all_bookings.ok
    print(all_bookings.json())
  

def test_post(context:APIRequestContext):
    api_request_context = context.request
    data = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    headers = 'Content-Type: application/json'
    all_bookings = api_request_context.post(url=url_api+'/booking', data=data)
    assert all_bookings.ok
    print(all_bookings.json())


def test_get_concrete_booking(context:APIRequestContext):
    api_request_context = context.request
    all_bookings = api_request_context.get(url_api+'/booking/2246')
    assert all_bookings.ok
    print(all_bookings.json())


