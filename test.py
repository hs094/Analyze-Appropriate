import datetime
from datetime import date
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import hashlib


def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

def clear_page():
    with st.empty():
        pass

# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(name TEXT, dob TEXT, highQual TEXT, tech INTEGER, username TEXT,password TEXT)')

def add_userdata(name, dob, highQual, tech, username, password):
	c.execute('INSERT INTO userstable(name,dob,highQual,tech,username,password) VALUES (?,?,?,?,?,?)',(name,dob,highQual,tech,username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

choice = option_menu(
            menu_title=None,  # required
            options=["Home","SignUp", "Login","Contact"],  # required
            icons=["house", "info-circle-fill", "person-circle", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

if choice == "Home":
    st.title("Hello")

if choice == "Login":
	st.title("Login")
	username = st.text_input("User Name")
	password = st.text_input("Password",type='password')
	if st.button("Login"):
		create_usertable()
		hashed_pswd = make_hashes(password)
		st.button("Clear", on_click=clear_page)
		result = login_user(username,check_hashes(password,hashed_pswd))
		if result:
			st.success("Logged In as {}".format(username))
			task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
			if task == "Add Post":
				st.subheader("Add Your Post")
			elif task == "Analytics":
				st.subheader("Analytics")
			elif task == "Profiles":
				st.subheader("User Profiles")
				user_result = view_all_users()
				clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
				st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")


if choice == "SignUp":
    st.title("Create New Account")
    create_usertable() 
    new_name = st.text_input("Name")
    new_dob = st.date_input("Date of Birth", min_value=datetime.date(1923, 1, 1), max_value=date.today())
    education_qualifications = [
    "None",
    "High School Diploma",
    "Associate's Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "Doctoral Degree",]
	# Get user input using a selectbox
    highest_education_qualification = st.selectbox(
    "What is your highest education qualification?",
    education_qualifications,
    )
    new_tech =  st.slider("Years of Technical Experience", 0, 10)
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    
    if st.button("Signup"):
        add_userdata(new_name,new_dob,highest_education_qualification,new_tech,new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")
    	
if choice == "Contact":
    import contact
    contact.main()
		