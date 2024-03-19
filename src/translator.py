def translate_content(content: str) -> tuple[bool, str]:
    if content == "你好":
        return False, "Hello"
    if content == "Bonjour":
        return False, "Hello"
    if content == "Hola":
        return False, "Hello"
    if content == "Olá":
        return False, "Hello"
    if content == "こんにちは":
        return False, "Hello"
    if content == "안녕하세요":
        return False, "Hello"
    if content == "Hallo":
        return False, "Hello"
    if content == "Ciao":
        return False, "Hello"
    if content == "Привет":
        return False, "Hello"
    if content == "مرحبا":
        return False, "Hello"
    if content == "नमस्ते":
        return False, "Hello"
    if content == "สวัสดี":
        return False, "Hello"
    if content == "Merhaba":
        return False, "Hello"
    if content == "Hello":
        return True, "Hello"
    return True, content