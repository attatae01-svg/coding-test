def solution(lines):
    a=lines[0]              # 세가지 선분 중 첫번째 선분 정의
    b=lines[1]              # 두번째 선분 정의
    c=lines[2]              # 세번째 선분 정의
    
    
    aa=range(a[0],a[1])     # 첫번째 선분의 길이 정의
    bb=range(b[0],b[1])     # 두번째 선분의 길이 정의
    cc=range(c[0],c[1])     # 세번재 선분의 길이 정의
    
    
    s1=set(aa)&set(bb)      # 첫번째 선분과 두번째 선분의 중복을 제거한 합을 위해 set 이후 교집합 찾기
    s2=set(cc)&set(bb)      # 세번째 선분과 두번째 선분의 중복을 제거한 합을 위해 set 이후 교집합 찾기
    s3=set(aa)&set(cc)      # 첫번째 선분과 세번째 선분의 중복을 제거한 합을 위해 set 이후 교집합 찾기
    s4 = s1 | s2 | s3       # 각각의 교집합을 다 더해서 합집합 찾기

    
    return len(s4)          # 마지막으로 선분의 길이 리턴하기
