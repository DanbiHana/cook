package com.mbc.cook.controller;

import com.mbc.cook.dto.community.CommentDTO;
import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.service.community.CommentService;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;

@Slf4j
@RestController
public class CommentController {
    @Autowired
    CommentService commentService;

    @PostMapping(value = "/comment/register")
    public void commentRegister(
            @AuthenticationPrincipal UserDetails userDetails,
            HttpServletResponse response,
            CommentDTO commentDTO,
            @RequestParam(value = "commu_num") int commu_num,//게시글 넘버
            @RequestParam(value = "comment_num") long comment_num,//댓글 넘버
            @RequestParam(value = "comment") String comment
    ) throws IOException {
        int step = commentDTO.getStep();
        String userid = userDetails.getUsername();
        LocalDateTime nowday = LocalDateTime.now();
        commentDTO.setCommunityNum(commu_num);
        commentDTO.setCommentId(userid);
        commentDTO.setCommentDate(nowday);
        commentDTO.setCommentUpdateDate(nowday);
        commentDTO.setCommentContent(comment);
        commentDTO.setIndent((int)comment_num);
        CommentEntity commentEntity = commentDTO.commentEntity();
        commentService.commentRegister(commentEntity);
        commentService.commentup(comment_num);
        PrintWriter prw = response.getWriter();
        prw.print("댓글을 저장했습니다.");
    }

    @PostMapping(value = "/comment/update")
    public void commentUpdate(
            CommentDTO commentDTO,
            HttpServletResponse response,
            @RequestParam(value = "seq") long seq,
            @RequestParam(value = "content") String content
    ) throws IOException {
        LocalDateTime nowday = LocalDateTime.now();
        commentService.commentUpdate(seq,content,nowday);
        PrintWriter prw = response.getWriter();
        prw.print("댓글을 수정했습니다.");
    }

    @PostMapping(value = "/comment/delete")
    public void commentDelete(
            @RequestParam(value = "commu_num") long commu_num,
            @RequestParam(value = "commu_indent") int commu_indent
    ){
        if(commu_indent!=0){
            commentService.commentdw(commu_indent);
        }
        commentService.commentDelete(commu_num);
    }
}
