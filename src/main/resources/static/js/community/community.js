//리스트 페이지에서 상세보기 페이지로 넘어가기
function goToDetail(communityNum) {
    location.href = "/community/detail?num="+communityNum;
}

//상세보기 페이지에서 수정창으로 이동
function goToUpdate() {
    confirmShow('게시물 수정','수정하시겠습니까?','commu_update');
}

//상세보기 페이지에서 confirm창으로 삭제하기
function goToDelete() {
    confirmShow('게시물 삭제','정말로 삭제하시겠습니까?<br>삭제하면 되돌릴 수 없습니다.','commu_delete');
}
function confirmOk(value){
    //삭제
    if(value == 'commu_delete'){
        var commu_num = $('#commu_num').val();
        location.href = '/community/delete?num='+commu_num;
        return alertShow('삭제 확인','삭제되었습니다.');
    }
    //수정
    else if(value == 'commu_update'){
            var commu_num = $('#commu_num').val();
            location.href = '/community/update?num='+commu_num;
            console.log("받은 번호 : "+commu_num);
    }
}

//상세보기 페이지 댓글달기
function goToComment(communityNum) {
    var comment = $('#plusComment').val();
    var id = $('#commu_id').val();
    console.log("받아온 글번호 : "+communityNum);
    console.log("받아온 아이디 : "+id);
    console.log("받아온 댓글 : "+comment);
    if(comment == "" || comment == null) {
        alertShow('댓글 작성 오류','댓글을 입력해주세요.');
    }
    else {
        location.href = "/community/commentRegister?num="+communityNum+"&id="+id+"&comment="+comment;
    }
}

//공지사항 더보기 토글
function adminReadMore(object){
    var object_val = object.dataset.type;
    if(object_val == 'off'){
        $('#admin_readmore').text('공지 숨기기');
        $('#admin_readmore').attr('data-type', 'on');
        $('.admin_inner').css('height', 'auto');
    }
    else{
        $('#admin_readmore').text('공지 더보기');
        $('#admin_readmore').attr('data-type', 'off');
        $('.admin_inner').css('height', '132px');
    }
}