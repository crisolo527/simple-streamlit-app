import streamlit as st

BIRTHDAY_LIST = {
    "joe": "May 27th",
    "lim": "October 25th",
    "rae": "July 12th",
    "pat": "April 14th",
}

st.title("Hello, friends!")
st.write("This is a simple Streamlit Birthday app!")

with st.form("birthday_form"):
    name = st.text_input("Enter your friend's first name and find out their birthday!")
    submit_button = st.form_submit_button("Check Birthday")

if submit_button:
    if name.lower() in BIRTHDAY_LIST.keys():
        st.write(f"{name} ---- {BIRTHDAY_LIST[name.lower()]}")
    elif name not in BIRTHDAY_LIST.keys() and name != "":
        st.write(f"Sorry, \"{name}\" is not in the birthday list. Please add them!")
    elif name.strip() == "":
        st.write("Please enter a name.")
