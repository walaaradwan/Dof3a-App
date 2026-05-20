import streamlit as st
import google.generativeai as genai
import time
from datetime import date

st.set_page_config(page_title="تطبيق الدحيح AI", page_icon="🎓", layout="centered")
st.markdown("""
    <style>
    * { direction: rtl; text-align: right; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .stButton>button { background-color: #F97316; color: white; border-radius: 8px; font-weight: bold; width: 100%; }
    .stProgress > div > div > div > div { background-color: #10B981; }
    </style>
""", unsafe_allow_html=True)

# محاولة الاتصال بالذكاء الاصطناعي مع إظهار الأخطاء
model = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("❌ تنبيه: لم يتم العثور على المفتاح في إعدادات Secrets.")
except Exception as e:
    st.error(f"❌ خطأ أثناء إعداد المفتاح: {e}")

st.title("🎓 الدحيح AI - رفيقك للقمة")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📅 الخطة الذكية", "🤖 المساعد الذكي", "📊 متتبع الإنجاز", "⏱️ بومودورو", "🔥 التحفيز"
])

with tab1:
    st.subheader("صانع الجداول الذكي")
    subjects = st.text_input("ما هي المواد التي تريد مذاكرتها اليوم؟ (مثال: فيزياء، كيمياء)")
    hours = st.slider("كم عدد الساعات المتاحة للمذاكرة؟", 1, 10, 3)
    if st.button("إنشاء خطة المذاكرة 🚀"):
        if subjects:
            if model:
                with st.spinner("جاري تصميم خطتك الذكية..."):
                    prompt = f"طالب ثانوية عامة مصري يريد مذاكرة ({subjects}) ولديه ({hours}) ساعات. ضع له جدول زمني مقسم بالساعات يحوي فترات راحة قصيرة."
                    try:
                        response = model.generate_content(prompt)
                        st.success("تم إنشاء الخطة بنجاح!")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"⚠️ خطأ من سيرفرات جوجل: {e}")
            else:
                st.error("⚠️ لا يمكن الاتصال بالذكاء الاصطناعي حالياً.")
        else:
            st.error("يرجى كتابة المواد أولاً.")

with tab2:
    st.subheader("مدرسك الخصوصي 24/7")
    task_type = st.selectbox("كيف يمكنني مساعدتك؟", ["تلخيص درس", "شرح نقطة صعبة", "اقتراح أسئلة مراجعة"])
    user_query = st.text_area("اكتب طلبك هنا:")
    if st.button("إرسال للمساعد 💬"):
        if user_query:
            if model:
                with st.spinner("المساعد يفكر..."):
                    prompt = f"أنت مساعد دراسي لطلاب الثانوية في مصر. المستخدم يطلب ({task_type}) بخصوص: {user_query}. أجب بشكل مبسط ومباشر."
                    try:
                        response = model.generate_content(prompt)
                        st.info("الإجابة:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"⚠️ خطأ من سيرفرات جوجل: {e}")
            else:
                st.error("⚠️ لا يمكن الاتصال بالذكاء الاصطناعي حالياً.")
        else:
            st.error("يرجى كتابة طلبك أولاً.")

with tab3:
    st.subheader("لوحة التحكم الخاصة بك")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="ساعات الدراسة (هذا الأسبوع)", value="14 ساعة", delta="2+ ساعة")
    col2.metric(label="المهام المنجزة", value="24 مهمة", delta="5 مهام")
    col3.metric(label="أيام متتالية", value="7 أيام", delta="🔥")
    st.write("نسبة إنجاز المنهج الكلية:")
    st.progress(65)

with tab4:
    st.subheader("تقنية بومودورو للتركيز")
    st.write("جلسة تركيز 25 دقيقة بدون تشتت.")
    if st.button("ابدأ جلسة التركيز ⏱️"):
        timer_placeholder = st.empty()
        for i in range(25, 0, -1):
            timer_placeholder.markdown(f"<h1 style='text-align: center; color: #F97316;'>{i}:00</h1>", unsafe_allow_html=True)
            time.sleep(0.1) 
        st.success("انتهت الجلسة! خذ استراحة 5 دقائق.")

with tab5:
    st.subheader("جرعة التحفيز اليومية")
    exam_date = date(2026, 6, 20)
    today = date.today()
    days_left = (exam_date - today).days
    st.error(f"⏳ متبقي على امتحانات الثانوية العامة: {max(days_left, 0)} يوماً! استمر في القتال.")
    if st.button("أحتاج لدفعة أمل! ✨"):
        if model:
            with st.spinner("جاري جلب التحفيز..."):
                try:
                    response = model.generate_content("اكتب رسالة تحفيزية قصيرة جداً (سطرين) لطالب ثانوية عامة مصري لرفع معنوياته.")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"⚠️ خطأ من سيرفرات جوجل: {e}")
        else:
            st.error("⚠️ لا يمكن الاتصال بالذكاء الاصطناعي حالياً.")
