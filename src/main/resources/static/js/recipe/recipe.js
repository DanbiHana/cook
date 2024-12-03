//규리
function confirmOk(object){
    var id =$('#id').val();
    if(object=='cartOk'){
        var length = $("input[name='ingredient']:checked").length;
        var ingredient = "";
        if(length > 1){
            $("input[name='ingredient']:checked").each(function(index){
                var value = $(this).val();
                if(length-1 == index){
                    ingredient += value;
                }else{
                    ingredient += value + ",";
                }
            });
        }
        $.ajax({
            url:"/recipe/cartsave",
            type:"post",
            async:"true",
            data:{"id":id,"ingredient":ingredient},
            success:function(data){
                confirmShow(data,"","cartgo");
                $('.btn_hide').text("확인");
                $('#pop_confirm_btn').text("장바구니로 가기");
            },
            error:function(){alertShow("에러","");}
        });
    }
    if(object == 'cartgo'){
        location.href="/recipe/cart?id="+id;
    }
    if(object == 'cartClear'){
        var id =$('#id').val();
        $.ajax({
          url:"/cart/delete",
          type:"post",
          async:"true",
          data:{"id":id},
          success:function(data){
             setTimeout(function(){
                $('.btn_hide').hide();
                confirmShow("장바구니가 비워졌습니다.","","reloadok");},600);
          },
          error:function(){alertShow("에러","");}
        });
    }
    if(object == 'reloadok'){
        location.reload();
    }
}
//장바구니 요약 창 구성
function summary(){
    var sum=0;
    var delivery;
    $('input[name="total"]').each(function(index){
        sum += parseInt($(this).val());
    });
    if(sum > 50000 || sum == 0){delivery=0;}
    else{delivery=3000;}

    var tot = sum + delivery;
    $('#tot').text(addCommas(sum));
    $('#delivery').text(addCommas(delivery));
    $('#total').text(addCommas(tot));
}
//총액 표기
function tot(a){
    var num = $('#num'+a).val();
    var price = $('#eachprice'+a).val();
    var tot = num * price;
    $('#total'+a).val(tot);
    $('#totChange'+a).text(addCommas(tot));
    summary();
    orderItem(); //주문내용 변경
}
function addCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function orderItem(){
    var len = $('#listSize').val();
    var text="";
    $('input[name="ingreid"]').each(function(index){
        var id = $(this).val();
        text += id + "x"+ $('#num'+id).val();
        if(index != len-1){text += ",";}
    });
    $('#order_item').val(text);
}
//재료 삭제
function deleteIngredient(ingreNum){
    var id = $('#id').val();
    $.ajax({
        url:"/cart/ingreDelete",
        type:"post",
        async:"true",
        data:{"ingredient":ingreNum, "id":id},
        success:function(data){
            standbyShow("삭제 중입니다","");
            setTimeout(function(){
            location.reload();}, 500);
       },
       error:function(){alertShow("에러","");}
   });
}
//카트 비우기
function deleteCart(){
    confirmShow("장바구니를 비우시겠습니까?","","cartClear");
}
//주문 전 주소 확인
function address(){
    var id = $('#id').val();
    addrCheck(id);
}
$(document).ready(function(){
    if(win_href.includes("recipe/select") && win_search.includes("path=detail")){
        var recipe = $('#recipe').val().split("<br>");
        var recipe_div = "";
        for (var i in recipe){
            recipe_div += "<div class='recipeProcess'>"
            recipe_div +=   "<p>"+ (Number(i)+1) +"</p><input type='text' id='recipeProcess_"+i+"' name='recipeProcess_"+i+"' value='"+recipe[i]+"' readonly>";
            recipe_div += "</div>";
        }
        $('#recipeProcess').append(recipe_div);

        $('#cartClick').click(function(){
            confirmShow("해당 상품들을 장바구니에 담으시겠습니까?","","cartOk");
        });
    }
    if(win_href.includes("recipe/cart")){
        summary();
        orderItem();
    }
});
