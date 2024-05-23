# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashSpreadGrid(Component):
    """A DashSpreadGrid component.


Keyword arguments:

- id (string; optional)

- active_columns (list; optional)

- active_rows (list; optional)

- borderWidth (number; default 1)

- clicked_cell (dict; optional)

- clicked_custom_cell (dict; optional)

- columnWidths (list; optional)

- columns (list; default [{ "type": "DATA-BLOCK" }])

- data (boolean | number | string | dict | list; optional)

- data_selector (string; default "data[row.id][column.id]")

- edited_cells (list; optional)

- filtering (list; optional)

- filters (list; optional)

- focusedCell (dict; optional)

- formatting (list; optional)

- highlightedCells (list; optional)

- pinned_bottom (number; default 0)

- pinned_left (number; default 0)

- pinned_right (number; default 0)

- pinned_top (number; default 0)

- rowHeights (list; optional)

- rows (list; default [{ "type": "HEADER" }, { "type": "DATA-BLOCK" }])

- selected_cells (list; optional)

- sortBy (list; optional)

- sorting (list; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_spread_grid'
    _type = 'DashSpreadGrid'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, columns=Component.UNDEFINED, rows=Component.UNDEFINED, formatting=Component.UNDEFINED, filtering=Component.UNDEFINED, sorting=Component.UNDEFINED, data_selector=Component.UNDEFINED, pinned_top=Component.UNDEFINED, pinned_bottom=Component.UNDEFINED, pinned_left=Component.UNDEFINED, pinned_right=Component.UNDEFINED, borderWidth=Component.UNDEFINED, focusedCell=Component.UNDEFINED, selected_cells=Component.UNDEFINED, highlightedCells=Component.UNDEFINED, edited_cells=Component.UNDEFINED, filters=Component.UNDEFINED, sortBy=Component.UNDEFINED, columnWidths=Component.UNDEFINED, rowHeights=Component.UNDEFINED, clicked_cell=Component.UNDEFINED, clicked_custom_cell=Component.UNDEFINED, active_columns=Component.UNDEFINED, active_rows=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'active_columns', 'active_rows', 'borderWidth', 'clicked_cell', 'clicked_custom_cell', 'columnWidths', 'columns', 'data', 'data_selector', 'edited_cells', 'filtering', 'filters', 'focusedCell', 'formatting', 'highlightedCells', 'pinned_bottom', 'pinned_left', 'pinned_right', 'pinned_top', 'rowHeights', 'rows', 'selected_cells', 'sortBy', 'sorting']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'active_columns', 'active_rows', 'borderWidth', 'clicked_cell', 'clicked_custom_cell', 'columnWidths', 'columns', 'data', 'data_selector', 'edited_cells', 'filtering', 'filters', 'focusedCell', 'formatting', 'highlightedCells', 'pinned_bottom', 'pinned_left', 'pinned_right', 'pinned_top', 'rowHeights', 'rows', 'selected_cells', 'sortBy', 'sorting']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashSpreadGrid, self).__init__(**args)
