#!/bin/sh
IG_ARGS=""
for ig in $EXTRA_IGS; do IG_ARGS="$IG_ARGS -ig $ig"; done
# The validator HTTP server only binds to 127.0.0.1; expose it on 0.0.0.0:$PORT.
socat TCP-LISTEN:${PORT},fork,reuseaddr,bind=0.0.0.0 TCP:127.0.0.1:${INTERNAL_PORT} &
SOCAT_PID=$!
JAVA_PID=""
trap 'kill $JAVA_PID $SOCAT_PID 2>/dev/null; exit 0' TERM INT
# The tx server drops caches idle >30 min and the validator never recovers; restart the JVM periodically.
while true; do
  java -Xmx${JAVA_XMX} -jar ${VALIDATOR_JAR} -server ${INTERNAL_PORT} \
    -version ${FHIR_VERSION} $IG_ARGS -ig /ig/resources -tx ${TX_SERVER} &
  JAVA_PID=$!
  if [ "${RESTART_INTERVAL:-1500}" -gt 0 ]; then
    sleep ${RESTART_INTERVAL:-1500} &
    wait $!
    kill $JAVA_PID 2>/dev/null
  fi
  wait $JAVA_PID
done
