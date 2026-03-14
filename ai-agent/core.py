"""
مسعود - وكيل الحوكمة والامتثال الذكي
Masoud AI Governance Agent
"""

import os
from typing import List, Dict, Any

class MasoudComplianceAgent:
    """
    الوكيل الرئيسي لتحليل الامتثال للأنظمة السعودية
    """
    
    def __init__(self, regulations_path: str = "regulations"):
        self.name = "مسعود"
        self.regulations_path = regulations_path
        self.regulations = {}
        self.supported_authorities = [
            "CMA", "SAMA", "NCA", "SDAIA", "DGA", "ZATCA", "MC"
        ]
        print(f"✅ وكيل {self.name} جاهز للعمل")
        self._load_all_regulations()
    
    def _load_all_regulations(self):
        """
        تحميل جميع اللوائح من مجلد regulations
        """
        print("📥 جاري تحميل جميع اللوائح...")
        
        # التأكد من وجود المجلد
        if not os.path.exists(self.regulations_path):
            print(f"⚠️ مجلد {self.regulations_path} غير موجود")
            return
        
        # قراءة جميع ملفات .txt في المجلد
        for filename in os.listdir(self.regulations_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.regulations_path, filename)
                authority = filename.replace("_governance.txt", "").upper()
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.regulations[authority] = content
                        print(f"   ✅ تم تحميل {authority}")
                except Exception as e:
                    print(f"   ❌ خطأ في تحميل {authority}: {e}")
        
        print(f"✅ تم تحميل {len(self.regulations)} لائحة")
    
    def get_regulation_summary(self, authority: str = None) -> Dict:
        """
        عرض ملخص اللوائح المتاحة
        """
        if authority:
            if authority in self.regulations:
                content = self.regulations[authority]
                lines = content.strip().split('\n')
                return {
                    "authority": authority,
                    "title": lines[0] if lines else "",
                    "length": len(content),
                    "preview": "\n".join(lines[1:5])  # أول 5 أسطر بعد العنوان
                }
            else:
                return {"error": f"اللائحة {authority} غير موجودة"}
        
        # ملخص كل اللوائح
        summary = {}
        for auth, content in self.regulations.items():
            lines = content.strip().split('\n')
            summary[auth] = {
                "title": lines[0] if lines else "",
                "length": len(content)
            }
        return summary
    
    def analyze_document(self, document_path: str, authorities: List[str] = None):
        """
        تحليل مستند ومقارنته بلوائح الجهات المحددة
        """
        if authorities is None:
            authorities = list(self.regulations.keys())
        
        print(f"🔍 تحليل المستند {document_path}...")
        print(f"📋 الجهات المطلوبة: {', '.join(authorities)}")
        
        # هنا راح نضيف لاحقاً منطق التحليل الفعلي
        gaps = self._find_gaps(document_path, authorities)
        
        return self._generate_report(gaps, authorities)
    
    def _find_gaps(self, document: str, authorities: List[str]) -> List[Dict]:
        """
        (دالة داخلية) اكتشاف الفجوات في المستند
        """
        # مؤقتاً نرجع قائمة فارغة
        return []
    
    def _generate_report(self, gaps: List[Dict], authorities: List[str]) -> Dict:
        """
        (دالة داخلية) إنشاء تقرير الفجوات
        """
        report = {
            "agent": self.name,
            "authorities_analyzed": authorities,
            "summary": "تم التحليل بنجاح",
            "gaps_count": len(gaps),
            "recommendations": []
        }
        return report

# اختبار سريع
if __name__ == "__main__":
    agent = MasoudComplianceAgent()
    print("\n📋 ملخص اللوائح:")
    summary = agent.get_regulation_summary()
    for auth, info in summary.items():
        print(f"   - {auth}: {info['title']}")
