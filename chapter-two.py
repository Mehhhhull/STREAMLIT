import streamlit as st

st.title("CHAI MAKER APP")

if st.button("MAKE CHAI"):
  st.success("Your chai is being brewed")

add_masala=st.checkbox("Add Masala")

if add_masala:
  st.write("Masala Added to your chai")

tea_types=st.radio('Pick your chai base:', ["Milk","Water","Almond Milk"])
st.write(f"Selected base {tea_types}")

flavours=st.selectbox("Choose Flavour: ", ["Adrak","Tulsi","Kesar"])
st.write(f"Selected Flavour {flavours}")

sugar=st.slider("Sugar Level (Spoon)",0 ,5,2)
st.write(f"Sugar Level (Spoon) {sugar}")

cups=st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Sugar Level (Spoon) {cups}")

name=st.text_input('Enter your name')
if name:
  st.write(f"Welcome , {name} ! Your Chai is on the way!")

dob=st.date_input("Select your DOB")
st.write(f"Your Date of Birth is {dob}")