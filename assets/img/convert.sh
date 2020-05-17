#!/usr/bin/env bash

for img in *.jpg; do
	wpf=$(echo "$img" | sed "s/jpg/webp/")
	echo $img $wpf
	convert "$img" "$wpf"
	
done
