from src.translator import translate_content


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

def test_french():
    is_english, translated_content = translate_content("Ceci est un message en français")
    assert is_english == False
    assert translated_content == "This is a French message"

def test_llm_normal_response():
    is_english, translated_content = translate_content("今個週末附近學校有個網球比賽。")
    assert is_english == False
    assert translated_content == "There is a tennis match this weekend at the nearby school."

def test_llm_gibberish_response():
    pass