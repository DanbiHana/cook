package com.mbc.cook.dto.community;

import com.mbc.cook.entity.community.CommentEntity;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class CommentDTO {
    long commentNum;
    String commentId;
    String commentContent;
    LocalDateTime commentDate;
    LocalDateTime commentUpdateDate;
    int communityNum;
    int indent;
    int step;

    public CommentEntity commentEntity() {
        return (new CommentEntity(commentNum,commentId,commentContent,commentDate,commentUpdateDate,communityNum,indent,step));
    }
}
