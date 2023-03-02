#!/usr/bin/env bash

cd $(dirname "$0")

cc -x c - < ../../c/hello_world_1/main.c -o hello

./hello
