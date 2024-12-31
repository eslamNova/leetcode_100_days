import requests

# API endpoint
API_URL = "****"

# Session variables
current_session_id = None
current_chat_id = None

def create_new_session():
    """Start a new session by clearing the session ID and chat ID."""
    global current_session_id, current_chat_id
    current_session_id = None
    current_chat_id = None
    print("Session has been reset. Starting a new session...")

def send_question(question):
    """Send a question to the API and handle session continuity."""
    global current_session_id, current_chat_id

    # Request payload
    payload = {
        "question": question
    }

    # Add session data if it exists
    if current_session_id:
        payload["sessionId"] = current_session_id
    if current_chat_id:
        payload["chatId"] = current_chat_id

    # Send the request
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        # Update session details from the response
        current_session_id = data.get("sessionId", current_session_id)
        current_chat_id = data.get("chatId", current_chat_id)
        return data["text"]
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

def main():
    """Main function to handle user interaction."""
    global current_session_id

    print("Welcome to the API chat interface!")
    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat. Goodbye!")
            break
        elif user_input.lower() == "new session":
            create_new_session()
        else:
            try:
                response_text = send_question(user_input)
                print(f"API: {response_text}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
