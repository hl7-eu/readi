# FHIR validation API for the READI IG (HL7 validator in HTTP server mode).
# Build from the repo root:  docker build -f docker/validator/Dockerfile -t readi-fhir-validator .
#   POST /validateResource   (Content-Type: application/fhir+json)  ->  OperationOutcome
ARG SUSHI_VERSION=3.21.0
ARG VALIDATOR_VERSION=7.0.3

# --- Stage 1: compile the FSH into the IG resources the validator loads ---
FROM node:20-slim AS sushi
ARG SUSHI_VERSION
WORKDIR /ig
RUN npm install -g fsh-sushi@${SUSHI_VERSION}
COPY sushi-config.yaml ./
COPY input/ ./input/
RUN sushi .

# --- Stage 2: validator runtime ---
FROM eclipse-temurin:17-jre
ARG VALIDATOR_VERSION
ENV VALIDATOR_JAR=/opt/validator_cli.jar \
    FHIR_VERSION=4.0.1 \
    TX_SERVER=https://tx.fhir.org \
    EXTRA_IGS="hl7.fhir.uv.xver-r5.r4#0.1.0 hl7.fhir.uv.extensions.r4#5.2.0" \
    PORT=8000 \
    INTERNAL_PORT=8001 \
    JAVA_XMX=2g
RUN apt-get update && apt-get install -y --no-install-recommends curl socat \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSfL -o ${VALIDATOR_JAR} \
       https://github.com/hapifhir/org.hl7.fhir.core/releases/download/${VALIDATOR_VERSION}/validator_cli.jar
COPY --from=sushi /ig/fsh-generated/resources /ig/resources
COPY docker/validator/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Warm the package cache at build time (best effort) so the container starts offline-ready.
COPY docker/validator/warmup.json /tmp/warmup.json
RUN java -jar ${VALIDATOR_JAR} /tmp/warmup.json -version ${FHIR_VERSION} \
    -ig hl7.fhir.uv.xver-r5.r4#0.1.0 -ig hl7.fhir.uv.extensions.r4#5.2.0 -ig /ig/resources -tx n/a || true

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=90s \
  CMD curl -sf -X POST -H 'Content-Type: application/fhir+json' \
      -d '{"resourceType":"Basic","code":{"text":"x"}}' http://localhost:${PORT}/validateResource -o /dev/null || exit 1
ENTRYPOINT ["/entrypoint.sh"]
