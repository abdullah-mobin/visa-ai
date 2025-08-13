import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print all available voices to choose one
for idx, voice in enumerate(voices):
    print(f"Voice {idx}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}")
    print()

# Choose a voice by index or specific ID
engine.setProperty('voice', voices[1].id)  # Change index as needed

# Test speech
engine.say("Hello, this is a new voice.")
engine.runAndWait()
