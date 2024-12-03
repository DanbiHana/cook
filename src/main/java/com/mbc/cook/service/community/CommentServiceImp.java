package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.repository.community.CommentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CommentServiceImp implements CommentService {

    @Autowired
    CommentRepository commentRepository;


    @Override
    public void insertcomment(CommentEntity commententity) {
        commentRepository.save(commententity);
    }
}
