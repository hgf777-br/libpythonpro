from unittest.mock import Mock
from libpythonpro import github_api
import pytest


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/66914517?v=4"
    resp_mock.json.return_value = {"login": "hgf777-br", "id": 66914517,
                                   "avatar_url": url}
    get_mock = mocker.patch("libpythonpro.github_api.requests.get")
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar("hgf777-br")
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar("hgf777-br")
    assert "https://avatars.githubusercontent.com/u/66914517?v=4" == url
