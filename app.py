import streamlit as st
import os
import sys

# إضافة مسار المجلدات
sys.path.append(os.path.dirname(__file__))
from ai_agent.core import MasoudComplianceAgent

# إعداد الصفحة
st.set_page_config(
    page_title="مسعود - حوكمة ذكية",
    page_icon="🤖",
    layout="wide"
)

# عنوان رئيسي
st.title("🤖 مسعود - المستشار الذكي للحوكمة والامتثال")
st.markdown("---")

# تحميل الوكيل
@st.cache_resource
def load_agent():
    return MasoudComplianceAgent()

agent = load_agent()

# عرض الجهات المتاحة
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📋 الجهات الرقابية")
    authorities = list(agent.regulations.keys())
    selected = st.multiselect(
        "اختر الجهات للتحليل",
        authorities,
        default=authorities[:3] if authorities else []
    )
    
    st.markdown("---")
    st.subheader("📄 رفع المستند")
    uploaded_file = st.file_uploader(
        "اختر ملف سياسات الشركة",
        type=['txt', 'pdf', 'docx']
    )

with col2:
    st.subheader("🔍 نتائج التحليل")
    
    if uploaded_file is not None:
        # حفظ الملف مؤقتاً
        with open("temp_doc.txt", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with st.spinner("جاري تحليل المستند..."):
            result = agent.analyze_document("temp_doc.txt", selected if selected else None)
            
        st.success("✅ تم التحليل بنجاح")
        st.json(result)
    else:
        st.info("👈 الرجاء رفع ملف مستند الشركة لبدء التحليل")
        
        st.markdown("### 📚 اللوائح المتاحة:")
        summary = agent.get_regulation_summary()
        if summary:
            for auth, info in summary.items():
                with st.expander(f"**{auth}** - {info.get('title', '')}"):
                    st.text(info.get('preview', 'لا يوجد معاينة'))
        else:
            st.warning("لا توجد لوائح محملة حالياً")
