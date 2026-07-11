import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Anti Creep Clicker",
    page_icon="🖱️",
    layout="centered"
)

# --- Удаляем всю старую информацию и выводим новую ---

# Заголовок
st.title("🖱️ Anti Creep Clicker")

# Текст о разработчике
st.markdown("""
## Привет! Я разработчик кликера **Anti Creep Clicker**!

Это моя игра, в которой вам предстоит кликать по ползучим врагам.  
Она создана с любовью и вниманием к деталям.
""")

# Разделитель
st.divider()

# Секция с APK
st.header("📲 Скачать игру")

st.markdown("""
**Версия для Android (APK) уже доступна!**

Нажмите на кнопку ниже, чтобы скачать установочный файл и начать играть.
""")

# КНОПКА ДЛЯ СКАЧИВАНИЯ APK
# ВАЖНО: Замените URL ниже на прямую ссылку для скачивания вашего APK-файла
apk_url = "https://ваша-ссылка-на-ваш-файл.apk"  # <--- ИЗМЕНИТЕ ЭТУ ССЫЛКУ

st.download_button(
    label="📥 Скачать Anti Creep Clicker (APK)",
    data=open(apk_url, "rb").read(),  # Открывает файл для чтения в бинарном режиме
    file_name="AntiCreepClicker.apk",
    mime="application/vnd.android.package-archive",
    use_container_width=True,
)

# Если файл лежит не в той же папке, что и app.py, нужно указать путь.
# Например: data=open("static/AntiCreepClicker.apk", "rb").read(),

# Дополнительная информация
st.divider()
st.caption("© 2026 Anti Creep Clicker. Все права защищены.")
