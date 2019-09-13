#!/bin/bash

set -e

echo Build dist

cd dist/OpenWalletService

python build.py \
--package=org.openwallet.android \
--service=OpenWallet:OpenWallet.py \
--private=../../service \
--whitelist=../../.p4a-whitelist \
--name=OpenWallet \
--version=0.1

cd ../..
