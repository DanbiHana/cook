package com.mbc.cook.service.home;

import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.repository.home.HomeCommuRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class HomeServiceImp implements HomeService {
    @Autowired
    HomeCommuRepository homeRepository;

    @Override
    public List<CommunityEntity> findCommuFive() {
        return homeRepository.findCommuAdmin();
    }

    @Override
    public List<CommunityEntity> findCommuFive2() {
        return homeRepository.findCommuOther();
    }

    @Override
    public HomeInterface countCommu(String id) {
        return homeRepository.countCommu(id);
    }

    @Override
    public HomeInterface countComment(String id) {
        return homeRepository.countComment(id);
    }

    @Override
    public List<CommunityEntity> findMyCommu(String id) {
        return homeRepository.findMyCommu(id);
    }
}