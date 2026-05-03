import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AgriSmart Punjab", page_icon="🌾", layout="wide")

st.markdown(
    """
    <style>
    .reportview-container .main .block-container { padding: 1.5rem 2rem 2rem; }
    .css-18e3th9 { background-color: #f9fafb; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3rem; background-color: #2e7d32; color: white; font-weight: 600; }
    .stSidebar { background-color: #ffffff; }
    h1, h2, h3, h4, h5 { color: #1f2937; }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div>div { color: #111827; }
    .css-14xtw13 { color: #111827; }
    .stSidebar .stSelectbox label, .stSidebar .stRadio label, .stSidebar p, .stSidebar h3, .stSidebar h4, .stSidebar .stMarkdown, .stSidebar .stAlert { color: #111827 !important; }
    .stSidebar .stSelectbox div[data-baseweb="select"] span, .stSidebar .stRadio div label { color: #111827 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

languages = {
    "English": {
        "title": "AgriSmart Punjab",
        "subtitle": "Farmer decision support for Punjab",
        "city_label": "Select city",
        "language_label": "Select language",
        "section_label": "Go to",
        "government_updates": "Government & Subsidy Updates",
        "subsidy_title": "Subsidy Programs",
        "soil_title": "Soil Analysis",
        "mandi_title": "Mandi Rate Advice",
        "tips_title": "Educational Tips",
    },
    "اردو": {
        "title": "ایگری سمارٹ پنجاب",
        "subtitle": "پنجاب کے کسانوں کے لیے فیصلہ ساز مدد",
        "city_label": "شہر منتخب کریں",
        "language_label": "زبان منتخب کریں",
        "section_label": "سیکشن منتخب کریں",
        "government_updates": "سرکاری سبسڈی اور اپ ڈیٹس",
        "subsidy_title": "سبسڈی پروگرام",
        "soil_title": "مٹی کا تجزیہ",
        "mandi_title": "منڈی ریٹ مشورہ",
        "tips_title": "تعلیمی مشورے",
    },
}

city_options = ["Lahore", "Faisalabad", "Multan", "Rawalpindi", "Gujranwala"]

city_support = {
    "Lahore": {
        "rate_note": "Strong rice demand and stable wheat pricing.",
        "subsidies": ["Tractor subsidy 30%", "Kisan Card fertilizer support"],
    },
    "Faisalabad": {
        "rate_note": "Cotton prices are favorable for harvest season.",
        "subsidies": ["Pesticide subsidy", "Seed support program"],
    },
    "Multan": {
        "rate_note": "Sugarcane and mango farmer support is active.",
        "subsidies": ["Irrigation scheme", "Crop insurance support"],
    },
    "Rawalpindi": {
        "rate_note": "Vegetable mandi is strong and local demand is high.",
        "subsidies": ["Dairy farming support", "Cold storage subsidy"],
    },
    "Gujranwala": {
        "rate_note": "Wheat and rice markets are steady for now.",
        "subsidies": ["Organic fertilizer support", "Small tractor financing"],
    },
}

lang = st.sidebar.selectbox(languages["English"]["language_label"], list(languages.keys()), index=1)
city = st.sidebar.selectbox(languages[lang]["city_label"], city_options)
section = st.sidebar.radio(
    languages[lang]["section_label"],
    [
        languages[lang]["title"],
        languages[lang]["soil_title"],
        languages[lang]["mandi_title"],
        "Selling Advice",
        languages[lang]["tips_title"],
    ],
)

st.sidebar.markdown(f"### {languages[lang]['government_updates']}")
for subsidy in city_support[city]["subsidies"]:
    st.sidebar.success(f"• {subsidy}")
st.sidebar.info(city_support[city]["rate_note"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Latest Alerts")
st.sidebar.warning("Humidity alerts in southern Punjab. Monitor crops closely.")
st.sidebar.info("Subsidy applications open for tractor and dairy support.")

st.title(f"🌾 {languages[lang]['title']}")
st.markdown(f"**{languages[lang]['subtitle']}**")
st.markdown(f"**City:** {city}   •   **Language:** {lang}")

if section == languages[lang]["title"]:
    st.subheader("Smart Farming Dashboard")
    st.markdown(
        "Use the sidebar to choose the section you want. This page brings government subsidy information, mandi advice, soil guidance and tips in a clean professional layout."
    )
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("Soil Advisory", "Live", "Accurate crop guidance")
    col2.metric("Market Insight", "Updated", city_support[city]["rate_note"])
    col3.metric("Subsidy Access", "Available", "Check sidebar programs")

if section == languages[lang]["soil_title"]:
    st.subheader("🌱 Soil Analysis & Crop Recommendations")
    st.markdown("Enter your soil data for clear fertilizer and crop guidance.")
    n = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=90)
    p = st.number_input("Phosphorus (P)", min_value=0, max_value=150, value=42)
    k = st.number_input("Potassium (K)", min_value=0, max_value=200, value=43)
    ph = st.slider("Soil pH", min_value=4.0, max_value=9.0, value=7.0, step=0.1)
    temp = st.number_input("Soil Temperature (°C)", min_value=10, max_value=40, value=25)
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=60)
    st.markdown("---")

    if st.button("Generate Recommendation"):
        if n > 80 and p > 40 and 6.0 < ph < 8.0:
            st.success("✅ Recommended Crop: Basmati Rice")
            st.write("High NPK levels and neutral pH are ideal for quality rice production.")
        elif 40 < n <= 80 and temp < 30 and humidity < 70:
            st.success("✅ Recommended Crop: Wheat (Gandum)")
            st.write("Balanced nutrients and cooler conditions support a strong wheat crop.")
        elif ph < 6.0:
            st.warning("⚠️ Soil pH is acidic")
            st.write("Apply lime and wait 2-3 weeks before planting sensitive crops.")
        elif n < 40:
            st.error("⚠️ Nitrogen is very low")
            st.write("Use urea or organic manure to rebuild soil fertility.")
        else:
            st.info("Soil is moderate")
            st.write("Monitor levels and practice crop rotation for long-term health.")

        tips = []
        if n < 50:
            tips.append("Add nitrogen-rich fertilizers like urea.")
        if p < 30:
            tips.append("Use DAP or simple superphosphate for phosphorus.")
        if k < 30:
            tips.append("Apply potash to support strong roots.")
        if ph < 6.5:
            tips.append("Add lime to raise soil pH safely.")
        if temp > 35:
            tips.append("Irrigate early morning to protect the crop from heat.")
        if humidity > 80:
            tips.append("Watch for fungal diseases and use proper ventilation.")

        if tips:
            st.markdown("**Actionable Tips:**")
            for item in tips:
                st.write(f"- {item}")

if section == languages[lang]["mandi_title"]:
    st.subheader("📈 Mandi Rate Advice")
    st.markdown("City-specific market prices and trends for Punjab commodities.")
    market_data = pd.DataFrame(
        {
            "Commodity": ["Wheat", "Basmati Rice", "Cotton", "Sugar Cane", "Maize"],
            "Lahore": [3950, 9200, 8200, 450, 2850],
            "Faisalabad": [3920, 9150, 8350, 440, 2800],
            "Multan": [3900, 9100, 8100, 460, 2780],
            "Rawalpindi": [3930, 9180, 8250, 455, 2820],
            "Gujranwala": [3940, 9175, 8300, 452, 2830],
        }
    )
    st.table(market_data[["Commodity", city]])
    st.line_chart(market_data.set_index("Commodity")[city])
    st.markdown("---")
    st.write(
        f"**Market note for {city}:** {city_support[city]['rate_note']}"
    )

if section == "Selling Advice":
    st.subheader("💰 Selling Advice & Profit Planning")
    st.markdown("Enter your harvest details and get clear profit guidance.")
    crop_options = ["Wheat", "Basmati Rice", "Cotton", "Sugar Cane", "Maize"]
    selected_crop = st.selectbox("Select Crop", crop_options)
    quantity = st.number_input("Quantity (40kg bags)", min_value=1, value=10)
    current_price = st.number_input("Market Price per 40kg (Rs.)", min_value=0, value=3950)
    cost_per_bag = st.number_input("Your Cost per 40kg bag (Rs.)", min_value=0, value=3000)
    st.markdown("---")

    if st.button("Get Selling Advice"):
        total_revenue = quantity * current_price
        total_cost = quantity * cost_per_bag
        profit = total_revenue - total_cost
        trend = "Stable"
        if selected_crop == "Basmati Rice":
            trend = "Rising"
        elif selected_crop == "Cotton":
            trend = "Falling"

        if trend == "Rising":
            st.success("📈 Hold and wait for a better price")
        elif trend == "Falling":
            st.warning("📉 Consider selling soon before prices drop further")
        else:
            st.info("🔄 Prices are stable. Sell when it fits your cash needs.")

        st.write(f"**Total Revenue:** Rs. {total_revenue:,}")
        st.write(f"**Total Cost:** Rs. {total_cost:,}")
        if profit >= 0:
            st.success(f"**Projected Profit:** Rs. {profit:,}")
        else:
            st.error(f"**Projected Loss:** Rs. {abs(profit):,}")

if section == languages[lang]["tips_title"]:
    st.subheader("📚 Educational Tips for Smart Farming")
    st.markdown("Best practices to improve crop yield, soil health, and market readiness.")
    with st.expander("Crop Rotation Tips"):
        st.write(
            "Rotate wheat with maize, cotton or legumes to keep soil healthy and reduce pests."
        )
    with st.expander("Irrigation Best Practices"):
        st.write(
            "Use drip irrigation where possible and water in early morning or late afternoon to reduce evaporation."
        )
    with st.expander("Soil Testing Guidance"):
        st.write(
            "Test soil every 2-3 years and adjust NPK levels before planting the next season."
        )
    with st.expander("Market Readiness"):
        st.write(
            "Monitor mandi rates weekly and align harvest timing with higher demand seasons."
        )
    with st.expander("Government Scheme Awareness"):
        st.write(
            "Check for tractor, fertilizer, and irrigation subsidies through the Punjab Agriculture Department."
        )
