package com.mbc.cook.repository.recipe;

import com.mbc.cook.entity.recipe.IngreEntity;
import com.mbc.cook.entity.recipe.RecipeEntity;
import com.mbc.cook.service.recipe.RecipeInterface;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Repository
public interface IngreRepository extends JpaRepository<IngreEntity, Long> {
    @Override
    List<IngreEntity> findAll();

    @Transactional
    @Modifying
    @Query(value = "select ingre_seq, name, price, keyword from ingredient where keyword=:ingredient", nativeQuery = true)
    List<IngreEntity> findIngredient(@Param(value = "ingredient") String ingredient);

    @Transactional
    @Modifying
    @Query(value = "select ingre_seq, name, price, keyword from ingredient " +
            "WHERE (name LIKE %:ingredient%) " +
            "OR (keyword LIKE %:ingredient%)", nativeQuery = true)
    List<IngreEntity> findIngredientLike(@Param(value = "ingredient") String ingredient);

}
