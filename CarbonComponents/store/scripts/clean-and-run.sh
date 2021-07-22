#!/bin/bash
start=`date +%s`

printf "\nCleaning up existing containers/images...\n\n"
qapp clean -i

printf "\nBuilding React application...\n\n"
cd react-app && yarn build
cd ..

printf "\nStarting container...\n\n"
qapp run -d

end=`date +%s`
runtime=$((end-start))

printf "\nDone in $runtime seconds!\n"
