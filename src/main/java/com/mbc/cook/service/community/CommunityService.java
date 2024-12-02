package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommunityEntity;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public interface CommunityService {
    void insertcommunity(CommunityEntity centity);

    Page<CommunityEntity> list(int page);


    CommunityEntity getCommunity(long num);

    void readcntUp(long num);

    void deleteCommunity(long num);

    void updateCommunity(long num, String title, String content, LocalDateTime update_date);
}
