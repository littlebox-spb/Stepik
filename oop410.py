# Напишите определение классов Device Light Thermostat и SmartTV
class Device:
    __slots__ = ("_name", "_location", "_status")

    def __init__(self, _name, _location, _status="ON") -> None:
        self._name = _name
        self._location = _location
        self._status = _status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"


class Light(Device):
    __slots__ = ("_brightness", "_color")

    def __init__(self, _name, _location, _brightness, _color) -> None:
        super().__init__(_name, _location)
        self._brightness = _brightness
        self._color = _color

    @property
    def color(self):
        return self._color

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = value


class Thermostat(Device):
    __slots__ = ("_current_temperature", "_target_temperature")

    def __init__(self, _name, _location, _current_temperature, _target_temperature) -> None:
        super().__init__(_name, _location)
        self._current_temperature = _current_temperature
        self._target_temperature = _target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value


class SmartTV(Device):
    __slots__ = "_channel"

    def __init__(self, _name, _location, _channel) -> None:
        super().__init__(_name, _location)
        self._channel = _channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


# Код ниже не удаляйте, он нужен для проверок


device1 = Device("Устройство 1", "Гостиная")
assert device1.name == "Устройство 1"
assert device1._name == "Устройство 1"
assert device1.location == "Гостиная"
assert device1._location == "Гостиная"
assert device1.status == "ON"
assert device1._status == "ON"

device1.turn_off()
assert device1.status == "OFF"
device1.location = "Кухня"
assert device1.location == "Кухня"
assert device1._location == "Кухня"
device1.turn_on()
assert device1.status == "ON"

light1 = Light("Лампа", "Гостиная", 50, "белый")
light1.name == "Лампа"
light1.location == "Гостиная"
light1.status == "ON"
light1.brightness == "50"
light1.color == "белый"

light1.turn_off()
light1.status == "OFF"

thermostat_1 = Thermostat("Термометр", "Балкон", 10, 15)
thermostat_1.name == "Термометр"
thermostat_1.location == "Балкон"
thermostat_1.status == "ON"
thermostat_1.current_temperature == 10
thermostat_1.target_temperature == 15

tv = SmartTV("Samsung", "Спальня", 20)
tv.name == "Термометр"
tv.location == "Балкон"
tv.status == "ON"
tv.channel == 20

print("GOOD")
