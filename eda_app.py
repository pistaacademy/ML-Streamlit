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
    age = load_data("data/age.csv")
    new = load_data("data/new.csv")

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

                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)
            with st.expander("Dist of Class"):
                fig = plt.figure()
                sns.countplot(df, x='class')
                st.pyplot(fig)
        with colp2:
            with st.expander("Gender Distribution"):
                st.dataframe(gen_df)
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())
        with st.expander("Frequency Dist of age"):
            p2 = px.bar(age, x='Age', y='count')
            st.plotly_chart(p2)
        with st.expander("Outlier Detection Plot"):
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)

            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3)
        with st.expander("Correlation Plot"):
            corr_matrix = new.corr()
            fig = plt.figure(figsize=(20, 10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)

            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)