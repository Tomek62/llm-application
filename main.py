import httpx
import streamlit as st

from rest.service import Chat, client

st.set_page_config(
    page_title="JuniaGPT",
    page_icon="🚀",
)
# Define temperature labels and corresponding values
temperature_mapping = {"Accurate": 0, "Balanced": 0.7, "Creative": 1}
# Let the user chose the temperature category he wants
temperature_choice = st.sidebar.radio(
    label="Model Behavior",
    options=temperature_mapping.keys(),
    index=1,
)
# get the float value associated
temperature = temperature_mapping.get(temperature_choice)


def get_chatbot_response(prompt):
    # Replace this with your actual chatbot logic
    if "hello" in prompt.lower():
        return "Hello to you too!"
    else:
        return (
            "I'm still learning to understand. Can you try asking something different?"
        )


st.title("JuniaGPT 🚀")
st.write("Bienvenue sur mon super chatbot ! 🤖")

# Initialize chat history and variables
if "messages" not in st.session_state:
    st.session_state.messages = []
# Redisplay the entire chat history after each user input
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?", key="user_prompt"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        chat = Chat(
            model="mistral",
            temperature=temperature,
            messages=st.session_state.messages,
        )
        response = client.post(chat=chat)
        if response.status_code == httpx.codes.OK:
            message = response.json()["message"]["content"]
            st.markdown(message)
            st.session_state.messages.append(
                {"role": "assistant", "content": message},
            )
        else:
            st.write("It seems that something broke down 😅")
            st.write(response.status_code)
