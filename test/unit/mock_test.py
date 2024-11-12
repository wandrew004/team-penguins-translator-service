import os
from mock import patch
from openai import AzureOpenAI
from src.translator import query_llm_robust


@patch('src.translator.client.chat.completions.create')
def test_unexpected_language(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "Invalid request."
  # TODO assert the expected behavior
  query = query_llm_robust("สวัสดี Hier ist dein erstes Beispiel. 私は日本出身です。")
  assert query == (False, "Invalid request.")

@patch('src.translator.client.chat.completions.create')
def test_malformed_language(mocker):
  mocker.return_value.choices[0].message.content = "Unintelligible or malformed post."
  # TODO assert the expected behavior
  query = query_llm_robust("!important text here but it's !missing !something")
  assert query == (False, "Unintelligible or malformed post.")


@patch('src.translator.client.chat.completions.create')
def test_english(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "This is a fun assignment."
  # TODO assert the expected behavior
  result = query_llm_robust("This is a fun assignment.")
  assert result == (False, 'This is a fun assignment.')

@patch('src.translator.client.chat.completions.create')
def test_unintelligible_language(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "Unintelligible or malformed post."
  # TODO assert the expected behavior
  result = query_llm_robust("fhwoeh238740327&&&&&&&&&&")
  assert result == (False, "Unintelligible or malformed post.")

@patch('src.translator.client.chat.completions.create')
def test_empty(mocker):
  # we mock the model's response to return a random message
  mocker.return_value.choices[0].message.content = "Invalid request."
  # TODO assert the expected behavior
  result = query_llm_robust("")
  assert result == (False, "Invalid request.")