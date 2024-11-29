# Streaming LLM Using Gemini
![Streaming LLM Banner](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_SS.width-1300.jpg)
This project integrates Google's Gemini model into a conversational interface built with Streamlit. The application streams responses from the language model based on the user's input, creating a dynamic, interactive chatbot. This chatbot is powered by LangChain and provides real-time, context-aware responses.

## Features

- **Real-Time Streaming**: The application streams AI responses as the user interacts, offering a dynamic and responsive experience.
- **Conversational Memory**: The chatbot maintains a history of conversations, allowing it to offer more contextually aware and meaningful responses.
- **Google Gemini Integration**: Uses the `ChatGoogleGenerativeAI` from LangChain to interact with Google's Gemini language model for natural language processing.
- **Customizable Templates**: The chatbot uses a customizable prompt template to ensure the AI responds in a friendly, helpful, and concise manner.

## Requirements

To run this application locally, you will need the following dependencies:

- Python 3.7 or later
- Streamlit
- LangChain
- Google Generative AI (Gemini)
- dotenv

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/JonathanJourney99/Streaming-LLM.git
    ```

2. Install required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:

    - Create a `.env` file in the root of your project directory.
    - Add your API keys and credentials for LangChain and Google Generative AI.
    
    Example `.env` file:
    
    ```
    GOOGLE_API_KEY=your_google_api_key
    ```

4. Ensure that the Google Gemini API is accessible and the `langchain_google_genai` library is configured correctly.

## How to Run

1. After setting up the environment and installing dependencies, run the application with:

    ```bash
    streamlit run app.py
    ```

2. Open the web application in your browser at `http://localhost:8501`.

3. Start interacting with the chatbot by typing your queries in the input box.

## How It Works

1. **Initialization**: The application uses `Streamlit` to create an interface for the user to interact with. The `ChatGoogleGenerativeAI` model is initialized with the `gemini-1.5-flash` model.
   
2. **Chat History**: The conversation history is stored in `st.session_state.chat_history`, which is passed to the model to provide context-aware responses.
   
3. **Streaming Responses**: When the user inputs a message, the model generates a response using the LangChain flow. The response is streamed and displayed dynamically, offering a smooth user experience.
   
4. **Dynamic Prompts**: The `ChatPromptTemplate` is used to build dynamic prompts with user input and previous chat history to ensure context is maintained throughout the conversation.

## Example Interaction

1. **User**: "Hello, how are you?"
2. **Assistant**: "Hi! I'm here to help. How can I assist you today?"

The assistant responds based on the previous interactions and maintains the context throughout the conversation.

## Code Explanation

### Key Parts of the Code:

- **`model_response` function**: This function constructs a LangChain pipeline that takes the user's input and chat history, generates a response using the Gemini model, and outputs it.
  
- **Streamlit Setup**: The app uses `st.session_state` to store and update the conversation history. It renders the conversation between the human and the AI using `st.chat_message`.

- **Conversation History**: Each message, whether from the user or the assistant, is appended to `st.session_state.chat_history` to maintain the chat history, which is used to generate contextually aware responses.

## Troubleshooting

### Issue: **Missing or Invalid API Keys**
- Ensure that your `.env` file contains valid API keys for the Google Gemini model and other necessary configurations.
  
### Issue: **No response from the assistant**
- Ensure your internet connection is stable and that the API keys are valid.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your proposed changes. Please make sure to follow the code style and write tests for any new features or changes.

## License

This project is licensed under the MIT License
