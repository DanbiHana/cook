package com.mbc.cook.repository.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.service.community.CommentInterface;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface CommentRepository extends JpaRepository<CommentEntity,Long> {
    @Transactional
    @Query(value = "select * from cookcomment " +
            "where community_num=:num and indent=0 " +
            "order by comment_date desc, comment_update_date desc", nativeQuery = true)
    List<CommentEntity> getComment(@Param(value = "num") long num);

    @Transactional
    @Query(value = "select * from cookcomment " +
            "where community_num=:num and indent!=0 " +
            "order by comment_date desc, comment_update_date desc", nativeQuery = true)
    List<CommentEntity> getRecomment(@Param(value = "num") long num);

    @Transactional
    @Modifying
    @Query(value = "UPDATE cookcomment SET " +
            "comment_content = :content, " +
            "comment_update_date = :nowday " +
            "where comment_num = :seq", nativeQuery = true)
    void commentUpdate(@Param(value = "seq") long seq,
                       @Param(value = "content") String content,
                       @Param(value = "nowday") LocalDateTime nowday);

    @Transactional
    @Modifying
    @Query(value = "UPDATE cookcomment SET " +
            "step = step + 1 " +
            "where comment_num = :comment_num", nativeQuery = true)
    void commentUp(@Param(value = "comment_num") long comment_num);

    @Transactional
    @Modifying
    @Query(value = "UPDATE cookcomment SET " +
            "step = step - 1 " +
            "where comment_num = :commuIndent", nativeQuery = true)
    void commentDw(@Param(value = "commuIndent") int commuIndent);
}
