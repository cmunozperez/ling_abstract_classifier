import streamlit as st
from main import classify_abstract

# Title for the app
st.title("Linguistics Abstract classifier")

st.write("<i>It is very simple: you introduce a linguistics abstract and the app tells you the areas of linguistics related to it.</i>", unsafe_allow_html=True)

st.markdown("\n\n")

# Input field for text
user_input = st.text_area("Enter your abstract here:", height=20)

# Button to trigger an action
if st.button("Classify!"):
    if user_input:
        classification = classify_abstract(user_input)
        if len(classification) == 0:
            st.write('The linguistic subdiscipline of this abstract is unknown.')
        else:
            st.write('This is an abstract on the following area(s) of linguistics: ' + ', '.join(classification))
    else:
        st.write("Please enter an abstract.")