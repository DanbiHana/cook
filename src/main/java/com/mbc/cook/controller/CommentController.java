package com.mbc.cook.controller;

import com.mbc.cook.dto.community.CommentDTO;
import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.service.community.CommentService;
import jakarta.persistence.Column;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;

@RestController
public class CommentController {

    @Autowired
    CommentService commentService;

    @GetMapping(value = "/commentRegister")
    public String commentResister(Model model, @RequestParam("num") int num, @RequestParam("id") String id, @RequestParam("comment") String comment, CommentDTO commentDTO) {
        model.addAttribute("cssPath", "/community/detail");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "커뮤니티 상세");//타이틀 제목
        //댓글 저장
        commentDTO.setCommentId(id);
        commentDTO.setCommentContent(comment);
        LocalDateTime present = LocalDateTime.now();
        commentDTO.setCommentDate(present);
        commentDTO.setCommentUpdateDate(present);
        commentDTO.setCommunityNum(num);
        commentDTO.setIndent(0);
        commentDTO.setStep(0);
        System.out.println("받아온 아이디 : "+commentDTO.getCommentId());
        CommentEntity commententity = commentDTO.commentEntity();
        commentService.insertcomment(commententity);
        return "redirect:/community/detail?num="+num;
    }
}
