"""
see class documentation of `NetworkInterface` for more information

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

from typing import Optional

import requests

from islabtech_upw_sensor_v1._devices._implementations import Interface
from islabtech_upw_sensor_v1.measurements import Measurement, SuccessfulMeasurement
from islabtech_upw_sensor_v1.system_status import SystemStatus


class NetworkInterface(Interface):
    """
    implements the sensor interface (`islabtech_upw_sensor_v1._devices._implementations.Interface`)
    by querying the sensor's RESTful API via the network
    """

    _ip_address: str
    _port: int
    _tls: bool
    _timeout_ms: int

    def __init__(
        self,
        ip_address: str,
        port: int = 80,
        tls: Optional[bool] = None,
        timeout_ms=5000,
    ) -> None:
        super().__init__()
        self._ip_address = ip_address
        self._port = port
        self._tls = tls if tls is not None else (True if port == 443 else False)
        self._timeout_ms = timeout_ms
        self.test_connection()

    def _base_url(self) -> str:
        return (
            ("https" if self._tls else "http")
            + "://"
            + self._ip_address
            + ":"
            + str(self._port)
        )

    def test_connection(self) -> None:
        """tests that:
        1. a connection to the device can be established
        2. the device is indeed an UPW Sensor v1 by Ilka Schulz Labortechnik
        """
        system_status = self.system_status()
        assert system_status.product.vendor == "Ilka Schulz Labortechnik"
        assert system_status.product.name == "UPW Sensor v1"

    def latest_measurement(self) -> Optional[Measurement]:
        """this function is documented in _devices._implementations.interface.Interface"""
        response = requests.get(
            self._base_url() + "/api/v1/measurements/latest", timeout=self._timeout_ms
        )
        response.raise_for_status()
        response = response.json()
        return None if response is None else Measurement.from_json(response)

    def latest_successful_measurement(self) -> Optional[SuccessfulMeasurement]:
        """this function is documented in _devices._implementations.interface.Interface"""
        response = requests.get(
            self._base_url() + "/api/v1/measurements/latest_successful",
            timeout=self._timeout_ms,
        )
        response.raise_for_status()
        response = response.json()
        return None if response is None else SuccessfulMeasurement.from_json(response)

    def measurement_history(self) -> list[Measurement]:
        response = requests.get(
            self._base_url() + "/api/v1/measurements/all", timeout=self._timeout_ms
        )
        response.raise_for_status()
        return list(
            map(
                lambda x: None if x is None else Measurement.from_json(x),
                response.json()["values"],
            )
        )

    def system_status(self) -> SystemStatus:
        response = requests.get(
            self._base_url() + "/api/v1/system/status", timeout=self._timeout_ms
        )
        response.raise_for_status()
        response = response.json()
        return SystemStatus.from_json(response)
        # return make_dataclass(
        #     "SystemStatus", ((k, type(v)) for k, v in response.items())
        # )(**response)

    # @abstractmethod
    # def temperature_calibration(self):
    #     raise NotImplementedError()
    # @abstractmethod
    # def conductivity_calibration(self):
    #     raise NotImplementedError()
    #
    # def settings(self):
    #     raise NotImplementedError()
