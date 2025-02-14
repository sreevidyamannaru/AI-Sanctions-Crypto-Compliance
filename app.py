import streamlit as st
import pandas as pd
import sqlite3

st.title("AI-Powered Sanctions & Crypto Compliance Dashboard")

conn = sqlite3.connect("compliance_data.db")

transactions = pd.read_sql("SELECT * FROM transactions", conn)

st.write("## Recent Transactions")
st.dataframe(transactions)

st.write("## High-Risk Transactions")
st.dataframe(transactions[transactions["risk"] == "High"])
