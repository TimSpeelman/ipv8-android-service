#!/bin/bash

set -e

echo Export dist

mkdir -p dist

p4a export_dist \
--release \
--sdk_dir=$ANDROID_SDK_HOME \
--ndk_dir=$ANDROID_NDK_HOME \
--ndk_version=13 \
--android_api=18 \
--arch=armeabi-v7a \
--dist_name=OpenWalletService \
--bootstrap=service_only \
--requirements=openwallet \
./dist
