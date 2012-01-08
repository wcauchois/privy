#!/bin/bash
# ghetto database management
rm dev.db
echo no | ./manage.py syncdb
