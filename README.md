pyromarc-template
=================

Templating system for pyromarc : https://github.com/agrausem/pyromarc

Install
-------

- Install python3.3
- Install pyyaml (if you use yaml)
- Clone the project

Use with yaml
-------------

- Import :

```
import log
from template import Template
import yaml
```

- To build data from mir :

```
template = Template(yaml.safe_load("...YAML SPEC..."))
template.build_data_from_mir(yaml.safe_load("...YAML MIR..."))
my_yaml_data = yaml.dump(template.data)
```

- To build mir from data :

```
template = Template(yaml.safe_load("...YAML SPEC..."))
template.build_mir_from_data(yaml.safe_load("...YAML DATA..."))
my_yaml_mir = yaml.dump(template.mir)
```

- For example, see the main.py file

Test
----

- To run test, launch : 
```
python test.py
```
