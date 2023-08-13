<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Number Base System Converter from Decimal</title>
  </head>
  <body>
    <h1>
      Konversi Sistem Bilangan dari Desimal
      <br />
      (Number Base System Converter from Decimal)
    </h1>
    <hr>
    <form method="post">
      <label for="inputNum">Input Number:</label>
      <input type="text" id="inputNum" name="inputNum"><br><br>
      <label for="base1">Input Base:</label>
      <input type="text" id="base1" name="base1"><br><br>
      <input type="submit" name="convert" value="Convert"><br><br>
    </form>
    <div id="result">
      <?php
        function reVal($num) {
          if ($num >= 0 && $num <= 9) return chr($num + 48);
          else return chr($num - 10 + 65);
        }

        function fromDeci($base1, $inputNum) {
          $s = "";
          while ($inputNum > 0) {
            $s .= reVal($inputNum % $base1);
            $inputNum = intval($inputNum / $base1, 10);
          }
          $res = str_split($s);
          $res = array_reverse($res);
          return implode("", $res);
        }

        if(isset($_POST['convert'])) {
          $inputNum = $_POST['inputNum'];
          $base1 = $_POST['base1'];
          $output = $inputNum . "[" . $base1 . "] = " . fromDeci($base1, $inputNum);
          echo $output;
        }
      ?>
    </div>
  </body>
</html>
