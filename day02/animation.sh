#!/bin/bash

for i in {1..10}
    do
    for ch in '-' '/' '|' '\'
    do
        printf "waiting... %s\r" $ch
        sleep 0.2
    done
done
