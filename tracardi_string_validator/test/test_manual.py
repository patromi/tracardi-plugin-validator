from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_string_validator.plugin import ValidatorAction

init = {
    'validation_name': 'email',
    'data': "my@email.com"
}

payload = {}

result = run_plugin(ValidatorAction, init, payload)
print(result)
assert result.output.value is True
