def IsStringLong(input: str):
    if len(input) > 5:
        return True
    return False


def test_IsStringLong():
    result = IsStringLong("abc")
    assert False == result


if __name__ == "__main__":
    test_IsStringLong()
    print("Everything passed")
