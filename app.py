import streamlit as st
from extractor import extract_claims
from verifier import verify_claim
from analyzer import classify_root_cause
from scorer import calculate_score

st.set_page_config(page_title="HalluciScope", layout="wide")

st.title("🔬 HalluciScope")
st.markdown("### *LLM Hallucination Autopsy Tool*")

# Two-column layout for inputs
col_input, col_output = st.columns(2)
with col_input:
    context = st.text_area("📄 Ground Truth (Source Context)", height=200)
with col_output:
    model_output = st.text_area("🤖 AI Response (To Audit)", height=200)

if st.button("🚀 Run Full Diagnostic", use_container_width=True):
    if not context or not model_output:
        st.warning("Please provide both context and output.")
    else:
        with st.spinner("Analyzing claims..."):
            claims = extract_claims(model_output)
            data_points = []
            
            for c in claims:
                v, r, conf = verify_claim(c, context)
                cause = classify_root_cause(c, v, r)
                data_points.append({"text": c, "verdict": v, "reason": r, "conf": conf, "cause": cause})
            
            score = calculate_score(data_points)
            
            # --- Metrics ---
            m1, m2 = st.columns(2)
            m1.metric("Hallucination Score", f"{score * 100}%")
            
            unique_causes = list(set(d['cause'] for d in data_points if d['cause']))
            m2.warning(f"Root Causes: {', '.join(unique_causes)}") if unique_causes else m2.success("No Hallucinations Found")

            # --- Results ---
            st.divider()
            for d in data_points:
                is_false = d['verdict'] == "false"
                icon = "❌" if is_false else "✅"
                with st.expander(f"{icon} Claim: {d['text'][:80]}..."):
                    st.write(f"**Reasoning:** {d['reason']}")
                    st.progress(d['conf'], text=f"Confidence: {int(d['conf']*100)}%")