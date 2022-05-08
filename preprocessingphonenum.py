import numpy as np
import pandas as pd


phonedf=pd.DataFrame(columns=['phone'])
phonedf.loc[1]='010-1234-일이35'
phonedf.loc[2]='공일공-일이삼사-1235'
phonedf.loc[3]='010.하나234.일이삼오'
phonedf.loc[4]='공1공-1둘삼넷.1이3오'
def get_preprocess_phone(phone):
    mapping_dict={
        '영':'0','하나':'1',
        '일':'1','둘':'2',
        '이':'2','셋':'3',
        '삼':'3','넷':'4',
        '사':'4','다섯':'5',
        '오':'5','여섯':'6',
        '육':'6','일곱':'7',
        '칙':'7','여덟':'8',
        '팔':'8','아홉':'9',
        '구':'9','공':'0',
        '-':'','.':'',
    }
    for key,value in mapping_dict.items():
        phone=phone.replace(key,value)
    return phone
phonedf['num_phone']=phonedf['phone'].apply(get_preprocess_phone)