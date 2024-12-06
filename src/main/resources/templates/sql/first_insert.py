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
c.execute('insert into usermember (id,pw,name,tel1,tel2,tel3,jumin1,jumin2,email_id,email_domain,addr,streetaddr,detailaddr) ' +
          'values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13)'
          ,('admin',hashed_password.decode('utf-8'),'관리자','000','0000','0000','930210','1','admin','naver.com','16455','경기 수원시 팔달구 향교로2','3층 mbc 아카데미'))
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


#재료
#치킨덮밥마요
#1
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('야들리애 100% 닭다리 순살 후라이드 가라아게 치킨, 250g, 1개',8900,'치킨마요덮밥'))
#2
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('곰곰 신선한 대란, 10구, 1개',3790,'치킨마요덮밥'))
#3
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('국내산 친환경 깐양파, 300g, 1개',2980,'치킨마요덮밥'))
#4
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('1인 가구 필수템 오뚜기 밥 210g, 1박스',15200,'치킨마요덮밥'))
#5
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('오뚜기 골드 마요네즈, 500g, 1개',4730,'치킨마요덮밥'))
#6
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('햇살담은 두번 달여 더 진한 진간장, 200ml, 2개',2520,'치킨마요덮밥'))
#7
c.execute('insert into ingredient (ingre_seq,name,price,keyword) values(ingre_seq.nextval,:1,:2,:3)',('큐원 갈색설탕, 1kg, 1개',2560,'치킨마요덮밥'))



#한식

#중식

#일식
#밥
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
           '밥위에 볶음 양파, 치킨을 올리고 마요네즈를 뿌린다.<br>',0))

#양식


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
