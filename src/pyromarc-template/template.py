# -*- coding: utf-8 -*-
import yaml
from logging.handlers import RotatingFileHandler
import log
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
        self.data = {}
        self.template = {}

    def _load_mir_str(self,d):
        """ load mir str """
        return {self.spec[d[0]] : d[1],}
        
    def _load_mir_dict(self, d):
        """ load mir dict """
        return {self.spec[d[0]][i[0]]:i[1] for i in d[1]}

    def _load_mir_list(self, d):
        """ load mir list """
        log.logger.info("TODO load_mir_list")
        return {}

    def load_mir_data(self, data):
        """ load mir data into template"""
        self.data = yaml.safe_load(data)
        for d in self.data:
            spec_value = self.spec[d[0]] 
            if isinstance(spec_value, str):
                self.template.update(self._load_mir_str(d))
            elif isinstance(spec_value, dict):
                self.template.update(self._load_mir_dict(d))
            elif isinstance(spec_value, list):
                self.template.update(self._load_mir_list(d))


if __name__=="__main__":
    log.logger.info("start pyromarc template")
    
    url = "/home/morgan/dev/pyromarc-template/src/pyromarc-template/spectest.yml"
    data = """
    - [001, PPNxxxx ]
    - [200, [ [a, Doe], [b, john], [b, elias], [b, frederik] ]]
    - [200, [ [a, Doe], [b, jane]                            ]]
    - [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
    """
    
    with open(url) as f:
        template = Template(f)
        template.load_mir_data(data)

    log.logger.info("Spec: %s" % (template.spec,))
    log.logger.info("Data: %s" % (template.data,))
    log.logger.info("Template: %s" % (template.template,))
