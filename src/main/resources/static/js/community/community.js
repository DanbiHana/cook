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
    //글 삭제
    if(value == 'commu_delete'){
        var commu_num = $('#commu_num').val();
        location.href = '/community/delete?num='+commu_num;
        return alertShow('삭제 확인','삭제되었습니다.');
    }
    //글 수정
    else if(value == 'commu_update'){
        var commu_num = $('#commu_num').val();
        location.href = '/community/update?num='+commu_num;
    }
    //댓글 삭제
    else if(value == 'comment_delete'){
        var commu_num = $('#comment_num').val();
        var commu_type = $('#comment_type').val();
        var commu_indent = $('#comment_indent').val();
        commentDelete(commu_num,commu_type,commu_indent);
    }

}

//상세보기
//댓글달기
function sendComment(communityNum) {
    var comment = $('#comment_content').val();
    if(comment == "" || comment == null) {
        alertShow('댓글 작성 오류','댓글을 입력해주세요.');
    }
    else {
        $.ajax({
            url: "/comment/register",
            type: "post",
            async: true,
            data: {
                "num":communityNum,
                "comment":comment
            },
            success:function(data){
                alertShow("댓글 저장", "댓글 저장되었습니다.");
                $('.btn_confirm').attr('onclick','pageReload()');
            },
            error:function(){
                alertShow("에러","다시 시도해주세요.");
            }
        });
    }
}
//댓글 수정
function commentChange(object){
    var ths_type = object.dataset.type;
    var ths_id = object.dataset.id;
    var ths_seq = object.dataset.seq;
    var content = $('#'+ths_id).val();
    if(ths_type == 'off'){
        $('#'+ths_id).prev('p').hide();
        $('#'+ths_id).attr('readonly', false);
        $('#'+ths_id).attr('hidden', false);
        $('#'+ths_id).next('.comment_btn').find('.comment_update').attr('data-type', 'on');
        $('#'+ths_id).next('.comment_btn').find('.comment_update').text('수정 완료');
    }else if(ths_type == 'on'){
        $.ajax({
            url: "/comment/update",
            type: "post",
            async: true,
            data: {
                "content":content,
                "seq":ths_seq
            },
            success:function(data){
                alertShow("댓글 수정", "댓글이 수정되었습니다.");
                $('.btn_confirm').attr('onclick','pageReload()');
            },
            error : function(jqXHR, textStatus, errorThrown) {
                const responseText = JSON.parse(jqXHR.responseText);
                console.log("에러 발생\nException : " + responseText.exception);
                alertShow('오류 발생', '잠시만 기다려주세요.');
            }
        });
    }
}
//댓글 삭제
function commentDeleteChk(ths){
    var ths_seq = ths.dataset.seq;
    var ths_type = ths.dataset.type;
    var ths_indent = ths.dataset.indent;
    confirmShow('삭제 확인', '정말 삭제하시겠습니까?', 'comment_delete');
    $('#comment_num').val(ths_seq);
    $('#comment_type').val(ths_type);
    $('#comment_indent').val(ths_indent);
}
function commentDelete(commu_num,commu_type,commu_indent){
    $.ajax({
        url: "/comment/delete",
        type: "post",
        async: true,
        data: {
            "commu_num":commu_num,
            "commu_type":commu_type,
            "commu_indent":commu_indent
        },
        success:function(data){
            alertShow("댓글 삭제", "댓글이 삭제되었습니다.");
            $('.btn_confirm').attr('onclick','pageReload()');
        },
        error : function(jqXHR, textStatus, errorThrown) {
            const responseText = JSON.parse(jqXHR.responseText);
            console.log("에러 발생\nException : " + responseText.exception);
            alertShow('오류 발생', '잠시만 기다려주세요.');
        }
    });
}
//(대)댓글달기
function sendComment(ths) {
    var ths_type = ths.dataset.type;
    var ths_commu = ths.dataset.commu;
    var ths_comment = ths.dataset.comment;
    var comment;
    var comdata;
    if(ths_type == 'comment'){
        comment = $('#comment_content').val().trim();
        comdata = {"commu_num":ths_commu,"comment_num":0,"comment":comment};
    }else{
        comment = $('#recomment'+ths_comment).val().trim();
        comdata = {"commu_num":ths_commu,"comment_num":ths_comment,"comment":comment};
    }
    if(comment == "" || comment == null) {
        alertShow('댓글 미입력','댓글을 입력해주세요.');
    }
    else {
        $.ajax({
            url: "/comment/register",
            type: "post",
            async: true,
            data: comdata,
            success:function(data){
                alertShow("댓글 저장", "댓글 저장되었습니다.");
                $('.btn_confirm').attr('onclick','pageReload()');
            },
            error:function(){
                alertShow("에러","다시 시도해주세요.");
            }
        });
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