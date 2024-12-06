import sys
import sqlite3
import oracledb
import time
import re
from datetime import datetime
import bcrypt
import os
import hashlib

# 비밀번호 해싱
password = "test1234"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# 오라클 라이브러리 경로 설정
oracledb.init_oracle_client(lib_dir="C:\\project\\cook\\instantclient-basic-windows.x64-11.2.0.4.0\\instantclient_11_2")

# 오라클 데이터베이스 연결
connect = oracledb.connect(user='lhr', password='1234', dsn='localhost')
c = connect.cursor()  # 커서 생성

today = datetime.today()

#관리자 로드
#usermember/id/pw/name/tel1/tel2/tel3/jumin1/jumin2/email_id/email_domain/addr/detailaddr/streetaddr
###관리자
c.execute('insert into usermember (id,pw,name,tel1,tel2,tel3,jumin1,jumin2,email_id,email_domain,addr,streetaddr,detailaddr) ' +
          'values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)'
          ,('admin',hashed_password.decode('utf-8'),'관리자','000','0000','0000','930210','1','admin','naver.com','16455','경기 수원시 팔달구 향교로2','3층 mbc 아카데미'))
###일반유저
c.execute('insert into usermember (id,pw,name,tel1,tel2,tel3,jumin1,jumin2,email_id,email_domain,addr,streetaddr,detailaddr) ' +
          'values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)'
          ,('test1234',hashed_password.decode('utf-8'),'테스터','010','1234','5678','920505','2','test1234','naver.com','16455','경기 수원시 팔달구 향교로2','3층 mbc 아카데미'))

# 데이터베이스에 저장
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '탕/찌개'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '반찬'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('한식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('일식', '간식'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('중식', '요리'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '면'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '밥'))
c.execute('insert into recipecategory (categorynum, maincategory, subcategory) values(category_seq.nextval, :1, :2)',('양식', '요리'))

##########ingredient
#####1. 치킨덮밥마요
##치킨(1),계란(2),깐양파(3),밥(4),마요네즈(5),진간장(6),설탕(7)
#1 치킨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('야들리애 100% 닭다리 순살 후라이드 가라아게 치킨, 250g, 1개',8900,'치킨마요덮밥'))
#2 계란
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 신선한 대란, 10구, 1개',3790,'치킨마요덮밥'))
#3 양파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 친환경 깐양파, 300g, 1개',2980,'치킨마요덮밥'))
#4 밥
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('1인 가구 필수템 오뚜기 밥 210g, 1박스',15200,'치킨마요덮밥'))
#5 마요네즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 골드 마요네즈, 500g, 1개',4730,'치킨마요덮밥'))
#6 진간장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇살담은 두번 달여 더 진한 진간장, 200ml, 2개',2520,'치킨마요덮밥'))
#7 설탕
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('큐원 갈색설탕, 1kg, 1개',2560,'치킨마요덮밥'))

#####2. 청국장
##청국장(8),된장(9),양파(3),김치(10),대파(11),멸치(12),물(13),다진마늘(14),두부(15)
#8 청국장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('다담 청국장 양념, 530g, 1개',5200,'청국장'))
#9 된장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원순창 재래식 생된장, 1kg, 1개',4700,'청국장'))
#10 김치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰 국내산 포기 김치, 4kg, 1개',20090,'청국장'))
#11 대파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 국내산 절단대파, 500g, 1개',2800,'청국장'))
#12 멸치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('이어수산 통영 산지 직거래 국물용 멸치 (냉동), 500g, 1봉',9970,'청국장'))
#13 물
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('탐사수 무라벨, 2L, 12개',6790,'청국장'))
#14 다진마늘
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 국산 다진마늘, 500g, 1개',6650,'청국장'))
#15 두부
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('풀무원 소가 찌개두부, 290g, 1개',1240,'청국장'))

#####3. 미역국
##미역(16),다진마늘(14),간장(6),된장(9),소금(17)
#16 미역
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 미역, 250g, 1개',7990,'미역국'))
#17 소금
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 천일염 가는소금, 500g, 1개',3590,'미역국'))

#####4. 김치찌개
##쌀뜰물(13),대파(11),청양고추(18),돼지고기목살(19),김치(10),국간장(20),고춧가루(21),다진마늘(14),새우젓(22),된장(9)
#18 청양고추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 청양고추, 150g, 1개',1980,'김치찌개'))
#19 돼지 목살
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('포크밸리 1등급이상 돼지고기 찌개용 (냉장), 500g, 1팩',9990,'김치찌개'))
#20 국간장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 햇살담은 국간장, 500ml, 1개',3090,'김치찌개'))
#21 고추가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇님마을 양념이 잘 어우러지는 국산 고춧가루 보통매운맛, 110g, 1개',6900,'김치찌개'))
#22 새우젓
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('일미식품 국내산 참새우젓, 1개, 200g',4800,'김치찌개'))

#####5. 제육볶음
##돼지고기 앞다리살(23),양파(3),청양고추(18),대파(11),고추장(24),고춧가루(21),다진마늘(14),설탕(7),매실액(25),간장(6),통깨(26),후추(27)
#23 돼지 앞다리살
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 한돈 앞다리살 찌개용 (냉장), 500g, 1개',8660,'제육볶음'))
#24 고추장
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('순창궁 태양초 골드 고추장, 500g, 1개',3480,'제육볶음'))
#25 매실액
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('백설 리얼 매실청, 310ml, 1개',4530,'제육볶음'))
#26 통깨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 볶음참깨, 200g, 1개',5480,'제육볶음'))
#27 후추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 순후추, 100g, 1개',4640,'제육볶음'))

#####6. 잡채
##당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
#28 당면
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 자른 당면, 500g, 1개',6150,'잡채'))
#29 소고기
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 호주산 소고기 앞다리살 국거리용 (냉장), 300g, 1개',8700,'잡채'))
#30 파프리카
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('파프리카 혼합, 2개입, 1개',2790,'잡채'))
#31 당근
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 세척당근, 600g, 1개',4990,'잡채'))
#32 느타리버섯
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 무농약 느타리버섯, 200g, 1개',1430,'잡채'))
#33 시금치
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 시금치, 600g, 1개',6270,'잡채'))
#34 생강가루
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('내츄럴스파이스 생강분말, 35g, 1개',4200,'잡채'))
#35 식용유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('해표 콩기름 식용유, 1.8L, 1개',4500,'잡채'))
#36 올리고당
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 요리 올리고당, 1.2kg, 1개',4980,'잡채'))
#37 참기름
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기옛날 참기름, 500ml, 1개',7020,'잡채'))

#####7. 소불고기
##소불고기(38),식용유(35),물(13),후추(27),쪽파(39),간장(6),설탕(7),청주(40),다진파(41),다진마늘(14),다진생강(42),참기름(37)
#38 소불고기
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('고기듬뿍 양념 소불고기 (냉장), 500g, 1개',9980,'소불고기'))
#39 쪽파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 깐쪽파, 200g, 1개',3980,'소불고기'))
#40 청주
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 맛술, 830ml, 1개',3580,'소불고기'))
#41 다진 파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('친정엄마꾸러미 뚝딱 대파 (냉동), 500g, 1개',4880,'소불고기'))
#42 다진 생강
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 짜서쓰는 다진 생강, 300g, 1개',7730,'소불고기'))

#####8. 꼬막무침
##새꼬막(43),쪽파(39),소금(17),다진마늘(14),고춧가루(21),간장(6),설탕(7),식초(44),멸치액젓(45),참기름(37),참깨(46)
#43 새꼬막
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('우리바다좋은산지 벌교 출신 새꼬막, 1kg, 2봉',19380,'꼬막무침'))
#44 식초
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 사과식초, 360ml, 1개',1380,'꼬막무침'))
#45 멸치액젓
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('청정원 남해안 멸치액젓 골드, 500g, 1개',2300,'꼬막무침'))
#46 참깨
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 옛날 볶음참깨, 200g, 1개',5480,'꼬막무침'))

#####9. 비빔밥
##돼지고기목살(19),애호박(47),양파(3),당근(31),고추장(24),간장(6),설탕(7),깨소금(48),참기름(37),식초(44)
#47 애호박
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 애호박, 1개입, 1개',1580,'비빔밥'))
#48 깨소금
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇님마을 고소함이 가득한 우리집 깨소금, 1개, 100g',3800,'비빔밥'))

#####10. 김치볶음밥
#김치(10),설탕(7),간장(6),고춧가루(21),참기름(37),마요네즈(5),된장(9),파(39)
#추가 재료 없음

#####11. 간장계란밥
##밥(4),달걀(2),물(13),햄(49),다진대파(50),피자치즈(51),슬라이스치즈(52),간장(6),소금(17),후추(27)
#49 햄
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('롯데 의성마늘햄, 1kg, 1개',8440,'간장계란밥'))
#50 다진대파
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('대파 슬라이스, 150g, 1개',2190,'간장계란밥'))
#51 피자치즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 모짜렐라 피자치즈, 1개, 1kg',10530,'간장계란밥'))
#52 슬라이스 치즈
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 데일리 체다치즈 슬라이스, 396g, 1개',5990,'간장계란밥'))

#####12. 가지밥
##현미(53),가지(54),파(39),올리브유(55),간장(6),부추(56),다진마늘(14),고춧가루(21),설탕(7),참기름(37),통깨(26),간장(6)
#53 현미
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 현미, 5kg, 1개',12900,'가지밥'))
#54 가지
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 가지, 2개입, 1개',1980,'가지밥'))
#55 올리브유
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('백설 압착 올리브유, 500ml, 1개',11890,'가지밥'))
#56 부추
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 부추, 300g, 1개',2670,'가지밥'))


##########recipe
#####한식
###탕/찌개
#####청국장
##청국장(8),된장(9),양파(3),김치(10),대파(11),멸치(12),물(13),다진마늘(14),두부(15)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('청국장','한식','탕/찌개','cheongukjang.jpg','8,9,3,10,11,12,13,14,15',
           '멸치와 물을 넣고 육수를 끓인다.<br>'+
           '물이 끓기 시작하면 멸치를 빼고 먹기 좋게 썰은 김치를 넣는다.<br>'+
           '양파도 먹기 좋은 크기로 잘라 넣는다.<br>'+
           '대파를 넣는다.<br>'+
           '다진마늘을 넣는다.<br>'+
           '된장을 한 스푼 떠서 풀어준다.<br>'+
           '끓을 때 청국장을 넣는다(기호에 맞게 조금씩 넣으면서 맛보는 거 추천).<br>'+
           '푹 끓어지면 두부를 넣어줍니다.<br>'+
           '완성!',0))

#####미역국
##미역(16),다진마늘(14),간장(6),된장(9),소금(17)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('미역국','한식','탕/찌개','miyukguk.jfif','16,14,6,9,17',
           '미역을 물에 담궈 불려준다.<br>'+
           '불려진 미역을 잘라서 냄비에 넣고 참기름과 볶아준다.(미역이 물기가 없어 냄비에 달라 붙을 지경이 될 때까지)<br>'+
           '볶아진 미역에 물을 미역이 잠기기 않을 정도로 부어준다.<br>'+
           '다진마늘을 한 스푼정도 넣어준다.<br>'+
           '센 불에 끓여준다.<br>'+
           '물이 졸아들면 다시 물을 미역이 잠길 만큼 부어준다.<br>'+
           '간장 1티,되장 2/1티,소금(원하는 간만큼)을 넣어준다.<br>'+
           '완성!',0))

#####김치찌개
##쌀뜨물(13),대파(11),청양고추(18),돼지고기목살(19),김치(10),국간장(20),고춧가루(21),다진마늘(14),새우젓(22),된장(9)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('김치찌개','한식','탕/찌개','kimchizzigae.jfif','13,11,18,19,10,20,21,14,22,9',
           '2번째나 3번째 쌀뜨물을 준비한다.<br>'+
           '돼지고기 목살,대파,김치를 먹기 좋은 사이즈로 썰어준다.<br>'+
           '냄비에 쌀뜨물 700ml를 넣어준다.<br>'+
           '돼지고기목살을 넣어준다.<br>'+
           '된장을 1/2스푼 넣어준다.<br>'+
           '김치를 넣어준다.<br>'+
           '끓기 시작하면 다진마늘 한 스푼을 넣어준다.<br>'+
           '고춧가루와 국간장을 한 스푼을 넣어준다.<br>'+
           '간을 보며 새우젓을 넣어준다.<br>'+
           '청양고추와 대파를 넣고 끓여준다.<br>'+
           '완성!',0))

###반찬
#####제육볶음
##돼지고기 앞다리살(23),양파(3),청양고추(18),대파(11),고추장(24),고춧가루(21),다진마늘(14),설탕(7),매실액(25),간장(6),통깨(26),후추(27)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('제육볶음','한식','반찬','jaeyuk.jfif','16,14,6,9,17',
           '재료를 준비한다.<br>'+
           '고추장(3큰술),고춧가루(2큰술),다진마늘(1큰술),설탕(2큰술),간장(1큰술),통깨(약간),후추(약간)을 모두 넣고 섞어준다.<br>'+
           '대파와 청양고추는 어슷썰어주고 양파는 먹기 좋은 크기로 잘라준다.<br>'+
           '돼지고기는 한 입 크기로 썰어준다.<br>'+
           '만들어둔 양념장에 고기를 버무려준다.<br>'+
           '바로 볶아도 되고 냉장고에 30분정도 두어 숙성시켜준다.<br>'+
           '팬에 식용유 2큰술과 대파를 넣고 강불로 3분정도 볶아 파기름을 내준다.<br>'+
           '양념한 고기를 넣어준다.<br>'+
           '중볼로 볶아 고기를 완전히 익혀준다.<br>'+
           '양파와 청양고추를 넣어준다.<br>'+
           '마지막으로 통깨를 뿌려준다.<br>'+
           '완성!',0))

#####잡채
##당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('잡채','한식','반찬','jabchae.jfif','',
           '소고기는 다진마늘 0.5,후춧가루,소금,생강가루 적당량을 넣어 고기의 밑간을 해준다.<br>'+
           '잡채에 넣을 채소 당근,파프리카,양파를 채썰어주고 느타리 버섯은 가닥가닥 떼어 준비한다.<br>'+
           '시금치는 물에 씻어 물기를 빼고 준비한다.<br>'+
           '달군 팬에 식용유를 두르고 양파와 소금,후춧가루를 조금씩 넣어 볶아준다.<br>'+
           '같은 방법으로 소금,후춧가루로 간을 하고 느타리버섯을 볶아준다.<br>'+
           '시금치 역시 소금 간을 하고 살짝 볶아준다.<br>'+
           '마지막으로 밑간을 해놓은 소고기를 볶아준다..<br>'+
           '각각 재료를 볶아 준비해준다.<br>'+
           '냄비에 물을 담고 물이 팔팔 끓으면 당면을 넣고 10-11분 정도 삶아준다.<br>'+
           '삶아낸 당면은 찬물에 행군다.<br>'+
           '팬에 식용유 2,간장5,올리고당2를 넣고 삶아놓은 당면을 넣는다.<br>'+
           '물기가 사라질 때까지 볶아준다.<br>'+
           '볶아놓은 당면은 한 김 식히고 볶아놓았던 야채로 모두 한 곳에 넣고 참기름2,통깨1을 넣어 버무려준다.<br>'+
           '완성!',0))

#####소불고기
##소불고기(38),식용유(35),물(13),후추(27),쪽파(39),간장(6),설탕(7),청주(40),다진파(41),다진마늘(14),다진생강(42),참기름(37)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('소불고기','한식','반찬','sobulgogi.jfif','',
           '불고기를 먹기 좋은 크기로 썬다.<br>'+
           '양념장을 만든다(간장3t,물2t,설탕2t,청주2t,다진파1t,다진마늘1t,다진생각1/4t,참기름약간).<br>'+
           '불고기에 양념장을 넣고 잘 섞는다.<br>'+
           '팬에 약간의 기름을 두르고 불고기를 익힌다.<br>'+
           '고기가 타지 않도록 중간마다 물을 넣는다.<br>'+
           '후추를 약간 뿌린다.<br>'+
           '구운 고기 위에 쪽파를 뿌린다.<br>'+
           '완성!',0))

#####꼬막무침
##새꼬막(43),쪽파(39),소금(17),다진마늘(14),고춧가루(21),간장(6),설탕(7),식초(44),멸치액젓(45),참기름(37),참깨(46)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('꼬막무침','한식','반찬','ggomakmuchim.jfif','',
           '소금 1스푼을 넣고 꼬막을 깨끗하게 닦아준다.<br>'+
           '끓는물에 소금 1스푼 넣고 꼬막을 삶아준다.<br>'+
           '꼬막이 입을 벌리면 건져낸다.<br>'+
           '건져낸 꼬막은 흐르는 찬물에 닦아준다.<br>'+
           '껍질을 분리한다.<br>'+
           '껍질은 벗긴 꼬막은 물에 다시 씻고 물기를 빼준다.<br>'+
           '쪽파를 채썰어준다.<br>'+
           '물기를 뺀 꼬막에 준비된 양념과 쪽파를 넣어준다.(다진마늘1스푼,고춧가루2스푼,간장2스푼,설탕1.5스푼,식초0.5스푼,멸치액젓1스푼,참기름0.5스푼)<br>'+
           '완성!',0))

###밥
#####비빔밥
##돼지고기목살(19),애호박(47),양파(3),당근(31),고추장(24),간장(6),설탕(7),깨소금(48),참기름(37),식초(44)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('비빔밥','한식','밥','bibimbab.jfif','',
           '양파,당근,애호박을 채썰어서 준비한다.<br>'+
           '비빔밥에 비벼먹을 양념장을 준비한다.(고추장2T,간장2T,설탕1.5T,깨소금,참기름,식초1T)<br>'+
           '먼저 당근을 소금 1꼬집 넣고 색깔이 나게 볶아준다.<br>'+
           '애호박도 똑같이 볶아준다.<br>'+
           '양파는 간장 1T 넣고 중불에 오래 볶아준다.<br>'+
           '소금,후추로 밑간을 해놓은 채썰어준 돼지고기를 볶아준다.<br>'+
           '밥 위에 볶아놓은 야채와 고기를 올리고 반숙 계란후라이와 양념장을 올려준다.<br>'+
           '완성!',0))

#####김치볶음밥
##김치(10),설탕(7),간장(6),고춧가루(21),참기름(37),마요네즈(5),된장(9),파(39)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('김치볶음밥','한식','밥','kimchibab.jfif','',
           '김치를 잘게 썬다.<br>'+
           '김치에 양념을 넣고 잘 비벼준다.(고춧가루1스푼,설탕1스푼,진간장1스푼,참기름2스푼,마요네즈1스푼,된장1/3스푼,다진대파2큰술)<br>'+
           '식용유 3스푼을 붓고 달군 팬에 재료를 고루 펴서 부어준다.<br>'+
           '뚜껑을 열고 수분이 거의 남지않은 꾸덕한 상태가 되면 밥 2공기를 넣고 볶는다.<br>'+
           '흰밥이 보이지 않을 정도로 고루 섞어준다.<br>'+
           '밥을 펴 뚜껑을 덮고 센 불에 20-30초간 둔다.<br>'+
           '완성!',0))

#간장계란밥
##밥(4),달걀(2),물(13),햄(49),다진대파(50),피자치즈(51),슬라이스치즈(52),간장(6),소금(17),후추(27)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('간장계란밥','한식','밥','ganjangbab.jfif','',
           '햄,대파는 다져서 준비한다.<br>'+
           '전자레인지용 그릇에 달걀을 풀고, 물,후추,소금을 넣고 섞는다.(달걀1개,물100ml,소금후추 약간).<br>'+
           '달걀 물에 밥,햄,대파,간장(1/2T)를 넣어 잘 섞는다.<br>'+
           '랩을 덮어 구멍을 뚫은 후 전자레인지에 3분간 익힌다.<br>'+
           '전자레인지에서 꺼낸 후 잘 섞는다.<br>'+
           '달걀밥 위에 피자치즈를 올리고 슬라이스 치즈를 올려 전자레인지에 3분간 더 익혀준다.<br>'+
           '완성!',0))

#####가지밥
##현미(53),가지(54),파(39),올리브유(55),간장(6),부추(56),다진마늘(14),고춧가루(21),설탕(7),참기름(37),통깨(26),간장(6)
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('가지밥','한식','밥','gajibab.jfif','53,54,39,55,6,56,14,21,7,37,26,6',
           '가지를 손질해서 원하는 만큼 어슷 썰어준다.<br>'+
           '팬을 달구기 전에 올리브유 4큰술과 다진파 1컵을 넣은 후 중불에서 파를 노릇하게 볶아준다.<br>'+
           '파향이 올라오면 가지를 넣고 볶는다.<br>'+
           '가지가 숨이 죽을 쯤 간장 3큰술을 팬 가장자리에 눌리듯 넣어 볶는다.<br>'+
           '30분 정도 불린 현미쌀 2컵에 물을 평상시 밥하는 양보다 80%정도 넣고 볶은 가지를 올린 후 밥을 지어준다.<br>'+
           '밥이 지어질 동안 양념장을 준비한다.(다진부추1/2컵,다진파1/2컵,고춧가루2큰술,다진마늘1/2큰술 통깨 적당량,간장(재료들이 되직하게 섞일 정도)).<br>'+
           '매운 맛을 원하면 매운고추를 다져서 넣어준다.<br>'+
           '설탕은 간을 보며 넣어주고 참기름을 넣어준다.<br>'+
           '가지밥이 완성되면 양념장을 적당이 얹어 비빈다.<br>'+
           '완성!',0))



#####중식
#####음식이름
##필요한 재료:당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
#c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
#          ('음식이름','중식','2차 카테고리','음식사진src','재료시퀀스번호만나열',
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '완성!',0))#완성은 항상 붙이기

#####일식
##밥
c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
          ('치킨마요덮밥','일식','밥','chickenmayo.jpg','1,2,3,4,5,6,7',
           '계란 2개를 풀어 계란물을 만든다.<br>'+
           '팬에 기름을 두르고 계란물을 붓는다.<br>'+
           '젓가락을 이용해 에그 스크램블을 만든다.<br>'+
           '준비된 밥에 스크램블을 올린다.<br>'+
           '치킨을 구워준다.<br>'+
           '치킨이 구워지는 동안 양파 반개를 썰어준다.<br>'+
           '치킨이 다 구워지면 가위를 이용하여 먹기 좋게 잘라준다.<br>'+
           '팬에 기름을 두르고 양파를 볶아준다.<br>'+
           '양파가 투명해질때 간장 1스푼, 설탕 0.5스푼을 넣고 마저 볶아준다.<br>'+
           '밥위에 볶음 양파, 치킨을 올리고 마요네즈를 뿌린다.<br>'+
           '완성!',0))

#####양식
##음식이름
#필요한 재료:당면(28),소고기(29),양파(3),파프리카(30),당근(31),느타리버섯(32),시금치(33),다진마늘(14),소금(17),후춧가루(27),생강가루(34),식용유(35),간장(6),올리고당(36),참기름(37),통깨(26)
#c.execute('insert into recipe (recipeseq,food,category1,category2,image,ingredient,recipe,hits) values(recipe_seq.nextval,:1,:2,:3,:4,:5,:6,:7)',
#          ('음식이름','양식','2차 카테고리','음식사진src','재료시퀀스번호만나열',
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '.<br>'+
#           '완성!',0))#완성은 항상 붙이기


#공지사항
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','오픈 공지','오픈 예상 날짜는 2024년 12월 9일입니다! 많관부!',today,today,0))
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','레시피 공지','원하는 레시피가 없다면? 커뮤니티 타이틀에 [건의]를 붙여 글을 올려주세요.',today,today,0))
c.execute('insert into cookcommunity (community_num, community_id, community_title, community_content, community_date, community_update_date, community_readcnt)' +
          'values(community_num_seq.nextval, :1, :2, :3, :4, :5, :6)',('admin','게시판 공지','타인을 향한 악의적인 댓글, 비방, 욕설 등의 게시글, 댓글은 별도의 경고 없이 유저 차단 조치 합니다.',today,today,0))
#레시피
connect.commit()

print('완료')
