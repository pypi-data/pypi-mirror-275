# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CheckTreePicker(Component):
    """A CheckTreePicker component.


Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- appearance (string; default 'default'):
    The appearance of the component. Can be `default` or `subtle`.

- block (boolean; default False):
    Whether to take up the full width of the parent container.

- cascade (boolean; default True):
    Whether to enable cascade selection.

- cleanable (boolean; default True):
    Whether to display the clear button.

- countable (boolean; default False):
    Whether to display the count of selected items.

- custom_locale (dict; default nl_NL):
    Custom locale for component.

- data (list; default [    {        label: 'A',        value: 'a',        children: [            {label: 'A1', value: 'a1'},            {label: 'A2', value: 'a2'},        ],    },    {        label: 'B',        value: 'b',        children: [            {                label: 'B1',                value: 'b1',                children: [                    {label: 'B11', value: 'b11'},                    {label: 'B12', value: 'b12'},                ],            },            {label: 'B2', value: 'b2'},        ],    },]):
    The Tree Data.

- defaultExpandAll (boolean; default False):
    Whether to expand all nodes by default.

- placement (string; default 'bottomStart'):
    The placement of the popup. Can be 'bottomStart', 'bottomEnd',
    'topStart', 'topEnd'.

- selected (list of strings; optional):
    Selected value(s).

- style (dict; optional):
    Custom styling of the component."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_rsuite_components'
    _type = 'CheckTreePicker'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, appearance=Component.UNDEFINED, block=Component.UNDEFINED, cascade=Component.UNDEFINED, cleanable=Component.UNDEFINED, countable=Component.UNDEFINED, data=Component.UNDEFINED, custom_locale=Component.UNDEFINED, defaultExpandAll=Component.UNDEFINED, placement=Component.UNDEFINED, selected=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'appearance', 'block', 'cascade', 'cleanable', 'countable', 'custom_locale', 'data', 'defaultExpandAll', 'placement', 'selected', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'appearance', 'block', 'cascade', 'cleanable', 'countable', 'custom_locale', 'data', 'defaultExpandAll', 'placement', 'selected', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(CheckTreePicker, self).__init__(**args)
