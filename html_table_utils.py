import bs4.element
from bs4 import BeautifulSoup
import re


def get_tables(content, table_name):
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table', class_=table_name)
    return tables


def get_table_header(table):
    heads = table.find_all('th')

    return heads


def get_table_rows(table):
    rows = table.find_all('tr')

    return rows


def get_row_data(row):
    data_cells = row.find_all('td')

    return data_cells


def get_cell_data_tag(cell_data):
    cell_data_tag = BeautifulSoup(str(cell_data), 'html.parser').find('td')
    return cell_data_tag


def is_a_tag(cell_data_tag):
    a_tag = cell_data_tag.find_all('a')
    if a_tag:
        return True
    else:
        return False


def get_a_tag(cell_data_tag):
    a_tag = cell_data_tag.find('a')
    return a_tag


def parse_a_tag(a_tag):
    _list = []
    _title = a_tag.get('title')
    _text = a_tag.text

    if _text is not None and _title is not None:
        if _title.lower() != _text.lower():
            _name = _text
        else:
            _name = _title
        _list = [word.strip() for word in re.split(r',|;|&|/', _name)]
    elif _title is not None:
        _list.append(_title)

    return _list


def parse_sup_tag(tag):
    if type(tag.next_sibling) == bs4.element.NavigableString:
        _text = tag.next_sibling.strip()
        _text = ''.join([i for i in _text if i.isalpha()])
        if len(_text) > 0:
            return _text
    return None


def parse_br_tag(tag):
    if type(tag.next_sibling) == bs4.element.NavigableString:
        _text = tag.next_sibling.strip()
        if len(_text) > 0:
            return _text
    return None


def parse_tag(tag):
    _list = []
    if not tag.contents:
        return _list

    first_content = tag.contents[0]

    if type(first_content) == bs4.element.NavigableString:
        _list = [word.strip() for word in re.split(r',|;|&|/', first_content.strip())]

    all_tags = tag.find_all()
    ignore_a_tag = False
    for all_tag in all_tags:
        if all_tag.name == 'a' and ignore_a_tag is False:
            _list.extend(parse_a_tag(all_tag))
        elif all_tag.name == 'sup':
            sup_text = parse_sup_tag(all_tag)
            if sup_text is not None:
                _list.append(sup_text)

        elif all_tag.name == 'br':
            br_text = parse_br_tag(all_tag)
            if br_text is not None:
                _list.append(br_text)

        # ignore a tag if it's not the first tag
        ignore_a_tag = True

    if "?" in _list:
        return []

    return _list


def is_header_data_cell(data_cells):
    if len(data_cells) == 0:
        return True
    else:
        return False
