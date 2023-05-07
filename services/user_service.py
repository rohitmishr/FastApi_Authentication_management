from databases import ms


def get_user_data():
    print("-------------------------------- ",ms.user_db())
    data =  ms.user_db()
    return data

def register_user(username, hashed_password, role):
    data = ms.reg_user(username, hashed_password, role)
    return data
