#ADGSTUDIOS - server.py

from flask import Flask, render_template, Response
import openrtsp
import cv2

camera = cv2.VideoCapture('rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4')

app = Flask(__name__,template_folder='./pages')

# allows for files to be refreshed in server
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(openrtsp.gen_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000)