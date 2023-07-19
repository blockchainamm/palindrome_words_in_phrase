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
st.title("Speed converter from km/h to miles/h")

#speed = float(input('Enter the speed in km/h : '))
speed = st.number_input(label="Speed in km/h",step=1.,format="%.2f")

def kmph2mph():
    speed_mph = speed / 1.609344
    return speed_mph

speed_inmph = kmph2mph()
print ('speed in miles per hour : ', speed_inmph)

st.write('Miles per hour')
st.write(speed_inmph)