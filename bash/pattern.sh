#!/bin/bash
declare -A matrix
for ((i=1;i<=63;i++)) do
    for ((j=1;j<=100;j++)) do
        matrix[$i,$j]='_'
    done
done
function update_matrix {
p1=$1
p2=$(echo $2-1|bc)
p1=$(echo $p1-1|bc)
p3=$(echo 2^$p2|bc)
p4=$(echo 2*$p3|bc)
p5=$(echo $p3/2|bc)
p6=$3
for ((q1=$p3;q1<$p4;q1++)) do
        if [ "$(echo $q1-$p3|bc)" -lt "$p5" ]
            then
            q2=$(echo $p6-$(echo $p5-$(echo $q1-$p3|bc)|bc)|bc)
            q3=$(echo $p6+$(echo $p5-$(echo $q1-$p3|bc)|bc)|bc)
            matrix[$q1,$q2]=1
            matrix[$q1,$q3]=1
            #printf '%s' "$q1 $q2 -- $q1 $q3"
            #echo ""
            else
            matrix[$q1,$p6]=1
            #echo $q1 $p6
        fi
done

if [ $p1 -ge 1 ]
then
update_matrix $p1 $p2 $(echo $p6+$p5|bc)
update_matrix $p1 $p2 $(echo $p6-$p5|bc)
else
return
fi
}
read iteration
if [ $iteration -ge 1 ]
then
    update_matrix $iteration 6 32
fi
for ((i=1;i<=63;i++)) do
    for ((j=1;j<=100;j++)) do
        printf '%s' "${matrix[$i,$j]}"
    done
    echo ""
done