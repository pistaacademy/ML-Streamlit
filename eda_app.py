import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px


def load_data(data):
    df = pd.read_csv(data)
    return df

def run_eda_app():
    st.subheader("From Exploratory Data Analysis")
    df = load_data("data/diabete.csv")

    submenu = st.sidebar.selectbox("EDA Menu", ["Descriptive", "Plots"])

    if submenu == "Descriptive":
        st.dataframe(df)

        col1,col2,col3,col4 = st.columns(4)
        with col1:
            with st.expander("Data Types"):
                st.dataframe(df.dtypes)
        with col2:
            with st.expander("Descriptive Summary"):
                st.dataframe(df.describe())
        with col3:
            with st.expander("Class Distribuion"):
                st.dataframe(df['class'].value_counts())
        with col4:
            with st.expander("Gender Distribuion"):
                st.dataframe(df['Gender'].value_counts())


    elif submenu == "Plots":
        st.subheader("Plots")
        colp1, colp2 = st.columns(2)

        with colp1:
            with st.expander("Dist Plot of Gender"):
                st.subheader("Gender Distribution Plot")
                fig = plt.figure()
                sns.countplot(df, x='Gender')
                st.pyplot(fig)

                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                st.dataframe(gen_df)