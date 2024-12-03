package com.mbc.cook.service.recipe;

import com.mbc.cook.entity.recipe.CartEntity;
import com.mbc.cook.entity.recipe.IngreEntity;
import com.mbc.cook.entity.recipe.RecipeEntity;
import com.mbc.cook.repository.recipe.CartRepository;
import com.mbc.cook.repository.recipe.IngreRepository;
import com.mbc.cook.repository.recipe.RecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RecipeImplement implements RecipeService {
    @Autowired
    RecipeRepository recipeRepository;
    @Autowired
    IngreRepository ingreRepository;
    @Autowired
    CartRepository cartRepository;

    @Override
    public RecipeEntity select(long num) {
        return recipeRepository.findById(num).orElse(null);
    }

    @Override
    public void clickup(long num) {recipeRepository.clickup(num);}

    @Override
    public IngreEntity findIngredientByID(long num) { return ingreRepository.findById(num).orElse(null); }

    @Override
    public long findCartByID(String id, String status) {
        return cartRepository.findId(id, status);
    }

    @Override
    public void cartSave(String id, String ingredient) {
        cartRepository.save(id, ingredient);
    }

    @Override
    public void cartUpdate(String id, String ingredient) {
        cartRepository.update(id,ingredient);
    }

    @Override
    public String selectIngredient(String id,String status) {
        return cartRepository.selectIngredient(id,status);
    }

    @Override
    public void ingredientDelete(String ingreString, String id) {
        cartRepository.deleteIngredient(ingreString, id);
    }
    @Override
    public void deleteCart(String id,String status) {
        cartRepository.deleteCart(id, status);
    }
    @Override
    public String findAddress(String id) {
        return cartRepository.findAddress(id);
    }
    @Override
    public void order(String id, String orderItem, int price, String address) {
        cartRepository.order(id, orderItem, price, address);
    }

    @Override
    public List<CartEntity> orderlist(String id,String status) {
        return cartRepository.orderlist(id,status);
    }

    @Override
    public List<CartEntity> orderlistall(String status) {
        return cartRepository.orderAll(status);
    }

    @Override
    public String selectListIngredient(long id, String status) {
        return cartRepository.findingrebyid(id,status);
    }

}
