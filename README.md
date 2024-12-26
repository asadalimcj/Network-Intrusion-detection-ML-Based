# Network Intrusion Detection

## Overview
The **Network Intrusion Detection** project is a machine learning-based application designed to detect malicious traffic in a network. It uses a trained machine learning model (XGBoost) to classify network traffic data into various categories of intrusions or normal activity.

## How the Application Works

1. **Model Loading**:
   - The application uses a pre-trained machine learning model (`xgboost_model.pkl`) to make predictions. 
   - This model has been trained to classify network traffic into multiple categories.

2. **Label Mapping**:
   - The model outputs numerical labels, which are mapped to meaningful categories using the following mapping:

| Label | Intrusion Type       |
|-------|----------------------|
| 0     | Analysis            |
| 1     | Backdoor            |
| 2     | DoS                 |
| 3     | Exploits            |
| 4     | Fuzzers             |
| 5     | Generic             |
| 6     | Normal              |
| 7     | Reconnaissance      |
| 8     | Shellcode           |
| 9     | Worms               |

3. **User Interface**:
   - The application provides an intuitive interface built using **Streamlit**.

4. **Steps to Use**:
   - **Upload Dataset**:
     - Users upload a CSV file containing network traffic data.
   - **Preview Dataset**:
     - The uploaded dataset is displayed for the user to review.
   - **Select Row for Prediction**:
     - The user selects the row index from the dataset for which they want to make a prediction.
   - **Make Prediction**:
     - Upon clicking the "Predict" button, the selected row's data is fed into the model.
     - The model predicts the type of intrusion, which is then displayed to the user.

## Application Flow

1. **Start the Application**:
   - Run the application using `streamlit run app.py`.
   - The interface will load in your browser.

2. **Upload Data**:
   - Upload a CSV file containing network traffic data.

3. **Data Preview**:
   - View the dataset to verify its contents.

4. **Row Selection**:
   - Use the input box to select a row index corresponding to the traffic data you wish to analyze.

5. **Prediction**:
   - Click the "Predict" button to classify the selected row's data.
   - The application displays the predicted type of intrusion or "Normal" if no intrusion is detected.

6. **View Label Mapping**:
   - A detailed table showing the label-to-category mapping is displayed at the bottom of the application.

## Technical Details

- **Backend**:
  - Trained using the **XGBoost** algorithm for network intrusion detection.
  - The model is saved as `xgboost_model.pkl`.

- **Frontend**:
  - Developed using **Streamlit** to provide an interactive user interface.

- **Dependencies**:
  - Python 3.x
  - Libraries: `streamlit`, `joblib`, `pandas`, `scikit-learn`, `xgboost`

## How to Run the Project

1. Install dependencies:
   ```bash
   pip install streamlit pandas joblib scikit-learn xgboost
1. Run the project:
   ```bash
   streamlit run app.py
