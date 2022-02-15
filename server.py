#ADGSTUDIOS - server.py
from flask import Flask, render_template,Response,request,send_file,session
import openrtsp
import cv2
import base64
import yaml
import usercontroller


app = Flask(__name__,template_folder='./pages')

# allows for files to be refreshed in server
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'super secret key'    

@app.route('/')
def home():
  if 'username' in session:
    return render_template('index.html',cameras=usercontroller.ReturnCameras())
  else:
    return render_template('sign-in.html')

@app.route('/login')
def login():
  return render_template('sign-in.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('sign-in.html')


@app.route('/api/v1/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        if request.data:
            data = request.get_json()
            if data['username'] and data['password']:
                if usercontroller.AuthUser(data['username'],data['password']):
                    session['username'] = data['username']
                    return {'status':'success'}

                else:
                    return {'status':'Invalid username or password'}
            else:
                return {'status':'Invalid username or password'}

@app.route('/video_feed/<rtsplink>')
def video_feed(rtsplink):
    try:
      rtsplink =  base64.b16decode(rtsplink).decode('UTF-8')
      print(rtsplink)
      camera = cv2.VideoCapture(rtsplink)
      return Response(openrtsp.gen_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
      print(e)
      return send_file('./static/img/novideo.png', mimetype='image/gif') 

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000)