import json
import json2table


class AnimalDictionary(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AnimalDictionary, cls).__new__(cls)
        return cls.instance

    _dict = {}

    def setName(self, name, adj):
        self._dict[name] = adj

    def getName(self, name):
        return self._dict[name]

    def getAll(self):
        return self._dict

    def is_in_table(self, name):
        if name in self._dict:
            return True
        else:
            return False

    def convert_to_html(self):
        formatted_data = [{"animal": key, "collateral_adjective": value} for key, value in self._dict.items()]
        _json = json.dumps(formatted_data)
        infoFromJson = json.loads(_json)

        json_data = {
            "data": infoFromJson
        }

        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {
            "style": "width:100%",
            "border": 1
        }
        self._html = (json2table.convert(json_data,
                                   build_direction=build_direction,
                                   table_attributes=table_attributes))

    def get_html(self):
        return self._html


