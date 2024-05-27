# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GridGeographicSvg(Component):
    """A GridGeographicSvg component.


Keyword arguments:

- links (list; optional)

- nodes (list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'phylogenetic_tree_vis_comp'
    _type = 'GridGeographicSvg'
    @_explicitize_args
    def __init__(self, nodes=Component.UNDEFINED, links=Component.UNDEFINED, **kwargs):
        self._prop_names = ['links', 'nodes']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['links', 'nodes']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GridGeographicSvg, self).__init__(**args)
