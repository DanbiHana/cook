package com.mbc.cook.repository.home;

import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.service.home.HomeInterface;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import java.util.Optional;

@Repository
public interface HomeCommuRepository extends JpaRepository<CommunityEntity, Long> {
    //공지사항 최신글 5개
    @Transactional
    @Query(value = "select * from (" +
            "select * from cookcommunity " +
            "order by community_num desc) " +
            "where community_id='admin' and rownum <= 5", nativeQuery = true)
    List<CommunityEntity> findCommuAdmin();
    //자유게시판 최신글 5개
    @Transactional
    @Query(value = "select * from (" +
            "select * from cookcommunity " +
            "order by community_num desc) " +
            "where community_id!='admin' and rownum <= 5", nativeQuery = true)
    List<CommunityEntity> findCommuOther();
    //내 커뮤니티 갯수
    @Transactional
    @Query(value = "select count(community_id) as commuCount " +
            "from cookcommunity c where c.community_id=:id", nativeQuery = true)
    HomeInterface countCommu(@Param(value = "id") String id);
    //내 댓글 갯수
    @Transactional
    @Query(value = "select count(community_id) as commentCount " +
            "from cookcommunity c where c.community_id=:id", nativeQuery = true)
    HomeInterface countComment(@Param(value = "id") String id);
    //내가 쓴 글
    @Transactional
    @Query(value = "select community_num, community_date, " +
            "community_content, community_id, community_title, " +
            "community_update_date, community_readcnt " +
            "from cookcommunity c " +
            "where c.community_id=:id", nativeQuery = true)
    List<CommunityEntity> findMyCommu(@Param(value = "id") String id);
}