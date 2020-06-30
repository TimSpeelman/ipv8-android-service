#!/bin/bash
trap 'exit 0' SIGTERM

cd dist/OpenWalletService

./gradlew assembleDebug
cp build/outputs/apk/debug/* /mnt
