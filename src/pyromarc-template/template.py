# -*- coding: utf-8 -*-
import yaml
import types

""" 
Pyromarc-template
-----------------
Mir/data convertion with a yaml spec
"""


class Template(object):

    """ Template class to convert mir/data """

    def __init__(self, spec):
        """ load the yaml file into dict """
        self.spec = yaml.safe_load(spec)
        self.mir = []
        self.data = {}

    def _load_mir_str(self, tab):
        """ load mir str """
        return {self.spec[tab[0]]: tab[1], }

    def _load_mir_dict(self, tab):
        """ load mir dict """
        return {self.spec[tab[0]][elem[0]]: elem[1] for elem in tab[1]}

    def _load_mir_list(self, tab):
        """ load mir list """
        subdict = {}
        for elem in tab[1]:
            key = self.spec[tab[0]][1][elem[0]]
            value = elem[1]

            if key in subdict:
                if isinstance(subdict[key], list):
                    subdict[key].append(value)
                else:
                    subdict[key] = [subdict[key], value]
            else:
                subdict[key] = value

        return [subdict, ]

    def build_data_from_mir(self, mir_yaml):
        """ build data from mir """
        self.mir = yaml.safe_load(mir_yaml)
        self.data = {}
        for tab in self.mir:
            spec_value = self.spec[tab[0]]
            if isinstance(spec_value, str):
                self.data.update(self._load_mir_str(tab))
            elif isinstance(spec_value, dict):
                self.data.update(self._load_mir_dict(tab))
            elif isinstance(spec_value, list):
                parent_key = spec_value[0]
                if parent_key in self.data:
                    concat_list = self._load_mir_list(
                        tab) + self.data[parent_key]
                    self.data[parent_key] = concat_list
                else:
                    self.data.update(
                        {parent_key: self._load_mir_list(tab), })

    def _load_data_str(self, key, value):
        """ load data str """
        return [key, self.data[value]]

    def _load_data_dict(self, key, value):
        """ load data dict """
        l = []
        for subkey, subvalue in value.items():
            l.append([subkey, self.data[subvalue]])
        return [key, sorted(l)]

    def _load_data_list(self, key, value):
        """ load data list """
        parent_key = value[0]
        return_list = []
        if parent_key in self.data:
            parent_list = self.data[parent_key]
            l2 = []
            for line in parent_list:
                l = []
                for subkey, subvalue in value[1].items():
                    if isinstance(line[subvalue], list):
                        for i in line[subvalue]:
                            l.append([subkey, i])
                    else:
                        l.append([subkey, line[subvalue]])
                l2.append([key, sorted(l)])
            return_list += l2

        return return_list

    def build_mir_from_data(self, data_yaml):
        """ build mir from data """
        self.data = yaml.safe_load(data_yaml)
        self.mir = []

        for key, value in self.spec.items():
            if isinstance(value, str):
                self.mir.append(self._load_data_str(key, value))
            elif isinstance(value, dict):
                self.mir.append(self._load_data_dict(key, value))
            elif isinstance(value, list):
                self.mir += self._load_data_list(key, value)

        self.mir = sorted(self.mir)

    def get_yaml_data(self):
        """ get yaml data """
        return yaml.dump(self.data)

    def get_yaml_mir(self):
        """ get yaml mir """
        return yaml.dump(self.mir)
