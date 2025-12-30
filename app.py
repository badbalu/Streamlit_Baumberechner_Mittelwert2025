import streamlit as st

st.header("Baumvolumenberechner")

# Eingabe Mittelwert in cm
mittelwert = st.number_input("Mittelwert des Baumes (cm):", min_value=0.0, step=0.1)

# Auswahl der Länge
laenge = st.selectbox(
    "Wie lange ist der Baum?",
    ["5,20m", "4,10m", "Benutzerdefinierte Länge"]
)

# Benutzerdefinierte Länge
l = None
if laenge == "Benutzerdefinierte Länge":
    l = st.number_input("Benutzerdefinierte Länge (m):", min_value=0.0, step=0.1)

# Berechnung
if st.button("Berechnen"):
    # Mittelwert in Meter umrechnen
    mittelwert_m = mittelwert / 100  

    if laenge == "5,20m":
        laenge_m = 5.20
    elif laenge == "4,10m":
        laenge_m = 4.10
    elif laenge == "Benutzerdefinierte Länge":
        if l is None or l == 0:
            st.error("Bitte eine gültige Länge eingeben.")
        else:
            laenge_m = l

    # Volumenberechnung: Kreisfläche * Länge
    if laenge != "Benutzerdefinierte Länge" or (l is not None and l > 0):
        volumen = 3.14 * (mittelwert_m / 2) ** 2 * laenge_m
        st.write(f"Ergebnis: {volumen:.4f} m³")
