from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_string_validator.plugin import StringValidatorAction


def test_plugin():
    init = {
        'validation_name': 'email',
        'data': "my@email.com"
    }

    payload = {}

    result = run_plugin(StringValidatorAction, init, payload)
    assert result.output.value is True
