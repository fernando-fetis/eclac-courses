TYPST  ?= typst
PYTHON ?= python3

LECTURES := $(sort $(patsubst %/,%,$(dir $(wildcard lecture-*/slides.typ))))
DECKS    := $(addsuffix /slides.pdf,$(LECTURES))
SCRIPTS  := $(filter-out %/_common.py,$(wildcard lecture-*/scripts/*.py))
FIGURES  := $(foreach s,$(SCRIPTS),$(subst /scripts/,/figures/,$(s:.py=.pdf)))
SHARED   := common/scripts/plotstyle.py common/scripts/diagram.py

.PHONY: all slides figures check clean clean-figures watch help $(LECTURES)

## all: refresh stale figures, then compile every deck
all: figures slides

## slides: compile every deck, leaving the figures untouched
slides: $(DECKS)

## figures: regenerate every figure whose script changed
figures: $(FIGURES)

## lecture-N: figures and deck for one lecture, e.g. make lecture-2
$(foreach l,$(LECTURES),$(eval $(l): $$(filter $(l)/%,$$(FIGURES)) $(l)/slides.pdf))

## watch: rebuild one deck on every save, e.g. make watch LECTURE=lecture-1
watch:
	@test -n "$(LECTURE)" || { echo 'usage: make watch LECTURE=lecture-N'; exit 1; }
	$(TYPST) watch --root . $(LECTURE)/slides.typ $(LECTURE)/slides.pdf

## check: report slides whose content spills onto the next page
check:
	@status=0; for lecture in $(LECTURES); do $(PYTHON) common/scripts/check-overflow.py $$lecture/slides.typ || status=1; done; exit $$status

## clean: remove the compiled decks
clean:
	@rm -f $(DECKS)

## clean-figures: remove the generated figures
clean-figures:
	@rm -f $(FIGURES)

## help: list the targets
help:
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/^## /  /'

%/slides.pdf: %/slides.typ %/bib.yml common/theme.typ
	@$(TYPST) compile --root . $< $@
	@echo "  $@"

define figure_rule
$(subst /scripts/,/figures/,$(1:.py=.pdf)): $(1) $$(SHARED)
	@cd $$(dir $(1)) && $$(PYTHON) $$(notdir $(1))
	@echo "  $$@"
endef
$(foreach s,$(SCRIPTS),$(eval $(call figure_rule,$(s))))
