#!/bin/bash
# WANT_JSON

string1=$(cat $1 | grep -Po '(?<="string1": ")(.*?)(?=")')

result_string="$string1"
# sleep 300

echo "{\"result_str\": \"$result_string\", \"msg\": \"Success\"}"
