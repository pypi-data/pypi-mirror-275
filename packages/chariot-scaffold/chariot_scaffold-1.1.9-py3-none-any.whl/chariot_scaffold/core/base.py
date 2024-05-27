import abc
from chariot_scaffold import data_mapping, log
from chariot_scaffold.core.config import Lang


class Base(metaclass=abc.ABCMeta):
    def __init__(self, title=None, description=None, model=None):
        self.__vars_name = None
        self.__defaults = None
        self.__comments = None
        self.__annotations = None
        self.__params_name = None
        self._func_name = None

        self.model = model
        self.title = title
        self.description = description

        self.input = {}
        self.output = {}

    def __call__(self, func):
        self.bind_func_info(func)
        self.generate_func_info()
        self.hook()

        def wrapper(*args, **kwargs):
            mapping = self.get_params_mapping(*args, **kwargs)
            if self.model:
                self.check_model(mapping)

            res = func(*args, **kwargs)
            return res
        return wrapper

    def generate_func_info(self):
        self.bind_param()
        self.bind_datatype()
        self.bind_defaults()
        self.bind_comments()
        self.bind_output()

    def bind_func_info(self, func):
        self.__vars_name = func.__code__.co_varnames
        self.__params_name = [self.__vars_name[i] for i in range(func.__code__.co_argcount)]  # 参数名
        self.__annotations = func.__annotations__ # 注解
        self.__comments = func.__doc__ # 注释
        self.__defaults = func.__defaults__ # 默认值
        self._func_name = func.__name__

    def bind_param(self):
        """
        绑定参数名
        """
        for i in self.__params_name:
            if i != 'self':
                self.input[i] = {"name": i, "default": None, "title": None, "description": None, "type": None, "required": False}

    def bind_datatype(self):
        """
        绑定数据类型
        """
        # 注解参数类型映射绑定
        for i in self.__params_name:
            if i != "self":
                anno = self.__annotations.get(i)
                if anno.__name__ == "Annotated":
                    self.input[i]["type"] =  self.match_datatype(anno.__origin__)
                else:
                    self.input[i]["type"] = self.match_datatype(anno)

    @staticmethod
    def match_datatype(anno):
        # 用来匹配映射数据类型
        match str(type(anno)):
            case "<class 'type'>" | "<class 'types.GenericAlias'>":
                return data_mapping[str(anno)].__name__
            case "<class 'typing.NewType'>":
                return anno.__name__
            case _:
                log.warning(f"发现未适配的类型：{anno}, {str(type(anno))}")

    def bind_defaults(self):
        """
        绑定default默认值
        """
        # required和default属性绑定
        defaults_length = len(self.__defaults) if self.__defaults else 0

        # 参考python传参机制
        re_params_name = self.__params_name[::-1]                       # 翻转参数名的意义是python的默认值是从后往前找的
        re_defaults = self.__defaults[::-1] if defaults_length else []  # 默认值同上从后往前匹配， 注意空列表无法翻转

        for i in range(len(self.__params_name)):
            if re_params_name[i] != 'self':
                # 有默认值可以不传参, 无默认值则必传
                if i < defaults_length:
                    self.input[re_params_name[i]]["default"] = re_defaults[i]

                    if self.input[re_params_name[i]]["default"] is None:  # 参数类型为list,dict的默认值为None的全部处理成[],{}
                        if self.input[re_params_name[i]]["type"] == "[]string":     # 千乘array,object类型无法传入null
                            self.input[re_params_name[i]]["default"] = []
                        if self.input[re_params_name[i]]["type"] == "[]object":
                            self.input[re_params_name[i]]["default"] = {}

                    # 默认值映射枚举, 枚举类型默认值第一个
                    if str(type(self.input[re_params_name[i]]["default"].__class__)) == "<class 'enum.EnumMeta'>":
                        self.input[re_params_name[i]]["enum"] = [i.value for i in list(self.input[re_params_name[i]]["default"].__class__)]
                        self.input[re_params_name[i]]["default"] = self.input[re_params_name[i]]["default"].value

                else:
                    self.input[re_params_name[i]]["required"] = True

    def bind_comments(self):
        """
        绑定title和description
        """
        for i in self.__params_name:
            if i != "self":
                anno = self.__annotations.get(i)
                if "Annotated" in str(anno):
                    assert len(anno.__metadata__) == 2, "既然决定用Annotated了,那就把title, description都写了吧"

                    # 兼容过去默认绑定中文的插件, 引用Lang一键管理语言和值的关系
                    self.input[i]["title"] =        self.lang_checking(anno.__metadata__[0])
                    self.input[i]["description"] =  self.lang_checking(anno.__metadata__[1])

                else:
                    self.input[i]["title"] = self.lang_checking(i)
                    self.input[i]["description"] = self.lang_checking(i)



    def bind_output(self):
        """
        绑定output
        """
        output_type = self.__annotations.get("return")

        if output_type:
            # 返回值注解绑定
            if type(output_type) is dict:
                for k, v in output_type.items():
                    assert type(v).__name__ == "_AnnotatedAlias", "请使用Annotated作为返回值的注解"
                    assert len(v.__metadata__) == 2, "既然决定用Annotated了,那就把title, description都写了吧"

                    # 兼容过去默认绑定中文的插件, 引用Lang一键管理语言和值的关系
                    output = {
                        "title": self.lang_checking(v.__metadata__[0]),
                        "description": self.lang_checking(v.__metadata__[1]),
                        "type": self.match_datatype(v.__origin__)
                    }
                    self.output[k] = output

            else:
                # 返回值默认绑定
                self.output["output"] = {}
                self.output["output"]["type"] = self.match_datatype(output_type)
                # self.output["output"]["required"] = True

    def check_model(self, kwargs):
        """
        参数强类型校验
        :param kwargs: 参数
        :return: None
        """
        self.model(**kwargs)

    def get_params_mapping(self, *args, **kwargs) -> dict:
        """
        绑定args、kwargs与参数之间的映射关系, 便于强类型校验使用
        :param args:
        :param kwargs:
        :return: mapping
        """
        mapping = {}

        # 先绑定默认值
        if self.__defaults:
            for i in range(len(self.__defaults)):
                mapping[list(self.__params_name)[::-1][i]] = list(self.__defaults)[::-1][i]

        # 再按顺序填入arg
        for i in range(len(args)):
            if self.__params_name[i] != "self":
                mapping[self.__params_name[i]] = args[i]

        # 最后合并kwargs
        mapping.update(kwargs)
        return mapping

    @staticmethod
    def lang_checking(param):    # 兼容过去默认绑定中文的插件
        if isinstance(param, str):
            return {"zh-CN": param}
        elif isinstance(param, Lang):
            return param.convert()

    @abc.abstractmethod
    def hook(self):
        ...