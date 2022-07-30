<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>학보사 홍보이미지 생성기</title>
        <style>
            .generator{
                max-width: 500px;
                width: 80%;
                margin: 10px auto;
            }
            .generator div{
                margin: 10px 0;
            }
            .generator div input{
                width: calc(100% - 76px);
            }
            #submitBtn{
                width: 70px;
                text-align: center;
                height: 30px;
                background-color: #00AAFF;
                border: 0;
                border-radius: 5px;
                margin: 15px calc(50% - 35px);
                color: white;
            }
        </style>
    </head>
    <body>
        <h2 style="text-align: center; width: 100%">가톨릭대학보사 홍보이미지 생성기</h2>
        <div class="generator">
            <form action="make_image.php" method="post">
                <div>
                    <label for="lastDate">종료일자</label>
                    <input type="date" name="lastDate" id="lastDate" required>
                </div>
                <div>
                    <label for="totalDate">탐색일수</label>
                    <input type="number" name="totalDate" id="totalDate" required>
                </div>
                <div>
                    <input type="submit" id="submitBtn" value="생성">
                </div>
            </form>
            <p style="margin-top:30px; font-size: 0.75em; text-align: center">탐색일수는 종료일자 1일 전부터 계산됩니다.<br>(예시) 종료일자 3월 20일 & 탐색일수 3일 : 3월 17~19일 탐색<br><b>기사개수가 1개 이하인 구간은 오류발생<br>기사개수가 4개 이상인 구간은 최근 기사 4개만 출력</b></p>
            <p style="margin-top:20px; font-size: 0.75em; text-align: center">개발자 : 조현우 & 안창영<br>오류 발생시 010-8868-3897로 연락 바랍니다.</p>
        </div>
    </body>
</html>