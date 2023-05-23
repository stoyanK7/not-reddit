#!/bin/sh
# This script is expected to be run from root folder of repository.

source ./.dev/util.sh

checkForVariable "JWT_TOKEN"
checkForVariable "API_URL"

# Delete all data from databases
./.dev/delete-database-data.sh user
./.dev/delete-database-data.sh post
./.dev/delete-database-data.sh comment
./.dev/delete-database-data.sh vote

# Create user
curl -XPOST \
  -H "Authorization: Bearer $JWT_TOKEN" \
  "$API_URL/api/user"

# Create 6 text posts
for i in 1 2 3 4 5 6
do
  curl -s -XPOST \
    -H "Authorization: Bearer $JWT_TOKEN" \
    -H "Content-type: application/json" \
    -d "{
      \"title\": \"$i: Lorem ipsum 1234567890!@#$%^&*()_+{}:<>\",
      \"body\": \"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"
    }" \
    "$API_URL/api/post/text" | jq "."
done

# Create 4 media posts
for i in 1 2 3 4
do
  curl -s -XPOST \
    -H "Authorization: Bearer $JWT_TOKEN" \
    -F "title=$i: Lorem ipsum 1234567890!@#$%^&*()_+{}:<>" \
    -F "file=@docs/test/img/$i.png" \
    "$API_URL/api/post/media" | jq "."
done
