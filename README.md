# TravelPal - Your Travel Buddy

TravelPal is a chatbot designed to provide travel recommendations and assistance. With TravelPal, users can ask any travel-related questions, such as seeking destination suggestions, getting tips for planning a trip, or asking for recommendations on activities and attractions.

## Live Demo

Check out the live deployment of TravelPal: [https://travelpal.streamlit.app/](https://travelpal.streamlit.app/)

## Features

- **Travel Query Handling:** TravelPal can handle various travel-related queries, including destination recommendations, trip planning advice, and more.
- **Gemini AI Integration:** Powered by Google's Generative AI (Gemini), TravelPal provides intelligent responses to user queries.
- **Interactive Chat Interface:** Users can interact with TravelPal through a user-friendly chat interface.
- **Chat History:** TravelPal keeps a record of the conversation history for reference.

## Usage

To use TravelPal:

1. Install the necessary dependencies by running `pip install -r requirements.txt`.
2. Set up your environment variables. Refer to the `.env.example` file for the required variables.
3. Run the Streamlit app by executing `streamlit run app.py`.
4. Ask any travel-related questions in the input field and click "Submit" to get responses from TravelPal.

## Dependencies

- Streamlit: For building the web-based user interface.
- Google Generative AI (Gemini): For generating intelligent responses to user queries.
- dotenv: For managing environment variables.

## Configuration

Make sure to set up the required environment variables for the Gemini API key.

```bash
GOOGLE_API_KEY=your_api_key_here
