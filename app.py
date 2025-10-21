import pandas as pd
import streamlit as st
from datetime import datetime

# Pełna baza produktów z oferty
produkty = {
    'Kategoria': [
        # JAJKA
        'Jajka', 'Jajka', 'Jajka', 'Jajka',
        # WARZYWA
        'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa',
        'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa', 'Warzywa',
        'Warzywa', 'Warzywa', 'Warzywa',
        # PRZETWORY
        'Przetwory', 'Przetwory', 'Przetwory', 'Przetwory', 'Przetwory',
        'Przetwory', 'Przetwory',
        # MĄKI
        'Mąki', 'Mąki', 'Mąki', 'Mąki',
        # SYROPY
        'Syropy', 'Syropy',
        # NABIAŁ
        'Nabiał', 'Nabiał', 'Nabiał', 'Nabiał',
        # MIODY
        'Miody', 'Miody', 'Miody', 'Miody',
        # OLEJE
        'Oleje', 'Oleje', 'Oleje', 'Oleje', 'Oleje'
    ],
    'Produkt': [
        # JAJKA
        'Jajka L/XL', 'Jajka M', 'Jajka S (paletka 30 szt)', 'Jajka S (paletka 20 szt)',
        # WARZYWA
        'Ziemniaki Red Sonia (czerwone)', 'Ziemniaki Vineta (żółte)',
        'Cebula', 'Cebula czerwona', 'Cebula deserowa (do 10kg)', 'Cebula deserowa (od 10kg)',
        'Marchew (do 10kg)', 'Marchew (od 10kg)', 'Marchew na sok (opak 3kg)',
        'Pietruszka korzeń', 'Buraki (do 10kg)', 'Buraki (od 10kg)',
        'Czosnek', 'Seler korzeń', 'Por',
        # PRZETWORY
        'Dżem truskawkowy (315ml)', 'Powidła śliwkowe (315ml)', 'Gruszki w zalewie (0.9l)',
        'Ketchup z cukinii (315ml)', 'Ketchup z cukinii ostry (315ml)',
        'Przecier/sok pomidorowy (330ml)', 'Zakwas z buraka (0.9l)',
        # MĄKI
        'Mąka pszenna 500 (2kg)', 'Mąka pełnoziarnista 3000 (2kg)',
        'Mąka pszenna 500 (5kg)', 'Mąka pełnoziarnista 3000 (5kg)',
        # SYROPY
        'Syrop mniszek (330ml)', 'Syrop bez (330ml)',
        # NABIAŁ
        'Ser biały', 'Mleko 1l (butelka szklana)', 'Serwatka 1l (butelka szklana)', 'Śmietana 0.5l',
        # MIODY
        'Miód wielokwiatowy (1.2kg)', 'Miód wielokwiatowy (315ml)',
        'Miód lipowy (1.2kg)', 'Miód nawłociowy (1.2kg)',
        # OLEJE
        'Olej z ostropestu (250ml)', 'Olej z lnu (250ml)',
        'Olej z czarnuszki (250ml)', 'Olej z dyni (250ml)', 'Olej z wiesiołka (250ml)'
    ],
    'Jednostka': [
        # JAJKA
        'szt', 'szt', 'paletka', 'paletka',
        # WARZYWA
        'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'opak',
        'kg', 'kg', 'kg', 'szt', 'szt', 'szt',
        # PRZETWORY
        'słoik', 'słoik', 'słoik', 'słoik', 'słoik', 'butelka', 'słoik',
        # MĄKI
        'opak', 'opak', 'opak', 'opak',
        # SYROPY
        'butelka', 'butelka',
        # NABIAŁ
        'kg', 'butelka', 'butelka', 'słoik',
        # MIODY
        'słoik', 'słoik', 'słoik', 'słoik',
        # OLEJE
        'butelka', 'butelka', 'butelka', 'butelka', 'butelka'
    ],
    'Cena': [
        # JAJKA
        1.6, 1.4, 20.0, 14.0,
        # WARZYWA
        2.5, 2.5, 4.0, 6.0, 3.0, 2.5, 4.0, 3.5, 8.0,
        9.0, 5.0, 4.5, 3.0, 6.0, 5.0,
        # PRZETWORY
        14.0, 20.0, 25.0, 6.0, 6.0, 12.0, 22.0,
        # MĄKI
        10.0, 20.0, 24.0, 48.0,
        # SYROPY
        19.0, 19.0,
        # NABIAŁ
        48.0, 5.5, 3.0, 18.0,
        # MIODY
        40.0, 15.0, 50.0, 60.0,
        # OLEJE
        40.0, 30.0, 65.0, 60.0, 80.0
    ],
    'Uwagi': [
        # JAJKA
        '', '', '', '',
        # WARZYWA
        'pakowane po 2kg/5kg/15kg', 'pakowane po 2kg/5kg/15kg',
        '', '', '', 'od 10kg', '', 'od 10kg', '',
        '', '', 'od 10kg', '', '', '',
        # PRZETWORY
        '', '', '', '', '', '', '',
        # MĄKI
        '', '', '', '',
        # SYROPY
        'po otwarciu w lodówce', 'po otwarciu w lodówce',
        # NABIAŁ
        'minimum 0.5kg', 'kaucja 3.5zł', 'kaucja 3.5zł', '',
        # MIODY
        '', '', '', 'TYLKO 30 szt!',
        # OLEJE
        'Wiejska Manufaktura', 'Wiejska Manufaktura',
        'Wiejska Manufaktura', 'Wiejska Manufaktura', 'Wiejska Manufaktura'
    ]
}

# Skróty nazw produktów dla SMS
skroty = {
    'Jajka L/XL': 'Jajka L/XL',
    'Jajka M': 'Jajka M',
    'Jajka S (paletka 30 szt)': 'Jajka S 30szt',
    'Jajka S (paletka 20 szt)': 'Jajka S 20szt',
    'Ziemniaki Red Sonia (czerwone)': 'Ziemniaki czerw.',
    'Ziemniaki Vineta (żółte)': 'Ziemniaki żółte',
    'Cebula': 'Cebula',
    'Cebula czerwona': 'Cebula czerw.',
    'Cebula deserowa (do 10kg)': 'Cebula deser.',
    'Cebula deserowa (od 10kg)': 'Cebula deser. 10kg+',
    'Marchew (do 10kg)': 'Marchew',
    'Marchew (od 10kg)': 'Marchew 10kg+',
    'Marchew na sok (opak 3kg)': 'Marchew sok 3kg',
    'Pietruszka korzeń': 'Pietruszka',
    'Buraki (do 10kg)': 'Buraki',
    'Buraki (od 10kg)': 'Buraki 10kg+',
    'Czosnek': 'Czosnek',
    'Seler korzeń': 'Seler',
    'Por': 'Por',
    'Dżem truskawkowy (315ml)': 'Dżem trusk.',
    'Powidła śliwkowe (315ml)': 'Powidła śliw.',
    'Gruszki w zalewie (0.9l)': 'Gruszki',
    'Ketchup z cukinii (315ml)': 'Ketchup',
    'Ketchup z cukinii ostry (315ml)': 'Ketchup ostry',
    'Przecier/sok pomidorowy (330ml)': 'Sok pomid.',
    'Zakwas z buraka (0.9l)': 'Zakwas burak',
    'Mąka pszenna 500 (2kg)': 'Mąka 500 2kg',
    'Mąka pełnoziarnista 3000 (2kg)': 'Mąka pełnoz. 2kg',
    'Mąka pszenna 500 (5kg)': 'Mąka 500 5kg',
    'Mąka pełnoziarnista 3000 (5kg)': 'Mąka pełnoz. 5kg',
    'Syrop mniszek (330ml)': 'Syrop mniszek',
    'Syrop bez (330ml)': 'Syrop bez',
    'Ser biały': 'Ser biały',
    'Mleko 1l (butelka szklana)': 'Mleko',
    'Serwatka 1l (butelka szklana)': 'Serwatka',
    'Śmietana 0.5l': 'Śmietana',
    'Miód wielokwiatowy (1.2kg)': 'Miód wielokw. 1.2kg',
    'Miód wielokwiatowy (315ml)': 'Miód wielokw. 315ml',
    'Miód lipowy (1.2kg)': 'Miód lipowy',
    'Miód nawłociowy (1.2kg)': 'Miód nawłoc.',
    'Olej z ostropestu (250ml)': 'Olej ostropes.',
    'Olej z lnu (250ml)': 'Olej lniany',
    'Olej z czarnuszki (250ml)': 'Olej czarn.',
    'Olej z dyni (250ml)': 'Olej dyni',
    'Olej z wiesiołka (250ml)': 'Olej wiesioł.'
}

# Tworzenie DataFrame
df = pd.DataFrame(produkty)


# Funkcja generująca SMS z miejscem odbioru
def generuj_sms(df_zamowienie, miejsce_odbioru, adres_wlasny):
    data = datetime.now().strftime("%d.%m.%Y")
    sms = f"ZAMÓWIENIE {data}\n\n"

    # Dodanie miejsca odbioru
    if miejsce_odbioru == "Inny adres":
        sms += f"📌 {adres_wlasny}\n\n"
    else:
        sms += f"📌 {miejsce_odbioru}\n\n"

    for _, row in df_zamowienie.iterrows():
        nazwa_skrot = skroty.get(row['Produkt'], row['Produkt'][:20])
        ilosc = row['Ilość']
        jednostka = row['Jednostka']

        if ilosc == int(ilosc):
            ilosc_str = str(int(ilosc))
        else:
            ilosc_str = str(ilosc)

        sms += f"• {nazwa_skrot}: {ilosc_str}{jednostka}\n"

    suma_produkty = df_zamowienie['Wartość'].sum()
    sms += f"\nSuma: {suma_produkty:.2f}zł"

    butelki_mleko = df_zamowienie[df_zamowienie['Produkt'] == 'Mleko 1l (butelka szklana)']['Ilość'].sum()
    butelki_serwatka = df_zamowienie[df_zamowienie['Produkt'] == 'Serwatka 1l (butelka szklana)']['Ilość'].sum()
    suma_butelek = butelki_mleko + butelki_serwatka

    if suma_butelek > 0:
        kaucja = suma_butelek * 3.5
        sms += f"\nKaucja: {kaucja:.2f}zł ({int(suma_butelek)}but.)"
        sms += f"\nRAZEM: {suma_produkty + kaucja:.2f}zł"

    return sms


# Funkcja generująca długą wersję z miejscem odbioru
def generuj_wiadomosc_email(df_zamowienie, miejsce_odbioru, adres_wlasny):
    data = datetime.now().strftime("%d.%m.%Y %H:%M")
    msg = f"ZAMÓWIENIE - {data}\n"
    msg += "=" * 60 + "\n\n"

    # Dodanie miejsca odbioru
    if miejsce_odbioru == "Inny adres":
        msg += f"MIEJSCE DOSTAWY: {adres_wlasny}\n"
    else:
        msg += f"MIEJSCE ODBIORU: {miejsce_odbioru}\n"
    msg += "=" * 60 + "\n\n"

    for kategoria in df_zamowienie['Kategoria'].unique():
        msg += f"{kategoria.upper()}\n"
        msg += "-" * 40 + "\n"
        df_kat = df_zamowienie[df_zamowienie['Kategoria'] == kategoria]

        for _, row in df_kat.iterrows():
            ilosc = row['Ilość']
            if ilosc == int(ilosc):
                ilosc_str = str(int(ilosc))
            else:
                ilosc_str = f"{ilosc:.1f}"

            msg += f"{row['Produkt']}\n"
            msg += f"  {ilosc_str} {row['Jednostka']} × {row['Cena']:.2f}zł = {row['Wartość']:.2f}zł\n\n"

    suma_produkty = df_zamowienie['Wartość'].sum()
    msg += "=" * 60 + "\n"
    msg += f"SUMA ZA PRODUKTY: {suma_produkty:.2f} zł\n"

    butelki_mleko = df_zamowienie[df_zamowienie['Produkt'] == 'Mleko 1l (butelka szklana)']['Ilość'].sum()
    butelki_serwatka = df_zamowienie[df_zamowienie['Produkt'] == 'Serwatka 1l (butelka szklana)']['Ilość'].sum()
    suma_butelek = butelki_mleko + butelki_serwatka

    if suma_butelek > 0:
        kaucja = suma_butelek * 3.5
        msg += f"KAUCJA ZA BUTELKI: {kaucja:.2f} zł ({int(suma_butelek)} szt)\n"
        msg += f"\nDO ZAPŁATY RAZEM: {suma_produkty + kaucja:.2f} zł\n"
    else:
        msg += f"\nDO ZAPŁATY RAZEM: {suma_produkty:.2f} zł\n"

    msg += "=" * 60

    return msg


# Konfiguracja strony
st.set_page_config(
    page_title="Zamówienie Produktów Ekologicznych",
    page_icon="🥬",
    layout="wide"
)

# Inicjalizacja session state
if 'zamowienie' not in st.session_state:
    st.session_state.zamowienie = {}
if 'miejsce_odbioru' not in st.session_state:
    st.session_state.miejsce_odbioru = "📌 JELCZ-LASKOWICE"
if 'adres_wlasny' not in st.session_state:
    st.session_state.adres_wlasny = ""

# Nagłówek
st.title("🥬 Formularz Zamówienia - Produkty Ekologiczne")
st.markdown("---")

# Sekcja miejsca odbioru/dostawy
st.markdown("### 📍 Miejsce odbioru / dostawy")
col1, col2 = st.columns([1, 2])

with col1:
    miejsce_odbioru = st.selectbox(
        "Wybierz miejsce odbioru:",
        [
            "📌 JELCZ-LASKOWICE",
            "📌 NADOLICE WIELKIE",
            "📌 DOBRZYKOWICE",
            "📌 SIECHNICE",
            "📌 WROCŁAW",
            "📌 OLEŚNICA",
            "Inny adres"
        ],
        key="select_miejsce"
    )
    st.session_state.miejsce_odbioru = miejsce_odbioru

with col2:
    if miejsce_odbioru == "Inny adres":
        adres_wlasny = st.text_input(
            "Podaj adres dostawy (miejscowość, ulica, nr):",
            placeholder="np. Wrocław, ul. Kwiatowa 15",
            key="input_adres"
        )
        st.session_state.adres_wlasny = adres_wlasny
    else:
        st.info(f"Wybrane miejsce odbioru: **{miejsce_odbioru}**")

st.markdown("---")

# Filtry kategorii
col1, col2 = st.columns([1, 3])
with col1:
    kategoria = st.selectbox(
        "Filtruj według kategorii:",
        ["Wszystkie"] + sorted(df['Kategoria'].unique().tolist())
    )

# Filtrowanie danych
if kategoria == "Wszystkie":
    df_filtrowane = df
else:
    df_filtrowane = df[df['Kategoria'] == kategoria]

st.markdown("### 📋 Wybierz produkty i podaj ilość")

# Tworzenie formularza
for kategoria_nazwa in df_filtrowane['Kategoria'].unique():
    with st.expander(f"🔹 {kategoria_nazwa}", expanded=True):
        df_kat = df_filtrowane[df_filtrowane['Kategoria'] == kategoria_nazwa]

        for idx, row in df_kat.iterrows():
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 2])

            with col1:
                st.write(f"**{row['Produkt']}**")
            with col2:
                st.write(f"{row['Jednostka']}")
            with col3:
                st.write(f"{row['Cena']:.2f} zł")
            with col4:
                ilosc = st.number_input(
                    "Ilość",
                    min_value=0.0,
                    value=st.session_state.zamowienie.get(row['Produkt'], 0.0),
                    step=0.5,
                    key=f"ilosc_{idx}",
                    label_visibility="collapsed"
                )
                st.session_state.zamowienie[row['Produkt']] = ilosc
            with col5:
                if row['Uwagi']:
                    st.caption(f"ℹ️ {row['Uwagi']}")

st.markdown("---")

# Przyciski
col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    if st.button("📋 Pokaż Podsumowanie", use_container_width=True):
        st.session_state.pokazuj_podsumowanie = True
with col2:
    if st.button("🗑️ Wyczyść", use_container_width=True):
        st.session_state.zamowienie = {k: 0.0 for k in st.session_state.zamowienie.keys()}
        st.session_state.pokazuj_podsumowanie = False
        st.rerun()

# Podsumowanie
if st.session_state.get('pokazuj_podsumowanie', False):
    zamowienie_aktywne = {k: v for k, v in st.session_state.zamowienie.items() if v > 0}

    if zamowienie_aktywne:
        # Walidacja miejsca odbioru
        if st.session_state.miejsce_odbioru == "Inny adres" and not st.session_state.adres_wlasny:
            st.error("⚠️ Proszę podać adres dostawy!")
        else:
            st.markdown("### 💰 Podsumowanie Zamówienia")

            df_zamowienie = df[df['Produkt'].isin(zamowienie_aktywne.keys())].copy()
            df_zamowienie['Ilość'] = df_zamowienie['Produkt'].map(zamowienie_aktywne)
            df_zamowienie['Wartość'] = df_zamowienie['Cena'] * df_zamowienie['Ilość']

            # Wyświetlenie miejsca odbioru
            if st.session_state.miejsce_odbioru == "Inny adres":
                st.info(f"📍 **Miejsce dostawy:** {st.session_state.adres_wlasny}")
            else:
                st.info(f"📍 **Miejsce odbioru:** {st.session_state.miejsce_odbioru}")

            # Wyświetlanie tabeli
            st.dataframe(
                df_zamowienie[['Produkt', 'Jednostka', 'Cena', 'Ilość', 'Wartość']],
                use_container_width=True,
                hide_index=True
            )

            # Podsumowanie finansowe
            suma_produkty = df_zamowienie['Wartość'].sum()

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Suma za produkty", f"{suma_produkty:.2f} zł")

            # Kaucja
            butelki_mleko = df_zamowienie[df_zamowienie['Produkt'] == 'Mleko 1l (butelka szklana)']['Ilość'].sum()
            butelki_serwatka = df_zamowienie[df_zamowienie['Produkt'] == 'Serwatka 1l (butelka szklana)']['Ilość'].sum()
            suma_butelek = butelki_mleko + butelki_serwatka

            if suma_butelek > 0:
                kaucja = suma_butelek * 3.5
                with col2:
                    st.metric("Kaucja za butelki", f"{kaucja:.2f} zł",
                              help=f"{int(suma_butelek)} butelek × 3.50 zł")

                st.success(f"### 💵 DO ZAPŁATY RAZEM: {suma_produkty + kaucja:.2f} zł")
            else:
                st.success(f"### 💵 DO ZAPŁATY RAZEM: {suma_produkty:.2f} zł")

            st.markdown("---")
            st.markdown("### 📤 Wyślij zamówienie")

            # Generowanie wiadomości
            sms_text = generuj_sms(df_zamowienie, st.session_state.miejsce_odbioru, st.session_state.adres_wlasny)
            email_text = generuj_wiadomosc_email(df_zamowienie, st.session_state.miejsce_odbioru,
                                                 st.session_state.adres_wlasny)

            # Dwie kolumny
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### 📱 SMS / WhatsApp (krótka wersja)")
                st.info("👇 **Zaznacz tekst, kliknij prawym i wybierz 'Kopiuj'**")

                st.text_area(
                    label="Treść SMS:",
                    value=sms_text,
                    height=250,
                    key="sms_display",
                    help="Zaznacz tekst i skopiuj (Ctrl+C lub długie przytrzymanie na telefonie)"
                )

                st.download_button(
                    label="📥 Pobierz SMS (TXT)",
                    data=sms_text,
                    file_name=f"zamowienie_sms_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    type="primary"
                )

            with col2:
                st.markdown("#### 📧 Email (pełna wersja)")
                st.info("👇 **Zaznacz tekst, kliknij prawym i wybierz 'Kopiuj'**")

                st.text_area(
                    label="Treść Email:",
                    value=email_text,
                    height=250,
                    key="email_display",
                    help="Zaznacz tekst i skopiuj (Ctrl+C lub długie przytrzymanie na telefonie)"
                )

                st.download_button(
                    label="📥 Pobierz Email (TXT)",
                    data=email_text,
                    file_name=f"zamowienie_email_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain",
                    use_container_width=True,
                    type="primary"
                )

            st.markdown("---")

            # CSV na dole
            st.markdown("#### 💾 Pobierz jako arkusz kalkulacyjny")
            csv = df_zamowienie[['Kategoria', 'Produkt', 'Jednostka', 'Cena', 'Ilość', 'Wartość']].to_csv(index=False,
                                                                                                          encoding='utf-8-sig')
            st.download_button(
                label="📊 Pobierz CSV (Excel)",
                data=csv,
                file_name=f"zamowienie_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv",
                use_container_width=False
            )

            st.success(
                "💡 **Wskazówka na telefonie:** Przytrzymaj palec na tekście → Zaznacz wszystko → Kopiuj → Wklej w SMS/WhatsApp")

    else:
        st.warning("⚠️ Brak produktów w zamówieniu!")