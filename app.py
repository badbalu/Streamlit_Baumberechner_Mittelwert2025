import streamlit as st
import pandas as pd
from io import BytesIO
import hashlib

# --- Einfaches Login-System ---
st.session_state.setdefault("logged_in", False)

# Benutzername:Passwort-Hash (SHA256)
USER_CREDENTIALS = {
    "user1": hashlib.sha256("pass1".encode()).hexdigest(),
    "user2": hashlib.sha256("pass2".encode()).hexdigest(),
    "admin": hashlib.sha256("admin123".encode()).hexdigest()
}

def check_login(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password_hash:
        return True
    return False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Benutzername")
    password = st.text_input("Passwort", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success(f"Willkommen {username}!")
        else:
            st.error("Benutzername oder Passwort falsch")
    st.stop()

# --- App nach Login ---
st.header("Baumvolumenberechner")

# Tabelle initialisieren
if "baum_df" not in st.session_state:
    st.session_state.baum_df = pd.DataFrame(columns=["Baum Länge (m)", "Volumen (m³)"])

# Eingabe für einen Baum
mittelwert = st.number_input("Mittelwert des Baumes (cm):", min_value=0.0, step=0.1)

laenge = st.selectbox(
    "Wie lange ist der Baum?",
    ["5,20m", "4,10m", "Benutzerdefinierte Länge"]
)

l = None
if laenge == "Benutzerdefinierte Länge":
    l = st.number_input("Benutzerdefinierte Länge (m):", min_value=0.0, step=0.1)

# Berechnen & Tabelle aktualisieren
if st.button("Berechnen"):
    mittelwert_m = mittelwert / 100  # cm -> m

    if laenge == "5,20m":
        laenge_m = 5.20
    elif laenge == "4,10m":
        laenge_m = 4.10
    elif laenge == "Benutzerdefinierte Länge":
        if l is None or l == 0:
            st.error("Bitte eine gültige Länge eingeben.")
        else:
            laenge_m = l

    if laenge != "Benutzerdefinierte Länge" or (l is not None and l > 0):
        volumen = 3.14 * (mittelwert_m / 2) ** 2 * laenge_m
        st.session_state.baum_df = pd.concat([
            st.session_state.baum_df,
            pd.DataFrame({"Baum Länge (m)": [laenge_m], "Volumen (m³)": [volumen]})
        ], ignore_index=True)

# Tabelle anzeigen
st.subheader("Tabelle der berechneten Bäume")
st.dataframe(st.session_state.baum_df)

# CSV-Download
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")

if not st.session_state.baum_df.empty:
    csv = convert_df_to_csv(st.session_state.baum_df)
    st.download_button(
        label="Tabelle herunterladen als CSV",
        data=csv,
        file_name="baumvolumen.csv",
        mime="text/csv"
    )
