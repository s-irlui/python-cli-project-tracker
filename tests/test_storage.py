from app.storage import generate_id


def test_generate_id_empty_list():
    items = []

    result = generate_id(items, "user_id")

    assert result == 1


def test_generate_id_existing_items():
    items = [
        {"user_id": 1},
        {"user_id": 2},
        {"user_id": 3}
    ]

    result = generate_id(items, "user_id")

    assert result == 4