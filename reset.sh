#!/bin/bash
trap 'exit 0' SIGTERM

p4a clean_recipe_build aiohttp ipv8
p4a clean_recipe_build multidict
p4a clean_recipe_build ipv8
p4a clean_recipe_build openwallet
p4a clean_recipe_build pyasn1
