<?php
$nums = [2,3,4,5,6];
echo firstMissingPositive($nums);
function firstMissingPositive($nums) {
    // sort($nums);
    // $high = $nums[count($nums)-1];
    // if($high < 1)
    // return 1;
    $nums = array_flip($nums);
    for($i=1; $i<=count($nums)+1; $i++) {
        if (!isset($nums[$i])) return $i;
    }
}