import streamlit as st

st.header("Baumvolumenberechner")

mittelwert = float(st.number_input("Mittelwert des Baumes:"))

laenge = st.selectbox(
    "Wie lange ist er?",
    ["5,10m", "4,10m", "Benutzerdefinierte Länge"]
)

if laenge == "Benutzerdefinierte Länge":
    l = float(st.number_input("Wie lautet das Benutzerdefinierte maß? (cm)"))

if st.button("Berechnen"):
        if laenge == "5,10m":
            wert1 = mittelwert * mittelwert
            wert2 = wert1 * 3.14
            wert3 = wert2 * 510
            wert4 = wert3 / 1000000
        
            st.write(f"Ergebnis: {wert4}m³")
        
        elif laenge == "4,20m":
             wert1 = mittelwert * mittelwert
             wert2 = wert1 * 3.14
             wert3 = wert2 * 420
             wert4 = wert3 / 1000000

             st.write(f"Ergebnis: {wert4}m³")

        elif laenge == "Benutzerdefinierte Laenge":
            wert1 = mittelwert * mittelwert
            wert2 = wert1 * 3.14
            wert3 = wert2 * l
            wert4 = wert3 / 1000000

            st.write(f"Ergebnis: {wert4}m³")