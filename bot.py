import streamlit as st
from utils import write_message
from agent import generate_response

# Page Config
st.set_page_config("UGent ISyE Chatbot", page_icon="random")

# Show title and description.
st.title("🤖 UGent ISyE Chatbot")
st.write(
    "This is a chatbot that uses OpenAI's GPT-4.0 model to generate responses. "
)


# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello👋, I'm the UGent ISyE Chatbot🤖! What can I do for you?"},
    ]

# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
        # Call the agent
       response = generate_response(message)
       write_message('assistant', response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
