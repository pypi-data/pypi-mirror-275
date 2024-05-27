from pydantic import BaseModel
from typing import Annotated

class PluginSpecYamlModel(BaseModel):
    plugin_spec_version:  Annotated[str, ""] = "v2"
    extension: Annotated[str, "plugin"] = "plugin"
    entrypoint: Annotated[str, "程序入口"] = None
    module: Annotated[str, "模块名称"] = None
    name: Annotated[str, "插件id, 唯一id"] = None
    title: Annotated[str | dict, "插件名称"] = None
    description: Annotated[str | dict, "插件描述"] = None
    version: Annotated[str, "插件版本"] = "0.1.0"
    vendor: Annotated[str, "插件作者"] = "chariot"
    tags: Annotated[list, "插件标签"] = []
    connection: Annotated[dict, "插件连接器"] = {}
    actions: Annotated[dict, "插件动作"] = {}
    alarm_receivers: Annotated[dict, "告警接收器"] = {}
    asset_receivers: Annotated[dict, "资产接收器"] = {}

