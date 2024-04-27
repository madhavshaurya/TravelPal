from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import re

# Load environment variables
load_dotenv()

# Configure generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize generative model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to check if the input is related to travel
def is_travel_query(input_text):
    travel_keywords = ['travel', 'trip', 'destination', 'vacation', 'journey', 'tour',
                       'beach', 'beaches', 'coast', 'coastline', 'seaside',
                       'hill', 'hills', 'hill station', 'mountain', 'mountains']
    for keyword in travel_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', input_text, re.IGNORECASE):
            return True
    return False

# Function to get response from Gemini AI
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Set Streamlit page configuration
st.set_page_config(
    page_title="TravelPal - Your Travel Buddy",
    page_icon="✈️",
    layout="centered"
)

# Load logo image
logo_path = "logo.png"  # Replace with the actual path to your logo file

# Main content
st.image(logo_path, use_column_width=True)  # Display logo in the header
st.title("TravelPal - Your Travel Buddy")
st.subheader("Ask any travel-related questions!")

# Input text box and submit button
input_text = st.text_input("Ask a question:")
if st.button("Submit") and input_text:
    # Check if the input is related to travel
    if is_travel_query(input_text):
        # Get response from Gemini AI
        response = get_gemini_response(input_text)
        
        # Display response
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
    else:
        st.error("Please ask a travel-related question.")

# Chat history section
st.sidebar.title("Chat History")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if input_text and is_travel_query(input_text):
    st.session_state['chat_history'].append(("You", input_text))
for role, text in st.session_state['chat_history']:
    st.sidebar.text(f"{role}: {text}")
