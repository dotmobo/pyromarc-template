# -*- coding: utf-8 -*-
import log

""" 
Pyromarc-template
-----------------
Mir/data convertion with a spec
"""


class Template(object):

    """ Template class to convert mir/data """

    def __init__(self, spec):
        """ load the spec into dict """
        self.spec = spec
        self.mir = []
        self.data = {}

    def _do_mir_multivalue(self, d, key, value):
        """ do mir multivalue """
        if key in d:
            if isinstance(d[key], list):
                d[key].append(value)
            else:
                d[key] = [d[key], value]
        else:
            d[key] = value

        return d

    def _load_mir_str(self, tab):
        """ load mir str """
        return {self.spec[tab[0]]: tab[1], }

    def _load_mir_dict(self, tab):
        """ load mir dict """
        d = {}
        for elem in tab[1]:
            key = self.spec[tab[0]][elem[0]]
            value = elem[1]
            d = self._do_mir_multivalue(d, key, value)

        return d

    def _load_mir_list(self, tab):
        """ load mir list """
        subdict = {}
        for elem in tab[1]:
            key = self.spec[tab[0]][1][elem[0]]
            value = elem[1]
            d = self._do_mir_multivalue(subdict, key, value)

        return [subdict, ]

    def build_data_from_mir(self, mir):
        """ build data from mir """
        self.mir = mir
        self.data = {}
        for tab in self.mir:
            try:
                spec_value = self.spec[tab[0]]
                if isinstance(spec_value, str):
                    self.data.update(self._load_mir_str(tab))
                elif isinstance(spec_value, dict):
                    self.data.update(self._load_mir_dict(tab))
                elif isinstance(spec_value, list):
                    parent_key = spec_value[0]
                    if parent_key in self.data:
                        self.data[parent_key] += self._load_mir_list(tab)
                    else:
                        self.data.update(
                            {parent_key: self._load_mir_list(tab), })
            except KeyError as e:
                log.logger.warn("Spec %s doesn't exist" % (tab[0],))

    def _do_data_multivalue(self, d, v):
        """ do data multivalue """
        l = []
        for subkey, subvalue in d.items():
            if isinstance(v[subvalue], list):
                for i in v[subvalue]:
                    l.append([subkey, i])
            else:
                l.append([subkey, v[subvalue]])
        return l

    def _load_data_str(self, key, value):
        """ load data str """
        return [key, self.data[value]]

    def _load_data_dict(self, key, value):
        """ load data dict """
        l = self._do_data_multivalue(value, self.data)
        return [key, sorted(l)]

    def _load_data_list(self, key, value):
        """ load data list """
        parent_key = value[0]
        return_list = []
        if parent_key in self.data:
            for line in self.data[parent_key]:
                l = self._do_data_multivalue(value[1], line)
                return_list.append([key, sorted(l)])

        return return_list

    def build_mir_from_data(self, data):
        """ build mir from data """
        self.data = data
        self.mir = []
        try:
            for key, value in self.spec.items():
                if isinstance(value, str):
                    self.mir.append(self._load_data_str(key, value))
                elif isinstance(value, dict):
                    self.mir.append(self._load_data_dict(key, value))
                elif isinstance(value, list):
                    self.mir += self._load_data_list(key, value)
        except KeyError as e:
            log.logger.warn("Key %s doesn't exist" % (key,))

        self.mir = sorted(self.mir)
