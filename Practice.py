# Jump to Python 4-2

'''#011
price_list=[100,200,300]
for i in price_list:
    final_price=i+10
    print(final_price)
 '''
'''
#012
food_list=["김밥","라면","튀김"]
for i in food_list:
    print(f"오늘의 메뉴:{i}")
    '''
'''
#013
stock_list=["Sk하이닉스","삼성전자","LG전자"]
for i in stock_list:
    spells=len(i)
    print(spells)
  '''
'''
#015
animal_list=['dog','cat','parrot']
for name in animal_list:
    print(name[0])
    '''
'''
#021
num_list=[3,-20,-3,44]
for i in num_list:
    if int(i)<0:
        print(int(i))
    else:
        continue
'''
'''
#023
num_list=[13,21,12,14,30,18]
for number in num_list:
    if number%3==0 and number<20:
        print(number)
    else:
        continue
'''
'''
#025
alpha_list=['A','b','c','D']
for strings in alpha_list:
    if strings.isupper()==True:
        print(strings)
    else:
        continue
'''
'''
#027
anim_list=['dog','cat','parrot']
for kind in anim_list:
    print(kind.capitalize())
 '''
'''
#028
file_list=["hello.py","ex01.py","intro.hwp"]
for filename in file_list:
    print(filename.split('.')[0])
'''
'''
#029
file_list=['intra.h','intra.c','define.h','run.py']
for filename in file_list:
    splitted=filename.split('.')
    #print(splitted)
    if splitted[1]=="h":
        print(filename)
    else:
        continue
'''
'''
#045
my_list=["가","나","다","라"]
for i in range(3):
    print(my_list[i],my_list[i+1])
   '''
'''
#046
my_list=["가","나","다","라","마"]
for i in range(3):
    print(my_list[i],my_list[i+1],my_list[i+2])
  '''

'''
number=int(input("Type number, please:\n"))
count=0
while i < number:
    print('',number)
    count+=1

'''
'''
number=int(input("Type number, please:\n"))
count=1
while count<=number:
    print(count,count**2)
    count+=1
'''
'''
height=100
count=1
while count<=10:
    height=height*(3/5)
    print(count, round(height, 4))
    count+=1

'''
'''
#input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요.
# 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.
num=int(input("1~3 중 하나의 정수를 입력하세요:"))
if num==1:
    print("일")
elif num==2:
    print('이')
elif num==3:
    print('삼')

'''

'''
#백만 이상의 숫자를 입력받았을 때 1~10만자리 숫자를 생략하고 ‘M’을 붙여서 출력하게 코드를 수정해보세요.

num=int(input("입력:"))
if num>=1000000:
    million_num=num//1000000
    print(f"{million_num}M")
elif num>=0:
    pass

'''

'''
#input()으로 사용자로부터 입력받은 정수를 계속 더해나가다가,
#음수가 입력되면 중단하고 그 전까지 계산한 값을 출력하는 파이썬 스크립트를 작성하세요.

num=0
while True:
    num_input = int(input("양의 정수를 입력하세요:"))
    if num_input>=0:
        num+=+num_input
    elif num_input<0:
        print(num)
        break
        
'''

'''
# 2.1.1 연습 문제와 같이, 사용자로부터 input()으로 정수를 한 개 입력받아,
# 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요.
# 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, 이번에는 for 문을 사용하세요.

num_input=int(input("숫자를 하나 입력하세요:"))
for number in range(num_input):
    print('',num_input)
    
'''

'''
#1~N까지 합 중에서 100 넘는 순간에 N 값을 출력해라

sum=0
for i in range(1,101):
    sum=sum+i
    if sum>100:
        print(i)
        break
 '''

'''
groups={
    "빅뱅":['GD','태양','탑','대성','승리'],
    "마마무":["문별","솔라","휘인","화사"]
}
for group, members in groups.items():
    print(f"{group}의 멤버")
    for member in members:
        if member != '승리':   # member='승리' 면 출력 안되고, 아니면 출력하라는 것 - 결과적으로는 승리 뺴고 출력하는 것임
            print(member)
'''
'''
# 연습 문제 2.2와 같이, 정수를 한 개 입력받아 1부터 입력받은 수까지
# 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, 이번에는 for 문을 사용하세요.
num=int(input("숫자 하나를 입력하세요:"))
for i in range(1,num+1):
    print(i,i**2)

'''
'''
# 15초마다 온도를 측정해 프로그램에 제공
# 최소와 최대 안전온도를 나타내는 정수 두 개를 읽는다.
# 반응이 완료되면 -999를 출력
# 온도가 올바른 범위에 있을 경우 "Nothing to report" 출력
# 온도가 위험 수준에 도달하면 "Alert!"를 출력하고 온도 측정을 중단한다.

import random
freezing_point, boiling_point = input("온도의 범위를 입력하세요(2개):").split()

while True:
    temperature = int(input())
    if temperature > int(boiling_point) or temperature < int(freezing_point) and temperature != -999:
        print("Alert!")
        break
    elif int(freezing_point) <= temperature <= int(boiling_point):
        print("Nothing to report")
        continue
    elif temperature == -999:
        print("프로그램 종료")
        break
'''

'''
# 입력받은 정수에 해당하는 한글 문자열을 반환하는 함수
# korean_number()를 if 문을 사용하지 말고 작성하세요 0~9

def korean_number(n):
    number={0:'영',
        1:'일',
               2:'이',
               3:'삼',
               4:'사',
               5:'오',
               6:'육',
               7:'칠',
               8:'팔',
               9:'구'}
    return number[n]

print(korean_number(3))
'''
"""
txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

txt_split_list=txt.splitlines()     #  txt를 한 줄 씩 나눠서 리스트에 저장
print(txt_split_list)
dic = {}            # 빈 dictionary
for sentence in txt_split_list:     #  나눠진 txt 리스트 한 요소씩 sentence에 할당
    for idx in range(len(sentence)):    #  sentence의 길이 범위의 index 숫자를 idx에 할당
        char = sentence[idx]            #  char은 sentence의 한 문자 한 문자
        if chr(65)<= char <= chr(90) or chr(97) <= char <= chr(122):  # 만약 한 문자 한 문자인 char이 A~Z, a~z 사이의 값을 가지면
            dic[sentence[:(idx-1)]] = sentence[idx:]    # dictionary의 키값은 영어 이전, 밸류는 영어 이후
            break

print(dic)

"""
#  https://wikidocs.net/162243
'''
rule_dic={'111':'0',
          '110':'1',
          '101':'0',
          '100':'1',
          '011':'1',
          '010':'0',
          '001':'1',
          '000':'0'}

first_list=[0]
second_list=first_list*61
second_list[30]=1
base_list=second_list           #  기본 리스트 생성

def fractal(n1,n2=0):


print(rule_dic.keys())

for idx in range(len(base_list)):       #  리스트 길이 61까지 index를 idx에 할당
    former_idx=idx-1                    #  idx 앞
    later_idx=idx+1                     #  idx 뒤
    if str(f"{former_idx}{idx}{later_idx}")==rule_dic.keys():   #  만약 idx앞뒤가 rule_dic의 키값과 같다면,
        base_list[idx-1]=rule_dic[f"{former_idx}{idx}{later_idx}"]  #  base_list의 idx 앞자리가, rule_dic의 밸류로 바뀐다..


'''
'''
class Duck:
    def __init__(self, input_name):
        self.name = input_name

fowl = Duck("Daffy")
print(fowl.name)

fowl.name = "Daphne"
print(fowl.name)'''

# while 문 이용해서 구구단

# 1~9까지...
#
# num1 = 1
#
# while num1<10:
#     num2 = 1
#     while num2<=9:
#         result=num1*num2
#         print(f"{num1}*{num2} = {result}")
#         num2+=1
#     num1+=1
'''
num2=1
while num2<10:
    for num1 in range(1,10):
        result=num1*num2
        print(f"{num2}*{num1}={result}")
    num2+=1'''
#
# a,b,c = 0, 0, 0
# #  a+b+c == 400, a**2 + b**2 == c**2, a<b<c
#
# for a in range(1,401):
#     for b in range(1,401):
#         for c in range(1,401):
#             if a+b+c == 400 and a**2 + b**2 == c**2 and a<b<c:
#                 print(a,b,c)
#                 print(a*b*c)


# while a<400:
#     a+=1
#     while b<400:
#         b +=1 
#         while c<400:
#             c +=1
#             if a+b+c == 400 and a**2 + b**2 == c**2 and a<b<c:
#                 print(a*b*c)

#
# kakao_list = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
#
#
# def add_kkt(nm, ct):
#     tup_val = (nm, ct)
#     for i in range(len(kakao_list) - 1):
#         if int(ct) == int(kakao_list[0][1]):
#             kakao_list.insert(0, tup_val)
#             break
#         elif int(ct) >= int(kakao_list[i][1]):
#             kakao_list.insert(i, tup_val)
#             break
#
#     return kakao_list
#
#
# name = input("추가할 친구-->")
# count = input("카톡 횟수-->")
# add_kkt(name, count)
# print(kakao_list)

