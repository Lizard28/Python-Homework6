import pytest

def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

def test_average_num():
    assert average_num([1, 2, 3 ]) == 2.0

    assert average_num([1.99, 4.355, 6.7]) == 4.35

    assert average_num([1, 2.7, 3]) == 2.23

    with pytest.raises(ZeroDivisionError):
        average_num([])

    assert average_num(["1", "2", 3 ]) == 2.0

    assert average_num(["Hello", "my", "python"]) == "Bad request"

    assert average_num([1, 2.5, "c"]) == "Bad request"

    assert average_num([-1, -2, -3 ]) == -2.0

    assert average_num([1, -2.9, 3.0]) == 0.37

    assert average_num([0, 0, 0, 0]) == 0.0
