import wmi


# Returns the CPU's temperature
def getTemp():
    try:
        w = wmi.WMI(namespace="root\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]

        kelvin_temperature = temperature_info.CurrentTemperature / 10.0
        celsius_temperature = kelvin_temperature - 273.1
        return str(round(celsius_temperature, 1)) + " C"
    except wmi.x_access_denied:
        # Handle permission error here
        return "Run as Admin to use WMI"
