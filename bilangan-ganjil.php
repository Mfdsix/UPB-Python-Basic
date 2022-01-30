<?php

$pembagi = 3;
$awal = 2;
$akhir = 100;

function cekGanjil($angka)
{
    return $angka % 2 != 0;
}

function cekBisaDibagi($angka, $pembagi)
{
    return $angka % $pembagi == 0;
}

for ($i = $awal; $i < $akhir; $i++) {
    if (cekGanjil($i) && cekBisaDibagi($i, $pembagi)) {
        print($i . "\n");
    }
}
