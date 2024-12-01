package com.mbc.cook.repository.recipe;

import com.mbc.cook.entity.recipe.CartEntity;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CartRepository extends JpaRepository<CartEntity, Long> {
    @Transactional
    @Query(value = "select NVL(cart_seq,-1) from cart where id = :id", nativeQuery = true)
    long findId(@Param("id") String id);

    @Transactional
    @Modifying
    @Query(value = "insert into cart (cart_seq, id, order_item, status) values (cart_seq.nextval, :id, :ingredient, 'orderprev')",nativeQuery = true)
    void save(@Param("id") String id, @Param("ingredient") String ingredient);

    @Transactional
    @Modifying
    @Query(value = "update cart " +
            "set order_item = order_item || ',' || :ingredient " +
            "where id = :id", nativeQuery = true)
    void update(@Param("id") String id, @Param("ingredient") String ingredient);

    @Transactional
    @Query(value = "select order_item " +
            "from cart " +
            "where id=:id and status=:status",nativeQuery = true)
    String selectIngredient(@Param("id") String id, @Param("status") String status);

    @Transactional
    @Modifying
    @Query(value = "update cart set order_item= :ingreString where id = :id",nativeQuery = true)
    void deleteIngredient(@Param("ingreString") String ingreString, @Param("id") String id);

}
