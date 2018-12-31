<html>
<head>
    <meta charset="utf-8"/>
    <script src="http://code.jquery.com/jquery-1.9.1.min.js" ></script>
    <style>
        input, textarea{
            background-color:#FFFFFF;
            border:solid 1px #A9A9A9;
            font-size:13px;
            color:#000000;
            -moz-border-radius:10px;
            -webkit-border-radius:10px;
            border-radius:10px;
            padding-top:5px;
            padding-bottom:5px;
            padding-left:5px;
            padding-right:5px;
            width: 500px;
            resize: none;
        }

        button.button5 {
            border-radius: 50%;
            background: #00ffe1;
            font-family: "Arial Black", Gadget, sans-serif;
            font-size: 18px;
        }

        submit {
            width:100px;

        }

        body  {
            font-size:12px;
            font-family:veranda;
            background: rgb(2,0,36);
            background: linear-gradient(90deg, #00ffe1 0%, #3e005e 100%);
        }

        img.logo {
            width: 200px;
            height: auto;
        }

        div.note {
            width: 500px;
            padding: 5px 20px 20px 20px;
            min-height: 80px;
            font-family:veranda;
            border-radius:10px 10px 10px 10px;
            -moz-border-radius:10px 10px 10px 10px;
            -webkit-border-radius:10px 10px 10px 10px
            -webkit-box-shadow:0px 0px 5px 3px #444444 ;
            -moz-box-shadow:0px 0px 5px 3px #444444 ;
            box-shadow:0px 0px 5px 3px #444444 ;
            background-color:rgb(255, 255, 255);
	    white-space: normal;
            overflow-wrap: break-word;
            margin: 40px 40px 40px 40px;
        }

        h2.note{

            font-family: "Arial Black", Gadget, sans-serif;
            font-size: 16px;
            letter-spacing: -0.4px;
            word-spacing: -0.2px;
            color: #000000;
            font-weight: normal;
            text-decoration: none;
            font-style: normal;
            font-variant: normal;
            text-transform: lowercase;
            overflow-wrap: break-word;
        }

        div.content {
            position: absolute;
            top: 50px;
            left: 600px;
            margin-top: 0px;
            margin-left: 0px;
            width: 800px;
            height: 100%;
            background: none;
        }
        h2.content{
            font-family: "Arial Black", Gadget, sans-serif;
            font-size: 40px;
            letter-spacing: -3px;
            word-spacing: -1.8px;
            color: #000000;
            font-weight: normal;
            text-decoration: none;
            font-style: normal;
            font-variant: normal;
            text-transform: lowercase;
        }
    </style>
</head>
<body>
<div id="toplogo">
    <img  class="logo" src="ladidadi.png"></img>
</div>

<form action="/notes/notes2.php">
    Title: <br/><input type="text" name="title"><br>
    Note: <br/><textarea name="note" rows="10" cols="50"></textarea><br/>
    <input type="submit" value="Submit">
</form>


<script>
    $.getJSON('./notes.json', function(obj) {
        var newArray = [];
        for (var x in obj['notes']) {
            var newObj = obj['notes'][x];
            //console.log("var x: " + x);
            for (var y in newObj) {
                newArray.push(y);
            }
        }
        var arrayReverse = newArray.reverse();
        for(i = 0; i < arrayReverse.length; i++){
            for (var q in obj['notes']) {
                var lastObj = obj['notes'][q];
                for (var r in lastObj) {
                    if (r == arrayReverse[i]) {
                        $("p").append("<div class='note'><h2 class='note'>" + lastObj[r]['title'] + " @ " + r + "</h2><br/>" + lastObj[r]['note'] + "<br/><a href='http://xfid.net/notes/notes2.php?delete=" + r + "'>delete</a></div>");
                            }
                }
            }
        }
    });


</script>
<div class="content">
    <h2 class="content">notes.</h2>
    <p></p>
</div>

<?php
$title = ('"'.$_GET['title'].'"');
$note = ('"'.$_GET['note'].'"');
$delete = ('"'.$_GET['delete'].'"');

if (strlen($note) >= 5){
exec("/usr/bin/python /home/clbs/notes.py $title $note");
print("post triggered");
}

if (strlen($delete) >= 5){
print("true");
exec("/usr/bin/python /home/clbs/notes.py $delete");
print($delete);
}

?>


</body>
</html>
