html = """
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Insert title here</title>
  </head>
<body>
  <form>
    <!-- 서버로 메시지를 보낼 텍스트 박스 -->
    <input id="textMessage" type="text">
    <!-- 전송 버튼 -->
    <input onclick="sendMessage()" value="Send" type="button">
    <!-- 접속 종료 버튼 -->
    <input onclick="disconnect()" value="Disconnect" type="button">
  </form>
  <br />
  <!-- 출력 area -->
  <textarea id="messageTextArea" rows="10" cols="50"></textarea>
  <script type="text/javascript">
    // 웹 서버를 접속한다.
    var webSocket = new WebSocket("ws://localhost:8000/chat");
    // 웹 서버와의 통신을 주고 받은 결과를 출력할 오브젝트를 가져옵니다.
    var messageTextArea = document.getElementById("messageTextArea");
    // 소켓 접속이 되면 호출되는 함수
    webSocket.onopen = function(message){
      messageTextArea.value += "Server connect...\n";
    };
    // 소켓 접속이 끝나면 호출되는 함수
    webSocket.onclose = function(message){
      messageTextArea.value += "Server Disconnect...\n";
    };
    // 소켓 통신 중에 에러가 발생되면 호출되는 함수
    webSocket.onerror = function(message){
      messageTextArea.value += "error...\n";
    };
    // 소켓 서버로 부터 메시지가 오면 호출되는 함수.
    webSocket.onmessage = function(message){
      // 출력 area에 메시지를 표시한다.
      messageTextArea.value += "Recieve From Server => "+message.data+"\n";
    };
    // 서버로 메시지를 전송하는 함수
    function sendMessage(){
      var message = document.getElementById("textMessage");
      messageTextArea.value += "Send to Server => "+message.value+"\n";
      //웹소켓으로 textMessage객체의 값을 보낸다.
      webSocket.send(message.value);
      //textMessage객체의 값 초기화
      message.value = "";
    }
    function disconnect(){
      webSocket.close();
    }
  </script>	
</body>	
</html>
"""
