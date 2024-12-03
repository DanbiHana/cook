package com.mbc.cook.controller;

import com.mbc.cook.entity.info.CategoryEntity;
import com.mbc.cook.entity.member.MemberEntity;
import com.mbc.cook.entity.recipe.CartEntity;
import com.mbc.cook.entity.recipe.IngreEntity;
import com.mbc.cook.entity.recipe.RecipeEntity;
import com.mbc.cook.service.info.InfoService;
import com.mbc.cook.service.recipe.RecipeService;
import com.mbc.cook.service.recipe.RecipeService2;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.*;

//규리
@Slf4j
@Controller
public class RecipeController {
    @Autowired
    RecipeService recipeService;
    @Autowired
    InfoService infoService;
    @Autowired
    RecipeService2 recipeService2;

    @GetMapping(value = "/recipe/select")
    public String recipeDetail(@RequestParam("num") long num, @RequestParam("path") String path, Model model) {
        RecipeEntity dto = recipeService.select(num);
        //재료 ID -> 정보 가져와서 저장
        String [] ing_arr = dto.getIngredient().split(",");
        ArrayList<IngreEntity> ingreList = new ArrayList<IngreEntity>();
        ingreList = parseIngredient(ingreList, ing_arr);

        List<CategoryEntity> recipeList = infoService.getSubCategoryList(dto.getCategory1()); //삭제/수정 시 소분류 불러오기
        model.addAttribute("recipeList", recipeList);model.addAttribute("ingreList", ingreList);//저장된 재료들 숫자 → 이름 변환
        model.addAttribute("dto",dto);

        if(path.equals("detail")){
            pathSet("상세페이지",path, model);
            recipeService.clickup(num);
        }else if(path.equals("update")){
            pathSet("레시피 수정",path, model);
            List<IngreEntity> ingreList2 = recipeService2.findIngredientAll();
            model.addAttribute("ingreList2",ingreList2);//모든 재료 불러오기
        }else if(path.equals("delete")){
            pathSet("레시피 삭제",path, model);
        }
        return (path.equals("detail")) ? "recipe/detail" : (path.equals("delete")) ? "recipe/delete" : "recipe/update";
    }
    @ResponseBody
    @PostMapping(value="/recipe/cartsave")
    public String cartSave(@RequestParam("id") String id, @RequestParam("ingredient") String ingredient) {
        try {
            long cart =recipeService.findCartByID(id,"cart");
            if (cart == 0) {
                recipeService.cartSave(id, ingredient);
            }else {
                recipeService.cartUpdate(id, ingredient);
            }
            return "장바구니에 담겼습니다";
        } catch (Exception e) {
            return "장바구니 저장 중 오류가 발생했습니다";
        }
    }

    @GetMapping(value = "/recipe/cart")
    public String recipeCart(@RequestParam("id") String id,@RequestParam(value = "status",required = false,defaultValue = "cart") String status, Model model) {
        pathSet("장바구니","cart", model);
        ArrayList<IngreEntity> list = new ArrayList<IngreEntity>();
        String ingredientArray = recipeService.selectIngredient(id,status);
        if(ingredientArray != null) {
            String[] ingredientNum = ingredientArray.split(",");
            list = parseIngredient(list, ingredientNum);

            Set<IngreEntity> set = new HashSet<IngreEntity>(list); //재료들 중복값 제거
            List<Integer> pickList = new ArrayList<>();
            for (IngreEntity str : set) {
                pickList.add(Collections.frequency(list, str));
            }
            List<IngreEntity> ingreList = new ArrayList<>(set); //리스트로 변환
            model.addAttribute("cartList",ingreList);
            model.addAttribute("picksize",pickList);
        }else{
            cartDelete(id, status);
        }
        return "recipe/cart";
    }

    @ResponseBody
    @PostMapping("/cart/ingreDelete")
    public String deleteIngredient(@RequestParam("ingredient") String ingredient, @RequestParam("id") String id){
        String ingredientArray = recipeService.selectIngredient(id,"cart");
        String [] ingreNum = ingredientArray.split(",");
            String deleteIngreString = "";
            for(int i=0; i<ingreNum.length; i++){
                if(!ingreNum[i].equals(ingredient)){
                    deleteIngreString+=ingreNum[i];
                    if(i!=ingreNum.length-1){deleteIngreString+=",";}
                }
            }
            recipeService.ingredientDelete(deleteIngreString,id);
        return "삭제되었습니다";
    }
    //장바구니 비우기
    @ResponseBody
    @PostMapping("/cart/delete")
    public void cartDelete(@RequestParam("id") String id,@RequestParam(value = "status",required = false,defaultValue = "cart") String status){
        recipeService.deleteCart(id, status);
    }
    //주소지 확인
    @ResponseBody
    @PostMapping("/cart/orderAddress")
    public String findAddress(@RequestParam("id") String id){
        return recipeService.findAddress(id);
    }

    @ResponseBody
    @PostMapping("/cart/order")
    public void order(@RequestParam("id") String id, @RequestParam("orderitem") String orderItem, @RequestParam("price") int price, @RequestParam("address") String address){
        recipeService.order(id,orderItem,price,address);
        System.out.println("id: "+id);
        System.out.println("orderItem: "+orderItem);
        System.out.println("price: "+price);
        System.out.println("address: "+address);
    }
    //주문내역
    @GetMapping("recipe/order")
    public String order(@RequestParam("id") String id, @RequestParam(value = "status",required = false,defaultValue = "cart") String status, Model model){
        pathSet("주문 내역","cart", model);
        if(id.equals("admin")||id.equals("ADMIN")){
            List<CartEntity> list = recipeService.orderlistall(status);
            model.addAttribute("orderlist",list);
        }else{
            List<CartEntity> list = recipeService.orderlist(id, status);
            model.addAttribute("orderlist",list);
        }
        return "recipe/order";
    }
    @GetMapping("recipe/order/detail")
    public String orderDetail(){

        return "recipe/orderDetail";
    }

    @ResponseBody
    @PostMapping("/order/ingredientList")
    public String [] orderIngredientList(@RequestParam("id") long id){
        String ingredientString = recipeService.selectListIngredient(id,"order");
        String [] ingreEach = ingredientString.split(",");
        String [] list = new String[ingreEach.length];
        for(int i =0; i<ingreEach.length; i++){
            String [] ingreNum = ingreEach[i].split("x");
            IngreEntity ige = parseIngredient(ingreNum[0]);
            list[i] = ige.getIngre_seq()+"@"+ige.getName()+"@"+ige.getPrice()+"@"+ingreNum[1];
            System.out.println(i+": "+list[i]);
        }
        return list;
    }

    public void pathSet(String title,String path, Model model){
        model.addAttribute("cssPath", "/recipe/"+path);//css 패스 경로(바꾸지X)
        model.addAttribute("pageTitle", title);//타이틀 제목
    }
    public ArrayList<IngreEntity> parseIngredient(ArrayList<IngreEntity> list, String [] ing_arr){
        for (String s : ing_arr) {
            list.add(parseIngredient(s));
        }
        return list;
    }
    public IngreEntity parseIngredient(String s){
            return recipeService.findIngredientByID(Long.parseLong(s));
    }
}
