from src.translator import translate_content


def test_llm_normal_response():
    is_english, translated_content = translate_content("This is a normal English message")
    assert is_english == True
    assert translated_content == "This is a normal English message"

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("fhwoeh238740327&&&&&&&&&&")
    assert is_english == False
    assert translated_content == "Unintelligible or malformed post."