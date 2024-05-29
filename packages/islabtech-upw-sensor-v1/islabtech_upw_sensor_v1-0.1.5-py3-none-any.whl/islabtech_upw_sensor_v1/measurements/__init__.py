"""
Copyright 2023 Ilka Schulz Labortechnik UG (haftungsbeschränkt)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

# from abc import staticmethod
import datetime


@dataclass
class Measurement:
    timestamp: datetime.datetime

    temperature: Optional[float]
    """
    the temperature value in °C
    
    This value can be `None` if the temperature reading failed – also see `Successful Measurement`
    """

    conductivity: Optional[float]
    """
    the conductivity value in µS/cm

    This value can be `None` if the conductivity reading failed – also see `SuccessfulMeasurement`
    """

    @staticmethod
    def from_json(data: dict) -> Measurement:
        timestamp: datetime.datetime = datetime.datetime.fromtimestamp(
            data["epoch_timestamp"], datetime.UTC
        )
        timestamp = timestamp.replace(microsecond=data["epoch_microseconds"])
        point = Measurement(
            timestamp=timestamp,
            temperature=data["temperature"],
            conductivity=data["conductivity"],
        )
        point.timestamp.replace(microsecond=data["epoch_microseconds"])
        return point

    def __str__(self) -> str:
        timestamp = self.timestamp.astimezone().strftime("%Y/%m/%d, %H:%M:%S.%f")[:-3]
        cond = None if self.conductivity is None else f"{self.conductivity} µS/cm"
        temp = None if self.temperature is None else f"{self.temperature} °C"
        return f'Measurement(timestamp="{timestamp}", conductivity={cond}, temperature={temp})'


@dataclass
class SuccessfulMeasurement:
    timestamp: datetime.datetime

    temperature: float
    """
    the temperature value in °C

    This value can be `None` if the temperature reading failed
    """

    conductivity: float
    """
    the conductivity value in µS/cm
    """

    @staticmethod
    def from_json(data: dict) -> SuccessfulMeasurement:
        timestamp = datetime.datetime.fromtimestamp(
            data["epoch_timestamp"], datetime.UTC
        )
        timestamp = timestamp.replace(microsecond=data["epoch_microseconds"])
        point = SuccessfulMeasurement(
            timestamp=timestamp,
            temperature=data["temperature"],
            conductivity=data["conductivity"],
        )
        point.timestamp.replace(microsecond=data["epoch_microseconds"])
        assert point.temperature is not None and point.conductivity is not None
        return point

    def __str__(self) -> str:
        timestamp = self.timestamp.astimezone().strftime("%Y/%m/%d, %H:%M:%S.%f")[:-3]
        return f'SuccessfulMeasurement(timestamp="{timestamp}, conductivity={self.conductivity} µS/cm, temperature={self.temperature} °C)'
