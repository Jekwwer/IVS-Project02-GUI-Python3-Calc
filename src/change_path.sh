#!/bin/bash

new_path="/usr/share/WaterLift_calc/manual_for_help_window.pdf"
input_file=$1

RESULT=$(awk -v new_path="$new_path" '{gsub(/manual_for_help_window.pdf/,new_path)}1' "$input_file")
echo "$RESULT" > "$input_file"
