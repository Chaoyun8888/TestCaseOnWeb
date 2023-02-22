import pytest

@pytest.mark.createcodespace
def test_create_codespace(page):
    page.goto("https://github.com/codespaces")
    #page.wait_for_timeout(3000)
    page.get_by_role("login_field").fill("Chaoyun8888")
   