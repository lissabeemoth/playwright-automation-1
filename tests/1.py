from pytest import fixture

@fixture
def ultimate_answer():
    return 42

@fixture
def new_answer(ultimate_answer):
    return ultimate_answer + 1


def test_get_answer(ultimate_answer):
    assert 42 == ultimate_answer

def test_new_answer(new_answer):
    assert 43 == new_answer