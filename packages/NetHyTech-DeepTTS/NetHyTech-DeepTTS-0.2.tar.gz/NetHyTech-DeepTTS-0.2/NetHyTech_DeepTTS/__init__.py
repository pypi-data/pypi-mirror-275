import playsound
import requests
import os

# Voices


a = "aura-asteria-en" # Sophia (Female US English
b = "aura-luna-en" # Emily (Female US English) 
c = "aura-stella-en" # Rachel (Female US English)
d = "aura-athena-en" # Eliza (Female UK English)
e = "aura-hera-en" # Pam  (Female US English) 
f = "aura-orion-en" # Kevin  (Male US English) 
g = "aura-arcas-en" # Jeff (Male US English) 
h = "aura-perseus-en" # Alex (Male US English) 
i = "aura-angus-en" # Rory (Male Irish English) 
j = "aura-orpheus-en" # John (Male US English) 
k = "aura-helios-en" # Pete (Male UK English) 
l = "aura-zeus-en" # James (Male US English) 


def speak(text: str, model: str=id):
        filename :str="data.mp3"
        url = "https://api.deepai.org/speech_response"

        payload = {
            "model": model,
            "text": text
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200: return f"Error: {response.status_code} - {response.text}"
        else:
            with open(filename, 'wb') as f:
                f.write(response.content)
            playsound.playsound(filename)
            os.remove(filename)


speak("i dont know sir but i am felling not good today",l) 
