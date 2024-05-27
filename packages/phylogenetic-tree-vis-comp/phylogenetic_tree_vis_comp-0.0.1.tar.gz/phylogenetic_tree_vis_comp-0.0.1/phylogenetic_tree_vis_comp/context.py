# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class context(Component):
    """A context component.


Keyword arguments:

- children (dash component; optional)

- init (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'phylogenetic_tree_vis_comp'
    _type = 'context'
    @_explicitize_args
    def __init__(self, children=None, init=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'init']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'init']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(context, self).__init__(children=children, **args)
