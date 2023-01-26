/*
* slideShow.js
 */

$(function(){
    //현재 이미지의 index값 저장변수 생성
    var moveIndex=0
    // prev버튼 클릭

    // 초기 슬라이더 위치 랜덤하게 지정
    // 이미지 인덱스를 랜덤하게 설정

    var randomNumber = Math.floor(Math.random()*5);
    moveSlide(randomNumber);
    function moveSlide(index){
        //전달받은 index값을 다른 변수에 저장
        moveIndex=index;
        //슬라이드 이동거리 계산
        var moveleft=-(index*1280)//왼쪽으로 이동거리
        $('#slidePanel').animate({'left':moveleft},'slow');
    }
    $('#prevButton').on('click',function () {
        // 현재이미지가 첫번째 이미지면 버튼반응을 안함
        // 첫번쨰 이미지가 아닐 경우 에만 버튼 작동
        if(moveIndex != 0) {// 첫번쨰가 아니라면
            // 현재 이미지의 인덱스-1한 인덱스 값을 이용해서 함수 호출
            moveIndex = moveIndex - 1;
            moveSlide(moveIndex);
        }
    });

    // next버튼 클릭
    $('#nextButton').on('click',function () {
        if(moveIndex != 4) { // 마지막이 아니라면
            moveIndex = moveIndex + 1;
            moveSlide(moveIndex);
        }
    });
    // 각 컨트롤 버튼에 대해
    $('.controlButton').each(function(index){
        $(this).hover(
            function () { // 마우스가 이미지에 올려지면
                $(this).attr('src','image/controlButton2.png');
            },
            function () { // 마우스가 이미지에 올려지면
                $(this).attr('src','image/controlButton1.png');
            }
        ); // hover끝
        // 클릭했을 때 현재 인덱스 값을 moveslide() 함수에 전달
        $(this).on('click',function(){
            moveSlide(index);
        });
    });
    // 3초마다 자동으로 슬라이드 이동
    setInterval(function(){
        if(moveIndex!=4) // 마지막 이미지가 아니면
            moveIndex = moveIndex+1;
        else // 마지막 이미지
            moveIndex = 0; // 첫번째 이미지로 설정
        moveSlide(moveIndex);
    },3000);
})

