import streamlit
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🥑🍞 Build Your Own Fruit Smoothie 🥣 ')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# show my fruit list
#streamlit.dataframe(my_fruit_list)
# set my_fruit_list as a list: choose the fruit name column as the index
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets put a pick list se they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
# show my_fruit_list
#streamlit.dataframe(my_fruit_list)

## show all daat form the selected list
#fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
##display the table on the page
streamlit.dataframe(fruit_to_show)
#New Section to display fruityvice API response  --> lessons 09
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
