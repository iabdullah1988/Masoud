"""
اختبار وكيل مسعود
Masoud Agent Test
"""

from ai-agent.core import MasoudComplianceAgent

# إنشاء الوكيل
agent = MasoudComplianceAgent()

# عرض ملخص اللوائح
print("\n" + "="*50)
print("ملخص اللوائح المتاحة:")
print("="*50)

summary = agent.get_regulation_summary()
for authority, info in summary.items():
    print(f"\n📌 {authority}:")
    print(f"   {info['title']}")
    print(f"   عدد الأحرف: {info['length']}")

print("\n" + "="*50)
print("✅ وكيل مسعود جاهز للعمل!")
print("="*50)
