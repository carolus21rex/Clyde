import wmi


def getTemp():
    w = wmi.WMI(namespace="root\wmi")
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]

    kelvin_temperature = temperature_info.CurrentTemperature / 10.0
    celsius_temperature = kelvin_temperature - 273.15
    return str(round(celsius_temperature, 1))
