import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('xgboost_model.pkl')

# Define the label mapping
label_mapping = {
    0: 'Analysis',
    1: 'Backdoor',
    2: 'DoS',
    3: 'Exploits',
    4: 'Fuzzers',
    5: 'Generic',
    6: 'Normal',
    7: 'Reconnaissance',
    8: 'Shellcode',
    9: 'Worms'
}

# Display the label mapping as a table on Streamlit
st.title("Network Intrusion Detection")
st.write("Enter the input values to predict machine failure.")

# Upload file and predict based on user input

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type="csv")
if uploaded_file:
    df = load_data(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df)

    selected_row_idx = st.number_input("Select a row index for prediction", min_value=0, max_value=len(df) - 1, step=1)
    selected_row_reshaped = df.iloc[selected_row_idx, :-1].values.reshape(1, -1)  # Reshape for prediction

    if st.button("Predict"):
        prediction = model.predict(selected_row_reshaped)
        
        # Map the predicted label (which is an integer) to the failure type using the dictionary
        predicted_failure = label_mapping.get(int(prediction[0]), "Unknown")  # Ensure it's an integer
        
        # Display the result
        st.write(f"Prediction: {predicted_failure}")

st.subheader("Label Mapping")
label_table = pd.DataFrame(list(label_mapping.items()), columns=["Label", "Target"])
st.dataframe(label_table)
