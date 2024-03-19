# Install Dependencies

You need to install `flask` and `pytest` to run this application.

```
pip3 install flask
pip3 install pytest
```

# Deploy this service to Google cloud

Please follow [this](https://cmu-313.github.io/recitations/reci6-deployment/#task-1b-deploy-on-google-cloud-platform)
tutorial to deploy translator service to Google cloud.


# Test your deployment

Once you have deployed this service, you can access the following link `https://PATH_TO_YOUR_DEPLOYED_SERVICE/?q=你好` and you will see a JSON response

```json
{
    "is_english":false,
    "translated_content":"Hello"
}
```

# Implement LLM based translator

Please replace `translate` method in `src/translator.py` with your LLM based
implementation. The `translate` method takes a string `content` as input and
returns a tuple `(bool, str)`. Indicating if `content` is in English and
the translated content if `content` is not in English.

## Handle responses from LLM

You need to design your prompt so that you can parse the result from a LLM model.
However, your system needs to be robust if LLM does not respond as you expect.
It is up to you how your system reacts to unexpected responses. You can try a different prompt, return an error message, or simply assume the input is in English.

# Test your implementation

Now you need to test your implementation.

To do this, please complete the unit test in `test/unit/test_translator.py`.
In `test_llm_normal_response()`, please implement a unit test that verifies that
your program can return correct value if LLM provides an expected result.
In `test_llm_gibberish_response()`, please implement a unit test that verifies
that your program can handle a gibberish response.


