#!/bin/bash

time parallel --jobs 100%  "ping  {} > {}.log"  :::: dns_server.list
multitail *.log
