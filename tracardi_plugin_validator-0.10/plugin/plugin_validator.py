from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from pydantic import BaseModel
import re


class ValidationType(BaseModel):
    validation_type: str


class Data(BaseModel):
    data: str


class Configuration(BaseModel):
    validator: ValidationType
    data: Data


class Validate:
    def __init__(self, type: ValidationType, data : Data):
        self.type = type.validation_type
        self.data = data.data

    def _get_regex(self):
        """Get a actual regex with dict from validation_type."""
        dict_regex = {
            'email_regex': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url_regex': r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_:#]+\.([a-zA-Z]){2,'
                         r'6}([a-zA-Z0-9\.\&\/\?\:@\-_:#])*',
            'ipv4_regex': r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            'date_regex': r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))("
                          r"?:(?:1[ "
                          r"6-9]|["
                          r"2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579]["
                          r"26])|(?:("r"?:16|["
                          r"2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4("
                          r"?:(?:1["
                          r"6-9]|["
                          r"2-9]\d)?\d{2})$",
            'time_regex': r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9](:?)([0-5]?[0-9]?)$',
            'int_regex': r'^[0-9]+$',
            'float_regex': r'^[+-]?([0-9]{1,})[.,]([0-9]{1,})$',
            'number_phone_regex': r'\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,'
                                  r'10}\s?\d{1,6})?'}
        return dict_regex[self.type]

    def check(self) -> bool:
        """Check the validation"""
        if re.match(self._get_regex(), self.data):
            return True
        else:
            return False


class Validator(ActionRunner):
    def __init__(self, **kwargs):
        self.status = ''
        try:
            self.config = Configuration(**kwargs)
            self.check = Validate(self.config.validator,self.config.data)
        except Exception as exc:
            self.status += str(exc) + ' '

    async def run(self, void):
        try:
            if self.check.check():
                return Result(port='TRUE', value=True)
            else:
                return Result(port='FALSE', value=False)
        except Exception as exc:
            self.status += str(exc) + ' '
            ActionRunner.console = self.status
            return Result(port='ERROR', value=self.status)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='app.process_engine.action.v1.plugin_validator',
            className='Validator',
            inputs=["void"],
            outputs=["TRUE", "FALSE","ERROR"],
            init={
                'validator': {
                    'validation_type': None,
                },
                'data': {
                    "data": None,
                }
            },
            version='0.1',
            license="MIT",
            author="Patryk Migaj"

        ),
        metadata=MetaData(
            name='Validator',
            desc='Validation of data such as: email, url, ipv4, date, time,int,float, phone number, ean code',
            type='flowNode',
            width=200,
            height=100,
            icon='start',
            group=["Validations"]
        )
    )
