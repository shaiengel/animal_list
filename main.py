import requests
import table_parser
import route

collateral_adjective = 'Collateral adjective'
animal_column = ['Trivial name', 'Animal']
table_name = 'wikitable sortable'

if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_animal_names'
    site = requests.get(url)

    # parse table from site
    table_parser.read_and_parse_table(site.content, table_name, animal_column, collateral_adjective)

    # start server
    route.start_routing()
