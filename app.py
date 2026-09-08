import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="FlightDelay AI", page_icon="✈️", layout="wide", initial_sidebar_state="expanded")

rf = joblib.load("flight_delay_model.pkl")
model_columns = joblib.load("model_columns.pkl")
top_carriers = joblib.load("top_carriers.pkl")
top_origins = joblib.load("top_origins.pkl")
top_dests = joblib.load("top_dests.pkl")

# ---------- SVG ICONS (all single-line) ----------
ICON_PLANE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-1 .1-1.3.5l-.4.6c-.4.6-.2 1.4.4 1.8L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.6 5.5c.4.6 1.2.8 1.8.4l.6-.4c.4-.3.6-.8.5-1.3Z"/></svg>'
ICON_CALENDAR = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>'
ICON_PIN = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
ICON_CLOCK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
ICON_DISTANCE = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><path d="M8 3 4 7l4 4M16 21l4-4-4-4M4 7h16M20 17H4"/></svg>'
ICON_DOC = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-3px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg>'
ICON_DB = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/></svg>'
ICON_INFO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>'
ICON_CHECK = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>'
ICON_WARN = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/></svg>'
ICON_BULB = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-3px;"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.6.5 1 1.3 1 2.1v.4h6v-.4c0-.8.4-1.6 1-2.1A6 6 0 0 0 12 3Z"/></svg>'
ICON_CLIPBOARD = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px;"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>'
ICON_PLANE_BIG = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#93B4E8" stroke-width="2"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-1 .1-1.3.5l-.4.6c-.4.6-.2 1.4.4 1.8L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.6 5.5c.4.6 1.2.8 1.8.4l.6-.4c.4-.3.6-.8.5-1.3Z"/></svg>'

# ---------- CSS ----------
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #F8FAFC 0%, #F1F5FB 100%); }
.main .block-container { max-width: 1400px; padding-top: 2.5rem; padding-bottom: 2rem; padding-left: 3rem; padding-right: 3rem; }

section[data-testid="stSidebar"] > div:first-child {
    display: flex;
    flex-direction: column;
    height: 100vh;
}
.sidebar-illustration {
    margin-top: auto;
    margin-bottom: 0;
}

.brand { font-size: 1.55rem; font-weight: 800; color: #0F172A; margin-bottom: 0.35rem; }
.brand-blue { background: linear-gradient(135deg, #3B82F6, #1D4ED8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.tagline { color: #64748B; font-size: 0.95rem; line-height: 1.5; margin-bottom: 1.5rem; }
.sidebar-line { width: 70px; height: 3px; background: linear-gradient(90deg, #3B82F6, #93B4E8); border-radius: 10px; margin: 1rem 0; }

.sidebar-footer { color: #64748B; font-size: 0.82rem; line-height: 1.5; margin-top: 1rem; }

.data-badge { display: inline-block; background: #EFF6FF; color: #2563EB; border: 1px solid #DBEAFE; border-radius: 999px; padding: 0.45rem 0.9rem; font-size: 0.82rem; font-weight: 600; margin-bottom: 0.8rem; box-shadow: 0 2px 8px rgba(37,99,235,0.06); }
.page-title { font-size: 3rem; font-weight: 800; color: #0F172A; letter-spacing: -1.5px; line-height: 1.1; margin: 0; }
.page-title-blue { background: linear-gradient(135deg, #3B82F6, #1D4ED8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.page-subtitle { color: #64748B; font-size: 1.05rem; margin-top: 0.6rem; margin-bottom: 1.8rem; }
.realtime-note { text-align: right; color: #64748B; font-size: 0.85rem; padding-top: 0.6rem; }
[data-testid="stVerticalBlockBorderWrapper"] { border-radius: 16px !important; box-shadow: 0 4px 24px rgba(37,99,235,0.07) !important; border: 1px solid #EEF2FF !important; }
.card-header { font-size: 1.3rem; font-weight: 750; color: #0F172A; margin-bottom: 0.15rem; }
.card-subtitle { color: #64748B; font-size: 0.88rem; margin-bottom: 1.2rem; }
.field-label { display:flex; align-items:center; gap:6px; font-weight:600; color:#1E293B; margin-bottom:0.3rem; font-size:0.95rem; }
div.stButton > button { width: 100%; height: 3.2rem; background: linear-gradient(135deg, #3B82F6, #2563EB); color: white; border: none; border-radius: 10px; font-size: 1rem; font-weight: 700; box-shadow: 0 6px 18px rgba(37,99,235,0.25); }
div.stButton > button:hover { background: linear-gradient(135deg, #2563EB, #1D4ED8); color: white; box-shadow: 0 8px 22px rgba(37,99,235,0.32); }
.result-box { padding: 1.4rem; border-radius: 14px; border: 1px solid #BBF7D0; background: linear-gradient(135deg, #F0FDF4, #ECFDF5); margin-bottom: 1rem; box-shadow: 0 4px 20px rgba(21,128,61,0.08); }
.result-box-delayed { border: 1px solid #FECACA; background: linear-gradient(135deg, #FFF1F2, #FEF2F2); box-shadow: 0 4px 20px rgba(220,38,38,0.08); }
.result-title { font-size: 1.5rem; font-weight: 800; margin-bottom: 0.2rem; }
.result-probability { font-size: 1rem; color: #334155; }
.result-note { padding: 0.85rem 1rem; border-radius: 9px; margin-top: 1rem; font-size: 0.9rem; line-height: 1.45; }
.summary-title { font-size: 1.2rem; font-weight: 750; color: #0F172A; margin-bottom: 0.2rem; }
.summary-subtitle { color: #64748B; font-size: 0.85rem; margin-bottom: 0.8rem; }
.note-box { background: #EFF6FF; border: 1px solid #DBEAFE; padding: 1rem 1.2rem; border-radius: 12px; margin-top: 1.6rem; color: #475569; font-size: 0.88rem; }
.note-blue { color: #2563EB; font-weight: 700; }
[data-testid="stDateInput"] input, [data-testid="stNumberInput"] input, div[data-baseweb="select"] { border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div style="font-size:2.6rem; margin-bottom:0.4rem;">✈️</div>', unsafe_allow_html=True)
    st.markdown('<div class="brand">FlightDelay <span class="brand-blue">AI</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">Data today.<br>Smoother tomorrows.</div>', unsafe_allow_html=True)

# ---------- HEADER ----------
header_left, header_right = st.columns([4, 1])
with header_left:
    st.markdown(f'<div class="data-badge">{ICON_DB} Trained on 2018 US Domestic Flight Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title">Will your flight be <span class="page-title-blue">delayed?</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Enter your flight details to predict if it will arrive more than 15 minutes late.</div>', unsafe_allow_html=True)
with header_right:
    st.markdown(f'<div class="realtime-note">{ICON_INFO} Not real-time data</div>', unsafe_allow_html=True)

# ---------- MAIN COLUMNS ----------
col_form, col_result = st.columns([1.15, 0.85], gap="large")

with col_form:
    with st.container(border=True):
        st.markdown(f'<div class="card-header">{ICON_PLANE} Flight Details</div>', unsafe_allow_html=True)
        st.markdown('<div class="card-subtitle">Fill in the details below.</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="field-label">{ICON_CALENDAR} Flight Date</div>', unsafe_allow_html=True)
            fl_date = st.date_input("Flight Date", label_visibility="collapsed")
        with c2:
            st.markdown(f'<div class="field-label">{ICON_PLANE} Airline</div>', unsafe_allow_html=True)
            op_carrier = st.selectbox("Airline", top_carriers + ["Other"], label_visibility="collapsed")

        c3, c4 = st.columns(2)
        with c3:
            st.markdown(f'<div class="field-label">{ICON_PIN} Origin Airport</div>', unsafe_allow_html=True)
            origin = st.selectbox("Origin", top_origins + ["Other"], label_visibility="collapsed")
        with c4:
            st.markdown(f'<div class="field-label">{ICON_PIN} Destination Airport</div>', unsafe_allow_html=True)
            dest = st.selectbox("Destination", top_dests + ["Other"], label_visibility="collapsed")

        c5, c6 = st.columns(2)
        with c5:
            st.markdown(f'<div class="field-label">{ICON_CLOCK} Scheduled Departure Hour</div>', unsafe_allow_html=True)
            dep_hour = st.slider("Dep Hour", 0, 23, 8, label_visibility="collapsed")
        with c6:
            st.markdown(f'<div class="field-label">{ICON_DISTANCE} Distance (miles)</div>', unsafe_allow_html=True)
            distance = st.number_input("Distance", min_value=0, value=500, step=50, label_visibility="collapsed")

        st.write("")
        predict_clicked = st.button("✨ Predict Flight →")

with col_result:
    if predict_clicked:
        input_df = pd.DataFrame([{
            "FL_DATE": pd.to_datetime(fl_date),
            "OP_CARRIER": op_carrier,
            "ORIGIN": origin,
            "DEST": dest,
            "CRS_DEP_TIME": dep_hour * 100,
            "DISTANCE": distance
        }])
        input_df["DAY_OF_WEEK"] = input_df["FL_DATE"].dt.dayofweek
        input_df["MONTH"] = input_df["FL_DATE"].dt.month
        input_df["DEP_HOUR"] = dep_hour

        input_encoded = pd.get_dummies(input_df, columns=["OP_CARRIER", "ORIGIN", "DEST"])
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

        pred = rf.predict(input_encoded)[0]
        prob = rf.predict_proba(input_encoded)[0][1]

        if pred == 1:
            result_class = "result-box result-box-delayed"
            result_color = "#DC2626"
            icon_svg = ICON_WARN
            label = "Likely DELAYED"
            note = "This flight is predicted to arrive more than 15 minutes late."
            note_bg = "#FEE2E2"
        else:
            result_class = "result-box"
            result_color = "#15803D"
            icon_svg = ICON_CHECK
            label = "Likely ON-TIME"
            note = "This flight is predicted to arrive within the scheduled time (≤ 15 minutes delay)."
            note_bg = "#DCFCE7"

        st.markdown(f'<div class="{result_class}"><div style="display:flex; align-items:center; gap:15px;"><div style="width:58px; height:58px; border-radius:50%; background:{result_color}; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px {result_color}55;">{icon_svg}</div><div><div class="result-title" style="color:{result_color};">{label}</div><div class="result-probability"><b>{prob:.1%}</b> probability of delay</div></div></div></div>', unsafe_allow_html=True)

        st.progress(float(prob))
        st.markdown(f'<div style="text-align:right; color:#64748B; font-size:0.82rem; margin-top:-0.55rem; margin-bottom:0.8rem;">{prob:.1%}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-note" style="background:{note_bg}; color:{result_color};">{ICON_CLIPBOARD} {note}</div>', unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(f'<div class="summary-title">{ICON_DOC} Flight Summary</div>', unsafe_allow_html=True)
            st.markdown('<div class="summary-subtitle">Here are the details you entered and the model\'s prediction.</div>', unsafe_allow_html=True)

            summary_df = pd.DataFrame({
                "Field": ["Date", "Airline", "Route", "Scheduled Departure Hour", "Distance", "Predicted Delay Probability", "Prediction"],
                "Value": [str(fl_date), op_carrier, f"{origin} → {dest}", f"{dep_hour}:00", f"{distance:,} miles", f"{prob:.1%}", label]
            })
            st.table(summary_df.set_index("Field"))

    else:
        with st.container(border=True):
            st.markdown(f'<div style="text-align:center; padding:1.5rem 0.5rem;"><div style="margin-bottom:0.8rem;">{ICON_PLANE_BIG}</div><div style="font-size:1.2rem; font-weight:750; color:#0F172A; margin-bottom:0.4rem;">Your prediction will appear here</div><div style="color:#64748B; font-size:0.9rem; line-height:1.5;">Enter the flight details on the left<br>and click <b>Predict Flight</b>.</div></div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(f'<div class="note-box">{ICON_BULB} <span class="note-blue">Note:</span> Predictions are based on historical patterns from <b>2018 US domestic flights</b> and do not reflect real-time conditions.</div>', unsafe_allow_html=True)