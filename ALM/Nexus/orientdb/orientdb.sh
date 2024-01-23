#!/bin/bash

cd "/opt/sonatype-nexus/nexus/"

SCRIPT=${1:-none}
if [[ "${1}" != "none"]]
    java -jar "./lib/support/nexus-orient-console.jar" < ${1}
else
    java -jar "./lib/support/nexus-orient-console.jar"
fi
