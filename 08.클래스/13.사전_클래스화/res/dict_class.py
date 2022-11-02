# dict_class.py
# 속성(생성자 함수에서 구성) ek_dic
# 사전을 저장하기위한 파일명 file_name

# 메서드
# 검색을 위한 메서드 : search(self) dict_search(self,eng)
# 구성을 위한 메서드 : const_dict(self), input_dict(self,eng)
# 저장 및 로딩을 위한 메서드 : save_dict(self), load_dict(self)

class Dict_const:
    # 생성자 함수 - 객체 인스턴스 생성시 사전을 저장하거나 불러올 파일명을 인수로 받음
    def __init__(self,file_name):
        self.file_name=file_name # 저장을 위한 파일명
        self.ek_dic={} #사전구성 dict

    def const_dict(self):
        while True:
            # 영어단어 입력받기
            eng = input("\n영어 단어 입력 (종료는 'q') : ")
            # 종료검사
            if eng == 'q':
                print('단어 등록을 종료합니다.')
                break  # 반복종료 (반복 외에 함수에 다른 문장없으므로 함수 종료)
            elif eng not in self.ek_dic:  # 등록되지 않은 단어
                self.input_dict(eng)
            else:
                print("%s는 이미 등록된 단어 입니다." % eng)

    def input_dict(self,eng):
        # 단어에 해당하는 뜻 입력
        kor = input(eng + "뜻 입력 : ")
        self.ek_dic[eng] = kor

    def dict_search(self,eng):  # 단어가 사전에 있는 경우 호출
        print("%s의 뜻은 %s입니다. " % (eng, self.ek_dic[eng]))

    # 2. 단어 하나를 검색하는 함수
    # 단어 하나를 입력받아 입력 단어가 사전에 있으면 dict_search(eng)를 호출해서 뜻을 출력
    # 입력 단어가 사전에 없으면 사전에 등록할 것인지 여부 확인
    # 등록하겠다고 하면 input_dict(eng) 호출, 사전에 단어를 등록
    def search(self):
        # 검색단어부터 입력받기
        eng = input("\n 검색할 단어 입력 : ")
        if eng in self.ek_dic:  # 사전에 있는 단어라면
            self.dict_search(eng)
        else:  # 사전에 없는 단어라면
            print("%s는 사전에 없는 단어 입니다." % eng)
            answer = input('사전에 등록 하시겠습니까?(Y/N)')
            if answer == 'Y':
                self.input_dict(eng)
                print("사전 등록완료! 감사합니다!")
        print("검색을 종료합니다.")

    # 사전 읽어오기 저장하기 기능
    def load_dict(self):
        # 사전 파일은 초기에 빈파일을 하나 생성해 놓고 시작
        # 읽어오기
        # 저장을 한행에 한문장으로 저장하기 떄문에 리스트는 비어있거나 요소가 1개가 있음
        f = open('./res/'+self.file_name+'.txt', 'r', encoding='utf-8')
        results = f.readlines()
        # print(results)
        f.close()
        if results == []:
            return 0

        # 키와 값 나누기
        res = results[0].split('-')
        d_keys = res[0].split(',')[:-1]
        d_values = res[1].split(',')[:-1]
        dict_temp = dict(zip(d_keys, d_values))
        # print(dict_temp)
        # ek_dic=dict_temp 지역변수로 지정되버림 전역변수로 지정해야함
        # ek_dic가 딕셔너리 이므로 아이템을 추가하는 방식으로 부분변경
        # 공용변수에 dict_temp의 items들을 저장
        for item in list(dict_temp.items()):
            k, v = item
            self.ek_dic[k] = v

        print("사전 준비 완료!!!!")

    def save_dict(self):
        # 사전을 파일로 저장하는 함수
        result = ''
        f = open('./res/'+self.file_name+'.txt', 'w', encoding='utf-8')
        # ek_dic의 키 - value 형태의 문자열 구성
        d_key = self.ek_dic.keys()  # 키만 추출
        d_value = self.ek_dic.values()  # 값만 추출
        # key를 문자열로 저장
        for k in d_key:
            result += k + ','
        # value와 구분자 추가
        result += '-'
        for v in d_value:
            result += v + ','
        # 파일에 쓰기
        f.write(result)
        f.close()
        print("사전 저장 완료!!!!")
        # 저장하기
