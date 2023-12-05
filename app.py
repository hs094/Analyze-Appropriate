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
						st.subheader("Food Delivery App: Zomato")
						a10 = st.multiselect(
                                'After Experiencing the Zomato Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a11 = st.radio("**1.** How often do you use the Zomato app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a12 = st.radio("**2.** Are you aware that Zomato collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a13 = st.radio("**3.** Considering the Indian Personal Data Protection Bill 2019, do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a14 = st.radio("**4.** Zomato asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a15 = st.radio("**5.** What purpose do you think Zomato collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						st.image('./Zomato.jpeg', caption="Zomato app permissions")
						a16 = st.radio("**6.** Zomato app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a17 = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Zomato?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a18 = st.radio("**8.** Does the app provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a19 = st.radio("**9.** Does the app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Food Delivery App: Dominos")
						a20 = st.multiselect(
                                'After Experiencing the Dominos Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a21 = st.radio("**1.** How often do you use the Dominos app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a22 = st.radio("**2.** Are you aware that Dominos collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a23 = st.radio("**3.** Considering the NTSS , do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a24 = st.radio("**4.** Dominos asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a25 = st.radio("**5.** What purpose do you think Dominos collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						st.image('./Dominos.jpeg', caption="Dominos app permissions")
						a26 = st.radio("**6.** Dominos app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a27 = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Dominos?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a28 = st.radio("**8.** Does the US app. version of Dominos provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a29 = st.radio("**9.** Does the US app. version of Dominos app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Gaming App: Ludo King")
						a30 = st.multiselect(
                                'After Experiencing the Ludo King Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a31 = st.radio("**1.** How often do you use the Ludo King app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a32 = st.radio("**2.** Are you aware that Ludo King collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a33 = st.radio("**3.** Considering the Indian Personal Data Protection Bill 2019, do you find it ethically acceptable for Ludo King app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a34 = st.radio("**4.** Ludo King asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a35 = st.radio("**5.** What purpose do you think Ludo King collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						a36 = st.radio("**6.** Ludo King app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a37 = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Ludo King?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a38 = st.radio("**8.** Does the Indian gaming app provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a39 = st.radio("**9.** Does the Indian gaming app provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						st.subheader("Gaming App: Robolox")
						a40 = st.multiselect(
                                'After Experiencing the Robolox Application, what do you perceive as a intended data collection purpose?*',
                                ['Personalized ads and offers', 'Understanding user behavior', 'Optimization of apps for better engagement', 'Seek Device Information for tailor Device Needs', 'Location-Based Services', 'Social Sharing', 'Friend Recommendations', 'In-app messaging', 'Fitness tracking', 'Augmented reality experiences', 'Game control', 'Performance Monitoring to fix bugs and improve app stability', 'Enhance User Experience', 'Understand data consumption patterns to optimize performance', 'User feedback to to gauge user satisfaction', 'Login Crediantials for 3rd Party Use', 'IP Address Traking', 'Financial and Transactional Data Mishandling/3rd-Party Use', 'Audit logs and activity tracking'],
                                [])
						a41 = st.radio("**1.** How often do you use the Robolox app?*", ["Never", "Less than once a week", "Once a week", "Several times a week", "Everyday"], 2, horizontal=True)
						a42 = st.radio("**2.** Are you aware that Robolox collects data about your location, browsing history, and food preferences?*", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a43 = st.radio("**3.** Considering the NTSS, do you find it ethically acceptable for app developers to request permission to access files, contacts, and cameras for data collection purposes?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a44 = st.radio("**4.** Robolox asks for user consent for data collection. Were you able to understand from the consent which data will be collected by the app?*", ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"], 2, horizontal=True)
						a45 = st.radio("**5.** What purpose do you think Robolox collects data for?*", ["To improve the app's features and functionality", "To provide better/personalized user experience", "To target advertising", "To sell data to third parties", "Other (please specify)"])
						a46 = st.radio("**6.** Robolox app can be used with all features without giving any permissions, as shown in the screenshot above.  (T/F)?", ["True", "False", "I prefer not to answer."], 2, horizontal=True)
						a47 = st.radio("**7.** What do you know think is the purpose of microphone and camera access asked by Robolox?", ["Collect data to provide food preferences", "Permissions are required to access device feature", "For audio search and visual search to help with food recognition", "To sell data to third parties"])
						a48 = st.radio("**8.** Does the US app. version of Robolox provide information about its data retention policies and how long it stores user data?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						a49 = st.radio("**9.** Does the US app. version of Robolox provide users with information about how to report privacy concerns or complaints?", ["Yes", "No", "I prefer not to answer."], 2, horizontal=True)
						# data = pd.DataFrame([{
						# 	"Name": username,
						# 	# "Age": age(username=username),
						# 	"a10": a10,
						# 	"a11": a11,
						# 	"a12": a12,
						# 	"a13": a13,
						# 	"a14": a14,
						# 	"a15": a15,
						# 	"a16": a16,
						# 	"a17": a17,
						# 	"a18": a18,
						# 	"a19": a19,
						# 	"a20": a20,
						# 	"a21": a21,
						# 	"a22": a22,
						# 	"a23": a23,
						# 	"a24": a24,
						# 	"a25": a25,
						# 	"a26": a26,
						# 	"a27": a27,
						# 	"a28": a28,
						# 	"a29": a29,
						# 	"a30": a30,
						# 	"a31": a31,
						# 	"a32": a32,
						# 	"a33": a33,
						# 	"a34": a34,
						# 	"a35": a35,
						# 	"a36": a36,
						# 	"a37": a37,
						# 	"a38": a38,
						# 	"a39": a39,
						# 	"a40": a40,
						# 	"a41": a41,
						# 	"a42": a42,
						# 	"a43": a43,
						# 	"a44": a44,
						# 	"a45": a45,
						# 	"a46": a46,
						# 	"a47": a47,
						# 	"a48": a48,
						# 	"a49": a49,
                        # }])
						d = [username,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49]
						submit_button = st.form_submit_button(label="Submit")
						if submit_button:
							with open('Database.csv','a', newline='') as f:
								writer = csv.writer(f)
								writer.writerow(d)
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