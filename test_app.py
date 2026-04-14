from app import add

def test_add():
    result = add(2, 3)
    print(f"add(2, 3) = {result}")
    assert result == 5
    print("Test passed!")

if __name__ == "__main__":
    test_add()