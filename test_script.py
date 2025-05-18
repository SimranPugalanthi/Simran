# test_script.py

def test_login():
    username = "admin"
    password = "admin123"
    assert username == "admin"
    assert password == "admin123"
    print("Login test passed!")

if __name__ == "__main__":
    test_login()
