# coding=utf-8
import json
import os
import platform
import random
from typing import Optional, TypeVar, Any

T = TypeVar('T')


class Configuration:
    _default_instance: Optional['Configuration'] = None

    def __init__(self):
        self.base_dir = self._get_base_dir()

    @staticmethod
    def _get_base_dir():
        os_name = platform.system()
        if os_name in ['Windows', 'Darwin']:
            return './storage'
        return '/storage'

    @classmethod
    def _get_default_instance(cls) -> 'Configuration':
        if cls._default_instance is None:
            cls._default_instance = cls()

        return cls._default_instance

    @staticmethod
    def get_config_value(name: str, default: Any = None, parse_json: bool = False) -> Any:
        value = os.getenv(name)
        if value is None:
            return default

        if parse_json:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return default

        return value

    @classmethod
    def get_global_configuration(cls) -> 'Configuration':
        return cls._get_default_instance()

    @staticmethod
    def get_any_env(name: str) -> Any:
        return os.getenv(name.upper())

    @staticmethod
    def get_bool_env(name: str) -> bool:
        return os.getenv(name.upper(), 'false') == 'true'

    @staticmethod
    def get_int_env(name: str) -> int:
        return int(os.getenv(name.upper()))

    @staticmethod
    def get_float_env(name: str) -> float:
        return float(os.getenv(name.upper()))

    @staticmethod
    def get_string_env(name: str) -> str:
        return os.getenv(name.upper())

    @staticmethod
    def get_list_env(name: str) -> list:
        return [i.get('url') for i in json.loads(os.getenv(name.upper()))]

    @staticmethod
    def get_dict_env(name: str) -> dict:
        return json.loads(os.getenv(name.upper()))

    @staticmethod
    def get_proxy_list():
        proxy_url = os.getenv('proxy_url'.upper())
        if proxy_url:
            return proxy_url.split(',')

    def get_random_proxy(self):
        proxy_list = self.get_proxy_list()
        if proxy_list:
            return random.choice(proxy_list)
