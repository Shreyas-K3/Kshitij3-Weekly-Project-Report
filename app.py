import streamlit as st

email_content = """
**Team,**

Below is this week’s status update for **Project Atlas Copco**.  
Progress remains steady and we are tracking toward the upcoming milestone.

---

### 🔗 **Quick Links**
- 📊 **Viewer Link:** [Link](YOUR_VIEWER_URL)
- ❓ **RFI Sheet:** [Link](YOUR_RFI_SHEET_URL)

**✅ Project Status:** **83% Completed**

---

### 📝 **Note**
- 6 non-imp RFIs pending  
- Requesting your prompt responses on the above RFI sheet to keep workflows on schedule  
- Please review the model link and share comments if any  

---

### 📈 **Current Progress**
- PHE and ELEC models completed with clashes addressed; minor clashes resolved (screenshots attached)  
- FF and MECH models completed **80%+**

---

### 🗓 **Next Steps (4-Day Plan)**
- Complete FF and MECH  
- Start coordination  

---

Feedback and inputs are welcome.  
For any clarifications or additional details, feel free to reach out.
"""

st.markdown(email_content)
