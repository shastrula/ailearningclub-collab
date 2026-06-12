from unittest.mock import patch, MagicMock

@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.json.return_value = {'result': 0.95}
    
    predictor = APIPredictor('http://api.example.com')
    result = predictor.predict({'features': [1, 2, 3]})
    
    assert result == 0.95
    mock_get.assert_called_once()