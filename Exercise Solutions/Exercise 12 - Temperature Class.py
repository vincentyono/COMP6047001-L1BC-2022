class Temperature:
    # constructor
    def __init__(self, celsius: float):
        # Private property
        self.__celsius = celsius

    def to_celsius(self) -> float:
        return round(self.__celsius, 2)

    def to_fahrenheit(self) -> float:
        return round((self.__celsius * (9 / 5)) + 32, 2)

    def to_kelvin(self) -> float:
        return round(self.__celsius + 273.15, 2)

    def set_temperature(self, celsius: float) -> None:
        if celsius >= -273.15:
            self.__celsius = celsius

    def __str__(self):
        return f"Celsius: {self.to_celsius()}\nFahrenheit: {self.to_fahrenheit()}\nKelvin: {self.to_kelvin()}"


# Test Case
absolute_zero = Temperature(-273.15)

print(absolute_zero.to_celsius())  # Output: -273.15
print(absolute_zero.to_fahrenheit())  # Output: -459.67
print(absolute_zero.to_kelvin())  # Output: 0

print(absolute_zero)
# Output:
# Celsius: -273.15
# Fahrenheit: -459.67
# Kelvin: 0

water_boiling_point = Temperature(100)

print(water_boiling_point.to_celsius())  # Output: 100
print(water_boiling_point.to_fahrenheit())  # Output: 212
print(water_boiling_point.to_kelvin())  # Output: 373.15

print(water_boiling_point)
# Output:
# Celsius: 100
# Fahrenheit: 212
# Kelvin: 373.15

room_temperature = Temperature(20)

room_temperature.set_temperature(16)
room_temperature.set_temperature(-300)  # This shouldn't overwrite
print(room_temperature.to_celsius())  # Output: 16
print(room_temperature.to_fahrenheit())  # Output: 60.8
print(room_temperature.to_kelvin())  # Output: 289.15
