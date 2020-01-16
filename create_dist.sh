#!/bin/bash

set -e

echo Create dist

p4a create \
--force-build \
--require-perfect-match \
--release \
--sdk_dir=$ANDROID_SDK_HOME \
--ndk_dir=$ANDROID_NDK_HOME \
--ndk_version=13 \
--android_api=18 \
--arch=armeabi-v7a \
--package=org.openwallet.android \
--service=OpenWallet:OpenWallet.py \
--private=./service \
--dist_name=OpenWalletService \
--bootstrap=service_only \
--requirements=openwallet \
--whitelist=.p4a-whitelist
q