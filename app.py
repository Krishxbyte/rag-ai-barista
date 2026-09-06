import asyncio

import streamlit as st
from google.adk.runners import InMemoryRunner

from agent import barista_agent


st.set_page_config(
    page_title="RAG AI Barista",
    page_icon="☕",
)

st.title("☕ RAG AI Barista")
st.caption("Ask me about our coffee and pastries!")


# Create the ADK runner once.
if "runner" not in st.session_state:
    st.session_state.runner = InMemoryRunner(
        agent=barista_agent,
        app_name="rag_ai_barista",
    )

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input.
if prompt := st.chat_input("What would you like to order?"):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            async def ask_agent():
                response = await st.session_state.runner.run_debug(
                    prompt,
                    quiet=True,
                )

                # Find the final text response.
                for event in reversed(response):
                    if (
                        event.content
                        and event.content.parts
                        and event.content.parts[0].text
                    ):
                        return event.content.parts[0].text

                return "Sorry, I couldn't generate a response."

            answer = asyncio.run(ask_agent())

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
