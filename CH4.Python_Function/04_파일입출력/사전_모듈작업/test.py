# ek_dic={'dog':'강아지','cat':'고양이','note':'공책'}
#
# "dog,cat,note,-강아지,고양이,공책,"
# #키와 값을 따로 저장
# d_key=ek_dic.keys() #리스트로 키만 저장
# d_value=ek_dic.values() #리스트 값만 저장
# print(d_key)
# print(d_value)
#
# result=''
# for k in d_key:
#     result += k+','
# print(result)
#
# result+= '-'
# print(result)
#
# for v in d_value:
#     result+= v+','
# print(result)

#사전파일에서 data읽어오는 로직 설명
results=['dog,cat,-강아지,고양이,']
if results==[]: #파일에 데이터가 없어서 읽어온 것이 없을 때
    pass
res=results[0].split('-')
print(res)
d_keys=res[0].split(',')
print(d_keys) #결과값 ['dog', 'cat', ''] 마지막 의미없는 빈문자열 생성
#최종사용(마지막줄 제외 추출)
d_keys=res[0].split(',')[:-1]
print(d_keys)

d_values=res[1].split(',')[:-1]
print(d_values)
#zip함수 이용해서 딕셔너리 생성
print(list(zip(d_keys,d_values)))
dict_temp=dict(zip(d_keys,d_values))
print(dict_temp)

#dict_temp를 ek_dic 공용변수에 저장해야함
#일반 대입 연산자를 사용하면 지역변수가 생성됨
#부분 대입을 이용
ek_dic={}
for item in dict_temp.items():
    print(item)
    k,v=item
    ek_dic[k]=v
print(ek_dic)