#!/bin/bash

SELECTED_DATABASE=$1
echo "SELECTED_DATABASE: $SELECTED_DATABASE"

if [[ -z $SELECTED_DATABASE ]]; then
  echo "database is not set"
  echo "Usage: ${BASH_SOURCE[0]} <database>"
  exit 1
fi

DATABASE_POD=$(kubectl get pods -l app="$SELECTED_DATABASE-database" -o jsonpath="{.items[0].metadata.name}")

kubectl exec -it "$DATABASE_POD" -- psql -d "$SELECTED_DATABASE" -U postgres -c "DO \$\$
DECLARE
    table_name text;
BEGIN
    FOR table_name IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' LOOP
        EXECUTE 'DELETE FROM ' || quote_ident(table_name) || ';';
    END LOOP;
END \$\$;"
