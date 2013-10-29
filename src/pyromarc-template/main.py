# -*- coding: utf-8 -*-
import log
from template import Template

if __name__ == "__main__":
    log.logger.info("start pyromarc template\n----------")

    url = "./spectest.yml"
    mir_yaml = """
    - [001, PPNxxxx ]
    - [200, [ [a, Doe], [b, john], [b, elias], [b, frederik] ]]
    - [200, [ [a, Doe], [b, jane]                            ]]
    - [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
    """

    data_yaml = """
    authors:
        - { name: Doe, firstname: [john, elias, frederik] }
        - { name: Doe, firstname: jane }
    title: "i can haz title"
    subtitle: "also subs"
    id: PPNxxxx
    """

    with open(url) as f:
        template = Template(f)
        log.logger.info("Spec: %s\n----------\n" % (template.spec,))
        template.build_data_from_mir(mir_yaml)
        log.logger.info("BUILD DATA FROM MIR\n----------")
        log.logger.info("Mir: %s\n----------" % (template.mir,))
        log.logger.info("Mir Yaml: %s\n----------" % (template.get_yaml_mir(),))
        log.logger.info("Data: %s\n\n" % (template.data,))
        log.logger.info("Data Yaml: %s\n\n" % (template.get_yaml_data(),))
        template.build_mir_from_data(data_yaml)
        log.logger.info("BUILD MIR FROM DATA\n----------")
        log.logger.info("Mir: %s\n----------" % (template.mir,))
        log.logger.info("Mir Yaml: %s\n----------" % (template.get_yaml_mir(),))
        log.logger.info("Data: %s\n\n" % (template.data,))
        log.logger.info("Data Yaml: %s\n\n" % (template.get_yaml_data(),))
