#!/bin/bash
# WANT_JSON

addr=$(cat $1 | grep -Po '(?<="addr": ")(.*?)(?=")')
tls=$(cat $1 | grep -Po '(?<="tls": )(.*?)(?=,)')

echo $addr
echo $tls

if [ "$tls" == "true" ]; then
    schema='s'
else
    schema=''
fi

result_string=$(curl -s -o /dev/null -w "%{http_code}" http${schema}://${addr})

if [ "$result_string" == "200" ]; then
    rc=0
    failed=''
    msg='everything is ok'
else
    rc=1
    failed=", \"failed\": \"true\""
    msg='something went wrong'
fi

echo "{\"result_str\": \"$result_string\", \"msg\": \"$msg\", \"rc\": \"$rc\"$failed}"
