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
from abc import abstractmethod, ABCMeta
from typing import Optional

from islabtech_upw_sensor_v1.measurements import Measurement, SuccessfulMeasurement
from islabtech_upw_sensor_v1.system_status import SystemStatus


class Interface(metaclass=ABCMeta):
    """
    abstract base class (interface) for sensor interface classes

    Other classes, e.g. `NetworkInterface` and `UsbInterface`, may be derived from this class.
    They are then used to implement this interface in `islabtech_upw_sensor.Device`
    (design pattern: TODO: name)
    """

    def measure(self) -> Measurement:
        """
        read the latest temperature and conductivity
        """
        return self.latest_measurement()

    @abstractmethod
    def latest_measurement(self) -> Optional[Measurement]:
        """
        returns the latest measurement (conductivity and temperature) available or `None` if the
        sensor has just booted and not measured anything yet

        Calling this funtion will not trigger a new measurement. It will merely fetch the latest
        measurement.
        """
        pass

    @abstractmethod
    def latest_successful_measurement(self) -> Optional[SuccessfulMeasurement]:
        """
        returns the latest successful measurement available or `None` if the sensor has never
        read a successful measurement since it booted

        Calling this funtion will not trigger a new measurement. It will merely fetch the latest
        measurement.
        """
        pass

    @abstractmethod
    def measurement_history(self) -> list[Measurement]:
        """
        fetch the entire measurement history from the sensor's cache. This can take some time...
        """
        pass

    @abstractmethod
    def system_status(self) -> SystemStatus:
        """
        fetch the device's system status

        See documentation of type [`SystemStatus`] for more information
        """
        pass

    # @abstractmethod
    # def temperature_calibration(self):
    #     pass
    # @abstractmethod
    # def conductivity_calibration(self):
    #     pass

    # @abstractmethod
    # def settings(self):
    #     pass
