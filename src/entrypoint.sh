#!/bin/bash

/sbin/my_init
service postgresql start
exec "$@"