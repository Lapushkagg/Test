from typing import Literal
import pytest
from StringUtils import StringUtils

# позитиыные тесты
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", "Hello"),
        ("Hello", "Hello"),
        ("hello world", "Hello world")
    ],
)
def test_capitilize_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" hello", "hello"),
        ("    Hello", "Hello"),
        (" hello world", "hello world"),
        ("Hello", "Hello")
    ],
)
def test_trim_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("hello", ["hello"]),
        ("H,e,l,l,o", ["H","e","l","l","o"]),
        (" ,h,e,l,l,o, ,w,o,r,l,d", [" ","h","e","l","l","o"," ","w","o","r","l","d"]),
        ("1,2,3", ["1", "2", "3"])
    ],
)
def test_to_list_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.to_list(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        (" hello", "l",True),
        ("    Hello", " ",True),
        (" hello world", "wo",True),
        ("Hello", "a",False)
    ],
)
def test_contains_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.contains(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "l","heo"),
        ("    Ololo", "O", "    lolo"),
        ("hello world", "wo","hello rld"),
        ("hello world", " ","helloworld")
    ],
)
def test_delete_symbol_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "h",True),
        ("Hello", "h", True),
        (" hello world", " ",True),
        ("1hello world", "1",True),
        ("1hello world", "3",False)
    ],
)
def test_starts_with_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("hello", "o",True),
        ("HellO", "o", True),
        (" hello world ", " ",True),
        ("1hello world1", "1",True),
        ("1hello world", "3",False)
    ],
)    
def test_end_with_positive(input_text, symbol, expected_output):
    processor = StringUtils()
    assert processor.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("",True),
        (" ", True),
        (" hello world ",False)
    ],
)   
def test_is_empty_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.is_empty(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (["hello"],"hello" ),
        (["H","e","l","l","o"],"H, e, l, l, o" ),
        ([" ","h","e","l","l","o"," ","w","o","r","l","d"] , " , h, e, l, l, o,  , w, o, r, l, d" ),
        (["1", "2", "3"], "1, 2, 3")
    ],
)
def test_list_to_string_positive(input_text, expected_output):
    processor = StringUtils()
    assert processor.list_to_string(input_text) == expected_output




# негативные тесты
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        (" ", " "),
        (None, None),
        (12345, 12345)
    ],
)
def test_capitilize_negative(input_text, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
      assert processor.capitilize(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),
        (" ", " "),
        (None, None)
    ],
)
def test_trim_negative(input_text, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.trim(input_text) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", []),
        (" ", [" "]),
        (None, [])
    ],
)
def test_to_list_negative(input_text, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.to_list(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "l",False),
        (" ", "9",False),
        (None, "wo",False)
    ],
)
def test_contains_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.contains(input_text, symbol) == expected_output


@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "l",""),
        (" ", "O", " "),
        (None, "wo",None)
    ],
)
def test_delete_symbol_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.delete_symbol(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "l",""),
        (" ", "O", " "),
        (None, "wo",None)
    ],
)
def test_starts_with_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.starts_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("", "l",False),
        (" ", "9",False),
        (None, "wo",False)
    ],
)    
def test_end_with_negative(input_text, symbol, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
        assert processor.end_with(input_text, symbol) == expected_output

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("",False),
        (" ",False),
        (None,False)
    ],
)   
def test_is_empty_negative(input_text, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
      assert processor.is_empty(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ([], ""),
        ([" "]," " ),
        ([None], None)
    ],
)
def test_list_to_string_negative(input_text, expected_output):
    processor = StringUtils()
    with pytest.raises((AttributeError, AssertionError)):
      assert processor.list_to_string(input_text) == expected_output
