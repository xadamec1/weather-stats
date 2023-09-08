import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass
class ScrapedWeather:
    url: str
    temperature: float
    date: datetime.date


class GenericParser(ABC):

    @abstractmethod
    def parse(self) -> ScrapedWeather:
        pass
