from src.extract import extract, get_url
import pytest

@pytest.mark.skip
def test_extract_returns_dictionary():
    response = extract()
    assert isinstance(response, dict)

@pytest.mark.skip
def test_extract_sends_request(mocker):
    mock_requests_get = mocker.patch("requests.get")
    mock_requests_get.return_value.status_code = 200

    extract()

    assert mock_requests_get.call_count == 1

@pytest.mark.skip
def test_extract_recieves_response(mocker):
    mock_requests_get = mocker.patch("requests.get")
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = "boom"

    result = extract()

    assert mock_requests_get.call_count == 1
    assert result == "boom"

@pytest.mark.skip
def test_get_url_reads_env_vars(mocker):
    # Mock os.getenv for URL_TEMPLATE and API_VERSION
    mock_getenv = mocker.patch("os.getenv")
    
    # Define the return values of os.getenv
    mock_getenv.side_effect = lambda var: {
        "URL_TEMPLATE": "https://example.com/api/{date}/{api_version}/{endpoint}",
        "API_VERSION": "v5"
    }[var]
    
    # Call the function with test parameters
    url = get_url(currency="usd", date="2025-02-16")
    
    # Define the expected URL
    expected_url = "https://example.com/api/2025-02-16/v5/usd"
    
    # Assert that the generated URL matches the expected one
    assert url == expected_url
    assert mock_getenv.call_count == 2
