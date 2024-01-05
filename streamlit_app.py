import pandas as pd
import streamlit as st

df = pd.Dataframe(
            {"website":["https://malnadultra.com/","https://www.vagamonultrail.in/faq"],
              "Race Day":[None,None],
              "Last Day To Register":[None,None]
              })

st.table(df)