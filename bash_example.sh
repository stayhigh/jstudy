dd if=/dev/zero bs=16000 count=1000 | nc -vvv 216.239.32.10 -X 5 -x 127.0.0.1:1080 443 # test the speed with sock5 proxy
ping www.baidu.com & sleep 3; kill $! # ping 3 seconds
