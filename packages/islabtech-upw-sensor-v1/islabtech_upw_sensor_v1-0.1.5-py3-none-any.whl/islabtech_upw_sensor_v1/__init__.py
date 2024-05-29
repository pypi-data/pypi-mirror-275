"""
client library to connect to ISLabTech UPW Sensor

connect to your device with `Device.connect_via_network`

Example:
    ```
    import islabtech_upw_sensor_v1 as upw
    from time import sleep

    sensor = upw.Device.connect_via_network("192.168.x.x") # insert sensor IP address
    while True:
        print(sensor.latest_measurement())
        sleep(1)
    ```

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

from islabtech_upw_sensor_v1._devices import Device
