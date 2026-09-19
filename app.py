import streamlit as st 
import random 

st.title ('coin Flip App')
st.write('Click the button to flip the coin.')
if st.button ('Flip the Coin'):
    result = random.choice(['Heads', 'Tails'])
    st.subheader(f'Result: {result}')
