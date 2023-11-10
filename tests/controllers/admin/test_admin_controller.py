from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    history_one = HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    UserModel({"name": "xabloso", "token": "123456"}).save()
    user = UserModel.find_one({"name": "xabloso"})

    app_test.delete(
        f"/admin/history/{history_one.data['_id']}",
        headers={
            "Authorization": user.data["token"],
            "User": user.data["name"],
        },
    )
