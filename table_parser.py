import html_table_utils
import animal_dictionary
import re


def get_table_column(table, name, adjective):
    heads = html_table_utils.get_table_header(table)
    animal_column_index = 0
    for head in heads:
        if head.getText().strip() == name:
            break
        animal_column_index += 1

    adjective_column_index = 0
    for head in heads:
        if head.getText().strip() == adjective:
            break
        adjective_column_index += 1

    return animal_column_index, adjective_column_index


def get_list_from_cell(cell_data):
    cell_data_tag = html_table_utils.get_cell_data_tag(cell_data)

    _list = html_table_utils.parse_tag(cell_data_tag)

    return _list


""""
def check_plural(name):
    _dict = animal_dictionary.AnimalDictionary()
    if _dict.is_in_table(name + 's'):
        return name + 's'
    if name[-1] == 's':
        if _dict.is_in_table(name[:-1]):
            return name[:-1]
    return name
"""


def remove_parenthesis(adj_list):
    _list = []
    for adj in adj_list:
        if adj.find('(') != -1:
            index = adj.find('(')
            _list.append(adj[:index - 1].strip())
        else:
            _list.append(adj)
    return _list


def parse_table(table, name_index, adj_index):
    _dict = animal_dictionary.AnimalDictionary()
    rows = html_table_utils.get_table_rows(table)
    for row in rows:
        data_cells = html_table_utils.get_row_data(row)

        if html_table_utils.is_header_data_cell(data_cells):
            continue

        animal_list = get_list_from_cell(data_cells[name_index])
        adj_list = get_list_from_cell(data_cells[adj_index])

        if len(adj_list) == 0:
            continue

        adj_list = remove_parenthesis(adj_list)

        for animal in animal_list:
            _dict.setName(animal.lower(), adj_list)


def read_and_parse_table(content, table_name, animal_column, collateral_adjective):
    tables = html_table_utils.get_tables(content, table_name)
    i = 0
    for table in tables:
        animal_column_index, adjective_column_index = get_table_column(table, animal_column[i], collateral_adjective)
        parse_table(table, animal_column_index, adjective_column_index)
        i += 1

    _dict = animal_dictionary.AnimalDictionary()
    _dict.convert_to_html()
