#!/usr/bin/php
<?php
//reducer script for sample hadoop job

$word2count = array();

// input comes from STDIN
while (($line = fgets(STDIN)) !== false) {
    // remove leading and trailing whitespace
    $line = trim($line);
    // parse the input we got from mapper.php
    list($word, $count) = explode("\t", $line);
    // convert count (currently a string) to int
    $count = intval($count);
    // sum counts
    if ($count > 0) $word2count[$word] += $count;
}

ksort($word2count);  // sort the words alphabetically

// write the results to STDOUT (standard output)
foreach ($word2count as $word => $count) {
    echo "$word\t$count\n";
}