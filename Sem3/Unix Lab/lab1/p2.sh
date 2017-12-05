#!/bin/bash
clear
echo -n "enter the basic salary"
read bs
dp=$(echo "scale = 3; 0.50 * $bs"|bc)
val=$(echo "scale = 3; $dp + $bs"|bc)
da=$(echo "scale = 3; 0.35 * $val"|bc)
hra=$(echo "scale = 3; 0.080 * $val"|bc)
ma=$(echo "scale = 3; 0.03 * $val"|bc)
pf=$(echo "scale = 3; 0.10 * $val"|bc)
sal=$(echo "scale = 3; $bs + $dp + $da + $hra + $ma - $pf"|bc)
echo "$sal"