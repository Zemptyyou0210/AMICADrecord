import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from datetime import datetime

初始化Firebase
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def main():
    st.title("患者問卷系統")
    
    # 選擇操作
    operation = st.sidebar.selectbox("選擇操作", ["新增患者", "查看/編輯患者資料"])
    
    if operation == "新增患者":
        add_new_patient()
    else:
        view_edit_patient()

def add_new_patient():
    st.subheader("新增患者資料")
    
    # 基本資料
    name = st.text_input("姓名")
    patient_id = st.text_input("病歷號")
    gender = st.selectbox("性別", ["男", "女"])
    bed_number = st.text_input("床號")
    birth_date = st.date_input("出生年月日")
    doctor = st.selectbox("主治醫師", ["王宇澄", "黃國書", "張育晟", "王志偉", "潘泓智", "許楹奇", "施榮彰", "吳宏彬", "莊傑貿", "朱永譁", "陳彥旭"])
    admission_date = st.date_input("住院日")
    pharmacist = st.selectbox("評估藥師", ["簡妙格", "廖文佑", "洪英哲"])
    assessment_date = st.date_input("評估日期")
    
    # 病史和其他資料
    history = st.text_area("過去病史")
    surgery_record = st.text_area("手術記錄")
    chief_complaint = st.text_area("本次入院經過")
    allergies = st.text_area("過敏史")
    current_medication = st.text_area("目前用藥")
    smoking = st.selectbox("吸菸", ["是", "否"])
    alcohol = st.selectbox("飲酒", ["是", "否"])
    drug_abuse = st.selectbox("藥物濫用", ["是", "否"])
    
    # Lab data
    st.subheader("Lab Data")
    renal_function = st.text_input("腎功能")
    blood_lipids = st.text_input("血脂")
    hba1c = st.text_input("HbA1c")
    other_lab_data = st.text_area("其他lab data")
    
    # 其他評估
    polypharmacy = st.text_area("多重用藥整合")
    chinese_medicine = st.selectbox("是否使用中成藥、保健食品、營養品", ["是", "否"])
    medication_adherence = st.text_area("服藥順從性評估")
    
    # 問卷
    st.subheader("衛教類別")
    education_type = st.multiselect("選擇衛教類別", ["整體用藥注意事項", "抗凝血劑用藥指導", "其他特定藥品用藥指導"])
    
    st.subheader("用藥知識評估暨衛教內容(衛教前)")
    pre_education_assessment = {}
    for question in get_education_questions():
        pre_education_assessment[question] = st.selectbox(f"衛教前: {question}", ["是", "否"])
    
    if st.button("提交患者資料"):
        # 將資料保存到Firebase
        # 這裡需要實現保存邏輯
        st.success("患者資料已成功保存")

def view_edit_patient():
    # 實現查看/編輯患者資料的邏輯
    pass

def get_education_questions():
    return [
        "是否知道所用藥品之用途",
        "是否知道正確服藥方法及用量",
        "是否知道忘記服藥如何處理",
        "是否知道藥品保存方式",
        "是否知道遵醫囑服藥之重要性",
        "是否知道藥品可能與其他食物、藥品有交互作用",
        "是否知道所使用之藥品常見副作用",
        "是否知道副作用發生時之處理方式",
        "是否知道發生藥品相關問題詢問的管道",
        "是否知道如何使用衛教單張"
    ]

def get_patients():
    # 從Firebase獲取患者列表
    # 這裡需要根據您的Firebase結構進行調整
    return ["患者1", "患者2", "患者3"]

def get_previous_answers(patient):
    # 從Firebase獲取患者的前次問卷答案
    # 這裡需要根據您的Firebase結構進行調整
    return {"問題1": "答案1", "問題2": "答案2"}

def get_lab_data(patient):
    # 從Firebase獲取患者的lab data
    # 這裡需要根據您的Firebase結構進行調整
    return pd.DataFrame({"檢測項目": ["項目1", "項目2"], "結果": ["結果1", "結果2"]})

def new_questionnaire():
    # 創建新的問卷
    # 這裡需要根據您的具體需求添加問題
    question1 = st.text_input("問題1")
    question2 = st.text_input("問題2")
    
    if st.button("提交"):
        # 將新的問卷答案保存到Firebase
        # 這裡需要根據您的Firebase結構進行調整
        st.success("問卷已提交")

if __name__ == "__main__":
    main()
