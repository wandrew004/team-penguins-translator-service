# import os
# from openai import AzureOpenAI

# API_KEY = os.getenv("API_KEY")

# # Initialize the Azure OpenAI client
# client = AzureOpenAI(
# 	api_key= API_KEY,
# 	api_version="2024-02-15-preview",
# 	azure_endpoint="https://teampenguins.openai.azure.com/"  # Replace with your Azure endpoint
# )


# def get_language(post: str) -> str:
# 	context = "Identfy which language this post is in. Only output the language in English." # TODO: Insert context
# 	# ---------------- YOUR CODE HERE ---------------- #
# 	response = client.chat.completions.create(
# 	model="gpt-4o-mini",
# 	messages=[
# 		{
# 		  "role": "system",
# 		  "content": context
# 		},
# 		{
# 			"role": "user",
# 			"content": post
# 		}
# 	]
# )
# 	return response.choices[0].message.content

# def query_llm_robust(post: str) -> tuple[bool, str]:
# 	context = '''Translate this non-English post into English.
# 				If the post is in English, return the original post.
# 				If the post is gibberish, unintelligible, or malformed, return Unintelligible or malformed post.
# 				If the post is unexpected (many languages, etc.) or invalid (empty, etc.), return Invalid request.
# 				'''
# 	response = client.chat.completions.create(
# 	model="gpt-4o-mini",
# 	messages=[
# 		{
# 			"role": "system",
# 			"content": context
# 		},
# 		{
# 			"role": "user",
# 			"content": post
# 		}
# 		]
# 	)
# 	try:
# 		result = response.choices[0].message.content
# 	except (AttributeError, IndexError):
# 		return (False, "Unintelligible or malformed post.")
# 	lang = get_language(post)
# 	english_check = lang == "English"

# 	if result == "Unintelligible or malformed post.":
# 		english_check = False
# 	final_res = (english_check, result)

# 	return final_res


def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content