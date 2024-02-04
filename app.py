import streamlit as st
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Your machine learning model function
def predict(input_data):
    res = model.predict(input_data)

    print("\n------Output-----\n")
    return res[0]
    
     

# Streamlit app
st.title("Your ML Model Web App")


Ia = st.number_input("Line Current of Phase A:", step=0.1)
Ib = st.number_input("Line Current of Phase B:", step=0.1)
Ic = st.number_input("Line Current of Phase C:", step=0.1)
Va = st.number_input("Line Voltage of Phase A:", step=0.1)
Vb = st.number_input("Line Voltage of Phase B:", step=0.1)
Vc = st.number_input("Line Voltage of Phase C:", step=0.1)
# Input for user
user_input = np.array([[float(Ia), float(Ib), float(Ic), float(Va), float(Vb), float(Vc)]])

# Button to make predictions
if st.button("Predict"):
    # Call the predict function with user input
    prediction = predict(user_input)
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
    elif prediction[0] == 5:
        st.write("NO Fault")   
    else:
        st.write("Error")


