import streamlit as st
import requests

# Retrieve the API key securely from Streamlit's secrets
api_key = st.secrets["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"]

# Function to call the Q&A API and get a response
def get_answer_from_api(question):
    url = "https://api.example.com/q_and_a"  # Replace with your actual API endpoint
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"question": question}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error if the request fails
        answer = response.json().get("answer", "Sorry, I couldn't find an answer.")
    except requests.RequestException:
        answer = "Error connecting to the Q&A service. Please try again later."
    return answer

# Streamlit App Layout
st.title("My Application with Q&A Assistant")
st.write("Welcome to the main application interface!")

# Sidebar button to open Q&A Assistant
if st.sidebar.button("Open Q&A Assistant"):
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []  # Initialize chat history if not present

    # Display conversation history
    for entry in st.session_state['chat_history']:
        if entry['type'] == 'User':
            st.write(f"**User**: {entry['content']}")
        else:
            st.write(f"**Assistant**: {entry['content']}")

    # Capture the user's question
    question = st.text_input("Ask a question to the assistant:")
    if question:
        # Call the API to get the answer
        answer = get_answer_from_api(question)

        # Append question and answer to chat history in session state
        st.session_state['chat_history'].append({"type": "User", "content": question})
        st.session_state['chat_history'].append({"type": "Assistant", "content": answer})

        # Display the assistant's response
        st.write("**Assistant**: " + answer)
