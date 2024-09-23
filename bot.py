import streamlit as st
from utils import write_message

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
        # # TODO: Replace this with a call to your LLM
        from time import sleep
        sleep(1)
        write_message('assistant', message)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if question := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', question)

    # Generate a response
    handle_submit(question)
