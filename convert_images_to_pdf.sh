SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in $@
do
    args+="${f} "
done
echo 'Making PDF'
img2pdf -o $@
IFS=$SAVEIFS
echo 'done'