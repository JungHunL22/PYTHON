/**
 * subMenu.js
 */

// [전체보기] 메뉴 클릭했을 떄 모든 메뉴항목이 보이게

// $(function(){
//     // [전체보기] 메뉴 클릭했을 때
//     $('#showAllmenu').on('click',function(){
//         if($(this).text()=='전체보기 ▼'){
//             // subMenuBox 보이게
//             $('#subMenuBox').css('visibility','visible');
//             $(this).text('메뉴닫기 ▲').css('color','blue')
//         }  else{
//             // subMenuBox 안보이게
//             $('#subMenuBox').css('visibility','hidden');
//              $(this).text('전체보기 ▼').css('color','black')
//         }
//     }); //click 끝
// }); // ready 끝
$(function(){
    //[전체보기] 메뉴 클릭했을때
    $('#showAllMenu').on('click',function(){
        if($(this).text()=='전체보기 ▼'){
            //subMenuBox 보이게
            $('#subMenuBox').css('visibility','visible');
            $(this).text('메뉴닫기 ▲').css('color','blue')
        } else {
            //subMenuBox 안 보이게
            $('#subMenuBox').css('visibility','hidden');
            $(this).text('전체보기 ▼').css('color','black')
        }
    }); //click 끝
});  //ready 끝
