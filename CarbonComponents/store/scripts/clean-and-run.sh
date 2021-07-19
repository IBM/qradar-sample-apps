#!/bin/bash

printf "\nCleaning up existing containers/images...\n\n"
qapp clean -i

printf "\nBuilding React application...\n\n"
cd react-app && yarn build
cd ..

printf "\nStarting container...\n\n"
qapp run -d

printf "\nDone!\n"
