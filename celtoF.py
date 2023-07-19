import streamlit as st

# --- Hide Streamlit Style ---
hide_st_style = """
                <style>
                #MainMenu {Visibility: hidden;}
                footer {Visibility: hidden;}
                header {Visibility: hidden;}
                </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Celcius to Farenheit converter")

deg_c = st.number_input(label="Celcius in degrees",step=1.,format="%.2f")

def degC2F():
    deg_f = (deg_c * 1.8) + 32 
    return deg_f

farenheit = degC2F()

st.write(str(deg_c) + f' degree Celcius is equivalent to {farenheit} degree Farenheit')

st.write('Farenheit')
st.write(farenheit)