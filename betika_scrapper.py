import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, VotingRegressor
from sklearn.model_selection import train_test_split
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
import threading
import csv


# Step 1: Real-Time Data Streaming with Selenium
def scrape_betika_data():
    service = Service('/usr/bin/chromedriver')  #ChromeDriver path
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.betika.com/en-ke/aviator")
    time.sleep(10)  # Allow page to load

    data = []
    while True:
        try:
            game_elements = driver.find_elements(By.CLASS_NAME, 'payouts-block') #Adjust class name
            for element in game_elements:
                timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
                multiplier = float(element.find_element(By.CLASS_NAME, 'multiplier').text)  # Adjust class name
                data.append({'timestamp': timestamp, 'multiplier': multiplier})

            # Save data to CSV every 10 rounds
            if len(data) % 10 == 0:
                pd.DataFrame(data)
                df.to_csv('aviator_data.csv', index=False) #index=false prevent writing dataframe index as column

            time.sleep(5)  # Adjust delay based on game frequency
        except Exception as e:
            print(f"Error: {e}")
            break

    driver.quit()
    return pd.DataFrame(data)

# Step 2: Advanced Data Preprocessing
def preprocess_data(df):
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['minute'] = df['timestamp'].dt.minute
    df['second'] = df['timestamp'].dt.second
    df['time_since_last'] = df['timestamp'].diff().dt.total_seconds().fillna(0)

    # Rolling statistics : this method allows for various calculation of statistical measures over a moving window of data
    df['rolling_mean'] = df['multiplier'].rolling(window=5).mean()
    df['rolling_std'] = df['multiplier'].rolling(window=5).std()
    df['rolling_max'] = df['multiplier'].rolling(window=5).max()

    # Drop rows with NaN values in the original dataframe
    df.dropna(inplace=True)
    return df

# Step 3: Ensemble Machine Learning Model
def train_ensemble_model(df):
    X = df[['hour', 'minute', 'second', 'time_since_last', 'rolling_mean', 'rolling_std', 'rolling_max']]
    y = df['multiplier']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define models
    gb_model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=5, random_state=42)
    rf_model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)

    # Ensemble model
    ensemble_model = VotingRegressor([('gb', gb_model), ('rf', rf_model)])

    # Train ensemble model
    ensemble_model.fit(X_train, y_train)

    # Evaluate model
    y_pred = ensemble_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Ensemble Model Mean Squared Error: {mse}")
    return ensemble_model

# Step 4: Real-Time Prediction
def predict_next_round(model):
    while True:
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second

        # Load latest data
        df = pd.read_csv('/home/safari/Documents/aviator_cracker/aviator_data.csv')
        df = preprocess_data(df)

        # Predict next multiplier
        new_data = pd.DataFrame({
            'hour': [hour],
            'minute': [minute],
            'second': [second],
            'time_since_last': [0],
            'rolling_mean': [df['rolling_mean'].iloc[-1]],
            'rolling_std': [df['rolling_std'].iloc[-1]],
            'rolling_max': [df['rolling_max'].iloc[-1]]
        })

        prediction = model.predict(new_data)
        print(f"Predicted Multiplier for Next Round: {prediction[0]}")

        time.sleep(5)  # Adjust delay based on game frequency

# Step 5: Main Function
def main():
    # Start data scraping in a separate thread
    scrape_thread = threading.Thread(target=scrape_betika_data)
    scrape_thread.start()

    # Wait for initial data to be collected
    time.sleep(20)

    # Load and preprocess data
    df = pd.read_csv('/home/safari/Documents/aviator_cracker/aviator_data.csv')
    df = preprocess_data(df)

    # Train ensemble model
    model = train_ensemble_model(df)

    # Start real-time prediction
    predict_next_round(model)



if __name__ == "__main__":
    main()