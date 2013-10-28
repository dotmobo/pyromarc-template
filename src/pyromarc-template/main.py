# -*- coding: utf-8 -*-
import log
from template import Template

if __name__=="__main__":
    log.logger.info("start pyromarc template")
    
    url = "/home/morgan/dev/pyromarc-template/src/pyromarc-template/spectest.yml"
    datas = """
    - [001, PPNxxxx ]
    - [200, [ [a, Doe], [b, john], [b, elias], [b, frederik] ]]
    - [200, [ [a, Doe], [b, jane]                            ]]
    - [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
    """
    
    with open(url) as f:
        template = Template(f)
        template.load_mir_data(datas)

    log.logger.info("Spec: %s" % (template.spec,))
    log.logger.info("Data: %s" % (template.datas,))
    log.logger.info("Template: %s" % (template.template,))

