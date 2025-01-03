# 소개

이 프로젝트는 Django를 사용하여 제작된 동아리 관리용 웹 애플리케이션입니다. 선생님과 학생 모두 사용할 수 있는 기능을 제공하며, 출석 관리, To-Do 리스트 관리, 사용자 관리를 통해 효율적인 동아리 운영을 지원합니다.

## 주요 기능
### 사용자 기능
- 회원가입
    - 필수 입력 정보: 이름, ID, 비밀번호, 전화번호
    - 역할 선택: 선생님 또는 학생
    - 회원가입 후, 메인 페이지로 자동 이동 및 자동 로그인 처리.
- 로그인/로그아웃
    - 사용자는 로그인 및 로그아웃 가능.
    - 로그인 후 메인 페이지로 리디렉션.
- To-Do 리스트
    - 개인 To-Do 항목 추가 가능.
    - 완료된 항목 체크 가능(체크 상태 유지).
    - 삭제 버튼을 통해 항목 삭제 가능.
- 출석 체크
    - 하루에 한 번만 출석 체크 가능.    
    - 이미 출석 체크한 경우 “오늘 이미 출석체크를 하셨습니다.” 메시지 표시.
### 선생님 전용 기능
- 출석 체크 확인
    - 선생님은 학생들의 출석 현황만 확인 가능.
    - 출석 체크 페이지(학생용)와 다른 페이지로 구성.

## 페이지
### 관리자(admin) 페이지
- 사용자 관리
	- 모든 사용자 정보 확인 가능(이름, ID, 비밀번호, 전화번호).
- 사용자 To-Do 관리
    - 각 사용자의 To-Do 리스트와 완료 여부를 확인 가능.
- 출석 체크 관리
    - 각 사용자의 출석 기록 확인 및 관리 가능.
### 페이지 구성
- 메인 페이지: index.html
- 회원가입 페이지: register.html
- 로그인 페이지: login.html
- To-Do 리스트 페이지: todo.html
- 출석 체크 페이지: check.html
- 선생님 전용 출석 체크 페이지: teacher.html

## 기본 동작 흐름
1. 애플리케이션 실행 시
    - 메인 페이지(index.html)로 이동.
2.	회원가입
    - 회원가입 후 바로 메인 페이지로 이동 및 자동 로그인.
3.	로그인
    - 로그인 성공 시 메인 페이지로 이동.
4.	To-Do 관리
    - To-Do 항목 추가, 체크, 삭제 가능.
5.	출석 체크
    - 학생은 하루에 한 번 출석 체크 가능.
    - 이미 출석 체크한 경우 오류 메시지 출력.

## 기술 스택
- Framework: Django
- Frontend: HTML, CSS
- Database: SQLite (Django 기본 DB)

## 설치 및 실행 방법
1.	가상 환경 설정
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
2.	Django 설치
    ```
    pip install django
    ```
3.	프로젝트 생성 및 실행
    ```
    django-admin startproject club_management
    cd club_management
    python manage.py startapp club
    python manage.py runserver
    ```
4.	브라우저에서 http://127.0.0.1:8000로 접속.

5. 완성