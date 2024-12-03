package com.mbc.cook.entity.community;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name = "cookcomment")
@SequenceGenerator(name = "comment", sequenceName = "comment_num_seq", allocationSize = 1, initialValue = 10001)
public class CommentEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "comment")
    @Column(name = "comment_num")
    long commentNum;
    @Column(name = "comment_id")
    String commentId;
    @Column(name = "comment_content")
    String commentContent;
    @Column(name = "comment_date")
    LocalDateTime commentDate;
    @Column(name = "comment_update_date")
    LocalDateTime commentUpdateDate;
    @Column(name = "community_num")
    int communityNum;
    @Column(name = "indent")
    int indent;
    @Column(name = "step")
    int step;
}
