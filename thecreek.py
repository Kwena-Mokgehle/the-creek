#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:22:57 2026

@author: moloko_mokgehle
"""


import streamlit as st
import pandas as pd
import base64
from datetime import date 
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl  # Add this to your imports at the top
import requests


# --- INITIALIZE SESSION STATE ---
# Track daily counts
if 'appointments' not in st.session_state:
        st.session_state.appointments = {}
    
    # Track specific email + date combinations to prevent duplicates
if 'booked_emails' not in st.session_state:
        st.session_state.booked_emails = set()
    
    # Track if the current user has finished their submission
if 'submission_complete' not in st.session_state:
        st.session_state.submission_complete = False



# --- Creating a picture as background ---

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_faded_background(image_file):
    bin_str = get_base64(image_file)
    
    # 0.7 makes it 70% opaque (faded). 
    # Use rgba(255, 255, 255, 0.7) for a white fade (lighten).
    # Use rgba(0, 0, 0, 0.7) for a black fade (darken).
    overlay_color = "rgba(255, 255, 255, 0.7)" 
    
    page_bg_img = f'''
    <style>
    .stApp {{
        background: linear-gradient({overlay_color}, {overlay_color}), 
                    url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Call the function in your script
set_faded_background('logo.jpg')

# ---- Start of the Content ----


# Set page title
st.set_page_config(page_title="Welcome to The CREEK.", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Background", "Services", "Book Appointment", "Our Location", "Contact"],
)
# Sections based on menu selection
if menu == "Background":
    # ---- To set the title to be at centre ----
    # This is only set on the homepage only.
    st.markdown("""
        <style>
        /* Reduce padding at the top of the page */
        .block-container {
            padding-top: 1rem;
        }
        </style>
        <h1 style='text-align: center;'>Welcome to The CREEK!</h1>
        """, unsafe_allow_html=True)


    st.sidebar.header("Profile Options")

    # ---- Background ----
    st.write("**The CREEK: Where Heritage Meets Horsepower**")
    st.write("The story of **The CREEK** didn't start in a boardroom, it began in the grease stained garage of Joseph and Gladder Mokgehle.")
    st.write("As children, the Mokgehle siblings didn't just watch their father work, they lived the rhythm of the workshop. They grew up amidst the clinking of wrenches and the roar of engines, developing a natural, lifelong obsession with the art of the machine. Today, those same sons have united with their roots to form a parent company built on generations of shared expertise.")
    st.write("***Why 'The CREEK'?***")
    st.write("In nature, a creek is a vital lifeline that feeds the vast, powerful ocean. In our industry, we see ourselves the same way. We believe that no matter how big a factory or how massive a corporation becomes, they all require steady, reliable 'flow' of dedicated specialists like us to keep their operations moving.")
    st.write("We are not just a workshop, we are the essential current that powers the giants. From our father's hands to our collective future, **The CREEK** is where legacy drives innovation.")
    
       # Inserting 3 pictures and forcing them to the same size. 
# 1. Inject CSS to force all images to the same dimensions
    st.markdown("""
    <style>
    [data-testid="stImage"] img {
        width: 100%;
        height: 250px;       /* Set your desired height here */
        object-fit: cover;   /* This prevents stretching */
        border-radius: 10px; /* Optional: rounded corners */
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Create three equal columns
    img1, img2, img3 = st.columns(3)

# 3. Place your images (Replace names with your actual files in Spyder)
    with img1:
        st.image("logo.jpg", caption="Joseph Mokgehle")

    with img2:
        st.image("middle.jpg")

    with img3:
        st.image("mom1.jpg", caption="Gladder Mokgehle")

    # End message of the page    

    # Centered paragraph with normal font weight
    st.markdown("""
    <p style='text-align: center; font-weight: normal;'>
        "Be a Friend & Don't Ask For Credit. Gare Adimishi Di Tools." 
    </p>
    """, unsafe_allow_html=True)

# End of page message
    # Add a visual line to separate content from the footer
    st.divider()

    st.markdown("""
    <p style='text-align: center; color: gray; font-size: 0.8rem;'>
        © 2025 The CREEK 🛠️ | Thank you for visiting!
    </p>
    """, unsafe_allow_html=True)
  
 
# --- The Services Section ---    
elif menu == "Services":
    
    ko1, ko2, ko3 = st.columns(3)
    with ko2:
        st.subheader("⚒️ Services")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("- Engine Diagnostics & Repair")
        st.write("- Oil & Filter Changes")
        st.write("- Brake Inspections & Replacement")
        st.write("- Transmission Services & Rebuilds")
        st.write("- Suspension & Steering Repairs")

    with col2:
        st.write("- Battery Testing & Replacement")
        st.write("- Clutch Replacement")
        st.write("- Exhaust System Repairs")
        st.write("- Cooling System & Radiator Maintenance")
        st.write("- Auto Electrical Troubleshooting")
        
    with col3:
        st.write("- Timing Belt Replacement")
        st.write("- Spark Plug & Fuel Filter Replacement")
        st.write("- Engine Overhaul")
        st.write("- Engine & Gearbox Modification")
        
     # --- Machinery services --- 
     
    st.subheader("🝟Precision Engineering")
    me1, me2 = st.columns(2)
    
    with me1:
        st.write("At The CREEK, we understand that a high-performance engine is only as good as its seal. Our specialized head skimming and resurfacing machine is the heartbeat of our precision department. Whether dealing with warpage from overheating or preparing a head for a high-performance rebuild, our equipment ensures a perfectly flat mating surface to restore compression and prevent future leaks.")
        
    
    with me2:
        st.image("machine1.jpg")
        
        

# --- The Appointment slot    
elif menu == "Book Appointment":
        MY_EMAIL = "rsakwena321@gmail.com"
        MY_PASSWORD = "yfbj xlfp fhxr ckaz"
    
        def validate_sa_phone(number):
            pattern = r"^\+27\d{9}$"
            return re.match(pattern, number)
    
        def send_email(data):
            try:
                context = ssl.create_default_context()
                msg = MIMEMultipart()
                msg['From'] = MY_EMAIL
                msg['To'] = MY_EMAIL
                msg['Subject'] = f"New Service Appointment: {data['Car Reg']}"
                
                body = f"Name: {data['Name']} {data['Surname']}\nPhone: {data['Phone']}\nEmail: {data['Email']}\nCar: {data['Car Reg']}\nService: {data['Service']}\nDate: {data['Date']}"
                msg.attach(MIMEText(body, 'plain'))
        
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=15) as server:
                    server.login(MY_EMAIL, MY_PASSWORD)
                    server.send_message(msg)
                return True
            except Exception as e:
                st.error(f"Email failed to send: {e}")
                return False
    
        st.title("🚗 Car Service Booking")
    
        # --- SUCCESS VIEW ---
        if st.session_state.submission_complete:
            st.balloons()
            st.success("✅ Submission Successful! Your appointment has been recorded.")
            if st.button("Make another booking"):
                st.session_state.submission_complete = False
                st.rerun() # Refresh the page to show the form again
    
        # --- FORM VIEW ---
        else:
            with st.container():
                col1, col2 = st.columns(2)
                name = col1.text_input("Name")
                surname = col2.text_input("Surname")
                
                phone = st.text_input("Cellphone Number (e.g., +27821234958)")
                email = st.text_input("Email Address")
                car_reg = st.text_input("Car Registration")
                
                service_options = ["Minor Service", "Major Service", "Brake Replacement", "Oil Change", "Other"]
                service_choice = st.selectbox("Service Type", service_options)
                service_type = st.text_input("Please specify your service") if service_choice == "Other" else service_choice
        
                selected_date = st.date_input("Select Appointment Date", min_value=date.today())
                date_str = str(selected_date)
        
                # Capacity Check
                current_bookings = st.session_state.appointments.get(date_str, 0)
                
                # DUPLICATE EMAIL CHECK: Check if this email already booked for this specific date
                booking_key = f"{email}_{date_str}"
                is_duplicate = booking_key in st.session_state.booked_emails
        
                if current_bookings >= 5:
                    st.error("⚠️ This day has reached maximum capacity (5 appointments).")
                    can_submit = False
                elif is_duplicate:
                    st.warning(f"⚠️ An appointment for {email} on {date_str} already exists.")
                    can_submit = False
                else:
                    st.info(f"Available slots for {date_str}: {5 - current_bookings}")
                    can_submit = True
        
                form_ready = all([name, surname, phone, email, car_reg, service_type])
                
                if form_ready and can_submit:
                    if st.button("Submit Appointment"):
                        if not validate_sa_phone(phone):
                            st.error("Invalid Phone Number. Format must be +27821234958")
                        else:
                            user_data = {
                                "Name": name, "Surname": surname, "Phone": phone,
                                "Email": email, "Car Reg": car_reg, 
                                "Service": service_type, "Date": date_str
                            }
                            
                            if send_email(user_data):
                                # Update records
                                st.session_state.appointments[date_str] = current_bookings + 1
                                st.session_state.booked_emails.add(booking_key)
                                
                                # Hide form and show balloons on next rerun
                                st.session_state.submission_complete = True
                                st.rerun() # Force immediate UI update to success message
                elif not form_ready:
                    st.warning("Please fill in all details to enable the submission button.")
      
                

elif menu == "Our Location":
    # 1. Define Coordinates
    LAT, LON = -23.27571, 29.13121
    
    # 2. Helper Function for Address
    def get_address_no_geopy(lat, lon):
        """Fetches address from Nominatim OpenStreetMap API."""
        try:
            url = f"https://nominatim.openstreetmap.org{lat}&lon={lon}"
            headers = {"User-Agent": "my_streamlit_location_app_v1"}
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            return data.get("display_name", "Address not found")
        except Exception as e:
            return f"Error retrieving address: {e}"

    # 3. Main Logic
    st.subheader("📍 Our Location")
    

    # 4. Layout: Map and Engine Picture
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Streamlit's native map
        map_data = pd.DataFrame({'lat': [LAT], 'lon': [LON]})
        st.map(map_data, zoom=15)
    
    with col_right:
        st.markdown("### Location Details")
        
        
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={LAT},{LON}"
    st.link_button("🌍 Open in Google Maps", google_maps_url)


elif menu == "Contact":   
    # Business Information
    business_name = "The CREEK"
    phone_number = "27829385840"  # Full international format (e.g., 1 for US, 27 for SA)
    facebook_url = "https://www.facebook.com/share/1KPGLSSt5D/?mibextid=wwXIfr"
    message = "Hello! I am interested in your services."
    
    st.title(f"Contact {business_name}")
    
    # 1. Display Basic Contact Details
    st.subheader("Our Details")
    st.write(f"📞 **Phone:** +{phone_number}")
    
    # 2. WhatsApp Click-to-Text Button
    # Format: https://wa.me/<number>?text=<urlencodedtext>
    
    whatsapp_link = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
    st.write("Send us a message!😊")
    st.link_button("💬 Chat on WhatsApp", whatsapp_link)
    
    # 3. Facebook Page Link
    st.write("Visit Our Facebook Page.")
    st.link_button("🌐 Visit our Facebook Page", facebook_url)
     
    
    
    
    
    
    
    
    
    
    
    
    









