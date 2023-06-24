# PioT
dashboard for raspberry pi 

## Installation

1. Clone the repository: `git clone https://github.com/your/repository.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Make sure all hardware connections are properly set up.
2. Run the `main.py` script to initialize sensors and functions for data retrieval.
3. Start the Flask server by running `server.py`.
4. Access the following routes to retrieve sensor data:
    - Soil Moisture: `http://localhost:5000/soil-moisture`
    - Light: `http://localhost:5000/light`
    - Temperature and Humidity: `http://localhost:5000/temp-humid`
    - Video: `http://localhost:5000/video`
5. Customize the routes and functionality as per your project requirements.

## File Structure
* project_folder/
    * main.py
* server/
    * server.py
    * templates/
        * index.html


## Dependencies

- adafruit_seesaw
- RPi.GPIO
- board
- busio
- adafruit_sht4x
- adafruit_tsl2591
- opencv-python
- smbus2
- flask

## License

[MIT License](LICENSE)