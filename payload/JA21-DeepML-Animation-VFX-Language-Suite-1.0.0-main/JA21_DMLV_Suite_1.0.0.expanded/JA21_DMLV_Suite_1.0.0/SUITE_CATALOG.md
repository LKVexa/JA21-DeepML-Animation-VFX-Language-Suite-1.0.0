# DeepML VFX Suite Catalog

## Publication profile

| Field | Value |
|---|---|
| Suite | JA21 DeepML Animation VFX Language Suite 1.0.0 |
| Language profile | `deepml.vfx` |
| Reference header | `deepml vfx 0.3` |
| Operating posture | Air-gapped, deterministic, no-network |
| Primary authoring mode | Code-first animation and VFX |

## Corpus composition

| Class | Records |
|---|---:|
| Positive | 7,875 |
| Negative | 2,060 |
| Certification | 65 |

## Script pack composition

| Class | Scripts |
|---|---:|
| Positive | 850 |
| Negative | 85 |
| Certification | 65 |

## Topic coverage

| Topic | Corpus records |
|---|---:|
| Attribute | 111 |
| Attribute Packing | 187 |
| Cache Scheduling | 187 |
| Cinematic Effects | 417 |
| Cloth | 167 |
| Collision Field | 167 |
| Compositing Node | 111 |
| Coupled Simulation | 416 |
| Cyclic Render Graph | 125 |
| Dead Pass Removal | 188 |
| Destruction | 167 |
| Destruction Sequence | 416 |
| Differentiable Vfx | 417 |
| Domain Tiling | 187 |
| Emitter | 111 |
| Fluid | 166 |
| Fluid Cloth Interaction | 416 |
| Force | 112 |
| Invalid Shader Type | 125 |
| Light | 111 |
| Lighting Compositing Pipeline | 417 |
| Lighting Graph | 167 |
| Mask | 166 |
| Material | 111 |
| Missing Cache | 125 |
| Multipass Compositing | 416 |
| Negative Lifetime | 125 |
| Node Fusion | 188 |
| Nondeterministic Sampling | 125 |
| Particle System | 111 |
| Portal Effect | 417 |
| Procedural Effect | 417 |
| R12 Mcrt Lowering | 188 |
| Render Graph Ordering | 188 |
| Render Pass | 111 |
| Render Target | 166 |
| Resource Hazard | 125 |
| Scene Timeline Binding | 417 |
| Shader Function | 167 |
| Shader Node | 111 |
| Shader Specialization | 187 |
| Temporal Cache | 417 |
| Tolerance Violation | 125 |
| Unstable Simulation | 125 |
| Volumetric | 167 |
| Weather System | 417 |

## Main artifacts

- `README.md` — suite orientation and architecture.
- `textbook/DEEPML_VFX_TEXTBOOK.md` — eighteen-chapter textbook.
- `script_pack_1000/catalog.csv` — filterable script catalog.
- `corpus/technical/deepml_vfx_technical_corpus_10000.jsonl.gz` — normalized master corpus.
- `grammar/deepml_vfx.ebnf` — editorial reference grammar.
- `compiler/compiler_contract.json` and `runtime/runtime_contract.json` — pipeline contracts.
- `tests/` — conformance and coverage artifacts.
- `tools/validate_suite.py` — offline integrity check.
- `reference_source/` — reconstructed source corpus and original upload.
