convert this code insteadOf sedning sms , send email massage 
<?php

 // Your Account SID and Auth Token from twilio.com/console
$sid = 'AC85c59b536862c0df5bcdceda21b19cb8';
$token = 'aff3d9d1ff2cf9a791730a0cc4e613c8';

function send_twilio_text_sms($id, $token, $from, $to, $body)
{
$url = "https://api.twilio.com/2010-04-01/Accounts/".$id."/SMS/Messages";
$data = array (
  'From' => $from,
    'To' => $to,
    'Body' => $body,
);
$post = http_build_query($data);
$x = curl_init($url );
curl_setopt($x, CURLOPT_POST, true);
curl_setopt($x, CURLOPT_RETURNTRANSFER, true);
curl_setopt($x, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($x, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($x, CURLOPT_USERPWD, "$id:$token");
curl_setopt($x, CURLOPT_POSTFIELDS, $post);
$y = curl_exec($x);

curl_close($x);
return $y;
}


if(!empty($_POST['phone'])){

  $phone = $_POST['phone'];

  send_twilio_text_sms($sid,$token,'+18507794721',"+$phone",'astorx ');


}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>test</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

</head>
<body>

<form action="" method="post" class="list-group-item mt-5" style="max-width: 450px;margin: 0px auto;">
  <div class="form-group">
   
    <label >phone sms</label>
    <input type="text" class="form-control  m-1"  name="phone" value="">

    <hr>
    <label >phone sms</label>
    <input type="submit" class="form-control btn btn-success m-1"  name="send" value="send">

  </div>
</form>
    
</body>
</html>

