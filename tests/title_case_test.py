from src.title_case.title_case import title_case


def test_title_case_returns_a_string():
    # Arrange, Act
    tc = title_case('hello')
    # Assert
    assert type(tc) is str

def test_title_case_capitalizes_first_letter_of_word():
    tc = title_case('narnia')
    assert tc[0].isupper()
