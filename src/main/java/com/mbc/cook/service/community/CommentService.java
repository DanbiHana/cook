package com.mbc.cook.service.community;

import com.mbc.cook.entity.community.CommentEntity;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public interface CommentService {
    void commentRegister(CommentEntity commentEntity);

    void commentUpdate(long seq, String content, LocalDateTime nowday);

    void commentDelete(long num);

    void commentup(long comment_num);

    void commentdw(int commuIndent);
}
