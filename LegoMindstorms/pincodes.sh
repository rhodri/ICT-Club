#!/bin/sh
BTDIRS=`ls /var/lib/bluetooth/`
for BTDIR in $BTDIRS 
do
  echo 00:16:53:1A:77:D7 1234 > "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:1A:58:41 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:1A:55:EB 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:14:24:88 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:14:87:D1 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:17:E4:EF 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
done
