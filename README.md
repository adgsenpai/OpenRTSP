# OpenRTSP

a developer's platform to view any camera stream in HTML5 or a users platform to manage their security cameras

**Live Demo of Application**
openrtsp.com

## Getting Started - User Usage

First download the repo by running 
`git clone https://github.com/adgsenpai/OpenRTSP`

Install Requirements by running
`pip install -r requirements.txt`

Run Application by running 
`python3 server.py` 

### Configuration
go to `appconfig.yaml`

default config looks like this:
```
- accounts:
	- usernames:
		- adgsenpai
	- passwords:
		- 12345
- ipcameras:
	- rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4
```

To add accounts - i will show you an example of how to add 3 user accounts you could add accounts to Nth Degree
```
- accounts:
	- usernames:
		- AccountA
		- AccountB
		- AccountC
	- passwords:
		- PasswordA
		- PasswordB
		- PasswordC
- ipcameras:
	- rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4
```

Adding Cameras: you can add cameras to the Nth Degree
```
- accounts:
	- usernames:
		- AccountA
		- AccountB
		- AccountC
	- passwords:
		- PasswordA
		- PasswordB
		- PasswordC
- ipcameras:
	- rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4
	- linkA
	- linkB
	- linkNth
```

## How it works 

### App Breakdown
```
-pages				#Stores all the HTML pages for the website
	-index.html
	-sign-in.html
-static				#Stores all the assets for the website
	-css
		- corefiles
		...
	-fonts
		- corefiles
		...
	-img
		- corefiles
		...
	-js					#Front End Controllers to manage operations with the Back End Routes
		-authUser.js
		-cameraRoute.js
	-scss
		- corefiles
		...
appconfig.yaml  		#App Config
Dockerfile				#Instructions to run app as a container
openrtsp.py				# Module which converts your RTSP to a video img stream
server.py				# Server Logic
usercontroller.py		# Manages Auth and Returns Cameras from yaml file
requirements.txt		# Required modules for the app to run
```
The `server.py` is the brains of the app. It handles all the web stuff (Routes, Responses .. etc)
The `usercontroller.py` handles the user authentication/returns the camera as a dictionary and also handles the `yaml` user config operations.

### Routes

App has 5 Routes i will break it down for you now.

`/`
this is the homepage route - you should know what that does takes you to the homepage of the app in this app case the camera management page

`/login`
the login page

`/logout`
logs out from page and returns your login page / clears cookies from backend

`/api/v1/login` - **POST**
send a response such as `{'username':'usr','password':'pwd'}`
you it will return a response if auth is correct
`{'status':'success'}`
else
returns 
`{'status':'Invalid username or password'}`

`/video_feed/<rtsplink>`
this route requires the var - as `base16` 

it will return a stream for any given stream able link

### Conversion Process
![How can I send video stream to client side (Browser) by using RTSP - Stack  Overflow](https://i.stack.imgur.com/eUeFQ.png)

Basically it takes any given stream link and sends it to the Linux - Python Server and OpenCV converts that using `graphics`  libraries to a moving image which you can see in the browser.

### JavaScript Function to convert link to base16
```
function toHex(str) {
	var  result  =  '';
	for (var  i=0; i<str.length; i++) {
	result  +=  str.charCodeAt(i).toString(16);
	}
	return  result.toUpperCase();
}
```

## Using OpenRTSP to convert your streams on your website
Well its pretty powerful. 
How you can use OpenRTSP to convert your streams on your website is by
generating a `GET` request to OpenRTSP.com

### Example 

To get a stream - example using bunny stream
```
#BunnyStream
#rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4

# GET request to HTML
https://openrtsp.com/video_feed/727473703A2F2F776F777A6165633264656D6F2E73747265616D6C6F636B2E6E65742F766F642F6D70343A4269674275636B42756E6E795F3131356B2E6D7034

In your website paste this object
<img src="https://openrtsp.com/video_feed/727473703A2F2F776F777A6165633264656D6F2E73747265616D6C6F636B2E6E65742F766F642F6D70343A4269674275636B42756E6E795F3131356B2E6D7034">
```

#### How do we get the GET Request?
According to my routes

`/video_feed/<rtsplink>`
this route requires the var - as `base16` 

we just convert this camera string to base16 which is 
From `rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4` 
to
`727473703A2F2F776F777A6165633264656D6F2E73747265616D6C6F636B2E6E65742F766F642F6D70343A4269674275636B42756E6E795F3131356B2E6D7034`
 
Now append the `base16 to the GET request` which equates
```
https://openrtsp.com/video_feed/727473703A2F2F776F777A6165633264656D6F2E73747265616D6C6F636B2E6E65742F766F642F6D70343A4269674275636B42756E6E795F3131356B2E6D7034
```
