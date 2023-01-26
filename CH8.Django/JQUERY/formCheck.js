// formCheck
// 회원가입 폼 입력 유효성 확인
$(document).ready(function(){
    // 문서 로드후 id 입력창에 포커스
    $('#id').focus();

    //아이디와 비밀번호 입력란에 포커스가 있을 때 배경 색상 변경
    // focus blur 이벤트
    $('input[type="text"],input[type="password"]').on('focus',function(){
       $(this).css('background','rgb(232,232,232)');
    });
    // 아이디와 비밀번호 입력란에 포커스가 없어지면 배경 색상 변경
    $(':text,:password').on('blur',function (){
        $(this).css('background','rgb(255,255,255)');
    })

    // 키보드 이벤트 - 휴대폰 입력란에서 입력 값 개수 확인
    // 첫번째 번호 입력란에서 입력값이 3개가 되면 포커스 이동
    $('#hp1').on('keyup',function () {
       if($(this).val().length==3){
           $('#hp2').focus();
       }
    });
    // 키보드 이벤트 - 휴대폰 입력란에서 입력 값 개수 확인
    // 첫번째 번호 입력란에서 입력값이 3개가 되면 포커스 이동
    $('#hp2').on('keyup',function () {
       if($(this).val().length==4){
           $('#hp3').focus();
       }
    });
    
    // submit 이벤트 : submit 버튼 클릭 시 발생, form태그(input)위에서 enter키 누르변 발생
    // enter키를 눌렀을 때 무조건 submit 안되도록
    // 문서 전체에 이벤트 처리
    // [Enter]키의 아스키코드값 : 13
    $(document).on('keydown',function (e) {
        if(e.keyCode==13) return false;
        })
    // id 입력 후 엔터키 눌렀을 때 비밀번호 포커스 이동
    $('#id').on('keydown',function (e) {
        if($('#id').val()!="" && e.keyCode==13)
            $('#pwd').focus();
    })


    // 회원가입 폼 입력 유효성을 확인하는 시점- 전송버튼
    // submit버튼은 폼객체에서 발생하는 이벤트
    $('#newMemberForm').on('submit',function(){
      if($('#id').val()=="") {
          alert('아이디를 입력하세요.');
          $('#id').focus();
          return false;
      }

      if($('#pwd').val()==''){
          alert('비밀번호를 입력하세요.');
          $('#pwd').focus();
          return false;
      }

      if(!$('input[type="radio"]').is(':checked')){ //라디오버튼(학년) 선택하지 않은 경우
          alert('학년을 선택하세요.');
          return false;
      }
    if(!$('input[type="checkbox"]').is(':checked')) {
        alert('관심분야는 1개 이상 선택하세요.');
        return false;
    }
    if($('select').val()==''){
          alert('학과를 선택하세요.');
          $('select').focus();
          return false;
      }
    });

});


