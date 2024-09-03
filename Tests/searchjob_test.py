import re
import pytest
from EpamPages.careerssearch_page import CareerSearchPage
from EpamPages.index_page import IndexPage
from EpamPages.job_page import JobPage
from EpamPages.joblistings_page import JobListingPage


@pytest.mark.parametrize("keyword,location", [("python", "All Locations")])
# @pytest.mark.flaky(rerun=2, reruns_delay=2)
def test_search_job(create_driver, keyword, location):
    driver = create_driver
    page_index = IndexPage(driver)
    page_index.open_page()
    page_index.click_carriers()
    page_career_search = CareerSearchPage(driver)
    page_career_search.fill_keyword_box_click(keyword)
    page_career_search.select_location(location)
    page_career_search.check_remote_checkbox()
    page_career_search.click_find_button()
    page_job_listings = JobListingPage(driver)
    page_job_listings.click_apply()
    page_job = JobPage(driver)
    job_title_text = page_job.get_title_text()
    pattern = r'\b' + keyword + r'\b'
    assert re.search(pattern, job_title_text, re.IGNORECASE), f"The word '{keyword}' is not present in the text."
