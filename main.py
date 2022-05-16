# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
import Ptxt2spch as ptxt
import io
import time
from flask import Flask,render_template,request 
from google.cloud import storage
from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("speech.html")
    
@app.route('/', methods=['GET' , 'POST'])
def my_form():
    proctxt = request.form["pronounce"]
    os.chdir("/home/nairarungster/PText2Speech/CRED/")
    ptxt.text_to_wav("en-AU-Wavenet-A", proctxt)
    #newfile = proctxt + ".wav"
    #os.rename("en-AU.wav",newfile)
    #os.system("cloudshell download " + proctxt + ".wav")
    #time.sleep(10)
    BUCKET = 'positive-winter-350105.appspot.com'
    gcs = storage.Client()
    bucket = gcs.get_bucket(BUCKET)
    for file in Path('/home/nairarungster/PText2Speech/CRED/').rglob('*.wav'):
        blob = bucket.blob(file.name)
        blob.cache_control='no-cache'
        blob.upload_from_filename(str(file))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=int(os.environ.get("PORT", 8081)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
