import json
import yaml
import typing
from chariot_scaffold.schema.config_model import PluginSpecYamlModel


class Lang:
    def __init__(self, *arg, **kwargs):
        """
            Lang(1,2,lang=["zh-CN", "en"])
            Lang(1,2,lang=["zh-CN", "en"])
            arg应对lang中语言类型的两种写法, 可以只写一个, 默认中文
        """
        self.lang = kwargs.get("lang")
        if not self.lang:
            self.lang = ["zh-CN", "en"]
        self.arg = arg
        assert arg, "请传入正确的参数"
        assert len(self.lang) >= len(self.arg), "请按顺序传参"

    def convert(self):
        data = {i:None for i in self.lang}
        for i in range(len(self.arg)):
            data.update({self.lang[i]: self.arg[i]})
        return  data


class PluginSpecYaml(PluginSpecYamlModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __str__(self):
        return self.model_dump()

    def deserializer(self, yml=None):
        if yml:
            stream = open(yml, 'r', encoding='utf8').read()
        else:
            stream = open('plugin.spec.yaml', 'r', encoding='utf8').read()
        plugin_spec = yaml.safe_load(stream)
        PluginSpecYamlModel(**plugin_spec)
        self.__init__(**plugin_spec)


class DataMapping:
    def __init__(self):
        self.__data_mapping = {
            "<class 'int'>": Datatypes.integer,
            "<class 'float'>": Datatypes.float_,
            "<class 'str'>": Datatypes.string,
            "<class 'list'>": Datatypes.array,
            "<class 'dict'>": Datatypes.object_,
            "<class 'bool'>": Datatypes.boolean,
            "<built-in function any>": Datatypes.generic,
            "list[str]": Datatypes.array_str,
            "list[dict]": Datatypes.array_obj,
            "dist[str]": Datatypes.object_,
            "dist[int]": Datatypes.object_,
            "dist[float]": Datatypes.object_,
            "dist[list]": Datatypes.object_,
            "list[int]": Datatypes.array_int,
        }

    def __getitem__(self, item):
        return self.__data_mapping.get(item, "any")

    def __setitem__(self, key, value):
        self.__data_mapping[key] = value

    def __delitem__(self, key):
        self.__data_mapping.pop(key)

    def __repr__(self):
        return json.dumps(self.__data_mapping, ensure_ascii=False)


class Datatypes:
    object_ = typing.NewType("object", dict[any])
    array = typing.NewType("array", list[any])
    integer = typing.NewType("integer", int)
    float_ = typing.NewType("float", float)
    boolean = typing.NewType("boolean", bool)
    string = typing.NewType("string", str)
    generic = typing.NewType("any", str)
    array_str = typing.NewType("[]string", list[str])
    array_obj = typing.NewType("[]object", list[dict])
    array_int = typing.NewType("[]integer", list[int])
    text = typing.NewType("text", str)
    password = typing.NewType("password", str)
    date = typing.NewType("date", str)
    file = typing.NewType("file", dict)
    code = typing.NewType("code", str)
    python = typing.NewType("python", str)
