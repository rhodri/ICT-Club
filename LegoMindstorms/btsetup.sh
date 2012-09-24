#!/bin/sh
BTDIRS=`ls /var/lib/bluetooth/`
HOSTNAME=`hostname`
BTNAME=`echo $HOSTNAME | sed 's/\\.zoo\\.lan//'`
#BTNAME=$HOSTNAME
for BTDIR in $BTDIRS 
do
  echo Setting Bluetooth name as $BTNAME for $BTDIR
  echo 00:16:53:1A:77:D7 1234 > "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:1A:58:41 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:1A:55:EB 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:14:24:88 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:14:87:D1 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"
  echo 00:16:53:17:E4:EF 1234 >> "/var/lib/bluetooth/$BTDIR/pincodes"

  echo name $BTNAME > "/var/lib/bluetooth/$BTDIR/config"
  echo pairable yes >> "/var/lib/bluetooth/$BTDIR/config"
  echo class 0x420100 >> "/var/lib/bluetooth/$BTDIR/config"
done
