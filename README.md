# Raspberry-Pi-Network-Camera

![image](https://github.com/tmorovati/Raspberry-Pi-Network-Camera/assets/47552594/9018f34a-3b8a-44ef-8c8f-e829120a5312)
![image](https://github.com/tmorovati/Raspberry-Pi-Network-Camera/assets/47552594/a2b5b08b-1673-4a66-8ee8-b3ef21dffba7)

## Introduction
This project aims to create a network camera using a Raspberry Pi (in this case, a Raspberry Pi 3 B+) and a Raspberry Pi Camera Module (Version 2). The system captures images, applies image modifications, and makes them accessible to remote users on the same network. To achieve this, we use the Raspbian operating system, Python, and FTP for image transfer.

## Prerequisites
Before getting started, make sure you have the following:

Raspberry Pi 3 B+ (or compatible model)
Raspberry Pi Camera Module (Version 2)
A stable power source for the Raspberry Pi
A microSD card with Raspbian OS installed
A network connection (Wi-Fi or Ethernet) for the Raspberry Pi
Access to the local network for connecting from other devices

## Installation and Configuration
- Set up the Raspberry Pi:

Assemble your Raspberry Pi and connect the Camera Module.
Install Raspbian OS on a microSD card and boot up your Raspberry Pi.
Connect the Raspberry Pi to your local network, either through Wi-Fi or Ethernet.

- Capture Images:

Write a Python program to capture images continuously using the Camera Module.

- Modify Images:

Write a Python program to modify captured images as per your requirements. You can use libraries like OpenCV or the PiCamera library for this purpose.
I used Pi-Camera, if you want to install it on your raspian use this command: 

```Sudo apt-get install python-picamera python3-picamera ```

- Create a User Interface:
![image](https://github.com/tmorovati/Raspberry-Pi-Network-Camera/assets/47552594/53a054b7-ef94-4d7a-b23c-0d75ba529bb5)

I used motioneye, after installation, you can start it by following command on your terminal : 

```Sudo service motion start ```

to check the status of the service: 
```Sudo service motion status```

I enabled it, so that whenever the device gets plugged in the service starts to work, to do so use this command: 
```sudo systemctl enable motion ```


- FTP Image Transfer:

Set up an FTP (File Transfer Protocol) server on your Raspberry Pi. You can use software like vsftpd to create a simple FTP server.
Modify your Python program to send the captured and modified images to the FTP server on your Raspberry Pi.

## Usage

Start the Camera:

Run your Python program that captures images and sends them to the FTP server.
Access the Camera Feed:

On any device connected to the same local network as your Raspberry Pi, open a web browser.
Enter the Raspberry Pi's IP address and port to access the user interface you created.
View and Control:

Use the web interface to view the camera feed and potentially control the camera if you've added such features to your user interface.
Image Storage:

Images captured by the camera will be stored on your Raspberry Pi's FTP server. You can access these images via FTP from your local network.

## Troubleshooting
If you encounter issues, check your Raspberry Pi's network connection, ensure the FTP server is running, and review your Python programs for any errors.
Make sure your firewall settings allow FTP traffic to your Raspberry Pi.

## Acknowledgments
This project was developed using Raspbian, Python, and open-source software.
Special thanks to the Raspberry Pi community and the PiCamera library for making this project possible, and ToobaTech Company that provided me this opportunity to develop this device.

## License
This project is open-source and released under the MIT License.

## Contact
For questions or feedback, please contact Tahoura Morovati at t.morovati.99@gmail.com







