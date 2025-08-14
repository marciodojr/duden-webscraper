from duden_webscraper.duden_web_scraper import DudenWebScraper
import pytest

def read_html(word):
    file_path = f"./tests/html/{word}.html"
    f = open(file_path, "r", encoding="utf-8")
    return f.read()

@pytest.mark.parametrize("word, status_code", [
    ("Pferd", 200),
    ("Maskotte", 200),
    ("Kaf", 200),
    ("Shop", 200),
])
def test_lemma_must_be_equals_to_word(requests_mock, word, status_code):
    mocked_url = f"https://www.duden.de/rechtschreibung/{word}"
    html_content = read_html(word)

    requests_mock.get(mocked_url, text=html_content, status_code=status_code)

    scraper = DudenWebScraper()
    result = scraper.get_word_info(word)

    assert result["lemma"] == word
