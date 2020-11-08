SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in $@
do
    echo "removing alpha from $f"
    magick convert $f -background white -alpha remove -alpha off $f
done
IFS=$SAVEIFS