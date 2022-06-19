import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🥑🍞 Build Your Own Fruit Smoothie 🥣 ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# show my fruit list
#streamlit.dataframe(my_fruit_list)
# set my_fruit_list as a list: choose the fruit name column as the index
my_fruit_list = my_fruit_list.set_index('Fruit')


## show all daat form the selected list
#fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:" , list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
##display the table on the page
streamlit.dataframe(fruit_to_show)
#create the repeateavble code block (called a function)
def get_fruityvice_data(this_fruit_choice):
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       return fruityvice_normalized

#New Section to display fruityvice API response  --> lessons 09
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:                                    
      streamlit.error("Please select a fruit to get information.")
  else:    
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()

streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
       with my_cnx.cursor() as my_cur:
            my_cur.execute("select * from fruit_load_list")
            return my_cur.fetchall()
              

# don't run anything past here while we troubleshout
#streamlit.stop()

#Allow the enduser to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
            my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
            return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')

# Add a button to laod the fruit
if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)

