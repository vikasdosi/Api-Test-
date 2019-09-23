import requests


def test_get_user():
    user_id = 2
    end_point = "https://reqres.in/api" + "/users/{}".format(user_id)
    res = requests.get(end_point)
    res_json = res.json()
    data = res_json["data"]
    assert data["id"] == user_id



