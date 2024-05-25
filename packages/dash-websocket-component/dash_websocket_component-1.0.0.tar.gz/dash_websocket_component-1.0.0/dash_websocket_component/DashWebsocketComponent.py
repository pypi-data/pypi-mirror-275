# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashWebsocketComponent(Component):
    """A DashWebsocketComponent component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- error (dict | string; optional):
    This property is set with the content of the onerror event.

- maxReconnectAttempts (number; optional):
    Max count of the reconnect attempts. Default = -1 -> Unlimited.

- message (dict | string; optional):
    When messages are received, this property is updated with the
    message content.

- protocols (list of strings; optional):
    Supported websocket protocols (optional).

- reconnectIntervalMs (number; optional):
    Duration between attempts to reconnect. Default = 2000ms -> 2sec.

- send (dict | string; optional):
    When this property is set, a message is sent with its content.

- state (dict | string; optional):
    This websocket state (in the readyState prop) and associated
    information.

- url (string; optional):
    The websocket endpoint (e.g. wss://echo.websocket.org)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_websocket_component'
    _type = 'DashWebsocketComponent'
    @_explicitize_args
    def __init__(self, state=Component.UNDEFINED, message=Component.UNDEFINED, error=Component.UNDEFINED, send=Component.UNDEFINED, protocols=Component.UNDEFINED, reconnectIntervalMs=Component.UNDEFINED, maxReconnectAttempts=Component.UNDEFINED, url=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'error', 'maxReconnectAttempts', 'message', 'protocols', 'reconnectIntervalMs', 'send', 'state', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'error', 'maxReconnectAttempts', 'message', 'protocols', 'reconnectIntervalMs', 'send', 'state', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashWebsocketComponent, self).__init__(**args)
