import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Project Atlas Copco - Status Update",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        border-radius: 10px;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .progress-text {
        font-size: 3rem;
        font-weight: bold;
        margin: 0;
    }
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
    }
    .link-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        transition: transform 0.2s;
    }
    .link-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    .info-box {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .timeline-item {
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 3px solid #667eea;
        padding-left: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚀 Project Atlas Copco")
    st.subheader("Weekly Status Update")
with col2:
    st.metric("Week", f"{datetime.now().strftime('%W')}", "Current")

st.markdown("---")

# Status Overview
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="metric-card">
            <p style="margin:0; font-size:1.2rem;">Project Completion</p>
            <p class="progress-text">83%</p>
            <p style="margin:0;">✅ On Track</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <p style="margin:0; font-size:1.2rem;">Pending RFIs</p>
            <p class="progress-text">6</p>
            <p style="margin:0;">⚠️ Non-Critical</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <p style="margin:0; font-size:1.2rem;">Timeline</p>
            <p class="progress-text">4</p>
            <p style="margin:0;">📅 Days Plan</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Quick Links Section
st.markdown('<p class="section-header">🔗 Quick Access Links</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <a href="https://autode.sk/4rgD3cG" target="_blank" class="link-button">
            📊 Open Viewer Link
        </a>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <a href="https://docs.google.com/spreadsheets/d/1RDRCvOWoVXIMcnYJCmDs8JvboJvep7j-/edit?usp=drive_link&ouid=101341274280914933041&rtpof=true&sd=true" target="_blank" class="link-button">
            ❓ RFI Response Sheet
        </a>
    """, unsafe_allow_html=True)

# Important Notes
st.markdown('<p class="section-header">📝 Important Notes</p>', unsafe_allow_html=True)
st.info("""
**Action Required:**
- ⏰ **6 non-critical RFIs** are awaiting responses
- 🔍 Please review the model viewer and provide feedback
- ✍️ Update the RFI sheet to maintain project momentum
""")

# Current Progress Section
st.markdown('<p class="section-header">📈 Current Progress Breakdown</p>', unsafe_allow_html=True)

progress_col1, progress_col2 = st.columns(2)

with progress_col1:
    st.markdown("### Completed Models")
    st.success("**PHE Model** ✅ 100% Complete")
    st.progress(1.0)
    
    st.success("**ELEC Model** ✅ 100% Complete")
    st.progress(1.0)
    
    st.markdown("<small>🔧 Minor clashes resolved (screenshots attached)</small>", unsafe_allow_html=True)

with progress_col2:
    st.markdown("### In Progress Models")
    st.warning("**FF Model** 🔄 80%+ Complete")
    st.progress(0.8)
    
    st.warning("**MECH Model** 🔄 80%+ Complete")
    st.progress(0.8)

# Next Steps Timeline
st.markdown('<p class="section-header">🗓 Next Steps - 4-Day Plan</p>', unsafe_allow_html=True)

timeline_col1, timeline_col2 = st.columns([1, 3])

with timeline_col2:
    st.markdown("""
        <div class="timeline-item">
            <strong>Days 1-2:</strong> Complete FF and MECH models<br>
            <small style="color: #666;">Target: 100% completion of remaining models</small>
        </div>
        <div class="timeline-item">
            <strong>Days 3-4:</strong> Initiate coordination phase<br>
            <small style="color: #666;">Begin cross-discipline integration</small>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div class="info-box">
        <strong>💬 Feedback Welcome</strong><br>
        For clarifications, additional details, or any questions, please reach out to the project team.
    </div>
""", unsafe_allow_html=True)

# Expandable details section
with st.expander("📎 View Full Email Content"):
    st.markdown("""
    **Team,**
    
    Below is this week's status update for **Project Atlas Copco**.  
    Progress remains steady and we are tracking toward the upcoming milestone.
    
    All metrics and links are provided above in the dashboard format for easy access and tracking.
    """)

# Add a download button for the status report
if st.button("📥 Export Status Report", type="primary"):
    st.balloons()
    st.success("Status report exported successfully! (Demo feature)")
