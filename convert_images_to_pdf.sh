SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in $@
do
    echo "removing alpha from $f"
    args+="${f} "
done
# echo img2pdf -o $@
img2pdf -o $@
IFS=$SAVEIFS
# echo $args
echo 'done'

read a