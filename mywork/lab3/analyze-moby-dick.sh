SEARCH_PATTERN=$1
OUTPUT=$2

curl https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt > mobydick.txt

if [[ -v OUTPUT ]]; then 
    grep -o SEARCH_PATTERN < mobydick.txt > OUTPUT | wc -l > OCCURENCES
else
    grep -o SEARCH_PATTERN < mobydick.txt > results.txt | wc -l > OCCURENCES
fi

echo "The search pattern <$SEARCH_PATTERN> was found <$OCCURENCES> time(s)."


# SEARCH_PATTERN=$1
#OUTPUT=$2

#curl -s https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt > mobydick.txt

#if [[ -n "$OUTPUT" ]]; then
    #OCCURENCES=$(grep -o "$SEARCH_PATTERN" mobydick.txt | tee "$OUTPUT" | wc -l)
#else
    #grep -o "$SEARCH_PATTERN" mobydick.txt > results.txt
    #OCCURENCES=$(wc -l < results.txt)
#fi

#echo "The search pattern <$SEARCH_PATTERN> was found <$OCCURENCES> time(s)."

