#!/bin/bash
trap 'exit 0' SIGTERM

echo Resetting Recipe Caches

p4a clean_download_cache aiohttp
p4a clean_download_cache multidict
p4a clean_download_cache ipv8
p4a clean_download_cache openwallet
p4a clean_download_cache pyasn1

p4a clean_recipe_build aiohttp 
p4a clean_recipe_build multidict
p4a clean_recipe_build ipv8
p4a clean_recipe_build openwallet
p4a clean_recipe_build pyasn1
