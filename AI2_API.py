import base64
import requests

# Set the API URL and initial session ID
API_URL = "****"
current_session_id = None  # This will hold the current session ID

def audio_to_base64(filename):
    """Convert a WAV file to a base64 string."""
    with open(filename, "rb") as audio_file:
        base64_audio = base64.b64encode(audio_file.read()).decode("utf-8")
    print(f"Base64 audio data: {base64_audio[:100]}...")  # Log the first 100 chars (for debugging)
    return base64_audio

def send_to_api(data, input_type="text"):
    """Send text or base64 audio to the API using the current session."""
    global current_session_id  # Declare global to update session ID

    # Prepare the payload based on the input type (text or voice)
    if input_type == "text":
        payload = {
            "question": data  # For text, send as "question"
        }
        files = {}
    elif input_type == "voice":
        payload = {}
        files = {
            'file': ('audio.wav', data, 'audio/wav')  # Change to the actual file content
        }
    else:
        print("Invalid input type. Must be 'text' or 'voice'.")
        return

    # If we have an active session, include it in the payload
    if current_session_id:
        payload["sessionId"] = current_session_id

    # Send the request to the API
    try:
        response = requests.post(API_URL, data=payload, files=files)

        if response.status_code == 200:
            data = response.json()
            print("API Response:", data.get("text", "No response text found."))

            # Update session ID if a new one is returned
            current_session_id = data.get("sessionId", current_session_id)
        else:
            print(f"Error: {response.status_code}, {response.text}")
            print(f"Detailed response: {response.json()}")

    except Exception as e:
        print(f"An error occurred: {e}")

def get_input():
    """Prompt the user for either text or a voice file."""
    global current_session_id

    print("Do you want to continue with the current session or start a new one?")
    print("1. Continue with current session")
    print("2. Start a new session")
    choice = input("Choose an option (1/2): ")

    if choice == "2":
        current_session_id = None  # Reset session ID to start a new session
        print("Starting a new session...")
    
    print("\nChoose input type:")
    print("1. Text")
    print("2. Voice")
    input_choice = input("Enter 1 for text, 2 for voice: ")

    if input_choice == "1":
        question = input("Enter your question: ")
        send_to_api(question, input_type="text")
    elif input_choice == "2":
        audio_file = input("Enter the path to your audio file (WAV format): ")
        audio_base64 = audio_to_base64(audio_file)
        send_to_api(audio_base64, input_type="voice")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    while True:
        get_input()
        another = input("Do you want to ask another question? (y/n): ")
        if another.lower() != 'y':
            break
