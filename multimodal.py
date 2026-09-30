import os
import base64
from dotenv import load_dotenv
from google import genai

load_dotenv()

google_api_key = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=google_api_key)

def tts_function(text):
    interaction = client.interactions.create(
        model='gemini-3.8-flash-lite-tts',
        input=[
            {
                "type": "user_input",
                "content": [
                    {
                        "type": "text",
                        "text": text,
                        "annotations": [
                            {
                                "type": "speech_metadata",
                                "style": "friendly, clear and conversational"
                            }
                        ]
                    }
                ]
            }
        ],
        response_format={"type": "audio"},
        generation_config={
            "speech_config": [
                {"voice": "Kore"}
            ]
        }
    )

    audio_data = base64.b64decode(interaction.output_audio.data)

    with open('travel_response.wav', 'wb') as f:
        f.write(audio_data)
    
    return 'travel_response.wav'