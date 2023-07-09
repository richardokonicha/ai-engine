import speech_recognition as sr
from langid import classify
import openai
from app import config

# Set up your OpenAI API credentials
openai.api_key = config.OPENAI_TOKEN

def listen_and_chat():
    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    # Start listening to the microphone
    with sr.Microphone() as source:
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source)

                # Convert speech to text
                user_input = recognizer.recognize_google(audio)
                print("You:", user_input)

                # Detect the language of the user input
                lang = classify(user_input)[0]

                # Send the user input to ChatGPT and get a response
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=user_input,
                    max_tokens=50,
                    temperature=0.7,
                    n=1,
                    stop=None,
                    language=lang,
                    model="davinci",
                )
                response_text = response.choices[0].text.strip()
                print("ChatGPT:", response_text)

                # Check if the user wants to end the conversation
                if "bye Kumar" in response_text:
                    break

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

# Run the chat program
listen_and_chat()
