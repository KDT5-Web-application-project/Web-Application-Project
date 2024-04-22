'''
[ 데이터 전처리 관련 함수 ]
- 결측치, 중복 데이터
- 분류이기 때문에 클래스 균형 맞는지 확인 
- 텍스트 데이터 전처리 => 정제(불용어, 노이즈 제거), 토큰화, 2차 정제 => 단어사전 
- 텍스트 데이터 인코딩
- 텍스트 데이터 패딩
'''
import pandas as pd

# ====================================================================================
# 함수 이름 : check_na_dup_balance
# 힘수 목적 : 결측치 확인, 중복데이터 확인, 클래스 균형 확인 
# 반환 값 : 없음
# 파라 미터 : DataFrame 형식의 데이터, 비율 확인 하기 위한 컬럼명


def check_na_dup_balance(DATA, col):
    # 결측치 확인
    print(f"데이터의 결측치 확인")
    print(DATA.isnull().sum())

    # 중복 확인
    print(f"데이터의 중복 확인")
    print(DATA.duplicated().sum())

    # 데이터의 균형 확인을 위한 비율 확인
    print(f"{col}의 데이터 균형 확인")
    print(DATA[col].value_counts())



# ====================================================================================
# 함수 이름 : delete_noise_data
# 힘수 목적 : 노이즈 데이터 제거하기
# 반환 값 : feature_df
# 파라 미터 : FEATURE_DF, col (제거할 컬럼명), 정규식(default 존재)

import numpy as np
def delete_noise_data(FEATURE_DF, col, pattern = '[^ㄱ-ㅎ ㅏ-ㅣ 가-힣]'):
    print(f"제거 전: \n{FEATURE_DF[col][:5]}")
    print('-'*70)
    
    # 한글과 공백을 제외하고 모두 제거
    FEATURE_DF[col]= FEATURE_DF[col].str.replace(pattern, '', regex = True)
    print(f"pattern이외의 문자들 제거 후: \n{FEATURE_DF[col][:5]}")
    print('-' * 70)

    # 공백을 nan값으로 변경 후 제거
    FEATURE_DF[col]= FEATURE_DF[col].str.replace('^ +', '', regex = True)
    FEATURE_DF[col].replace('',np.nan, inplace = True)
    FEATURE_DF[col].dropna(inplace = True)
    print(f"공백 제거 후 : \n{FEATURE_DF[col][:5]}")

    return FEATURE_DF



# ====================================================================================
# 함수 이름 : make_voca_dict
# 힘수 목적 : 토큰화 된것을 바탕으로 각 토큰마다의 개수를 count해서 딕셔너리 형태로 저장
# 반환 값 : voca_dict
# 파라 미터 : 
# - token_model : 토큰 모델 인스턴스
# - FEATURE_DF : dataframe 형식의 피처
# - num : 토큰화 후 사용될 단어의 길이값 지정 (num 길이 이상의 단어만 사용하겠다)


def make_voca_dict(token_model, FEATURE_DF, num):
    voca_dict = {}

    for idx in range(FEATURE_DF.shape[0]):

        # 토큰 모델 인스턴스 통해 토큰화 진행
        result = token_model.morphs(FEATURE_DF.iloc[idx][0])   # 문자열만 쏙 뺴내기

        for word in result:
            if len(word) >= num : # 문자열이 2가 넘는 것만 추리겠다.
                if voca_dict.get(word): voca_dict[word] += 1
                else: voca_dict[word] = 1

    print('DONE')
    # get() 메서드는 딕셔너리에서 주어진 키(key)에 해당하는 값(value)을 반환 

    print('가장 많이 나온 단어를 내림차순으로 정렬해보자')
    print(sorted(voca_dict.items(), key = lambda a:a[1], reverse = True))

    return voca_dict



# ====================================================================================
# 함수 이름 : delete_stop_word
# 힘수 목적 : 불용어 제거 후 데이터프레임으로 반환
# 반환 값 : voca_DF, voca_dict
# 파라 미터 : 
# - stopword_datas : dataframe 형식으로 된 불용어
# - stop_col = stopword_df의 컬럼명

def delete_stop_word(stopword_datas, stop_col, voca_dict):
    list_stop = stopword_datas[stop_col].to_list()

    list_for_pop = []
    for k, v in voca_dict.items():
        if k in list_stop:
            list_for_pop.append(k)
    print(f"제거될 단어 개수 : {len(list_for_pop)}")

    print(f"제거 전 : {len(voca_dict.keys())}")
    for k in list_for_pop:
        voca_dict.pop(k)
    print(f"제거 후 : {len(voca_dict.keys())}")

    voca_DF = pd.Series(voca_dict).to_frame()
    print('voca_dict를 데이터프레임으로 변경 완료')
    return voca_DF, voca_dict



# ====================================================================================
# 함수 이름 : make_total_voca_dict
# 힘수 목적 : 최종적으로 사용한 데이터셋용 단어 사전 만들기
# 반환 값 : total_voca_dict
# 파라 미터 : voca_DF(불용어 제거된 voca dataframe)

def make_total_voca_dict(voca_DF):
    total_voca_dict = {0 : '<UNK>', 1 : '<PAD>'}

    for idx in range(len(voca_DF)):
        total_voca_dict[idx+2] = voca_DF.index[idx]
    print(total_voca_dict)

    return total_voca_dict



# ====================================================================================
# 함수 이름 : do_encoding
# 힘수 목적 : 문장 → 수치화
# 반환 값 : sentence
# 파라 미터 : test, total_voca_dict

def do_encoding(test, total_voca_dict):
    encoding = []
    sentence = []

    for tt in test:
        sentence.append(0) # 0 은 <UNK>에 해당함
        for k, v in total_voca_dict.items():
            if v == tt:
                sentence[-1] = k
                break # 하나만 맞추면 되니까 굳이 더 돌 필요 X
    
    return sentence



# ====================================================================================
# 함수 이름 : do_decoding
# 힘수 목적 : 수치값 → 문자열
# 반환 값 : words
# 파라 미터 : test, total_voca_dict

def do_decoding(sentence, total_voca_dict):
    decoding = []
    words = []

    for tt in sentence:
        words.append(vocab_dict.get(tt))
        
    print(words)
    
    return words