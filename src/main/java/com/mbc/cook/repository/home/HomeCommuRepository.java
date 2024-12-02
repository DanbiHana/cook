package com.mbc.cook.repository.home;

import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.service.home.HomeInterface;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;

@Repository
public interface HomeCommuRepository extends JpaRepository<CommunityEntity, Long> {
    @Transactional
    @Query(value = "select * from (" +
            "select * from cookcommunity " +
            "order by community_num desc) " +
            "where community_id='admin' and rownum <= 5", nativeQuery = true)
    List<CommunityEntity> findCommuAdmin();

    @Transactional
    @Query(value = "select * from (" +
            "select * from cookcommunity " +
            "order by community_num desc) " +
            "where community_id!='admin' and rownum <= 5", nativeQuery = true)
    List<CommunityEntity> findCommuOther();

    @Transactional
    @Query(value = "select count(community_id) as commuCount " +
            "from cookcommunity c where c.community_id=:id", nativeQuery = true)
    HomeInterface countCommu(@Param(value = "id") String id);

    @Query(value = "select count(community_id) as commentCount " +
            "from cookcommunity c where c.community_id=:id", nativeQuery = true)
    HomeInterface countComment(@Param(value = "id") String id);
}