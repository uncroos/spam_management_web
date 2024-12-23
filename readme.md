# Django 프로젝트

1. 가상환경
- 설치  
    ```
    python3 -m venv venv
    ```

- 활성화 
    ```
    source venv/bin/activate
    ```

2. Django
- 설치
    ```
    pip install django
    ```
- 설치한 패키지 관리
    ```
    pip freeze > requirements.txt
    ```

3. .gitignore 설정
-  venv 디렉토리는 Git에 포함되지 X
    ```
    venv/
    __pycache__/
    *.pyc
    *.sqlite3
    ```

## 기본
Django를 가지고 기초적인 웹을 만들거임.
웹 : 동아리 관리 웹

기능 : 
- 선생님 및 학생 기능
    - 선생님으로 가입을 하면, 학생의 출석 체크 현황만 확인 가능
    - 즉, 선생님은 출석 체크 페이지는 학생과 다르게 학생들의 출석 체크를 볼 수 있음
- 회원가입 기능
- 로그인기능
- 로그아웃 기능
- To-do 리스트 체크 기능
- 출석 체크 기능

페이지는 아래와 같다.
- 메인 페이지(index.html)
- 회원가입 페이지(register.html)
- 로그인 페이지(login.html)
- To-do 페이지(todo.html)
- 출석 체크 페이지(check.html)
- 선생님용 출석 체크 페이지(teacher.html)

실행 시, 바로 메인페이지(index.html)

회원가입 기능
- 이름, ID, PW, 전화번호를 필수로 받음
- 선생님 혹은 학생을 선택가능

To-Do 리스트 기능
- 사용자가 각자의 To-Do 리스트를 추가할 수 있음
- To-Do 리스트를 체크한 후, 체크된 상태 유지
- 삭제 버튼을 클릭 시, 삭제 가능

출석 체크 기능
- 출석은 하루에 한번만 가능
- 출석 체크 시, "오늘 이미 출석체크를 하셨습니다."

회원가입시
- 회원가입을 한 후에 바로 메인 페이지로 이동 및 바로 로그인

로그인 시
- 메인페이지로 이동

admin 페이지
- User 관리
    - 이름, ID, PW, 전화번호를 보여줌
- User의 To-Do 관리 ({{User.name}}의 To-Do 리스트와 "각 To-Do를 실행하였는가"를 했는지 안했는지 표시)
- User의 출석 체크를 관리

