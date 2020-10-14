# randomizer
> Another Python random number generator

randomizer is a Python project that generates pseudorandom numbers from both time-based seeds and weather-based seeds.

randomizer was made with the intent to build a random function without using any pre-built or pre-defined random number generation functionality. I also wanted to explore API usage, so I incorporated [OpenWeather's](https://openweathermap.org) API for seed generation. 
## Installing

$ git clone https://github.com/arrianj/randomizer.git

Make an account on, and generate an API key from [OpenWeather.](https://openweathermap.org/guide)

Create a text file named 'key.txt' in the project folder.

Save your API key in key.txt. Do not put anything else in the file, only the API key value.

$ pip install -r requirements.txt

$ python main.py

## Seed Generation

* randomizer takes in a few different seed values, performs some equations on them, and generates a final result from those values.

* The first seed is based on the current microsecond

* Next, the second seed is generated from the current temperature in farenheit for Rapid City, SD, USA. Rapid City was chosen based on the results of [a 2014 study from fivethirtyeight](https://fivethirtyeight.com/features/which-city-has-the-most-unpredictable-weather/), where it was found to have a high variance in its temperature range

* Finally, the third seed is generated from the current wind speed in Buffalo, NY, USA. The same study referenced above was used to choose Buffalo for its variable wind conditions.

## Roadmap

There are a few things I am interested in working on if I revisit this project in the future

* Building a GUI for randomizer. randomizer currently only runs in a command line interface.

* Expand upon the seed generation and add new sources of entropy.

* Functionality for generating multiple numbers

## License

The code in this project is licensed under the MIT license.
