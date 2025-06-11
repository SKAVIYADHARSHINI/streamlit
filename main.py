import streamlit as st

from streamlit_option_menu import option_menu

st.title("Hello, kaviya")

# with st.sidebar:

#     st.header("Hello, kaviya")

# st.write(" 😊kaviya dharshini ")

# st.text_input("Enter your name")

# st.button("submit")

with st.sidebar:

    data=option_menu(
        menu_title=" Kaviya",

        options =["Home","About","Contact"],

        icons=["house-fill","people","telephone-fill"]

 

    )

if data=="Home":

    # st.header("Registration Form")

    # st.text_input("Enter your name")

    # st.text_input("Enter your id")

    # st.text_input("Enter your phone number")

    # st.text_input("Enter your address")

    col1,col2=st.columns(2)

    with col1:

        name =st.text_input("Enter your name")

        id=st.text_input("Enter your id")

    with col2:

        phone=st.text_input("Enter your phone number")

        address=st.text_input("Enter your address")

if st.button("Submit"):

    st.write(name,id,phone,address)

    st.success("Data inserted succesfully")

    st.balloons()

st.metric(label="python",value=20,delta="20%")

st.number_input("Integer",max_value=0)

st.radio(label=":rainbow[Gender]",options=["Male","Female"])

# st.selectbox(label="city",options=["mdu","chennai","cbe"])

st.multiselect(label="city",options=["mdu","chennai","cbe"])

st.slider("Numbers",0,100)

st.file_uploader("Upload")

    # st.balloons()

# elif data=="About":

#     st.header("About Page")

# elif data =="Contact":

#     st.header("Contact Page")

 