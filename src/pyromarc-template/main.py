# -*- coding: utf-8 -*-
import log
from template import Template

if __name__ == "__main__":
    log.logger.info("start pyromarc template\n----------")

    url = "./spectest.yml"
    datas_mir = """
    - [001, PPNxxxx ]
    - [200, [ [a, Doe], [b, john], [b, elias], [b, frederik] ]]
    - [200, [ [a, Doe], [b, jane]                            ]]
    - [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
    """

    template_dict = """
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
        template.load_mir_data(datas_mir)
        log.logger.info("FROM DATA TO TEMPLATE\n----------")
        log.logger.info("Data: %s\n----------" % (template.datas,))
        log.logger.info("Template: %s\n\n" % (template.template,))
        template.load_dict_template(template_dict)
        log.logger.info("FROM TEMPLATE TO DATA\n----------")
        log.logger.info("Data: %s\n----------" % (template.datas,))
        log.logger.info("Template: %s\n\n" % (template.template,))
