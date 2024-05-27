import playsound
import requests
import os

# Voices

'''

"aura-asteria-en" == Sophia (Female US English
"aura-luna-en" == Emily (Female US English) 
"aura-stella-en" == Rachel (Female US English)
"aura-athena-en" == Eliza (Female UK English)
"aura-hera-en" == Pam  (Female US English) 
"aura-orion-en" == Kevin  (Male US English) 
"aura-arcas-en" == Jeff (Male US English) 
"aura-perseus-en" == Alex (Male US English) 
"aura-angus-en" == Rory (Male Irish English) 
"aura-orpheus-en" == John (Male US English) 
"aura-helios-en" == Pete (Male UK English) 
"aura-zeus-en" == James (Male US English) 

'''

def speak(text: str, model: str="aura-luna-en", filename :str="data.mp3"):
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


