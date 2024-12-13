package com.mbc.cook.repository.recipe;

import com.mbc.cook.entity.member.MemberEntity;
import com.mbc.cook.entity.recipe.CartEntity;
import jakarta.transaction.Transactional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CartRepository extends JpaRepository<CartEntity, String> {
    @Transactional
    @Query(value = "select NVL(count(cart_seq),0) from cart where id = :id and status = :status ", nativeQuery = true)
    long findId(@Param("id") String id,@Param("status") String status);

    @Transactional
    @Modifying
    @Query(value = "insert into cart (cart_seq, id, order_item, status) values (cart_seq.nextval, :id, :ingredient, 'cart')",nativeQuery = true)
    void save(@Param("id") String id, @Param("ingredient") String ingredient);

    @Transactional
    @Modifying
    @Query(value = "update cart " +
            "set order_item = order_item || ',' || :ingredient " +
            "where id = :id and status='cart'", nativeQuery = true)
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

    @Transactional
    @Modifying
    @Query(value = "delete from cart where id = :id and status = :status",nativeQuery = true)
    void deleteCart(@Param("id") String id, @Param("status") String status);

    @Transactional
    @Query(value = "select addr || '+' || streetaddr || '+' || detailaddr from usermember where id = :id",nativeQuery = true)
    String findAddress(@Param("id") String id);

    @Transactional
    @Modifying
    @Query(value = "update cart set price = :price, order_item = :orderItem, address = :address, status='order', orderdate = sysdate " +
            "where id = :id and status='cart'",nativeQuery = true)
    void order(@Param("id") String id, @Param("orderItem") String orderItem, @Param("price") int price, @Param("address") String address);

    @Transactional
    @Query(value = "select * from cart where id = :id and status = :status order by orderdate desc",nativeQuery = true)
    List<CartEntity> orderlist(@Param("id") String id, @Param("status") String status);

    @Transactional
    @Query(value = "select * from cart where status = :status order by orderdate desc",nativeQuery = true)
    List<CartEntity> orderAll(@Param("status") String status);


    @Transactional
    @Query(value = "select order_item " +
            "from cart " +
            "where cart_seq=:id and status=:status",nativeQuery = true)
    String findingrebyid(@Param("id") long id, @Param("status") String status);
}
