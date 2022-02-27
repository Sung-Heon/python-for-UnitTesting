def IsStringLong(input: str):
    return len(input) > 5


def test_IsStringLong():
    result = IsStringLong("abc")
    assert False == result


if __name__ == "__main__":
    test_IsStringLong()
    print("Everything passed")
