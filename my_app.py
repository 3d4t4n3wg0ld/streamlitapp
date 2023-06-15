import streamlit as st

# Adding a title
st.title("My Streamlit Data Science Project")

# Adding text
st.write("Welcome to my app!")

# Adding a file uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head())
