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

<!-- 
<script>
function output(input){
	//https://www.w3schools.com/php/php_ajax_php.asp
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("output").innerHTML = this.responseText;
            }
        };
        xmlhttp.open("POST", "TopicModel?input=" + input, true);
        xmlhttp.send();
}
</script> -->

<form method="GET" action="<?php $_PHP_SELF ?>">
<!--https://www.w3schools.com/html/html_forms.asp-->
<p>Input:</p>
<input type="text" name="input" width=200% height=200%>
<input type="submit" value="Get output" >
</form>

@php
    if(isset($_GET["input"])){
        $inputV = $_GET["input"];
        $outputV = shell_exec("python3 \"/Users/Gtt/Desktop/CC1-Project/Topic Model/api.py\" "."\"".$inputV."\"");
    }else{
        $inputV = "";
        $outputV = "";
    }
@endphp
</br>
<p>Output</p>
<span id="output">{{$outputV}}</span>



</div>
</section>
@endsection
