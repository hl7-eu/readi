#!/bin/sh
set -e
IG_ARGS=""
for ig in $EXTRA_IGS; do IG_ARGS="$IG_ARGS -ig $ig"; done
# The validator HTTP server only binds to 127.0.0.1; expose it on 0.0.0.0:$PORT.
socat TCP-LISTEN:${PORT},fork,reuseaddr,bind=0.0.0.0 TCP:127.0.0.1:${INTERNAL_PORT} &
exec java -Xmx${JAVA_XMX} -jar ${VALIDATOR_JAR} -server ${INTERNAL_PORT} \
  -version ${FHIR_VERSION} $IG_ARGS -ig /ig/resources -tx ${TX_SERVER}
