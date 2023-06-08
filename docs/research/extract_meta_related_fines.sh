#!/bin/bash

JSON_FILE=$1
NEW_FILE=$2
echo "JSON_FILE: $JSON_FILE"
if [[ -z $1 || -z $2 ]]; then
  echo "JSON file is required"
  echo "Usage: ${BASH_SOURCE[0]} <JSON file> <NEW File>"
  exit 1
fi

jq '.[] | select(.controller | test("(Meta|Facebook|WhatsApp|Instagram)"; "i"))' "$JSON_FILE" | sponge "$NEW_FILE"

echo "Converting $NEW_FILE file to JSON"
jq -s '.' "$NEW_FILE" | sponge "$NEW_FILE"
echo "There could be some false positives. Check file manually."
