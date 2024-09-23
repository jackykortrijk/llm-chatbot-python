import streamlit as st
from utils import write_message

# Create the LLM
from langchain_openai import ChatOpenAI
# Create the Embedding model
from langchain_openai import OpenAIEmbeddings


# Page Config
st.set_page_config("UGent ISyE Chatbot", page_icon="random")

# Show title and description.
st.title("🤖 UGent ISyE Chatbot")
st.write(
    "This is a chatbot that uses OpenAI's GPT-4.0 model to generate responses. "
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🔑")
else:
    #model="gpt-4o-mini"
    #llm = ChatOpenAI(openai_api_key, model, )
    #embeddings = OpenAIEmbeddings(openai_api_key)
    # Set up Session State
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello👋, I'm the UGent ISyE Chatbot🤖! What can I do for you?"},]
