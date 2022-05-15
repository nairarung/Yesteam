import os
import Ptxt2spch as ptxt

os.chdir("/home/nairarungster/PText2Speech/CRED/")
ptxt.text_to_wav("en-AU-Wavenet-A", "What is the temperature in Sydney?")

os.system("cloudshell download en-*.wav")