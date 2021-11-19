#!/bin/bash
# WANT_JSON

string1=$(cat $1 | grep -Po '(?<="string1": ")(.*?)(?=")')
string2=$(cat $1 | grep -Po '(?<="string2": ")(.*?)(?=")')
string3=$(cat $1 | grep -Po '(?<="string3": ")(.*?)(?=")')

result_string="$string1 $string2 $string3"
# sleep 300

echo "{\"result_str\": \"$result_string\", \"msg\": \"Strings concated successfully\"}"
