from src.translator import query_llm_robust


def test_llm_normal_response():
    is_english, translated_content = query_llm_robust("This is a normal English message")
    assert is_english == True
    assert translated_content == "This is a normal English message"

def test_llm_gibberish_response():
    is_english, translated_content = query_llm_robust("fhwoeh238740327&&&&&&&&&&")
    assert is_english == False
    assert translated_content == "Unintelligible or malformed post."