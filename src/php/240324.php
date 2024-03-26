<?php
$nums = [1,3,4,2,2];
$dup = getDuplicate($nums);
print_r($dup);
exit;
function getDuplicate($nums){
    $hashMap = [];
    foreach($nums as $num){
        if(isset($hashMap[$num])){
            return $num;
        }
        else{
            $hashMap[$num] = 1;
        }
    }
}