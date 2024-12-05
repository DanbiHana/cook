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
