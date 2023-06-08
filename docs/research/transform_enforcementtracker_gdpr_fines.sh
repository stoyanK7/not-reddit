#!/bin/bash


JSON_FILE=$1
echo "JSON_FILE: $JSON_FILE"
if [[ -z $1 ]]; then
  echo "JSON file is required"
  echo "Usage: $BASH_SOURCE <JSON file>"
  exit 1
fi

echo "Removing <img> tags"
sed -i "s/<img[^>]*>//g" "$JSON_FILE"

echo "Removing first item in each array"
jq 'del(.data[][] | select(. == ""))' "$JSON_FILE" | sponge "$JSON_FILE"

echo "Converting all to objects"
jq '.data[] | {id: .[0], country: .[1], authority: .[2], date: .[3], fine: .[4], sector: .[5], category: .[6], article: .[7], violation: .[8], summary: .[9], link: .[10], enforcement: .[11]}' "$JSON_FILE" | sponge "$JSON_FILE"

echo "Converting file to JSON"
jq -s '.' "$JSON_FILE" | sponge "$JSON_FILE"

echo "Removing <br> tags"
sed -i "s/<br \/>//g" "$JSON_FILE"
