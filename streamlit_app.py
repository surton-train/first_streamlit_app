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
fruit_choice = streamlit.text_input('What fruit would you like information about?' , 'Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())  #just write data to the screen  --> delete this part

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list") # ("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_rows = my_cur.fetchall()#my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:") #("Hello from Snowflake:")
streamlit.dataframe(my_data_rows) #streamlit.text(my_data_row)

#streamlit.text('What fruit would you like to add?')
fruit_choice2add = streamlit.text_input('What fruit would you like to add?' , 'jackfruit')
streamlit.write('Thanks for adding ', fruit_choice2add)
