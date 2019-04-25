#!/bin/bash
python3 MainWin.py
while true
do
$pid =  'pgrep -f MainWin.py'
	if [ ! $pid ] ; then
		python3 MainWin.py
	fi
	sleep 3
done
