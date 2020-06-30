#!/bin/bash
trap 'exit 0' SIGTERM

echo Assemble Debug APK

cd dist/OpenWalletService

./gradlew assembleDebug
cp build/outputs/apk/debug/* /mnt
