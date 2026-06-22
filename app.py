import streamlit as st

# --- НАСТРОЙКА СТРАНИЦЫ ---
st.set_page_config(
    page_title="Портфолио Шарнина Семёна",
    page_icon="🚀",
    layout="centered"
)

# --- СТИЛИ ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 0 !important;
    }

    .main > div {
        padding: 0 !important;
        max-width: 100% !important;
    }

    .block-container {
        padding-top: 0px !important;
        padding-bottom: 10px !important;
        padding-left: 20px !important;
        padding-right: 20px !important;
        max-width: 100% !important;
    }

    header {
        background: transparent !important;
        display: none !important;
    }

    .stApp > header {
        display: none !important;
    }

    .stApp .main .block-container:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    footer {
        display: none !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.5) !important;
        border-radius: 10px !important;
        padding: 8px 20px !important;
    }

    .stTabs [aria-selected="true"] {
        background: rgba(255,255,255,0.9) !important;
    }

    .main-header {
        text-align: center;
        padding: 15px;
        background: rgba(255,255,255,0.7);
        border-radius: 15px;
        margin-bottom: 15px;
        margin-top: 0px;
    }

    .main-header h1 {
        margin: 0 !important;
        padding: 0 !important;
    }

    .main-header h3 {
        margin: 0 !important;
        padding: 0 !important;
    }

    .info-card {
        background: rgba(255,255,255,0.85);
        padding: 20px 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        margin: 5px 0 10px 0;
    }

    .info-card p {
        margin: 8px 0 !important;
        line-height: 1.6 !important;
    }

    .contact-info {
        background: rgba(240, 244, 255, 0.9);
        padding: 15px 20px;
        border-radius: 10px;
        border-left: 4px solid #4A90D9;
        margin: 10px 0;
    }

    .instruction-box {
        background: rgba(248, 249, 250, 0.9);
        padding: 12px 18px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 8px 0;
    }

    .step {
        background: #4A90D9;
        color: white;
        display: inline-block;
        padding: 2px 10px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        margin-right: 8px;
    }

    hr {
        margin: 10px 0 !important;
    }

    .app-card {
        background: rgba(255,255,255,0.85);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        margin: 5px 0;
        height: 100%;
        border-left: none !important;
    }

    .stColumn {
        border-right: 3px solid #aaaaaa !important;
        padding-right: 20px !important;
    }

    .stColumn:last-child {
        border-right: none !important;
        padding-left: 20px !important;
        padding-right: 0px !important;
    }

    .stColumn > div {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- ЗАГОЛОВОК ---
st.markdown(
    '<div class="main-header"><h1>🚀 Портфолио</h1><h3>Шарнина Семёна</h3></div>',
    unsafe_allow_html=True
)

# --- ВКЛАДКИ ---
tab1, tab2 = st.tabs(["📄 Обо мне", "📦 Скачать мои приложения"])

# =====================================================
# ВКЛАДКА 1: ОБО МНЕ
# =====================================================
with tab1:
    st.markdown(
        """
        <div class="info-card">
            <h3 style="margin-top: 0;">👋 Привет! Я Семён</h3>
            <p>
                Меня зовут <strong>Шарнин Семён</strong>, я студент группы <strong>Гр-ИС-944</strong>. 
                Учусь на программиста и постепенно превращаю свои идеи в рабочие приложения.
            </p>
            <p>
                Сейчас я на старте своего пути в IT, но уже успел понять главное: 
                <strong>программирование — это не просто код, а способ решать реальные задачи</strong>. 
                Мне нравится создавать что-то полезное — будь то мобильное приложение или десктопная программа.
            </p>
            <hr>
            <p><strong>🎯 Чем я занимаюсь сейчас:</strong></p>
            <p>
                🎓 Учусь на <strong>2-м курсе</strong> по направлению <strong>"Информационные системы"</strong><br>
                🐍 Пишу небольшие проекты на <strong>Python</strong><br>
                📱 Изучаю мобильную разработку<br>
                💻 Создаю десктопные приложения
            </p>
            <hr>
            <p><strong>💡 Мои интересы в программировании:</strong></p>
            <p>
                📱 Создание мобильных приложений (APK)<br>
                💻 Разработка десктопного ПО (EXE)<br>
                🎨 Интерфейсы, которые приятно использовать<br>
                ⚡ Автоматизация повседневных задач
            </p>
            <hr>
            <div class="contact-info">
                <p style="margin: 0;"><strong>📬 Связь</strong></p>
                <p style="margin: 5px 0 0 0;">
                    Я открыт к общению, советам и сотрудничеству.<br>
                    Если вам интересны мои проекты или есть идея — пишите!
                </p>
                <p style="margin: 8px 0 0 0;">
                    📞 <strong>Телефон:</strong> 8-913-283-19-15 &nbsp;&nbsp;|&nbsp;&nbsp; 
                    📍 <strong>Адрес:</strong> г. Кемерово, ул. Терешковой, 35
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# ВКЛАДКА 2: СКАЧАТЬ МОИ ПРИЛОЖЕНИЯ (С ВАШИМИ ФАЙЛАМИ)
# =====================================================
with tab2:
    st.markdown("### 📦 Мои разработки")
    st.markdown("Здесь вы можете скачать и установить мои приложения")

    col_left, col_right = st.columns(2)

    # ===== ЛЕВАЯ КОЛОНКА: EXE =====
    with col_left:
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("#### 💻 Десктопное приложение (EXE)")
        st.markdown("""
        **Описание:**  
        Приложение для кондитерской. Управление заказами, 
        учёт продукции и работа с клиентами.

        **Особенности:**
        - 📊 Учёт заказов
        - 🧁 Каталог продукции
        - 👥 Работа с клиентами
        - 📈 Отчёты и статистика
        """)

        with st.expander("📖 Инструкция по установке EXE"):
            st.markdown("""
            <div class="instruction-box">
                <p><span class="step">1</span> Скачайте EXE-файл на ваш компьютер</p>
                <p><span class="step">2</span> Запустите файл двойным кликом</p>
                <p><span class="step">3</span> Если появится предупреждение Windows — нажмите "Выполнить"</p>
                <p><span class="step">4</span> Готово! Приложение готово к работе</p>
            </div>
            """, unsafe_allow_html=True)

        # КНОПКА СКАЧИВАНИЯ EXE (ВАШ ФАЙЛ)
        try:
            with open("static/Кондитерская_Desktop.exe", "rb") as file:
                st.download_button(
                    label="📥 Скачать EXE",
                    data=file,
                    file_name="Кондитерская_Desktop.exe",
                    mime="application/octet-stream",
                    use_container_width=True
                )
        except FileNotFoundError:
            st.error("❌ Файл не найден! Проверьте, что Кондитерская_Desktop.exe лежит в папке static")
            st.download_button(
                label="📥 Скачать EXE",
                data="",
                file_name="Кондитерская_Desktop.exe",
                mime="application/octet-stream",
                disabled=True,
                use_container_width=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    # ===== ПРАВАЯ КОЛОНКА: APK =====
    with col_right:
        st.markdown('<div class="app-card">', unsafe_allow_html=True)
        st.markdown("#### 📱 Мобильное приложение (APK)")
        st.markdown("""
        **Описание:**  
        Мобильное приложение для управления заказами кондитерской. 
        Клиенты могут просматривать каталог и оформлять заказы.

        **Особенности:**
        - 🧁 Каталог продукции
        - 🛒 Корзина заказов
        - 📱 Удобный интерфейс
        - 💳 Онлайн-оплата
        """)

        with st.expander("📖 Инструкция по установке APK"):
            st.markdown("""
            <div class="instruction-box">
                <p><span class="step">1</span> Скачайте APK-файл на ваш Android-смартфон</p>
                <p><span class="step">2</span> Откройте файл в проводнике</p>
                <p><span class="step">3</span> Разрешите установку из неизвестных источников</p>
                <p><span class="step">4</span> Нажмите "Установить"</p>
                <p><span class="step">5</span> Готово! Приложение появится в меню телефона</p>
            </div>
            """, unsafe_allow_html=True)

        # КНОПКА СКАЧИВАНИЯ APK (ВАШ ФАЙЛ)
        try:
            with open("static/app-debug.apk", "rb") as file:
                st.download_button(
                    label="📥 Скачать APK",
                    data=file,
                    file_name="app-debug.apk",
                    mime="application/vnd.android.package-archive",
                    use_container_width=True
                )
        except FileNotFoundError:
            st.error("❌ Файл не найден! Проверьте, что app-debug.apk лежит в папке static")
            st.download_button(
                label="📥 Скачать APK",
                data="",
                file_name="app-debug.apk",
                mime="application/vnd.android.package-archive",
                disabled=True,
                use_container_width=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

    st.info("💡 По вопросам сотрудничества: 8-913-283-19-15")