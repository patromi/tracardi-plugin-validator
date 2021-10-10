from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi.domain.profile_traits import ProfileTraits
from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_string_validator.plugin import ValidatorAction

init = {"data": "event@id",
        "validation_name": "time"}
payload = {}
profile = Profile(id="profile-id", traits=ProfileTraits(public={"test": "new test"}))
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(ValidatorAction, init, payload,
                    profile, None, event)
print(result)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)
