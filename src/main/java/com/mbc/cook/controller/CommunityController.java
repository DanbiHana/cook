package com.mbc.cook.controller;

import com.mbc.cook.dto.community.CommunityDTO;
import com.mbc.cook.entity.community.CommentEntity;
import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.service.community.CommentInterface;
import com.mbc.cook.service.community.CommunityService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import java.time.LocalDateTime;
import java.util.List;

//민성
@Slf4j
@Controller
@RequestMapping(value = "/community")
public class CommunityController {

    @Autowired
    CommunityService communityService;

//    @Autowired
//    CommentService commentService;


    @GetMapping(value = "/list")
    public String communityList(Model model, @RequestParam(required = false, defaultValue = "0", value = "page")int page) {
        model.addAttribute("cssPath", "/community/list");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "커뮤니티");//타이틀 제목
        List<CommunityEntity> adminList = communityService.adminList();
        // 페이징 처리
        Page<CommunityEntity> otherList = communityService.otherList(page);
        int totalPage = otherList.getTotalPages();
        int nowpage = otherList.getPageable().getPageNumber();//현재페이지//
        model.addAttribute("adminList",adminList);
        model.addAttribute("nowpage",nowpage);
        model.addAttribute("otherList",otherList.getContent());
        model.addAttribute("totalPage",totalPage);
        //
        return "community/list";
    }

    @GetMapping(value = "/register")
    public String communityRegister(CommunityDTO communityDTO, Model model) {
        model.addAttribute("cssPath", "/community/register");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "커뮤니티 등록");//타이틀 제목
        model.addAttribute("communityDTO", new CommunityDTO());//유효성 검사
    return "community/register";
    }
    //게시물 등록
    @PostMapping(value = "/save")
    public String communitySave(@ModelAttribute ("communityDTO") @Valid CommunityDTO communityDTO, BindingResult bindingResult) {
        if(bindingResult.hasErrors())
        {
            return "community/register";
        }
        else
        {
            LocalDateTime present = LocalDateTime.now();
            communityDTO.setCommunityDate(present);
            communityDTO.setCommunityUpdateDate(present);
            communityDTO.setCommunityReadcnt(0);

            CommunityEntity centity = communityDTO.communityEntity();
            communityService.insertcommunity(centity);
        }
        return "redirect:/community/list";
    }

    @GetMapping(value = "/update")
    public String communityUpdate(Model model, @RequestParam("num") long num) {
        model.addAttribute("cssPath", "/community/update");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "커뮤니티 수정");//타이틀 제목
        CommunityEntity communityEntity = communityService.getCommunity(num);//시퀀스에 해당하는 정보 가져오기
        model.addAttribute("communityUpdate",communityEntity);//정보를 수정창으로 보내기
        return "community/update";
    }

    //게시물 수정
    @PostMapping(value = "/updateSave")
    public String communityUpdateSave(HttpServletRequest request, @ModelAttribute ("communityDTO") @Valid CommunityDTO communityDTO, BindingResult bindingResult) {
        if(bindingResult.hasErrors())
        {
            return "community/update";
        }
        else
        {
            long num = Long.parseLong(request.getParameter("communityNum"));
            String title = request.getParameter("communityTitle");
            String content = request.getParameter("communityContent");
            LocalDateTime update_date = LocalDateTime.now();

            communityService.updateCommunity(num, title, content, update_date);
        }
        return "redirect:/community/list";
    }

    @GetMapping(value = "/delete")
    public String communityDelete(@RequestParam("commu_num") long commu_num) {
        communityService.deleteCommunity(commu_num);//게시물 삭제
        communityService.deleteAllComment(commu_num);//해당 게시글의 댓글 삭제
        return "redirect:/community/list";
    }

    @GetMapping(value = "/detail")
    public String communityDetail(Model model, @RequestParam("num") long num) {
        model.addAttribute("cssPath", "/community/detail");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "커뮤니티 상세");//타이틀 제목
        communityService.readcntUp(num);//조회수 증가
        CommunityEntity communityEntity = communityService.getCommunity(num);//시퀀스에 해당하는 정보 가져오기
        model.addAttribute("community",communityEntity);
        //댓글 리스트
        List<CommentEntity> commentList = communityService.getComment(num);
        model.addAttribute("commentList",commentList);
        //대댓글 리스트
        List<CommentEntity> recommentList = communityService.getRecomment(num);
        model.addAttribute("recommentList",recommentList);
        return "community/detail";
    }
}
