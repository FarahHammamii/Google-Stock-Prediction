import yfinance as yf
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
import traceback

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def fetch_store():
    try:

        google = yf.Ticker('GOOGL')
        df = google.history(period="1y", interval="1d") 
        
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].astype(str) 

        for _, row in df.iterrows():
            try:
 
                row = row.fillna(0)

                doc_data = {
                    'Date': str(row['Date']), 
                    'Open': float(row['Open']),
                    'High': float(row['High']),
                    'Low': float(row['Low']),
                    'Close': float(row['Close']),
                    'Adj Close': float(row.get('Adj Close', 0)),  
                    'Volume': int(row['Volume']),
                    'Symbol': 'GOOGL' 
                }

              
                doc_id = f"GOOGLE_{row['Date']}"

               
                db.collection('stocks').document(doc_id).set(doc_data)

            except Exception as inner_e:
                print(f"❌ Skipped row due to error:")
                print(row.to_dict())
                traceback.print_exc()

        print("Data for GOOGL saved.")
    
    except Exception as outer_e:
        print(f"Could not fetch data for GOOGL")
        traceback.print_exc()

if __name__ == "__main__":
    fetch_store()
