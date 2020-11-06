from jinja2 import Template, Environment, FileSystemLoader
from traitlets.config.loader import PyFileConfigLoader
from pathlib import Path

p = Path(__file__).with_name("config.py")
loader = PyFileConfigLoader(str(p))
c = loader.load_config()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')
rendered = template.render(data=c.data)

with open("index.html", "w") as fp:
    fp.write(rendered)
