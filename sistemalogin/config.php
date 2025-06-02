<?php
    $host = 'Localhost';
    $user = 'root';
    $pass = '';
    $db = 'meu_banco';

    $conn = new mysqli($host, $user, $pass, $db);
     if ($conn->connect_errno){
        echo "Erro";

     }

     else{
        echo "conexão efetuada com sucesso!";
     }







?>