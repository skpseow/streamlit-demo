import streamlit as st
from PIL import Image

# App title
st.title("Simple Streamlit Demo")

# Header and subheader
st.header("Welcome to My App")
st.subheader("An interactive Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("cat.jpg")
st.image(img, width=200)

# Checkbox
if st.checkbox("Show message"):
   st.write("Checkbox is checked!")
   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])
st.success(f"Selected: {gender}")
if gender = "Male":
    st.write("You have chosen Male")
else:
    st.write("You have chosen Female")

# Selectbox
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is:", hobby)

# Slider
level = st.slider("Choose a level", 1, 5)
st.write(f"Selected level: {level}")

# Text input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
   st.success(f"Hello, {name.title()}!")
