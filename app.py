import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('weather.pkl', 'rb') as model_file:
    weat_her = pickle.load(model_file)

# Your machine learning model function
def predict(input_data):
    res = model.predict(input_data)
    print("\n------Output-----\n")
    return res[0]

def weather_preds (weather_data):    
      
    sam = weat_her.predict(weather_data)
    return sam
    
    
     

# Streamlit app
st.title("Your ML Model Web App")


Ia = st.number_input("Line Current of Phase A:", step=0.1)
Ib = st.number_input("Line Current of Phase B:", step=0.1)
Ic = st.number_input("Line Current of Phase C:", step=0.1)
Va = st.number_input("Line Voltage of Phase A:", step=0.1)
Vb = st.number_input("Line Voltage of Phase B:", step=0.1)
Vc = st.number_input("Line Voltage of Phase C:", step=0.1)
sky=['clear', 'cloudy', 'foggy','rainy','semi cloudy','storm']
weather = st.selectbox('Select an option:', sky)
voltage = np.mean([Va,Vb,Vc],axis=0)
trip_hour= st.slider('Select a time:', min_value=1, max_value=24, value=12)


if weather == 'clear':
    weather=0
elif weather == 'cloudy':
    weather=1
elif weather == 'foggy':
    weather=2
elif weather == 'rainy':
    weather=3
elif weather == 'semi cloudy':
    weather=4
elif weather == 'storm':
    weather=5

# Input for user
user_input = np.array([[float(Ia), float(Ib), float(Ic), float(Va), float(Vb), float(Vc)]])

weather_data = np.array([[float(weather),float(voltage),float(trip_hour)]])
# Button to make predictions
if st.button("Predict"):
    # Call the predict function with user input
    prediction = predict(user_input)
    weather_pred = weather_preds(weather_data)
    st.write("Prediction:")
    if prediction[0] == 0:
        st.write("Line A Line B Line C")
    elif prediction[0] == 1:
        st.write("Line A Line B Line C to Ground Fault")
    elif prediction[0] == 2:
        st.write("Line A Line B to Ground Fault")
    elif prediction[0] == 3:
        st.write("Line A to Ground Fault")
    elif prediction[0] == 4:
        st.write("Line B to Line C Fault") 
    elif prediction[0] == 5 :
        st.write("NO Fault")   
    else:
        st.write("Fault location uncertain")

    st.write("Possible Issues:")
    print("weather:",weather_pred)
    if weather_pred[0] == 0:
        st.write("bad weather")
    elif weather_pred[0] == 1:
        st.write("breaker opened")
    elif weather_pred[0] == 2:
        st.write("earthing")
    elif weather_pred[0] == 3:
        st.write("foreign element")
    elif weather_pred[0] == 4:
        st.write("fuse failure") 
    elif weather_pred[0] == 5:
        st.write("relay burn")  
    elif weather_pred[0] == 6:
        st.write("transient fault")  
    elif weather_pred[0] == 7:
        st.write("trip from kite")  
    elif weather_pred[0] == 8:
        st.write("wire fallen")   
    else:
        st.write("Uncertain")


