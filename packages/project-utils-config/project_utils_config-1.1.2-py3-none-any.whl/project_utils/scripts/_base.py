import asyncio

from abc import ABCMeta, abstractmethod

from project_utils.conf import ConfigTemplate


class BaseScript(metaclass=ABCMeta):
    config: ConfigTemplate

    def __init__(self, config: ConfigTemplate):
        self.config = config
        self.loop = asyncio.get_event_loop()

    def async_start(self, *args, **kwargs):
        self.loop.run_until_complete(self.handler(*args, **kwargs))

    @abstractmethod
    async def handler(self, *args, **kwargs):
        ...

    @classmethod
    def run(cls, config: ConfigTemplate, *args, **kwargs):
        this: cls = cls(config)
        return this.async_start(*args, **kwargs)
