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
            icons=["house","info-circle-fill", "person-circle", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

if choice == "Home":
    st.title("Analyze Appropriate")
    st.text("Do you ever wonder what data those Indian and US apps are collecting on you? Are they being transparent about their intentions, or are they snooping where they shouldn't? Worry no more! Analyze Appropriate is your data collection detective, here to shine a light on the murky world of app permissions.")
    st.image('./logo.png', caption="")
    st.text("")
    st.text("With Analyze Appropriate, you can:")
    st.markdown("- Unmask hidden agendas: Upload any Indian or US app and instantly see a detailed breakdown of the data it collects. Location, contacts, browsing history - nothing escapes our scrutiny.")
    st.markdown("- Visualize the scoop: We don't just throw data at you. We present it in beautiful, easy-to-understand visualizations. See how data collection trends differ between Indian and US apps, and spot potential red flags at a glance.")
    st.markdown("- Compare and contrast: Curious how two similar apps stack up? Analyze Appropriate lets you compare data collection practices side-by-side, making informed choices about which app deserves your trust.")
    st.markdown("- Stay informed, stay empowered: Get regular updates on the latest data collection trends, emerging privacy concerns, and changes in app store policies. We empower you to make smart decisions about your data and protect your privacy.")
    st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)
    st.text("Analyze Appropriate is more than just an app; it's a movement towards data transparency and user empowerment. It's about holding app developers accountable and demanding respect for your digital footprint. Join us on this mission and download Analyze Appropriate today!")
    
    st.text("Together, let's make data collection appropriate, not appalling.")

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
			# st.success("Logged In as {}".format(username))
			# task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
			# if task == "Add Post":
			# 	st.subheader("Add Your Post")
			# elif task == "Analytics":
			# 	st.subheader("Analytics")
			# elif task == "Profiles":
			# 	st.subheader("User Profiles")
			# 	user_result = view_all_users()
			# 	clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
			# 	st.dataframe(clean_db)
			st.title("Survey Form")
			st.divider() 
	        # create_surveytable()
			st.header("Food Delivery App: Zomato")
			a1 = st.radio("**1.** How often do you use the Zomato app?", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
			a2 = st.radio("**2.** Are you aware that Zomato collects data about your location, browsing history, and food preferences?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
			a3 = st.radio("**3.** Considering the Indian Personal Data Protection Bill 2019, do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
			a4 = st.radio("**4.** Zomato asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
			a5 = st.radio("**5.** What purpose do you think Zomato collects data for?", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
			st.image('./Zomato.jpeg', caption="Zomato app permissions")
			a6 = st.radio("**6.** Zomato app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
			a7 = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Zomato?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
			a8 = st.radio("**8.** Does the app provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
			a9 = st.radio("**9.** Does the app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
			if st.button("Submit"):
				pass
			# add_surveydata(a1,a2,a3,a4,a5,a6,a7,a8,a9)
            # st.success("Moving towards Dominos Survey")
			# #  if st.button("Next"):
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
		 