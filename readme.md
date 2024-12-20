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
    ```
