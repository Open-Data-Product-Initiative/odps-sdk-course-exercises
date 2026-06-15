# Udemy Course Plan: Sections 3 and 4

## Source of truth

Udemy structure is the source of truth.

This plan focuses only on:

- Section 3: Introduction to the SDK
- Section 4: Final Stage: Build the Portfolio

---

# Section 3: Introduction to the SDK

## Lecture 6: What the Open Data Products SDK is

### Purpose

Give learners the mental model before commands.

### Learning outcome

Learner understands what the SDK does and why it exists.

### Core message

The SDK is the practical tooling layer for the Open Data Products standards family. It helps users validate, generate, explain, connect, and publish structured data product artifacts.

### Content plan

Start with the problem:

- Data product standards are useful, but teams need tools to apply them.
- Manual YAML writing does not scale.
- AI generation needs validation and structure.
- Portfolio work needs catalogs and graphs.

Explain the SDK:

- CLI for command-line workflows.
- Python API for notebooks and automation.
- Validation for standard files.
- Generation for product specs and portfolio objects.
- Fragments for smaller reusable objects.
- ODPC catalogs for portfolio structure.
- ODPG graphs for relationships.
- HTML views for human review.
- Agent-ready YAML for automation.

### Suggested slides

1. What problem the SDK solves
2. SDK as the operational layer
3. CLI, Python, validation, generation, graph, catalog
4. AI Agent First, but not AI Agent Only
5. Course flow from commands to portfolio builder

### Demo

No heavy demo.

Show one terminal command and one output folder screenshot.

### Do not cover

- Installation details.
- Deep generation config.
- Portfolio builder details.

---

## Lecture 7: Installing and running the SDK

### Purpose

Get learners ready to run commands.

### Learning outcome

Learner installs the SDK and runs the first basic command.

### Core message

Before building portfolios, you need a clean local or Colab environment.

### Content plan

Explain supported usage styles:

- Local terminal.
- Python notebook.
- Google Colab.

Show install:

- `pip install` command.
- Version check.
- Basic CLI help command.
- Python import check.

Suggested folder structure:

```text
source_docs/
fragments/
catalogs/
graphs/
portfolio/
reports/
```

### Hands-on

- Install the SDK.
- Run version check.
- Run help command.
- Create working folders.
- Run one simple command that produces output.

### Suggested slides

1. Setup options
2. Folder structure
3. First command
4. Common setup issues

### Demo result

A working SDK environment and project folder.

### Do not cover

- Provider config.
- Generation.
- Catalog build.

---

## Lecture 8: Validating and explaining standards files

### Purpose

Show that the SDK increases trust before it generates anything.

### Learning outcome

Learner validates a standards file and reads explanation output.

### Core message

Validation turns YAML into something safer for real workflows.

### Content plan

Explain why validation matters:

- Catches missing required fields.
- Finds wrong structure.
- Supports repeatable governance.
- Prevents bad artifacts from entering catalogs and graphs.

Show validation workflow:

- Input YAML.
- Run validation.
- Read errors or success output.
- Fix simple issue.
- Run validation again.

Explain `explain` capability:

- Use SDK to describe a file or parts of a file.
- Help learners understand structure.
- Help reviewers inspect files faster.

### Suggested slides

1. Why validation matters
2. Validation workflow
3. Error, fix, rerun
4. Explain before automate

### Hands-on

- Validate a sample ODPS or ODPC file.
- Introduce one intentional error.
- Fix it.
- Run explain command.

### Demo result

A valid file and learner understanding of feedback.

### Do not cover

- Full schema theory.
- Deep ODPS component details.

---

## Lecture 9: Use the ODPV Vocabulary Helpers

### Purpose

Show how the SDK helps users work with consistent vocabulary.

### Learning outcome

Learner uses ODPV helpers to inspect or apply controlled terms.

### Core message

Vocabulary helpers reduce inconsistency across product specs, catalogs, and generated outputs.

### Content plan

Explain ODPV:

- Vocabulary layer for consistent terms.
- Useful for data product types, lifecycle states, roles, access models, and other controlled values.
- Supports better review and automation.

Show why this matters:

- Without controlled terms, teams write the same concept in many ways.
- AI generation can create variation.
- Vocabulary helpers keep outputs aligned.

### Hands-on

- List available vocabulary terms.
- Look up one term.
- Use helper output in a generated or edited YAML file.
- Validate the result.

### Suggested slides

1. What ODPV helps with
2. Why vocabulary consistency matters
3. Human text vs controlled terms
4. Helper workflow

### Demo result

A standards file using consistent vocabulary.

### Do not cover

- Full ODPV specification.
- Custom vocabulary design unless already supported.

---

## Lecture 10: Working with local LLMs

### Purpose

Teach local model configuration for generation workflows.

### Learning outcome

Learner understands when and how to use a local LLM with the SDK.

### Core message

Local LLMs help with cost control, privacy, development testing, and restricted environments.

### Content plan

Explain why local LLMs matter:

- Lower cost during experimentation.
- Avoid sending sensitive source text to external services.
- Useful in government or enterprise contexts.
- Good for repeatable workflow testing.

Introduce config:

- `generation.config.yaml`
- `provider`
- `model`
- input defaults
- output defaults

Explain expected workflow:

- Create or copy config.
- Select local provider.
- Select model.
- Run generate command.
- Review output.
- Validate output.

### Hands-on

- Create generation config.
- Review fields.
- Set local provider and model.
- Run generation on a small source text.
- Validate generated YAML.

### Suggested slides

1. Why local LLMs
2. Local generation workflow
3. Config file anatomy
4. Generate, review, validate

### Demo result

A generated artifact from local model configuration.

### Do not cover

- Benchmarking models.
- Advanced prompt tuning.
- Online providers.

---

## Lecture 11: Working with online LLM providers

### Purpose

Teach provider-based online generation.

### Learning outcome

Learner configures an online provider and understands safe API key handling.

### Core message

The SDK lets users switch online providers through configuration without rewriting the generation workflow.

### Content plan

Explain provider abstraction:

- Same SDK workflow.
- Different provider.
- Different model.
- Config selects runtime behavior.

Explain secrets:

- API keys stay in environment variables.
- Do not store secrets in config files.
- Config references provider and model.

Explain extensibility:

- Default config includes provider entries.
- Users can add more vendor entries.
- Workflow stays stable.

### Hands-on

- Set environment variable.
- Select online provider in config.
- Run generate command.
- Review output.
- Validate output.

### Suggested slides

1. Online provider workflow
2. Config vs secret
3. Switching providers
4. Review and validation loop

### Demo result

A generated YAML artifact from an online provider.

### Do not cover

- Provider comparison.
- Cost analysis.
- Security policy beyond basic secret handling.

---

## Lecture 12: Generating ODPS Data Products from business requirements

### Purpose

Show direct generation of full data product specs.

### Learning outcome

Learner turns business requirement text into a draft ODPS data product YAML.

### Core message

The SDK can transform business requirements into structured ODPS drafts, but human review and validation still matter.

### Content plan

Start with source material:

- A short business requirement.
- Pain point.
- Target user.
- Expected value.
- Data need.
- Access expectation.
- Quality or SLA expectation.

Explain generation target:

- Full ODPS-style data product draft.
- Not a catalog fragment.
- Not a portfolio object.
- A product specification draft.

### Hands-on

- Prepare business requirement text.
- Run generate with ODPS data product target.
- Inspect generated YAML.
- Validate generated YAML.
- Improve source text or rerun if needed.

### Suggested slides

1. From requirement to product spec
2. What the generator needs
3. Generated YAML is a draft
4. Review, fix, validate

### Demo result

One generated ODPS data product YAML.

### Do not cover

- Fragments.
- Catalog generation.
- Portfolio builder.

---

## Lecture 13: Working with Generation and Fragments

### Purpose

Explain fragment-based authoring for portfolio work.

### Learning outcome

Learner understands fragments and generates smaller portfolio objects.

### Core message

Fragments are small standalone objects that later become catalogs and graphs.

### Fragment definition

A fragment is a small, valid, standalone YAML document that describes one portfolio object or one narrow object set. It is intended to be collected into a larger ODPC catalog or used as node input for an ODPG graph.

### Content plan

Explain why fragments exist:

- Full product specs are too large for every portfolio workflow.
- Portfolio work often starts with small objects.
- Fragments are easier to review.
- Fragments compose into catalogs and graphs.

Examples:

- `product_reference_<id>.yaml`
- `use_case_<id>.yaml`
- `business_objective_<id>.yaml`
- `signal_<id>.yaml`

### Hands-on

- Generate one product reference.
- Generate one use case.
- Generate one signal.
- Generate one business objective.
- Inspect files.
- Explain how they connect later.

### Suggested slides

1. What a fragment is
2. Fragment vs full ODPS spec
3. Common fragment types
4. From fragments to catalog and graph

### Demo result

A folder of generated fragments.

### Do not cover

- Full portfolio builder.
- HTML views.
- Version history.

---

## Lecture 14: Working with ODPG Graphs

### Purpose

Show how relationships are represented.

### Learning outcome

Learner understands how product portfolio objects become graph nodes and edges.

### Core message

Catalogs describe objects. Graphs describe relationships.

### Content plan

Explain graph role:

- Products connect to use cases.
- Use cases connect to business objectives.
- Signals support prioritization.
- Relationships make portfolio logic visible.
- Graphs help AI agents reason over data products.

Show graph elements:

- Nodes.
- Edges.
- Identifiers.
- Labels.
- Relationship types.
- Source and target.

### Hands-on

- Use generated fragments.
- Create or generate graph.
- Inspect nodes.
- Inspect edges.
- Find product-to-use-case relationship.
- Find use-case-to-objective relationship.
- Validate graph if supported.

### Suggested slides

1. Why graph matters
2. Nodes and edges
3. Product portfolio relationship map
4. Graphs for agents and portfolio analysis

### Demo result

An ODPG graph file with connected portfolio objects.

### Do not cover

- Complex graph algorithms.
- Graph database deployment.
- Full portfolio builder.

---

## Lecture 15: Working with ODPC Catalogs

### Purpose

Show how fragments become a structured catalog.

### Learning outcome

Learner understands ODPC catalogs and how they prepare the final portfolio workflow.

### Core message

The ODPC catalog collects portfolio objects into a reviewable, structured portfolio artifact.

### Content plan

Explain catalog role:

- Holds product references.
- Holds use cases.
- Holds business objectives.
- Holds signals.
- Gives a portfolio-level view.
- Works with graph output.

Compare:

- Fragments are separate authoring units.
- Catalog is the combined portfolio structure.
- Graph is the relationship view.

### Hands-on

- Use fragment folder.
- Create or assemble ODPC catalog.
- Inspect catalog sections.
- Validate catalog.
- Connect catalog to graph conceptually.

### Suggested slides

1. Why catalogs matter
2. Fragment folder to catalog
3. Catalog vs graph
4. Bridge to portfolio builder

### Demo result

A combined ODPC catalog built from fragments.

### Do not cover

- HTML portfolio output.
- Version history.
- Localization.

---

## Quiz 2: Section 3 quiz

### Purpose

Check understanding before final build.

### Suggested questions

- What is the SDK used for?
- Why validate generated YAML?
- What problem do ODPV helpers solve?
- Where should API keys be stored?
- What is the difference between full ODPS generation and fragments?
- What is the difference between ODPC and ODPG?
- Why are fragments useful before building a portfolio?

---

# Section 4: Final Stage: Build the Portfolio

## Lecture 16: From Commands to Portfolio Builder

### Purpose

Move from isolated SDK capabilities to the final workflow.

### Learning outcome

Learner understands why the portfolio builder exists.

### Core message

The earlier commands teach the parts. The portfolio builder combines them into one repeatable workflow.

### Content plan

Recap what learners already did:

- Install SDK.
- Validate files.
- Configure LLMs.
- Generate product specs.
- Generate fragments.
- Build graph.
- Build catalog.

Explain the limitation of isolated commands:

- Good for learning.
- Good for debugging.
- Good for targeted updates.
- Manual orchestration becomes slow.

Explain portfolio builder:

- Takes source material.
- Generates portfolio objects.
- Builds catalog.
- Builds graph.
- Creates reviewable outputs.
- Supports repeatable runs.

### Suggested slides

1. What we have learned so far
2. Limits of isolated commands
3. What portfolio builder automates
4. When to use each approach

### Demo

Show a simple input-output diagram.

### Do not cover

- Detailed builder output yet.
- Hands-on run yet.

---

## Lecture 17: What the Portfolio Builder Creates

### Purpose

Explain final outputs before building them.

### Learning outcome

Learner knows what to expect from the portfolio builder.

### Core message

The portfolio builder produces both human review artifacts and machine-readable artifacts.

### Content plan

Explain inputs:

- Source documents.
- Business requirements.
- Transcripts.
- Strategy notes.
- Customer signals.
- Existing YAML.

Explain outputs:

- Generated fragments.
- Combined ODPC catalog.
- ODPG graph.
- HTML portfolio view.
- `index.html`.
- Versioned output folders.
- Agent-ready YAML files.
- Reports or logs if available.

Business value slide:

Data product work is often fragmented. Ideas live in slides. Requirements live in spreadsheets. Governance notes live in documents. Technical details live in repositories. Catalog entries live elsewhere.

The portfolio builder connects this scattered intent into structured artifacts:

- Business objectives.
- Use cases.
- Product references.
- Signals.
- Catalogs.
- Graphs.
- HTML views.
- Agent-ready YAML.

### Suggested slides

1. Portfolio builder inputs
2. Portfolio builder outputs
3. Human view and machine-readable files
4. Why this matters for companies
5. Output folder anatomy

### Demo

Show expected output folder structure.

### Do not cover

- Running in Colab yet.
- Version history.
- Localization.

---

## Lecture 18: Build the First Portfolio in Colab

### Purpose

Run the full build.

### Learning outcome

Learner creates the first complete portfolio.

### Core message

One workflow turns source material into structured portfolio artifacts.

### Content plan

Set up Colab:

- Install SDK.
- Mount or upload source material.
- Prepare folder structure.
- Load config if needed.

Run build:

- Point builder to source folder.
- Set output folder.
- Run portfolio builder.
- Wait for output.
- Check logs or command response.

Review output:

- Fragments folder.
- Catalog file.
- Graph file.
- HTML portfolio view.
- Index page.

### Hands-on

- Run full build from sample source material.
- Open output files.
- Validate catalog and graph if supported.
- Open HTML view.

### Suggested slides

1. Colab workflow
2. Source material
3. Run portfolio builder
4. Review generated output

### Demo result

A complete first portfolio.

### Do not cover

- Updating portfolio.
- Localization.
- Final review framing.

---

## Lecture 19: Update the Portfolio and Review Version History

### Purpose

Show that the portfolio evolves.

### Learning outcome

Learner updates the portfolio and reviews versions.

### Core message

A portfolio is not a one-time output. It should change when business needs, signals, and product ideas change.

### Content plan

Explain why version history matters:

- Business priorities change.
- Use cases evolve.
- New signals appear.
- Products are added, merged, or retired.
- Reviewers need to compare outputs.

### Hands-on

- Add a new source document.
- Modify an existing requirement.
- Run portfolio builder again.
- Review new output folder.
- Open `index.html`.
- Compare previous and current version.
- Check what changed in catalog and graph.

### Suggested slides

1. Portfolio as living artifact
2. Update workflow
3. Versioned outputs
4. Review changes

### Demo result

Two portfolio versions with visible history.

### Do not cover

- Localization.
- Final human-agent review.

---

## Lecture 20: Localize the Portfolio Catalog and Graph

### Purpose

Show multilingual portfolio capability.

### Learning outcome

Learner localizes the combined catalog and graph into another language.

### Core message

The portfolio structure stays the same. The human-facing language changes.

### Content plan

Explain localization capability:

- The combined ODPC catalog can be translated.
- The ODPG graph can be translated.
- The same portfolio can support multiple audiences.
- Structure, IDs, and relationships remain stable.
- Labels, descriptions, and human-facing text change.

Explain why it matters:

- Regional teams can review in their language.
- Local governance teams can use localized artifacts.
- Public or internal portfolios can support multilingual users.
- AI agents can work with structured artifacts while humans read localized content.

### Hands-on

- Start from completed portfolio output.
- Select target language.
- Run localization for combined ODPC catalog.
- Run localization for ODPG graph.
- Review localized YAML.
- Check that IDs and relationships remain stable.
- Open localized HTML view if supported.

### Suggested slides

1. Why localization matters
2. What changes and what stays stable
3. Catalog localization
4. Graph localization
5. Multilingual portfolio package

### Demo result

Localized catalog and localized graph.

### Do not cover

- Translation theory.
- Manual translation workflow.
- Changing source artifacts.

---

## Lecture 21: Final Review: Human View and Agent-Ready YAML

### Purpose

Review the complete final package.

### Learning outcome

Learner understands the full value of the generated portfolio.

### Core message

The final output serves two audiences: humans and agents.

### Content plan

Review human-facing outputs:

- HTML portfolio view.
- Index page.
- Version history.
- Localized view if supported.
- Reviewable catalog structure.

Review agent-ready outputs:

- ODPC catalog YAML.
- ODPG graph YAML.
- Fragments.
- Localized YAML.
- Stable IDs and relationships.
- Files suitable for automation, validation, and AI workflows.

Explain review checklist:

- Are product references clear?
- Are use cases linked?
- Are business objectives represented?
- Are signals useful?
- Are graph relationships correct?
- Are localized outputs consistent?
- Are YAML files valid?

### Suggested slides

1. Human view
2. Agent-ready YAML
3. Review checklist
4. From course demo to real workflow

### Demo result

Walk through final output folder as a complete package.

### Do not cover

- New feature introduction.
- More generation examples.

---

## Lecture 22: Wrap-up and next steps

### Purpose

Close the course and point learners to practical use.

### Learning outcome

Learner knows how to apply the SDK workflow after the course.

### Core message

You now know how to move from business source material to validated, structured, multilingual, agent-ready data product portfolio artifacts.

### Content plan

Recap course journey:

- Standards family.
- SDK setup.
- Validation.
- Vocabulary helpers.
- Local and online generation.
- ODPS data product generation.
- Fragments.
- ODPG graphs.
- ODPC catalogs.
- Portfolio builder.
- Version history.
- Localization.
- Final review.

Explain next steps:

- Use your own source material.
- Start with one business area.
- Generate fragments.
- Review with humans.
- Build catalog and graph.
- Localize if needed.
- Keep portfolio versioned.
- Use YAML outputs for agents and automation.

### Suggested slides

1. What you built
2. Skills learned
3. Practical adoption path
4. Where to go next

### Final message

Do not sell the SDK as magic. Position it as a structured workflow that helps teams move from scattered business intent to reviewable, machine-readable data product portfolios.

---

## Quiz 3: Section 4 quiz

### Purpose

Check final workflow understanding.

### Suggested questions

- Why use portfolio builder after learning individual commands?
- What outputs does the portfolio builder create?
- Why is version history useful?
- What changes during localization?
- What should stay stable during localization?
- What is the difference between HTML output and YAML output?
- Why are catalogs and graphs both needed?
- How should teams review generated portfolio artifacts?
