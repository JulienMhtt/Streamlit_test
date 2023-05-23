
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

df_car_eu = df_car.loc[df_car["continent"] == " Europe.", :]
df_car_eu.drop("continent", axis=1, inplace=True )

df_car_us = df_car.loc[df_car["continent"] == " US.", :]
df_car_us.drop("continent", axis=1, inplace=True )

df_car_jp = df_car.loc[df_car["continent"] == " Japan.", :]
df_car_jp.drop("continent", axis=1, inplace=True )

st.title("Car caracteristics in Europe, US, and Japan")
st.markdown("<h2>Correlation for each car caracteristics", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

button_eu_hp = col1.button("Europe", key="button_eu_hp")
button_us_hp = col2.button("US", key="button_us_hp")
button_jp_hp = col3.button("Japan", key="button_jp_hp")


if button_eu_hp:
    eu_heatmap = sns.heatmap(df_car_eu.corr(), annot=True, cmap="coolwarm")
    eu_heatmap.set_title("Correlation european car caracteristics")
    st.pyplot(eu_heatmap.figure)
if button_us_hp:
    us_heatmap = sns.heatmap(df_car_us.corr(), annot=True, cmap="coolwarm")
    us_heatmap.set_title("Correlation american car caracteristics")
    st.pyplot(us_heatmap.figure)
if button_jp_hp:
    jp_heatmap = sns.heatmap(df_car_jp.corr(), annot=True, cmap="coolwarm")
    jp_heatmap.set_title("Correlation japanese car caracteristics")
    st.pyplot(jp_heatmap.figure)



st.markdown("<h2>Correlation for each car caracteristics", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

button_eu_l = col4.button("Europe", key="button_eu_l")
button_us_l = col5.button("US", key="button_us_l")
button_jp_l = col6.button("Japan", key="button_jp_l")

if button_eu_l:
    eu_line = sns.lineplot(data=df_car_eu, x="hp", y="time-to-60")
    eu_line.set_title("Link between speed performace and horsepower")
    fig = eu_line.get_figure()
    st.pyplot(fig)

if button_us_l:
    us_line = sns.lineplot(data=df_car_us, x="hp", y="time-to-60")
    us_line.set_title("Link between speed performace and horsepower")
    fig = us_line.get_figure()
    st.pyplot(fig)

if button_jp_l:
    jp_line = sns.lineplot(data=df_car_jp, x="hp", y="time-to-60")
    jp_line.set_title("Link between speed performace and horsepower")
    fig = jp_line.get_figure()
    st.pyplot(fig)
