import json

# Input Data
shap_values = {
    "ApplicantIncome": {"SHAP Value": -0.086386, "Feature Value": 39147},
    "CoapplicantIncome": {"SHAP Value": -0.259243, "Feature Value": 4750.0},
    "LoanAmount": {"SHAP Value": 0.321459, "Feature Value": 120.0},
    "Loan_Amount_Term": {"SHAP Value": 0.018896, "Feature Value": 360.0},
    "Credit_History": {"SHAP Value": 0.444260, "Feature Value": 1.0},
    "Gender": {"SHAP Value": 0.011829, "Feature Value": "Male"},
    "Married": {"SHAP Value": 0.121175, "Feature Value": "Yes"},
    "Dependents": {"SHAP Value": 0.000000, "Feature Value": 0},
    "Education": {"SHAP Value": 0.003957, "Feature Value": "Graduate"},
    "Self_Employed": {"SHAP Value": 0.003099, "Feature Value": "Yes"},
    "Property_Area": {"SHAP Value": 0.202747, "Feature Value": "Semiurban"}
}


ApplicantIncome = shap_values["ApplicantIncome"]["Feature Value"]
CoapplicantIncome = shap_values["CoapplicantIncome"]["Feature Value"]
LoanAmount = shap_values["LoanAmount"]["Feature Value"]
Loan_Amount_Term = shap_values["Loan_Amount_Term"]["Feature Value"]
Credit_History = shap_values["Credit_History"]["Feature Value"]

ApplicantIncome_SHAP = shap_values["ApplicantIncome"]["SHAP Value"]
LoanAmount_SHAP = shap_values["LoanAmount"]["SHAP Value"]
Loan_Amount_Term_SHAP = shap_values["Loan_Amount_Term"]["SHAP Value"]


# Calculate KPIs
Debt_to_Income_Ratio = LoanAmount / (ApplicantIncome + CoapplicantIncome)
EMI_to_Income_Ratio = (LoanAmount / Loan_Amount_Term) / (ApplicantIncome + CoapplicantIncome)

# Creditworthiness Score (adjust weights as needed)
Creditworthiness_Score = (Credit_History * 0.7) + (ApplicantIncome_SHAP * 0.1) + (LoanAmount_SHAP * 0.1) + (Loan_Amount_Term_SHAP * 0.1)

# Loan Burden Score
Loan_Burden_Score = (LoanAmount_SHAP * 0.5) + (Loan_Amount_Term_SHAP * 0.5)

# SHAP Insights
SHAP_Insights = "Credit History, Property Area, and Loan Amount positively influence the decision. Applicant and Coapplicant Income have a negative influence."

# Create JSON response
kpis = {
    "Debt_to_Income_Ratio": Debt_to_Income_Ratio,
    "EMI_to_Income_Ratio": EMI_to_Income_Ratio,
    "Creditworthiness_Score": Creditworthiness_Score,
    "Loan_Burden_Score": Loan_Burden_Score,
    "SHAP_Insights": SHAP_Insights
}

print(json.dumps(kpis))