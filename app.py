import streamlit as st
import mysql.connector
import requests
import os
os.system("pip install mysql-connector-python")
import pandas as pd
st.title('📚BookScape Explorer')
st.header('Clickhere')

def get_db_connection():
    return mysql.connector.connect(
        host=st.secrets["gateway01.ap-southeast-1.prod.aws.tidbcloud.com"],
        port=st.secrets[4000],
        user=st.secrets["4ABAUzjWF71mucC.root"],
        password=st.secrets["1vVrWbTp2oLR6led"],
        database=st.secrets["book_store"]
    )


def fetch_books_from_db():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)  # Dictionary cursor for column names
    cursor.execute("SELECT * FROM books LIMIT 1000")  # Fetch up to 1000 rows
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

if st.button("Fetch Books Data"):
    books_data = fetch_books_from_db()
    
    if books_data:
        df = pd.DataFrame(books_data)  # Convert to Pandas DataFrame
        st.success(f"✅ Loaded {len(df)} books successfully!")
        st.dataframe(df)  # Display in Streamlit table
    else:
        st.warning("⚠ No books found in the database!")
