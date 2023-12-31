def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    print_hi('PyCharm')

# __name__은 파이썬의 특별한 변수로, 현재 모듈의 이름을 나타냅니다. 
# 파이썬 스크립트가 직접 실행되는 경우에는 __name__이 '__main__'으로 설정됩니다. 
# 그러나 스크립트가 모듈로 사용될 때는 해당 모듈의 이름이 설정됩니다.

# 따라서, if __name__ == '__main__':이라는 구문은 
# 현재 스크립트가 직접 실행되는 경우에만 아래의 코드 블록을 실행하라는 의미를 갖습니다. 

# 이는 스크립트를 모듈로 사용할 때에는 특정 코드 블록이 실행되지 않도록 하는데 사용됩니다.