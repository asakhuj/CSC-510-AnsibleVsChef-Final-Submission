It feels like Ansible becomes slower with each release? Is it true?

This is an answer. We are using Ansible to measure Ansible's performance.
There are some tests in place.  Please run "preReq.sh" after making it executable using "chmod +x preReq.sh" with sudo priveleges.

I performed the following tests on NCSU VCL machine, creating virtual environments and testing the templates on all stable ansible versions.

My numbers:

```
Test 1
Subject: Testing template performance
------------------------------------------------------
v1.9.6 0:06.72
v2.0.2 0:13.45
v2.1.3 0:20.66
v2.2.0 0:20.91

Test 2
Subject: Testing big stack of variables
------------------------------------------------------
v1.9.6 0:07.20
v2.0.2 0:14.29
v2.1.3 0:21.59
v2.2.0 0:21.57

Test 3
Subject: Testing shell execution with register
------------------------------------------------------
v1.9.6 0:06.64
v2.0.2 0:08.31
v2.1.3 0:12.40
v2.2.0 0:11.53
```

