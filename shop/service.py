def get_order_params(item: str) -> str:
    data = {
        "alphabet": 'name',
        "asc": 'price_rub',
        "desc": '-price_rub',
        "popular": '-views',
        "difficult": 'difficulty'
    }
    return data.get(item)

