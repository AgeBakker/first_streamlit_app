import streamlit
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Bolied Free-Range Egg')
streamlit.text('🥑Avocado Toast')

streamlit.header('🍌🍓Build Your Own Fruit Smoothie🥝🍇')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_rows = my_cur.fetchall()

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("The fruit load list contains: ")
streamlit.dataframe(my_data_rows)

streamlit.header("🍌Fruityvice Fruit Advice")
streamlit.text("What fruit would you like to add?")
add_my_fruit = streamlit.text_input("")
streamlit.text("The user added " + add_my_fruit)
