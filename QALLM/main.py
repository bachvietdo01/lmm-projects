import streamlit as st
import os

from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature = 0)


def get_query():
    input_text = st.text_input("You: ", key = "input")
    return input_text

def return_answer(query):
    return llm(query)


# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

user_input = get_query()
response = return_answer(user_input)

submit = st.button("Generate")

if submit:
    st.subheader("Answer:")
    st.write(response)





