try:
    a = 100
    b = 100
    assert a == b
except AssertionError:
    print("Assertion Exception Raised.")
else:
    print("Success, no error!")
