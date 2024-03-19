from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("你好")
    assert is_english == False
    assert translated_content == "Hello"

def test_french():
    is_english, translated_content = translate_content("Bonjour")
    assert is_english == False
    assert translated_content == "Hello"

def test_llm_normal_response():
    pass

def test_llm_gibberish_response():
    pass