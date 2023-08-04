# rpi-digital-clock
This repository contains code that requires the `luma.core` library.

## luma.core
`luma.core` is a Python library that provides essential core functionality for interacting with various hardware interfaces to control displays, such as OLED and LCD screens. It offers a range of features and utilities to simplify the process of driving these displays, making it easier for developers to create engaging visual output for their projects.

Installation
To use the code in this repository, you'll need to install luma.core. You can install it using pip by running the following command:

```pip install luma.core```

For more detailed installation instructions and other options, please refer to the official luma.core repository on GitHub: https://github.com/rm-hull/luma.core

## Usage 
After installing all the necessary libraries, you can run the main.py file to execute the digital clock program with specific display configurations.

Open a terminal or command prompt, navigate to the directory where the main.py file is located, and then run the following command:

```python3 /home/pi/rpi-digital-clock/main.py -d sh1106 -i spi --rotate 2```

Explanation of the command-line options:

* `-d sh1106`: This option specifies the type of display to be used. In this case, it's set to sh1106, indicating the SH1106 OLED display.
* `-i spi`: This option selects the communication interface to communicate with the display. Here, it's set to spi, which stands for Serial Peripheral Interface, a common protocol for interfacing with various hardware devices.
* `--rotate 2`: This option determines the rotation of the displayed content on the screen. The value 2 signifies a 180-degree rotation.

Make sure you have properly connected your SH1106 OLED display to the Raspberry Pi and that it is compatible with the luma.core library. If everything is set up correctly, the digital clock program should start running, and you should see the clock displayed on your OLED screen.

in this project i use waveshare OLED HAT. Refer to the documentation on https://waveshare.com/wiki/1.3inch_OLED_HAT for detailed instructions on the wiring and setup.

![alt text](https://github.com/sptrheru/Rpi-digital-clock/blob/main/images/rpi-digital-clock.jpg?raw=true)

## License
Please note that the code in this repository, as well as the `luma.core` library, may be governed by specific licenses. Check the LICENSE file in the `luma.core` repository for more information on its licensing terms.
