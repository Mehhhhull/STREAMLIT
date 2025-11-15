import streamlit as st

st.title("HELLLO OWNER")
st.subheader("BREWED WITH STREAMLIT")
st.text("Welcome to your first interactive app")
st.write("Choose your fav variety of Car")


chai=st.selectbox("Your fav chai:",["Masala Chai","Lemon Tea","Adrak Chai","Kesar Chai"])
st.write(f"Your Choice {chai} . EXCELLLLLENT CHOICE.")

st.success("Your chai have been brewed")