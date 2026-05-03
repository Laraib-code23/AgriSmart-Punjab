import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AgriSmart Punjab",
    page_icon="🌾",
    layout="wide"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    body { background-color: #f0f4f8; }
    .stApp { color: #0f172a; font-family: 'Segoe UI', sans-serif; }
    [data-testid="stSidebar"] { 
        background: linear-gradient(135deg, #dbeafe 0%, #f3e8ff 100%);
    }
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] p {
        color: #1e293b !important;
    }
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 2.8em; 
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; font-weight: 600; border: none;
    }
    .stButton>button:hover { 
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    .main { background-color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

# Language selector
language = st.sidebar.selectbox("Language / زبان", ["English", "Urdu"])

texts = {
    "English": {
        "title": "AgriSmart Punjab",
        "location": "Select City",
        "soil": "Soil Analysis",
        "recommend": "Crop Recommendation",
        "advice": "Selling Advice",
        "market": "Market Rates",
        "schemes": "Government Schemes",
        "nitrogen": "Nitrogen (N)",
        "phosphorus": "Phosphorus (P)",
        "potassium": "Potassium (K)",
        "soil_ph": "Soil pH",
        "temperature": "Temperature (°C)",
        "humidity": "Humidity (%)",
        "analyze": "Analyze Soil",
        "rice": "Basmati Rice",
        "wheat": "Wheat (Gandum)",
        "cotton": "Cotton (Phutti)",
        "maize": "Maize (Makai)",
        "sugar": "Sugar Cane",
        "select_crop": "Select Crop to Sell",
        "quantity": "Quantity (40kg bags)",
        "price": "Current Price (Rs.)",
        "cost": "Your Cost (Rs.)",
        "get_advice": "Get Selling Advice",
        "hold": "HOLD - Wait for better rates",
        "sell": "SELL - Prices dropping",
        "monitor": "MONITOR - Stable market",
        "revenue": "Total Revenue",
        "profit": "Profit/Loss",
        "wheat_price": "Rs. 3,950",
        "rice_price": "Rs. 9,200",
        "cotton_price": "Rs. 8,200",
        "sugar_price": "Rs. 450",
        "maize_price": "Rs. 2,850",
        "stable": "Stable",
        "rising": "Rising",
        "falling": "Falling",
        "tractor": "Tractor Subsidy - 30,000 tractors available",
        "kissan": "Kissan Card - Interest-free loans",
        "water": "Water Scheme - Drip irrigation subsidies",
        "fertilizer": "Fertilizer Subsidy - 30% discount",
    },
    "Urdu": {
        "title": "AgriSmart Punjab",
        "location": "شہر منتخب کریں",
        "soil": "مٹی کا تجزیہ",
        "recommend": "فصل کی سفارش",
        "advice": "فروخت کا مشورہ",
        "market": "منڈی کے نرخ",
        "schemes": "حکومتی اسکیمیں",
        "nitrogen": "نیٹروجن (N)",
        "phosphorus": "فاسفورس (P)",
        "potassium": "پوٹاشیم (K)",
        "soil_ph": "مٹی کا pH",
        "temperature": "درجہ حرارت (°C)",
        "humidity": "نمی (%)",
        "analyze": "تجزیہ کریں",
        "rice": "باسمتی چاول",
        "wheat": "گندم",
        "cotton": "کپاس",
        "maize": "مکئی",
        "sugar": "گنے",
        "select_crop": "فصل منتخب کریں",
        "quantity": "مقدار (40 کلو بیگ)",
        "price": "موجودہ قیمت (روپے)",
        "cost": "آپ کی لاگت (روپے)",
        "get_advice": "مشورہ لیں",
        "hold": "انتظار کریں - بہتر نرخ",
        "sell": "فروخت کریں - قیمتیں گر رہی ہیں",
        "monitor": "نگرانی کریں - مستحکم",
        "revenue": "کل آمدنی",
        "profit": "منافع/نقصان",
        "wheat_price": "روپے 3,950",
        "rice_price": "روپے 9,200",
        "cotton_price": "روپے 8,200",
        "sugar_price": "روپے 450",
        "maize_price": "روپے 2,850",
        "stable": "مستحکم",
        "rising": "بڑھتا",
        "falling": "گرتا",
        "tractor": "ٹریکٹر سبسڈی - 30,000 دستیاب",
        "kissan": "کسان کارڈ - بغیر سود قرض",
        "water": "پانی کی بچت - ڈرپ سنچائی",
        "fertilizer": "کھاد میں 30% رعایت",
    }
}

t = texts[language]

# Sidebar
st.sidebar.title(t["title"])
st.sidebar.divider()

cities = ["Lahore", "Faisalabad", "Multan", "Rawalpindi", "Gujranwala", "Sialkot", "Sargodha", "Jhang"]
selected_city = st.sidebar.selectbox(t["location"], cities)

st.sidebar.divider()

# Navigation
page = st.sidebar.radio("Navigate", [t["soil"], t["advice"], t["market"], t["schemes"]])

st.sidebar.divider()
st.sidebar.caption(f"📍 {selected_city}")

# Main content
st.title(t["title"])
st.markdown(f"**Location:** {selected_city}")

if page == t["soil"]:
    st.header(t["soil"])
    col1, col2 = st.columns(2)
    
    with col1:
        n = st.number_input(t["nitrogen"], min_value=0, max_value=150, value=70)
        p = st.number_input(t["phosphorus"], min_value=0, max_value=150, value=35)
        k = st.number_input(t["potassium"], min_value=0, max_value=200, value=45)
    
    with col2:
        ph = st.slider(t["soil_ph"], min_value=4.0, max_value=9.0, value=7.2, step=0.1)
        temp = st.number_input(t["temperature"], min_value=10, max_value=40, value=28)
        humidity = st.slider(t["humidity"], min_value=0, max_value=100, value=55)
    
    if st.button(t["analyze"]):
        st.divider()
        if ph < 6.0:
            st.warning("pH too acidic. Apply lime.")
        elif n < 40:
            st.error("Nitrogen low. Use urea.")
        elif n > 85 and p > 45 and k > 55:
            st.success(f"### {t['rice']}")
            st.write("Excellent balance. Perfect for rice.")
        elif 60 < n <= 85 and p < 45 and temp < 30:
            st.success(f"### {t['wheat']}")
            st.write("Ideal for Rabi wheat season.")
        elif k > 50 and humidity < 60 and p > 30:
            st.success(f"### {t['cotton']}")
            st.write("Good potassium for cotton.")
        else:
            st.info("Soil moderate. Try crop rotation.")

elif page == t["advice"]:
    st.header(t["advice"])
    col1, col2 = st.columns(2)
    
    mandi_data = {
        "Crop": [t["wheat"], t["rice"], t["cotton"], t["sugar"], t["maize"]],
        "Trend": [t["stable"], t["rising"], t["falling"], t["stable"], t["rising"]]
    }
    df = pd.DataFrame(mandi_data)
    
    with col1:
        selected_crop = st.selectbox(t["select_crop"], [t["wheat"], t["rice"], t["cotton"], t["sugar"], t["maize"]])
        quantity = st.number_input(t["quantity"], min_value=1, value=10)
        current_price = st.number_input(t["price"], min_value=0, value=3950)
        cost_per_bag = st.number_input(t["cost"], min_value=0, value=3000)
    
    with col2:
        st.write("")
        st.write("")
        trend = df[df["Crop"] == selected_crop]["Trend"].values[0]
        revenue = quantity * current_price
        cost = quantity * cost_per_bag
        profit = revenue - cost
        
        if trend == t["rising"]:
            st.success(f"### {t['hold']}")
        elif trend == t["falling"]:
            st.error(f"### {t['sell']}")
        else:
            st.info(f"### {t['monitor']}")
        
        st.metric(t["revenue"], f"Rs. {revenue:,}")
        st.metric(t["profit"], f"Rs. {profit:,}")

elif page == t["market"]:
    st.header(t["market"])
    
    market_data = {
        "Crop": [t["wheat"], t["rice"], t["cotton"], t["sugar"], t["maize"]],
        "Price (40kg)": [t["wheat_price"], t["rice_price"], t["cotton_price"], t["sugar_price"], t["maize_price"]],
        "Trend": [t["stable"], t["rising"], t["falling"], t["stable"], t["rising"]]
    }
    df_market = pd.DataFrame(market_data)
    st.table(df_market)
    st.caption("Source: PAMRA & Agriculture Department")

elif page == t["schemes"]:
    st.header(t["schemes"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(t["tractor"])
        st.success(t["kissan"])
    
    with col2:
        st.warning(t["water"])
        st.info(t["fertilizer"])

st.divider()
st.caption("AgriSmart Punjab | 2026 | Farmers First")
