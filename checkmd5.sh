fmd=$(md5sum gethw.py)
tmd=$(cat gethw.md5)

[[ "$fmd" == "$tmd" ]] || { echo bad md5 ; exit 1 ; }

echo good md5
exit 0 
