import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    json_Data = HistoryModel.list_as_json()
    data = json.loads(json_Data)

    assert len(data) == 2
    assert data[0]["text_to_translate"] == "Hello, I like videogame"
    assert data[0]["translate_from"] == "en"
    assert data[0]["translate_to"] == "pt"
    assert data[1]["text_to_translate"] == "Do you love music?"
    assert data[1]["translate_from"] == "en"
    assert data[1]["translate_to"] == "pt"
