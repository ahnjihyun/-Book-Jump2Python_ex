## ==============================================================
## if문 한줄로 작성하기 (128p)
## ==============================================================
## 조건부 표현식
## (조건문이 참인 경우) if (조건문) else (조건문이 거짓인 경우)
## ==============================================================

score = 80
message=''

# 예시 코드 
if score >= 60:
    message = 'success'
    print('Before: ', message)
else:
    message = 'failure' 
    print('Before: ', message)


# 조건부 표현식 적용후
message='success' if sore>=60 else message='failure'
print('After: ', message)
