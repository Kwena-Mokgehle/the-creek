#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:22:57 2026

@author: moloko_mokgehle
"""


import streamlit as st
import pandas as pd
import base64

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
    ["Background", "Services", "STEM Data Explorer", "Contact"],
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
        "Be a Friend & Don't Ask For Credit. Gare Adimishi Di Tools. 
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
    
    


























