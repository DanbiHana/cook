package com.mbc.cook.service.home;

import com.mbc.cook.entity.community.CommunityEntity;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface HomeService {
    List<CommunityEntity> findCommuFive();

    List<CommunityEntity> findCommuFive2();

    HomeInterface countCommu(String id);

    HomeInterface countComment(String id);

    List<CommunityEntity> findMyCommu(String id);
}
