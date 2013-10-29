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


Data representation with yaml
-----------------------------

- Spec:

```
001: id
200: [ authors, { a: name, b: firstname } ]
300: { a: title, b: subtitle }
700: [ auth_author, { a: name, b: firstname } ]
701: [ auth_author, { a: name, b: firstname } ]
```

- Mir :

```
- [001, PPNxxxx ]
- [200, [ [a, Doe], [b, john], [b, elias], [b, frederik] ]]
- [200, [ [a, Doe], [b, jane]                            ]]
- [300, [ [a, "i can haz title"], [b, "also subs"]       ]]
```

- Data :

```
authors:
    - { name: Doe, firstname: [john, elias, frederik] }
    - { name: Doe, firstname: jane }
title: "i can haz title"
subtitle: "also subs"
id: PPNxxxx
```
