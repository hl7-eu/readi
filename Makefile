# Makefile for the READI FHIR IG. Run `make` or `make help` to list the targets.
# Requires: Node (npx), Java 17+, and for `validate` a local copy of the HL7 validator.

SUSHI_VERSION     ?= 3.21.0
VALIDATOR_VERSION ?= 7.0.3
FHIR_VERSION      ?= 5.0.0
TX_SERVER         ?= https://tx.fhir.org
EXTRA_IGS         ?=

VALIDATOR_DIR := $(HOME)/validator
VALIDATOR_JAR := $(VALIDATOR_DIR)/validator_cli-$(VALIDATOR_VERSION).jar
VALIDATION_OUT := validation-output
SUSHI := npx --yes fsh-sushi@$(SUSHI_VERSION)

SAMPLE_SRC := sources/READI-sample-1.json
SAMPLE_OUT := input/examples/Bundle-readi-sample-1-r4.json

.DEFAULT_GOAL := help
.PHONY: help sushi build build-nosushi build-notx update-publisher jekyll clean clean-all \
        sample validator validate validate-demo report open serve docker-build docker-run

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

sushi: ## Compile the FSH only (output in fsh-generated/)
	$(SUSHI) .

build: ## Full IG Publisher build (SUSHI + publisher)
	bash ./_build.sh build

build-nosushi: ## IG Publisher build without re-running SUSHI
	bash ./_build.sh nosushi

build-notx: ## IG Publisher build without the terminology server (offline)
	bash ./_build.sh notx

update-publisher: ## Download / update publisher.jar into input-cache/
	bash ./_build.sh update

jekyll: ## Rebuild the narrative pages only (needs a previous full build)
	bash ./_build.sh jekyll

sample: ## Regenerate the R4 sample Bundle from the FEvIR source (and copy to examples/)
	python3 sources/fevir-sample-to-r4.py $(SAMPLE_SRC) $(SAMPLE_OUT)
	cp $(SAMPLE_OUT) examples/

validator: $(VALIDATOR_JAR) ## Download the pinned FHIR validator

$(VALIDATOR_JAR):
	mkdir -p $(VALIDATOR_DIR)
	curl -sSfL -o $@ https://github.com/hapifhir/org.hl7.fhir.core/releases/download/$(VALIDATOR_VERSION)/validator_cli.jar

validate: sushi $(VALIDATOR_JAR) ## Validate examples/ against the READI profiles (same as the CI workflow)
	mkdir -p $(VALIDATION_OUT)
	-java -Xmx4g -jar $(VALIDATOR_JAR) $$(find examples -type f \( -name '*.json' -o -name '*.xml' \) | sort) \
	    -version $(FHIR_VERSION) $(foreach ig,$(EXTRA_IGS),-ig $(ig)) -ig fsh-generated/resources \
	    -tx $(TX_SERVER) \
	    -output $(VALIDATION_OUT)/results.json -html-output $(VALIDATION_OUT)/results.html \
	    | tee $(VALIDATION_OUT)/validator.log
	@test -s $(VALIDATION_OUT)/results.json
	python3 scripts/validation/report.py $(VALIDATION_OUT)/results.json \
	    --baseline scripts/validation/baseline.json --report $(VALIDATION_OUT)/report.md
	@cat $(VALIDATION_OUT)/report.md

DEMO_FILE ?= input/examples/Demo_NCT01931527.json

validate-demo: sushi $(VALIDATOR_JAR) ## Validate a single file (default: DEMO_FILE=input/examples/Demo_NCT01931527.json) against R4 + READI profiles
	mkdir -p $(VALIDATION_OUT)
	-java -Xmx4g -jar $(VALIDATOR_JAR) $(DEMO_FILE) \
	    -version $(FHIR_VERSION) $(foreach ig,$(EXTRA_IGS),-ig $(ig)) -ig fsh-generated/resources \
	    -tx $(TX_SERVER) \
	    -output $(VALIDATION_OUT)/demo-results.json -html-output $(VALIDATION_OUT)/demo-results.html \
	    | tee $(VALIDATION_OUT)/demo-validator.log

report: ## Re-build the validation report from the last results.json
	python3 scripts/validation/report.py $(VALIDATION_OUT)/results.json \
	    --baseline scripts/validation/baseline.json --report $(VALIDATION_OUT)/report.md
	@cat $(VALIDATION_OUT)/report.md

open: ## Open the built IG in the browser
	open output/index.html

serve: ## Serve output/ on http://localhost:8010
	cd output && python3 -m http.server 8010

clean: ## Remove generated folders (fsh-generated, output, temp, validation-output)
	rm -rf fsh-generated output temp $(VALIDATION_OUT)

clean-all: clean ## Also remove input-cache (publisher.jar, package cache)
	rm -rf input-cache

docker-build: ## Build the validation API image (readi-fhir-validator)
	docker build -f docker/validator/Dockerfile -t readi-fhir-validator .

docker-run: ## Run the validation API on http://localhost:8002
	docker run --rm -p 8002:8000 readi-fhir-validator
