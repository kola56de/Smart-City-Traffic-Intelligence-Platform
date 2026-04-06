# ----------------------------
# IMPORTS
# ----------------------------
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import requests
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from openai import OpenAI
from fpdf import FPDF

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Smart Traffic System", layout="wide")
st.title("🌍 Smart City Traffic Intelligence Platform")

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    data = {
        "ROUTE": ["Banex–Hospital", "Maitama–Wuse", "CBD–Airport", "Jabi–Utako", "Asokoro–Garki"],
        "LENGTH_KM": [2.5, 5.0, 8.0, 6.5, 4.0],
        "TIME_SEC": [471, 900, 1400, 1100, 700],
        "AVG_SPEED": [19, 25, 30, 22, 28],
        "LAT": [9.0765, 9.0800, 9.0600, 9.0700, 9.0500],
        "LON": [7.3986, 7.4000, 7.4500, 7.4200, 7.4800],
        "HOUR": [8, 9, 14, 18, 20]
    }
    return pd.DataFrame(data)

df = load_data()

# ----------------------------
# MODEL TRAINING
# ----------------------------
X = df[["LENGTH_KM", "TIME_SEC", "HOUR"]]
y = df["AVG_SPEED"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# ----------------------------
# USER INPUT
# ----------------------------
route = st.selectbox("Select Route", df["ROUTE"])
selected = df[df["ROUTE"] == route].iloc[0]

hour = st.slider("Select Hour (0–23)", 0, 23, int(selected["HOUR"]))

pred_speed = model.predict([[selected["LENGTH_KM"], selected["TIME_SEC"], hour]])[0]

# ----------------------------
# TRAFFIC ANALYSIS
# ----------------------------
speed_diff = selected["AVG_SPEED"] - pred_speed
percent_diff = (speed_diff / pred_speed) * 100

if percent_diff < -20:
    severity = "🔴 Critical"
elif percent_diff < -10:
    severity = "🟠 Heavy"
elif percent_diff < -5:
    severity = "🟡 Moderate"
else:
    severity = "🟢 Normal"

# ----------------------------
# DASHBOARD METRICS
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Predicted Speed", f"{pred_speed:.2f} km/h")
col2.metric("Actual Speed", f"{selected['AVG_SPEED']} km/h")
col3.metric("Difference (%)", f"{percent_diff:.1f}%")
col4.metric("Traffic Status", severity)

# ----------------------------
# RUSH HOUR ALERT
# ----------------------------
if 7 <= hour <= 10 or 16 <= hour <= 20:
    st.warning("🚦 Rush Hour Detected")

# ----------------------------
# MAP (ROUTE LINE)
# ----------------------------
st.subheader("🗺️ Route Map")

route_path = [
    [selected["LON"], selected["LAT"]],
    [selected["LON"] + 0.01, selected["LAT"] + 0.01]
]

layer = pdk.Layer(
    "PathLayer",
    data=[{"path": route_path}],
    get_path="path",
    get_width=5,
    get_color=[255, 0, 0],
)

view_state = pdk.ViewState(
    latitude=selected["LAT"],
    longitude=selected["LON"],
    zoom=12
)

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# ----------------------------
# LIVE TRAFFIC (SIMULATED)
# ----------------------------
st.subheader("📡 Live Traffic Feed")

def get_live_traffic():
    return {
        "Traffic Level": "Heavy",
        "Average Speed": "18 km/h",
        "Incident": "Minor accident reported"
    }

st.write(get_live_traffic())

# ----------------------------
# RULE-BASED ACTIONS
# ----------------------------
st.subheader("🔧 Recommended Actions")

actions = []

if "🔴" in severity:
    actions += ["Deploy officers immediately", "Open alternative routes"]

elif "🟠" in severity:
    actions += ["Adjust traffic lights", "Monitor congestion"]

elif "🟡" in severity:
    actions += ["Observe traffic trends"]

else:
    actions += ["Traffic is stable"]

for act in actions:
    st.write(f"- {act}")

# ----------------------------
# OPENAI SETUP
# ----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ----------------------------
# AI REPORT
# ----------------------------
st.subheader("🤖 AI Engineering Report")

if st.button("Generate AI Report"):
    prompt = f"""
    You are a transportation engineer in Abuja.

    Route: {route}
    Predicted Speed: {pred_speed:.2f}
    Actual Speed: {selected['AVG_SPEED']}
    Congestion Level: {severity}

    Provide root cause, impact, and solutions.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Traffic expert"},
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response.choices[0].message.content)

# ----------------------------
# CHATBOT
# ----------------------------
st.subheader("💬 Ask Traffic AI")

question = st.text_input("Ask anything about traffic...")

if st.button("Ask"):
    if question:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Traffic engineer in Abuja"},
                {"role": "user", "content": question}
            ]
        )
        st.write(response.choices[0].message.content)

# ----------------------------
# PDF REPORT
# ----------------------------
def generate_pdf(route, pred_speed, actual_speed, severity):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Traffic Analysis Report", ln=True)
    pdf.cell(200, 10, txt=f"Route: {route}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Speed: {pred_speed:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Actual Speed: {actual_speed}", ln=True)
    pdf.cell(200, 10, txt=f"Status: {severity}", ln=True)

    file_name = "traffic_report.pdf"
    pdf.output(file_name)
    return file_name

st.subheader("📄 Export Report")

if st.button("Download PDF Report"):
    file = generate_pdf(route, pred_speed, selected["AVG_SPEED"], severity)

    with open(file, "rb") as f:
        st.download_button("Download", f, file_name=file)
