import streamlit as st

# -------------------------------
# Reference Ranges for Lab Values
# -------------------------------
reference_ranges = {
    "Hemoglobin": {"min": 12, "max": 16, "unit": "g/dL", 
                   "explain_low": "May indicate anemia (low blood count).",
                   "explain_high": "Could suggest dehydration or other conditions."},
    
    "Bilirubin": {"min": 0.1, "max": 1.2, "unit": "mg/dL",
                  "explain_low": "Usually not a concern.",
                  "explain_high": "May indicate liver stress or jaundice."},
    
    "Glucose": {"min": 70, "max": 100, "unit": "mg/dL",
                "explain_low": "May indicate hypoglycemia (low blood sugar).",
                "explain_high": "Possible diabetes or impaired sugar control."},
    
    "Protein (Urine)": {"min": 0, "max": 0.1, "unit": "g/L",
                        "explain_low": "Normal finding.",
                        "explain_high": "Could suggest kidney issue."}
}

# -------------------------------
# Function to check values
# -------------------------------
def check_value(test_name, value):
    ref = reference_ranges[test_name]
    if value < ref["min"]:
        return f"❌ {test_name}: LOW ({value} {ref['unit']}). {ref['explain_low']}"
    elif value > ref["max"]:
        return f"❌ {test_name}: HIGH ({value} {ref['unit']}). {ref['explain_high']}"
    else:
        return f"✅ {test_name}: NORMAL ({value} {ref['unit']})."

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🩺 Health Report Assistant")
st.markdown("Upload or enter your blood/urine test values to get a simple explanation.")

# Inputs
hemoglobin = st.number_input("Hemoglobin (g/dL)", 0.0, 30.0, 13.5)
bilirubin = st.number_input("Bilirubin (mg/dL)", 0.0, 10.0, 0.8)
glucose = st.number_input("Glucose (mg/dL)", 0.0, 300.0, 90.0)
protein = st.number_input("Protein (Urine) (g/L)", 0.0, 10.0, 0.0)

if st.button("Analyze Report"):
    st.subheader("📋 Results:")
    st.write(check_value("Hemoglobin", hemoglobin))
    st.write(check_value("Bilirubin", bilirubin))
    st.write(check_value("Glucose", glucose))
    st.write(check_value("Protein (Urine)", protein))

    st.markdown("---")
    st.success("⚠️ Disclaimer: This is a demo app for hackathon purposes. Always consult a doctor for medical advice.")
