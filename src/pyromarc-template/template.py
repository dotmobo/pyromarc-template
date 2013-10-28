# -*- coding: utf-8 -*-
import yaml
import types

""" 
Pyromarc-template
-----------------
Convert mir to dict with a yaml spec
"""


class Template(object):
    """ Template class to convert mir/dict """

    def __init__(self, spec):
        """ load the yaml file into dict """ 
        self.spec = yaml.safe_load(spec)
        self.datas = {}
        self.template = {}

    def _load_mir_str(self, data):
        """ load mir str """
        return {self.spec[data[0]] : data[1],}
        
    def _load_mir_dict(self, data):
        """ load mir dict """
        return {self.spec[data[0]][elem[0]]:elem[1] for elem in data[1]}

    def _load_mir_list(self, data):
        """ load mir list """
        subdict = {}
        for elem in data[1]:
            key = self.spec[data[0]][1][elem[0]]
            value = elem[1]

            if key in subdict:
                if isinstance(subdict[key], list):
                    subdict[key].append(value)
                else:
                    subdict[key] = [subdict[key], value ]
            else:
                subdict[key] = value 

        return [subdict,]

    def load_mir_data(self, datas):
        """ load mir data into template"""
        self.datas = yaml.safe_load(datas)
        for data in self.datas:
            spec_value = self.spec[data[0]] 
            if isinstance(spec_value, str):
                self.template.update(self._load_mir_str(data))
            elif isinstance(spec_value, dict):
                self.template.update(self._load_mir_dict(data))
            elif isinstance(spec_value, list):
                parent_key = spec_value[0]
                if parent_key in self.template:
                    concat_list = self._load_mir_list(data) + self.template[parent_key]
                    self.template[parent_key] = concat_list
                else:
                    self.template.update({parent_key: self._load_mir_list(data),})


