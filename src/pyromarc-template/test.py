# -*- coding: utf-8 -*-
import unittest
from template import Template
import yaml


class TemplateTest(unittest.TestCase):

    """ unit test for template """

    def setUp(self):
        """ set up data """
        self.spec_yaml = """
            001: id
            200: [ authors, { a: name, b: firstname } ]
            300: { a: title, b: subtitle }
            700: [ auth_author, { a: name, b: firstname } ]
            701: [ auth_author, { a: name, b: firstname } ]
            002: code 
            400: { a: ville, b: adresse }
        """
        self.mir_yaml = """
            - [001, PPNxxxx ]
            - [002, toto ]
            - [200, [ [a, Doe], [b, elias], [b, frederik], [b, john] ]]
            - [200, [ [a, Doe], [b, jane]                            ]]
            - [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
            - [400, [ [a, "Strasbourg"], [b, "rue 1"], [b, "rue 2"]       ]]
        """
        self.data_yaml = """
            authors:
                - { name: Doe, firstname: [elias, frederik, john] }
                - { name: Doe, firstname: jane }
            title: "i can haz title"
            subtitle: "also subs"
            id: PPNxxxx
            code: toto
            adresse: [rue 1, rue 2]
            ville: Strasbourg
        """
        self.template = Template(yaml.safe_load(self.spec_yaml))

    def test_build_data_from_mir(self):
        """ test to build data from mir """
        self.template.build_data_from_mir(yaml.safe_load(self.mir_yaml))
        template_data_dump = yaml.dump(self.template.data)
        test_data_dump = yaml.dump(yaml.safe_load(self.data_yaml))
        self.assertEqual(template_data_dump, test_data_dump)

    def test_build_mir_from_data(self):
        """ test to build mir from data """
        self.template.build_mir_from_data(yaml.safe_load(self.data_yaml))
        template_mir_dump = yaml.dump(self.template.mir)
        test_mir_dump = yaml.dump(yaml.safe_load(self.mir_yaml))
        self.assertEqual(template_mir_dump, test_mir_dump)

if __name__ == '__main__':
    unittest.main()
