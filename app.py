import streamlit as st
import pandas as pd
import csv
import os

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# DB Management
import sqlite3 
conn = sqlite3.connect('data1.db')
c = conn.cursor()
features = {"Name": [],
			 "a0": [],
        "a1": [],
        "a2": [], 
        "a3": [], 
        "a4": [], 
        "a5": [], 
        "a6": [], 
        "a7": [], 
        "a8": [], 
        "a9": [], 
    }
filenames = ["file1.csv", "file2.csv", "file3.csv", "file4.csv"]
path = "pdata/"
folder_path = "pdata"
if not os.path.exists(folder_path):
	os.makedirs(folder_path)
data = pd.DataFrame(features)
for filename in filenames: 
	full_path = path+filename
	data.to_csv(full_path, index=False) 
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def age(username):
	c.execute('SELECT * FROM userstable WHERE username =?',(username))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def encode_data(data):
    encoded_data = []
    
    for value in data:
        if isinstance(value, list):  # Handle multiselect lists
            encoded_values = []
            for v in value:
                encoded_values.append(encode_value(v))
            encoded_data.append(encoded_values)
        else:
            encoded_data.append(encode_value(value))
    
    return encoded_data

def encode_value(value):
	if value in ["Everyday"]:
		return 5
	elif value in ["Several times a week"]:
		return 4
	elif value in ["Once a week"]:
		return 3
	elif value in ["Strongly Agree", "Agree", "Yes", "Less than once a week" , "True"]:
		return 2
	elif value in ["Neutral", "I prefer not to answer.", "Never"]:
		return 1
	elif value in ["Strongly Disagree", "Disagree", "No", "False"]:
		return 0
	else:
		return value  # Keep non-categorical values as they are

# ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"]
# "Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"
def main():
	"""Simple Login App"""
	
	st.title("Analyze Appropriate")

	menu = ["Home","Login","SignUp","Contact"]
	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Contact":
		import contact
		contact.main()
	
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

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)
			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(username))
				with st.form(key="zomato_form"):
						st.subheader("Complaince Opinion - India ")
						i = [None] * 4
						u = [None] * 4
						a1 = [None] * 10 
						a2 = [None] * 10 
						a3 = [None] * 10 
						a4 = [None] * 10 
						i[0] = st.radio("Do you feel there is unauthorised access?", ["Yes", "No"], 0, horizontal=True)
						i[1] = st.radio("Do you feel that applications follow user location data related guidelines?" , ["Yes", "No"], 0, horizontal=True)
						i[2] = st.radio("Do you think that your sensitive data is being acssessed?)(Call Logs, Financial Data and Files)", ["Yes", "No"], 0, horizontal=True)
						i[3] = st.radio("Do you feel safe while providing your mobile wallet data etc.?", ["Yes", "No"], 0, horizontal=True)
						st.subheader("Complaince Opinion - US ")
						u[0] = st.radio("Are there fair App Permissions?", ["Yes", "No"], 0, horizontal=True)
						u[1] = st.radio("Are ther adequate Security Measures", ["Yes", "No"], 0, horizontal=True)
						u[2] = st.radio("Is User Authorization seeked for Data Usage/Sharing?", ["Yes", "No"], 0, horizontal=True)
						u[3] = st.radio("Do you feel safe for your biometrics?", ["Yes", "No"], 0, horizontal=True)
						st.subheader("Food Delivery App: Zomato")
						a1[0] = st.multiselect(
                                'After Experiencing the Zomato Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a1[1] = st.radio("**1.** How often do you use the Zomato app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a1[2] = st.radio("**2.** Are you aware that Zomato collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a1[3] = st.radio("**3.** Considering the Indian Personal Data Protection Bill 2019, do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a1[4] = st.radio("**4.** Zomato asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a1[5] = st.radio("**5.** What purpose do you think Zomato collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						st.image('./Zomato.jpeg', caption="Zomato app permissions")
						a1[6] = st.radio("**6.** Zomato app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a1[7] = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Zomato?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a1[8] = st.radio("**8.** Does the app provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a1[9] = st.radio("**9.** Does the app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Food Delivery App: Dominos")
						a20 = st.multiselect(
                                'After Experiencing the Dominos Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a2[1] = st.radio("**1.** How often do you use the Dominos app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a2[2] = st.radio("**2.** Are you aware that Dominos collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a2[3] = st.radio("**3.** Considering the NTSS , do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a2[4] = st.radio("**4.** Dominos asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a2[5] = st.radio("**5.** What purpose do you think Dominos collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						st.image('./Dominos.jpeg', caption="Dominos app permissions")
						a2[6] = st.radio("**6.** Dominos app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a2[7] = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Dominos?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a2[8] = st.radio("**8.** Does the US app. version of Dominos provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a2[9] = st.radio("**9.** Does the US app. version of Dominos app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Gaming App: Ludo King")
						a3[0] = st.multiselect(
                                'After Experiencing the Ludo King Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a3[1] = st.radio("**1.** How often do you use the Ludo King app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a3[2] = st.radio("**2.** Are you aware that Ludo King collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a3[3] = st.radio("**3.** Considering the Indian Personal Data Protection Bill 2019, do you find it ethically acceptable for Ludo King app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a3[4] = st.radio("**4.** Ludo King asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a3[5] = st.radio("**5.** What purpose do you think Ludo King collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						a3[6] = st.radio("**6.** Ludo King app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a3[7] = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Ludo King?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a3[8] = st.radio("**8.** Does the Indian gaming app provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a3[9] = st.radio("**9.** Does the Indian gaming app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Gaming App: Robolox")
						a4[0] = st.multiselect(
                                'After Experiencing the Robolox Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a4[1] = st.radio("**1.** How often do you use the Robolox app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a4[2] = st.radio("**2.** Are you aware that Robolox collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a4[3] = st.radio("**3.** Considering the NTSS, do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a4[4] = st.radio("**4.** Robolox asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a4[5] = st.radio("**5.** What purpose do you think Robolox collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						a4[6] = st.radio("**6.** Robolox app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a4[7] = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Robolox?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a4[8] = st.radio("**8.** Does the US app. version of Robolox provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a4[9] = st.radio("**9.** Does the US app. version of Robolox provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						d =  a1 + a2 + a3 + a4 + i + u
						encoded_data = [username] + encode_data(d)
						submit_button = st.form_submit_button(label="Submit")
						if submit_button:
							with open('Database.csv','a', newline='') as f:
								writer = csv.writer(f)
								writer.writerow(encoded_data)
							st.success("Details successfully submitted!")							    

					
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

if __name__ == '__main__':
	main()