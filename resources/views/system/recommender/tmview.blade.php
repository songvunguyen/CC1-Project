@extends('system.layouts.header')
@section('css')
<link href="{{ asset('jscss/dropzone/dropzone.css') }}" rel="stylesheet">
<!-- Style sheet for the Chatbot -->
<link rel="stylesheet"  href="{{ asset('jscss/custom/chatbot/chatbot.css') }}">
<!-- end of style sheet for ChatBot -->
@endsection


@section('content')
<section class='bg-light'>
<div class="container">


<script>
function output(){
	//https://www.w3schools.com/php/php_ajax_php.asp
    //https://stackoverflow.com/questions/24468459/sending-a-json-to-server-and-retrieving-a-json-in-return-without-jquery
	//https://stackoverflow.com/questions/18441375/submit-form-field-values-to-a-javascript-function
    var xmlhttp = new XMLHttpRequest();
    var input = document.getElementById("input").value;
	xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("output").innerHTML = this.responseText;
            }
        };
        var text = JSON.stringify({"text": input});
        xmlhttp.open("POST", "http://localhost:9000/api/topics", true);
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        xmlhttp.send(text);
}
</script> 
<!-- <script>
function output(){
    var input = document.getElementById("input").value;
    var text = JSON.stringify({"text": input});
    document.getElementById("input").value = text;
    document.getElementById("myForm").submit();
}
</script> -->

<form method="POST" action="http://localhost:9000/api/topics" id="myForm">
<!--https://www.w3schools.com/html/html_forms.asp-->
<p>Input:</p>
<input type="text" name="input" id="input">
<input type="button" value="Get output" onclick="output()">
</form>

<!-- @php
    $outputV = file_get_contents("http://localhost:9000/");
@endphp -->
</br>
<p>Output</p>
<span id="output"></span>



</div>
</section>
@endsection
