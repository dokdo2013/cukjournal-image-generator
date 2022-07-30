<?
    echo "<h1>처리 중입니다. 잠시만 기다려주세요</h1>";
    if(file_exists('test.png')){
        unlink('test.png');
    }
    $last_date = $_POST["lastDate"];
    $total_date = $_POST["totalDate"];

    $config_file = fopen("config.txt","w");
    $config_text = "$last_date -$total_date";
    fwrite($config_file, "$config_text");
    //fclose($config_file);
    system("python3 image.py");
    echo "<meta http-equiv=\"refresh\" content=\"5; URL=http://hakbo.haenu.com/image_view.php\">";
?>