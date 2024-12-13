let win_href = window.location.href;//페이지 전체 경로
let win_path = window.location.pathname;//페이지 이름 경로
let win_search = window.location.search;//페이지 ?a=b에 대한 경로

//주소 API CDN 방식 사용
function execDaumPostcode(){
    new daum.Postcode({
        oncomplete: function(data){
            // 팝업을 통한 검색 결과 항목 클릭 시 실행
            var addr = ''; // 주소_결과값이 없을 경우 공백
            var extraAddr = ''; // 참고항목
            //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
            if (data.userSelectedType === 'R'){ // 도로명 주소를 선택
                addr = data.roadAddress;
            } else{ // 지번 주소를 선택
                addr = data.jibunAddress;
            }
            if(data.userSelectedType === 'R'){
                if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                    extraAddr += data.bname;
                }
                if(data.buildingName !== '' && data.apartment === 'Y'){
                    extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                }
                if(extraAddr !== ''){
                    extraAddr = ' (' + extraAddr + ')';
                }
            } else{
                document.getElementById("streetaddr").value = '';
            }
            // 선택된 우편번호와 주소 정보를 input 박스에 넣는다.
            document.getElementById('addr').value = data.zonecode;
            document.getElementById("streetaddr").value = addr;
            document.getElementById("streetaddr").value += extraAddr;
            document.getElementById("detailaddr").focus(); // 우편번호 + 주소 입력이 완료되었음으로 상세주소로 포커스 이동
        }
    }).open();
}
//비밀번호 일치 유무
function passwordCheck(){
    var pw = $("#pw").val();
    var pwcheck = $("#pwcheck").val();
    var pw_message = document.getElementById("pw_message");	//확인 메세지
    var correctColor = "#3d7797";	//맞았을 때 출력되는 색깔.
    var wrongColor = "#bb0000";		//틀렸을 때 출력되는 색깔
    if(pw == pwcheck){ //password 변수의 값과 passwordConfirm 변수의 값과 동일하다.
        if(pw.length<6 ||pw.length>16){
            pw_message.style.color = wrongColor;
            pw_message.innerHTML = "비밀번호는 6~16자 이내로 입력해주세요.";
        }
        else{
            pw_message.style.color = correctColor;/* span 태그의 ID(confirmMsg) 사용  */
            pw_message.innerHTML = " 비밀번호가 일치합니다.";/* innerHTML : HTML 내부에 추가적인 내용을 넣을 때 사용하는 것. */
        }
    }else{
        pw_message.style.color = wrongColor;
        pw_message.innerHTML = " 비밀번호가 일치하지 않습니다.";
    }
}
function pageReload(){
    location.reload(true);
}