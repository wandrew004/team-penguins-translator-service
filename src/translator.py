import os
from openai import AzureOpenAI

API_KEY = os.getenv("API_KEY")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
	api_key= API_KEY,
	api_version="2024-02-15-preview",
	azure_endpoint="https://teampenguins.openai.azure.com/"  # Replace with your Azure endpoint
)


def get_language(post: str) -> str:
	context = "Identfy which language this post is in. Only output the language in English." # TODO: Insert context
	# ---------------- YOUR CODE HERE ---------------- #
	response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages=[
		{
		  "role": "system",
		  "content": context
		},
		{
			"role": "user",
			"content": post
		}
	]
)
	return response.choices[0].message.content

def query_llm_robust(post: str) -> tuple[bool, str]:
	context = '''Translate this non-English post into English.
				If the post is in English, return the original post.
				If the post is gibberish, unintelligible, or malformed, return Unintelligible or malformed post.
				If the post is unexpected (many languages, etc.) or invalid (empty, etc.), return Invalid request.
				'''
	response = client.chat.completions.create(
	model="gpt-4o-mini",
	messages=[
		{
			"role": "system",
			"content": context
		},
		{
			"role": "user",
			"content": post
		}
		]
	)
	try:
		result = response.choices[0].message.content
	except (AttributeError, IndexError):
		return (False, "Unintelligible or malformed post.")
	lang = get_language(post)
	english_check = lang == "English"

	if result == "Unintelligible or malformed post.":
		english_check = False
	final_res = (english_check, result)

	return final_res
