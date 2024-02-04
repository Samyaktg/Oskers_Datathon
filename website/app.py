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

    if res[0] == 0:
        return("Line A Line B Line C")
    elif res[0] == 1:
        return("Line A Line B Line C to Ground Fault")
    elif res[0] == 2:
        return("Line A Line B to Ground Fault")
    elif res[0] == 3:
        return("Line A to Ground Fault")
    elif res[0] == 4:
        return("Line B to Line C Fault") 
    elif res[0] == 5:
        return("NO Fault")   
    else:
        return("Error")
     

# Streamlit app
st.title("Your ML Model Web App")


Ia = float(input("Line Current of Phase A\t"))
Ib = float(input("Line Current of Phase B\t"))
Ic = float(input("Line Current of Phase C\t"))
Va = float(input("Line Voltage of Phase A\t"))
Vb = float(input("Line Voltage of Phase B\t"))
Vc = float(input("Line Voltage of Phase C\t"))
# Input for user
user_input = np.array([[float(Ia), float(Ib), float(Ic), float(Va), float(Vb), float(Vc)]])

# Button to make predictions
if st.button("Predict"):
    # Call the predict function with user input
    prediction = predict(user_input)

    # Display the prediction
    st.write("Prediction:", prediction)

# Run the app
if __name__ == '__main__':
    st.run()
