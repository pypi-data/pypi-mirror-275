# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class TreeStructureSvg(Component):
    """A TreeStructureSvg component.


Keyword arguments:

- branchTee (list; optional)

- treeLeaves (list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'phylogenetic_tree_vis_comp'
    _type = 'TreeStructureSvg'
    @_explicitize_args
    def __init__(self, treeLeaves=Component.UNDEFINED, branchTee=Component.UNDEFINED, **kwargs):
        self._prop_names = ['branchTee', 'treeLeaves']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['branchTee', 'treeLeaves']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(TreeStructureSvg, self).__init__(**args)
