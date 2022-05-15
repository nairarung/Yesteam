
import os

pwd = os.getcwd()
cred = ""
for f in os.listdir("/home/nairarungster/PText2Speech/CRED/"):
    if ".json" in f:
     cred = f
if cred =="":
     print("no credentials")
     quit()
else:
    credential = os.path.join(pwd,"credentials",cred)
    print("credentials in file",cred)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cred
    
    import google.cloud.texttospeech as tts
    def text_to_wav(voice_name: str, text: str):
       language_code = "-".join(voice_name.split("-")[:2])
       text_input = tts.SynthesisInput(text=text)
       voice_params = tts.VoiceSelectionParams(
           language_code=language_code, name=voice_name
        )
       audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

       client = tts.TextToSpeechClient()
       response = client.synthesize_speech(
           input=text_input, voice=voice_params, audio_config=audio_config
        )
       filename = f"{language_code}.wav"
       with open(filename, "wb") as out:
           out.write(response.audio_content)
           print(f'Generated speech saved to "{filename}"')
    



