from jinja2 import Environment, FileSystemLoader


class TemplatePropusk:
    def __init__(self, obj: any, env_dir: str, name_file: str = "template_propusk.html"):
        self._env = Environment(loader=FileSystemLoader(env_dir))
        self._obj = obj
        self._rederer_text = self._env.get_template(name_file).render(
            self._obj
        )

    def __str__(self) -> str:
        return self._rederer_text
    
    def get_object(self) -> any:
        return self._obj
