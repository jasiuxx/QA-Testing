import re
from playwright.sync_api import Page, expect
import pytest

#dane wejsciowe 
@pytest.mark.parametrize("phrase", [
    "the pickup", 
    "abcxyz123"
    ])
def test_example(page: Page,phrase) -> None:
    page.goto("https://vod.film/") #wejscie na strone glowna 
    page.get_by_role("button", name="Zgadzam się", exact=True).click() #zatwierzenie zbierania danych 
    page.get_by_role("textbox", name="Wyszukuj filmy i seriale...").click()  #klik w pole wyszukiwania
    page.get_by_role("textbox", name="Wyszukuj filmy i seriale...").fill(phrase) #wyszukanie frazy
    expect(page.locator("header")).to_contain_text(re.compile(rf".*{phrase}.*", re.IGNORECASE)) #sprawdzenie film jest na liscie 
    print(page.locator("header").text_content())

    page.get_by_role("link", name=re.compile(rf".*{phrase}.*", re.IGNORECASE)).first.click() # wejscie w szczegoly filmu
    expect(page.locator("h1")).to_contain_text(re.compile(rf".*{phrase}.*", re.IGNORECASE)) #sprawdzenie czy h1 zawiera fraze 
    expect(page.locator("#player-container")).to_contain_text("Play") #sprawdzenie czy jest przycisk play
    page.locator("#player-container button").filter(has_text=re.compile(r"^Play$")).click() #klik w przycisk play
    page.get_by_role("button", name="Mute").click() #wyciszenie dźwięku
    page.wait_for_timeout(1000)  #czekanie od 1 sekundy po odwtworzeniu playera
    page.locator("#popup").get_by_text("Zarejestruj się").click(timeout=60000) #czekanie do 60 sekund na popout
    print('Przekierowanie popup: ' + page.url) #sprawdzenie url popupa
