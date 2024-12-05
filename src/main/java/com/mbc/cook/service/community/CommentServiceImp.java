package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.repository.community.CommentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class CommentServiceImp implements CommentService {
    @Autowired
    CommentRepository commentRepository;

    @Override
    public void commentRegister(CommentEntity commentEntity) {
        commentRepository.save(commentEntity);
    }

    @Override
    public void commentUpdate(long seq, String content, LocalDateTime nowday) {
        commentRepository.commentUpdate(seq, content, nowday);
    }

    @Override
    public void commentDelete(long num) {
        commentRepository.deleteById(num);
    }

    @Override
    public void commentup(long comment_num) {
        commentRepository.commentUp(comment_num);
    }

    @Override
    public void commentdw(int commuIndent) {
        commentRepository.commentDw(commuIndent);
    }

    @Override
    public void recommentDelete(long commuNum) {
        commentRepository.recommentDelete(commuNum);
    }
}
