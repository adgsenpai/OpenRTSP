function toHex(str) {
    var result = '';
    for (var i=0; i<str.length; i++) {
      result += str.charCodeAt(i).toString(16);
    }
    return result.toUpperCase();
}
function changeCamera(){
    var rtsplink = document.getElementById('edtCameraIP').value;
    document.getElementById('cameraA').src = "/video_feed/"+toHex(rtsplink);
}

function loadFirstCamera(){
  document.getElementById('edtCameraIP').value = document.getElementById('edtCameraIP').list.options[0].value;
  changeCamera();
}