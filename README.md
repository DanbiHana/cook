# 🍽 COOK:EAT
MBC 아카데미 Spring Boot 프로젝트 with 김규리, 김민성, 박현준, 이혜린, 천시아
<br>
pdf 다운로드: [COOK_EAT.pdf](https://github.com/user-attachments/files/18217940/COOK_EAT.pdf)
<br><br>
## 🍴 프로젝트 소개
&nbsp;<b>< 이름 소개 ></b>
<br>
COOK: - 요리하다&ensp;/&ensp;EAT - 먹다
<br/>
'내가 요리한 음식을 내가 먹는다'는 뜻으로, 1인 가구가 타겟층입니다.
<br><br>
&nbsp;<b>< 개요 ></b>
<br>
COOK:EAT은 <b>1인 가구</b>를 위한 레시피 소개 웹페이지입니다.
<br/>
한식, 중식, 일식, 양식으로 나누어 다양한 요리를 소개합니다.
![002](https://github.com/user-attachments/assets/1336c10a-c220-4989-a577-339089b39a09)
![030](https://github.com/user-attachments/assets/a97b3a37-ec37-4492-baff-b9609c06f63c)
<br>
<br>
<br>

## 🍴 프로젝트 개발 기간
2024.11.11 ~ 2024.12.06
<br><br><br>

## 🍴 팀 멤버
김규리, 김민성, 박현준, 이혜린[조장🌟], 천시아
![003](https://github.com/user-attachments/assets/1facde83-ebad-44d5-991c-ca8421063af5)
<br>
<br>
<br>

## 🍴 기술 스택
✔️ HTML, CSS, JavaScript<br>
✔️ Ajax, JQuery<br>
✔️ Oracle<br>
✔️ Java, SpringBoot<br>
✔️ Git<br>
✔️ Python<br><br>
![COOK_EAT-004](https://github.com/user-attachments/assets/5790c08f-6d2b-4b49-ada6-a8228d50e220)
<br>
<br>
<br>

## 🍴 페이지 구성
### 1. 레시피<br>
&ensp;- 등록: 관리자가 레시피를 등록 가능.(파이썬을 이용한 쿠팡 웹 크롤링 이용)
<br/>
&ensp;- 리스트: 관리자가 등록한 레시피 리스트업.(검색 기능 부여)
<br/>
&ensp;- 상세: 레시피의 재료와 방법을 볼 수 있음.(필요한 재료 장바구니 추가 기능, 로그인 후 이용 가능)
<br/>
&ensp;- 수정: 관리자가 레시피를 수정.
<br/>
&ensp;- 삭제: 관리자가 레시피를 삭제.
![013](https://github.com/user-attachments/assets/0575772e-c1ef-4be9-97a1-19a8f2620e6a)
![016](https://github.com/user-attachments/assets/9418a6f5-89bd-4084-a8bd-b9b113832490)
![018](https://github.com/user-attachments/assets/dc04b611-3488-49ca-9127-a9d5a05725fd)
<br/>
<br/>
<br/>
### 2. 커뮤니티(로그인 후 이용 가능)<br>
&ensp;- 등록: 제목, 내용을 등록
<br/>
&ensp;- 리스트: 관리자/일반 유저가 등록한 게시글이 리스트업.(관리자: 공지사항 / 일반 유저: 자유게시판)
<br/>
&ensp;- 상세: 클릭한 게시글의 상세 글을 볼 수 있음.(댓글/대댓글 기능 추가)
<br/>
&ensp;- 수정: 게시글을 쓴 유저만 게시글 수정 기능 부여.
<br/>
&ensp;- 삭제: 게시글을 쓴 유저만 게시글 삭제 기능 부여.
<br/>
&ensp;- 공지: 관리자가 쓴 글이 공지로 등록되며 목록 화면 상단에 표출.
![021](https://github.com/user-attachments/assets/c8c5d837-3525-4fc9-affb-58cab0606047)
![023](https://github.com/user-attachments/assets/72454cdf-89de-4f82-a82f-76a06b9a28c4)
![024](https://github.com/user-attachments/assets/4fd36612-b6e5-4cc7-9bf1-d0169135904b)
<br/>
<br/>
<br/>
### 3. 뭐 먹지?<br>
&ensp;- 오늘 뭐 먹을지 고민하는 분들을 위한 랜덤 뽑기.
![025](https://github.com/user-attachments/assets/5110002a-6fac-4297-a98b-6e39c247a48d)
![026](https://github.com/user-attachments/assets/d6e617c0-158c-41a3-a2b0-acffef0d5a37)
<br/>
<br/>
<br/>
### 4. 설정<br>
&ensp;- 문의: FAQ로 자주 묻는 질문을 관리자가 리스트업.
<br/>
&ensp;- 카테고리: 관리자가 한식/중식/일식/양식의 하위 카테고리를 추가/수정/삭제 가능.
![027](https://github.com/user-attachments/assets/7d6f35cc-533b-41bd-b4bf-131ac15c21b6)
![028](https://github.com/user-attachments/assets/4aacacea-0730-4ac8-b86f-a22accd013c3)
![029](https://github.com/user-attachments/assets/b54391ba-48c4-40ad-97c7-e55e95a49d0f)
<br/>
<br/>
<br/>
### 5. 장바구니/주문내역<br>
&ensp;- 장바구니: 장바구니에 담긴 상품을 수정/결제.
<br/>
&ensp;- 주문내역: 결제된 주문 내역 리스트업. (관리자는 전체아이디 리스트)
![019](https://github.com/user-attachments/assets/c713526f-b318-4810-b897-c09b5d72ec30)
![020](https://github.com/user-attachments/assets/725bb086-3151-48de-9ead-cd896630deed)
<br/>
<br/>
### 6. 회원관리<br>
&ensp;- 회원 가입: 개인 정보 입력으로 회원가입 가능.(비밀번호 암호화, 다음 API, 아이디 중복확인, 관리자는 'admin'으로 회원가입을 해야 진입 가능)
<br/>
&ensp;- 마이페이지: 비밀번호 확인을 통한 마이페이지.(아이디를 제외한 개인정보 수정 가능)
<br/>
&ensp;- 회원 목록: 사이트에 가입한 회원 목록 리스트업.(관리자 기능)
![006](https://github.com/user-attachments/assets/129cc0ca-6544-47a7-89f9-46eb62ba853f)
![007](https://github.com/user-attachments/assets/6c3e6733-9c13-4ff3-8630-f6578a2f48d8)
![010](https://github.com/user-attachments/assets/9b81babc-d09a-48c1-a831-d79fc0098f39)
![011](https://github.com/user-attachments/assets/758fae7e-7aed-4ea3-91db-e68b1fb8ac54)
<br/>
<br/>
### 7.로그인<br>
&ensp;- 로그인: Security를 활용한 로그인, 이용 가능 사이트 제한.
![008](https://github.com/user-attachments/assets/e5a0ae0a-11dd-4415-b368-b45b6dc23de7)
<br/>
&ensp;- 아이디 찾기/비밀번호 찾기: 간단한 회원 정보 입력으로 아이디 및 비밀번호 찾기 기능 부여.
![009](https://github.com/user-attachments/assets/32b95554-fd2e-4352-b384-817f2fe1d602)
<br/>
