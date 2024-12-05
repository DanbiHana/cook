package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.repository.community.CommentRepository;
import com.mbc.cook.repository.community.CommunityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class CommunityServiceImp implements CommunityService {
    @Autowired
    CommunityRepository communityRepository;
    @Autowired
    CommentRepository commentRepository;

    @Override
    public void insertcommunity(CommunityEntity centity) {
        communityRepository.save(centity);
    }

    @Override
    public List<CommunityEntity> adminList() {
        return communityRepository.adminList();
    }

    @Override
    public Page<CommunityEntity> otherList(int page) {
        return communityRepository.otherList(PageRequest.of(page,10));
    }

    @Override
    public CommunityEntity getCommunity(long num) {
        return communityRepository.findById(num).orElse(null);
    }

    @Override
    public void readcntUp(long num) {
        communityRepository.readcntUp(num);
    }

    @Override
    public void deleteCommunity(long commu_num) {
        communityRepository.deleteById(commu_num);
    }

    @Override
    public void updateCommunity(long num, String title, String content, LocalDateTime update_date) {
        communityRepository.updateSave(num, title, content, update_date);
    }

    @Override
    public List<CommentEntity> getComment(long num) {
        return commentRepository.getComment(num);
    }

    @Override
    public List<CommentEntity> getRecomment(long num) {
        return commentRepository.getRecomment(num);
    }

    @Override
    public void deleteAllComment(long commu_num) {
        commentRepository.deleteAllComment(commu_num);
    }
}
