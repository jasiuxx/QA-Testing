

def test_api_get(playwright):
     browser = playwright.chromium.launch(headless=False)
     context = browser.new_context()
     request=context.request
     response=request.post("https://vod.film/search-route",data={"host": "vod.film", "locale": "pl", "searchTerm": "the pickup"})
     
     assert response.ok #sprawdzenie czy kod response to 2xx
     json_data=response.json()
     print(json_data)
     

     assert any('the pickup' in str(value).lower() for key,value in json_data['data'][0].items())
     
     
     #assert(json_data["id"]==1)
     
     request.dispose()
     print("API GET test passed.") 