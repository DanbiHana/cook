package com.mbc.cook.controller;

import com.mbc.cook.entity.community.CommunityEntity;
import com.mbc.cook.entity.recipe.RecipeEntity;
import com.mbc.cook.service.home.HomeInterface;
import com.mbc.cook.service.home.HomeService;
import com.mbc.cook.service.recipe.RecipeService2;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Slf4j
@Controller
public class HomeController {
    @Autowired
    RecipeService2 recipeService2;
    @Autowired
    HomeService homeService;

    @GetMapping(value = "/")
    public String index(Model model, @AuthenticationPrincipal UserDetails userDetails) {
        String username = userDetails.getUsername();
        List<RecipeEntity> recipeList = recipeService2.recipeFindAll();
        List<CommunityEntity> commulist = homeService.findCommuFive();
        List<CommunityEntity> commulist2 = homeService.findCommuFive2();
        HomeInterface communum = homeService.countCommu(username);
        HomeInterface comentnum = homeService.countComment(username);
        model.addAttribute("cssPath", "/home/index");//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", "메인");//타이틀 제목
        model.addAttribute("recipeList", recipeList);//레시피
        model.addAttribute("commuAdmin", commulist);//공지사항
        model.addAttribute("commuOther", commulist2);//자유게시판
        model.addAttribute("commuLen", communum.getCommuCount());//글 갯수
        model.addAttribute("commentLen", comentnum.getCommentCount());//글 갯수
        return "home/index";
    }
}
