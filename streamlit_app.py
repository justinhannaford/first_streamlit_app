import streamlit

streamlit.title('Hey, how is it going?')

streamlit.header('🥣 🥗 🐔 🥑🍞 All the thingsyou need to know')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# displaythe table on the page
streamlit.dataframe(my_fruit_list)
