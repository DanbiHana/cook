package com.mbc.cook.service.community;

import java.time.LocalDateTime;

public interface CommentInterface {
    public long getCommentNum();

    public String getCommentId();

    public String getCommentContent();

    public LocalDateTime getCommentDate();

    public LocalDateTime getCommentUpdateDate();

    public int getCommunityNum();

    public int getIndent();

    public int getStep();
}
