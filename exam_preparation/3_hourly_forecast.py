def forecast(*data):
    result = []

    def add_location(type_of_location):   #type_of_location = Sunny or Cloudy or Rainy
        locations = []

        for location, weather in data:
            if weather == type_of_location:
                locations.append(location)

        for l in locations:
            result.append(f"{l} - {type_of_location}")

    add_location("Sunny")
    add_location("Cloudy")
    add_location("Rainy")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
