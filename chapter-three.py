import streamlit as st

st.title("Chai Taste Poll")

col1,col2=st.columns(2)

with col1:
  st.header("Masala Chai")
  st.image("https://moonrice.net/wp-content/uploads/2022/10/Chai-500x500.jpg", width=200)
  vote1=st.button("Vote Masala Chai")
with col2:
  st.header("Adrak Chai")
  st.image("https://media.istockphoto.com/id/1482828620/photo/clay-tea-cup-being-hold-in-the-hand.jpg?s=612x612&w=0&k=20&c=zULj4iZBUdV4TjzeYQLBr3QGD_1lPRuGtnD1i57p-A8=", width=200)
  vote2=st.button("Vote Adrak Chai")

if vote1:
  st.success("Thanks for voting Masala Chai")
elif vote2:
  st.success("Thanks for voting Adrak Chai")

name=st.sidebar.text_input("Enter your name")
tea=st.sidebar.selectbox("Chooose your chai",["Masala","kesar","Adrak"])

st.write(f"Welcome {name} and your {tea} is getting ready")

with st.expander("Show Chai Making Instructions"):
  st.write("""
  1.Boil Water with tea leafes \n
  2.Add milk and spices \n
  3.Serve hot
  """)


st.markdown('###Welcome to Chai App')
st.markdown('>Blockquote')
