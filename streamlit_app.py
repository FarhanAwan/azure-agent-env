import streamlit as st
from agent_runtime import agent_loop

st.title("Azure Natural Language Agent")

query = st.text_input("Enter your query here:")

if st.button("Submit") and query:
    response = agent_loop(query)
    st.write("### Response")
    st.write(response)
