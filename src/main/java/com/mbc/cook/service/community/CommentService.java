package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.entity.community.CommunityEntity;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public interface CommentService {

    void insertcomment(CommentEntity commententity);
}
