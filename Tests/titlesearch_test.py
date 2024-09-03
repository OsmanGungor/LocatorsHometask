import pytest
from EpamPages.index_page import IndexPage
from EpamPages.search_page import Searchpage


@pytest.mark.parametrize("text_to_search", ["BLOCKCHAIN", "Cloud", "Automation"])
def test_search_titles(create_driver, text_to_search):
    driver = create_driver
    indexpage = IndexPage(driver)
    indexpage.open_page()
    indexpage.click_magnifier()
    indexpage.populate_search_field(text_to_search)
    searchpage = Searchpage(driver)
    searchresults = searchpage.get_result_text()
    incorrect_titles = []
    for result in searchresults:
        if text_to_search.lower() not in result.lower():
            incorrect_titles.append(result)
    assert not incorrect_titles, f"'{text_to_search}' not found in the following titles: {incorrect_titles}"
