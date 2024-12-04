package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.entity.community.CommunityEntity;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public interface CommunityService {
    void insertcommunity(CommunityEntity centity);

    List<CommunityEntity> adminList();

    Page<CommunityEntity> otherList(int page);

    CommunityEntity getCommunity(long num);

    void readcntUp(long num);

    void deleteCommunity(long num);

    void updateCommunity(long num, String title, String content, LocalDateTime update_date);

    List<CommentEntity> getComment(long num);

    List<CommentEntity> getRecomment(long num);
}
