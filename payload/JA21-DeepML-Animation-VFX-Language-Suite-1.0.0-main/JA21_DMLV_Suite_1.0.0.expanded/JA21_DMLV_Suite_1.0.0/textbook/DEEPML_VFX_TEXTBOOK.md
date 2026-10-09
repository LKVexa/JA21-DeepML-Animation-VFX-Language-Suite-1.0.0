# DEEPML VFX
## A Standalone JA21 Language Suite for Animation, Simulation, Rendering, and Compositing

**Textbook edition:** 1.0.0  
**Language profile:** `deepml.vfx`  
**Reference syntax:** `deepml vfx 0.3`  
**Publication architecture:** SOPHIA · CHARLOTTE · LANDON · Professor + Podium

---

## Preface

This book turns the original DeepML Animation VFX corpus into a coherent language course and engineering reference. It is written for technical artists, animator-programmers, simulation engineers, compiler developers, and reviewers who need to understand both the expressive surface of the language and the evidence required for deterministic execution. The book is intentionally paired with the normalized 10,000-record technical corpus and the 1,000-script example pack.

The suite treats visual authoring as code-first engineering. A script is not only an instruction to produce an image; it is a governed declaration with types, policies, provenance, expected compiler behavior, runtime evidence, and replay obligations. This approach supports air-gapped environments and helps separate the artistic decision from implementation accidents.

## How to Use This Book

Read Chapters 1–3 before editing examples. Chapters 4–11 cover production domains. Chapters 12–16 cover optimization, compiler semantics, diagnostics, and 8S coupling. Chapters 17–18 turn the material into studio practice. Each chapter ends with a laboratory, review questions, and an evidence checklist. The script catalog can be filtered by topic, class, tier, and expected stage.


# Chapter 1: The Language and Its Place in JA21

DeepML VFX is the animation, simulation, rendering, and compositing language profile of the JA21 suite. It is designed as a declarative language: authors describe effects, resources, policies, and relationships, while the compiler proves as much as possible before runtime. The standalone suite preserves the original 0.3 language identity while adding a publication layer, a normalized corpus, a curated script library, and a complete learning path.


## Core Model


The language is organized around declarations rather than imperative loops. Particle systems, simulations, shader interfaces, render passes, caches, and composites are named artifacts. This makes dependencies visible to the compiler and supports static checks before any expensive runtime work begins. The standalone suite retains the original namespace root and MCRT profile, so corpus records remain traceable.

A DeepML package should answer five questions: What is being declared? Which resources does it read and write? Which policies govern execution? Which compiler and runtime evidence proves admission? Which hashes and identifiers make the result replayable?


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 2: Program Anatomy and Policy Envelopes

Every DeepML VFX program begins with a version header and module identity. Policies are not decorative metadata; they constrain compiler admission and runtime behavior. The canonical standalone profile requires deterministic execution, no network access, stable identifiers, provenance preservation, and rejection of unknown code execution.


## Core Model


The canonical envelope is a header, module, policies, and one or more declarations. `policy deterministic` requires stable ordering, stable random streams, and declared provider behavior. `policy no_network` forbids runtime retrieval. Provenance records the origin of source, assets, caches, compiler profile, and semantic transformations. A policy failure occurs before runtime admission.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00002
policy deterministic
policy no_network
particle_system Effect00002 {
  emitter Main rate 12/s lifetime 3s seed 2
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 0.5 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00002] target Color
composite Color over SceneColor
```


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 3: Types, Units, Spaces, and Resources

Animation systems fail when values are numerically plausible but semantically incompatible. DeepML therefore treats vectors, colors, durations, rates, textures, depth targets, coordinate spaces, and provider-bound resources as typed entities. Units and spaces should be explicit at interfaces, and conversions must be intentional rather than inferred from appearance.


## Core Model


Type checking should reject incompatible shader stage interfaces, color spaces, texture formats, vector dimensions, and resource roles. A rate is not a duration; a world-space vector is not automatically a tangent-space vector; a premultiplied color is not interchangeable with straight alpha. Explicit conversions should be represented as named operations so they remain visible in AST, R12, and replay evidence.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 4: Particles, Emitters, Attributes, and Forces

Particles are compact state records updated by a deterministic schedule. Emitters define creation; attributes define state; forces define motion; shaders and materials define appearance. Stable random streams derive from declared seeds and semantic identifiers so batching, parallelism, or platform changes do not silently alter results.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Particle System

Defines a deterministic particle domain, its emitters, attributes, forces, materials, and render participation.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00004
policy deterministic
policy no_network
particle_system Effect00004 {
  emitter Main rate 14/s lifetime 5s seed 4
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 0.7 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00004] target Color
composite Color over SceneColor
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Emitter

Creates particles according to a stable rate, lifetime distribution, shape, and seed-derived random stream.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00003
policy deterministic
policy no_network
particle_system Effect00003 {
  emitter Main rate 13/s lifetime 4s seed 3
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 0.6 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00003] target Color
composite Color over SceneColor
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Force

Applies deterministic acceleration or field response while preserving unit and coordinate-space contracts.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00001
policy deterministic
policy no_network
particle_system Effect00001 {
  emitter Main rate 11/s lifetime 2s seed 1
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 0.4 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00001] target Color
composite Color over SceneColor
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 5: Fields, Collisions, and Spatial Coupling

A field maps space and time to a response. Collision fields add signed distance, contact normal, friction, restitution, and tolerance behavior. Coupled fields must declare order, update sequence, and any higher-order interaction. The compiler should reject ambiguous space conversions or cyclic dependencies without delayed feedback.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Collision Field

Collision Field is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01004
policy deterministic
policy no_network
effect Effect01004 {
  fluid Smoke { grid: [76,76,60] solver: stable_fluids }
  cloth Banner { resolution: [28,28] stiffness: 0.5 }
  destruction Debris { pieces: 52 fracture: voronoi seed: 1004 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.5 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Coupled Simulation

Coupled Simulation is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_02505
policy deterministic
policy no_network
effect Effect02505 {
  coupled simulation PortalSim seed 2505 { fluid: Energy cloth: Veil particles: Sparks }
  procedural operator Distort(time, portal_state) differentiable
  cache PortalCache8 interval 0s..10s step 1/60s hash sha256("cache:02505")
  bind scene PortalScene6
  bind timeline PortalSequence9
  render_graph { Sim -> Lighting -> Distortion -> Composite }
  composite multipass [SceneColor, PortalGlow, Distortion, Atmosphere]
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 6: Fluids and Volumetric Effects

Fluid and volumetric systems combine numerical simulation with rendering. A robust declaration identifies the state representation, boundary conditions, advection, pressure solve, substeps, stability thresholds, cache format, and render adapter. Quality settings are semantic when they affect visible or certifying output; optimizers may not change them without an explicit equivalence profile.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Fluid

Defines fluid state, boundaries, solver tolerances, substeps, cache schema, and a render adapter.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01007
policy deterministic
policy no_network
effect Effect01007 {
  fluid Smoke { grid: [79,79,63] solver: stable_fluids }
  cloth Banner { resolution: [31,31] stiffness: 0.8 }
  destruction Debris { pieces: 55 fracture: voronoi seed: 1007 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.8 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Volumetric

Represents density, temperature, emission, scattering, and bounded spatial sampling for smoke, fog, fire, and clouds.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01003
policy deterministic
policy no_network
effect Effect01003 {
  fluid Smoke { grid: [75,75,59] solver: stable_fluids }
  cloth Banner { resolution: [27,27] stiffness: 0.4 }
  destruction Debris { pieces: 51 fracture: voronoi seed: 1003 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.4 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Weather System

Weather System is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_05001
policy deterministic
policy no_network
vfx_package Effect05001 {
  weather system Weather3 { wind: vec3(2,0,1) rain: 601/s }
  destruction sequence Collapse1 bind timeline.Destruction
  interaction fluid Smoke with cloth Banner collision two_way
  portal effect Portal6 { particles: Sparks volumetric: Fog shader: Distortion }
  lighting pipeline { key: Sun fill: PortalGlow exposure: auto_deterministic }
  compositing pipeline { passes: [Scene, Weather, Portal, Grade] }
}
package vfx Effect05001 as "vfx_05001.msslb"
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 7: Cloth and Coupled Simulation

Cloth binds topology to physical constraints. Source mesh hashes, mass distribution, stretch, shear, bend, pins, collision geometry, solver order, tear policy, and cache identity belong in the reproducibility envelope. Coupled simulation adds cross-domain exchange, such as fluid pressure acting on cloth and cloth displacement altering the fluid boundary.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Cloth

Binds a source mesh to mass, stretch, shear, bend, pin, collision, and tear policies.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01006
policy deterministic
policy no_network
effect Effect01006 {
  fluid Smoke { grid: [78,78,62] solver: stable_fluids }
  cloth Banner { resolution: [30,30] stiffness: 0.7 }
  destruction Debris { pieces: 54 fracture: voronoi seed: 1006 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.7 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Fluid Cloth Interaction

Fluid Cloth Interaction is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_05005
policy deterministic
policy no_network
vfx_package Effect05005 {
  weather system Weather0 { wind: vec3(2,0,1) rain: 605/s }
  destruction sequence Collapse0 bind timeline.Destruction
  interaction fluid Smoke with cloth Banner collision two_way
  portal effect Portal1 { particles: Sparks volumetric: Fog shader: Distortion }
  lighting pipeline { key: Sun fill: PortalGlow exposure: auto_deterministic }
  compositing pipeline { passes: [Scene, Weather, Portal, Grade] }
}
package vfx Effect05005 as "vfx_05005.msslb"
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 8: Destruction, Fracture, and Reassembly

Destruction is a graph problem as much as a geometry problem. Fracture pieces form nodes; constraints form edges; events activate failures; debris classes choose collision and render behavior. Deterministic caches record source hashes, fracture parameters, seeds, toolchain identity, and output hashes. Reassembly and reset behavior should be explicit.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Destruction

Defines fracture and constraint graphs, activation events, debris classes, and deterministic cache provenance.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01014
policy deterministic
policy no_network
effect Effect01014 {
  fluid Smoke { grid: [86,86,22] solver: stable_fluids }
  cloth Banner { resolution: [38,38] stiffness: 0.8 }
  destruction Debris { pieces: 62 fracture: voronoi seed: 1014 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.7 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Destruction Sequence

Destruction Sequence is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_05006
policy deterministic
policy no_network
vfx_package Effect05006 {
  weather system Weather1 { wind: vec3(2,0,1) rain: 606/s }
  destruction sequence Collapse1 bind timeline.Destruction
  interaction fluid Smoke with cloth Banner collision two_way
  portal effect Portal2 { particles: Sparks volumetric: Fog shader: Distortion }
  lighting pipeline { key: Sun fill: PortalGlow exposure: auto_deterministic }
  compositing pipeline { passes: [Scene, Weather, Portal, Grade] }
}
package vfx Effect05006 as "vfx_05006.msslb"
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 9: Shaders, Materials, and Lighting

Shader declarations expose typed stage interfaces and resource bindings. Materials connect shader functions to textures, blending, and surface parameters. Lighting adapters declare color space, exposure, coordinate space, sampling policy, shadow participation, and volumetric response. External compiler or GPU providers are trusted boundaries and must be named in provenance.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Shader Node

Declares a typed shader operation with stable inputs, outputs, resource bindings, and provider boundaries.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00009
policy deterministic
policy no_network
particle_system Effect00009 {
  emitter Main rate 19/s lifetime 2s seed 9
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 1.2 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00009] target Color
composite Color over SceneColor
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Material

Connects shader graphs, textures, blend modes, surface parameters, and color-space conventions.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_00008
policy deterministic
policy no_network
particle_system Effect00008 {
  emitter Main rate 18/s lifetime 1s seed 8
  attribute position: vec3
  attribute velocity: vec3
  force gravity vec3(0,-9.81,0)
  shader node ColorOverLife { input age output color }
  material PortalMat { shader: ColorOverLife blend: additive }
  light Glow { intensity: 1.1 color: rgb(0.2,0.5,1.0) }
}
render_pass MainPass inputs [Effect00008] target Color
composite Color over SceneColor
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Lighting Graph

Coordinates lights, probes, volumetric participation, exposure, shadowing, and scene adapters.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_01002
policy deterministic
policy no_network
effect Effect01002 {
  fluid Smoke { grid: [74,74,58] solver: stable_fluids }
  cloth Banner { resolution: [26,26] stiffness: 0.3 }
  destruction Debris { pieces: 50 fracture: voronoi seed: 1002 }
  collision_field WorldSDF source scene.Collider
  volumetric Fog { density: 0.3 }
  shader function ShadePortal(x: vec3) -> color
  render_target FXColor format rgba16f
  mask PortalMask source scene.PortalA
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 10: Render Graphs and Resource Lifetimes

A render graph is a dependency graph of passes and resources. Reads require prior initialization; simultaneous writes require a merge rule; aliasing requires nonoverlapping liveness; feedback requires an explicitly delayed resource. Stable topological ordering and transparent barrier insertion are essential for replay and cross-platform diagnostics.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Render Graph Ordering

Derives a stable pass order from declared read/write dependencies and delayed feedback edges.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_07501
policy deterministic
policy no_network
render_graph Effect07501 {
  pass A { shader: Shared inputs: [Position, Velocity] }
  pass B { shader: Shared inputs: [Position, Velocity] }
  pass Dead enabled false
  cache C frames 0..85
  domain Sim tiles [3,3,2]
}
optimize Effect07501 using [node_fusion, dead_pass_removal, attribute_packing, shader_specialization, cache_scheduling, domain_tiling, render_graph_ordering]
lower Effect07501 to DEEPML_VFX_R12
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Resource Hazard

Rejects unsafe overlapping reads/writes, missing barriers, aliasing without liveness proof, or uninitialized resources.


```deepml
deepml vfx 0.3
module textbook.placeholder
policy deterministic
policy no_network
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 11: Compositing, Masks, and Temporal Systems

Compositing combines layers under strict format, dimensions, color-space, alpha, depth, and motion-vector contracts. Temporal accumulation introduces history resources and therefore versioning, invalidation, and camera-cut behavior. A missing or stale cache is a semantic problem when the result depends on prior frames.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Multipass Compositing

Combines typed image layers using masks, depth, motion vectors, premultiplication, and color transforms.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_02506
policy deterministic
policy no_network
effect Effect02506 {
  coupled simulation PortalSim seed 2506 { fluid: Energy cloth: Veil particles: Sparks }
  procedural operator Distort(time, portal_state) differentiable
  cache PortalCache9 interval 0s..10s step 1/60s hash sha256("cache:02506")
  bind scene PortalScene7
  bind timeline PortalSequence10
  render_graph { Sim -> Lighting -> Distortion -> Composite }
  composite multipass [SceneColor, PortalGlow, Distortion, Atmosphere]
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Temporal Cache

Stores versioned simulation or image history with source hashes, parameter hashes, frame range, and replay rules.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_02503
policy deterministic
policy no_network
effect Effect02503 {
  coupled simulation PortalSim seed 2503 { fluid: Energy cloth: Veil particles: Sparks }
  procedural operator Distort(time, portal_state) differentiable
  cache PortalCache6 interval 0s..10s step 1/60s hash sha256("cache:02503")
  bind scene PortalScene4
  bind timeline PortalSequence7
  render_graph { Sim -> Lighting -> Distortion -> Composite }
  composite multipass [SceneColor, PortalGlow, Distortion, Atmosphere]
}
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 12: Optimization Without Semantic Drift

Optimization is permitted only when the declared equivalence class is preserved. Safe examples include dead-pass removal, node fusion with identical numeric behavior, attribute packing that preserves layout contracts, domain tiling with equivalent boundaries, and cache scheduling that does not change dependencies. Every optimization should emit evidence describing what changed and why the result remains equivalent.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Dead Pass Removal

Dead Pass Removal is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_07512
policy deterministic
policy no_network
render_graph Effect07512 {
  pass A { shader: Shared inputs: [Position, Velocity] }
  pass B { shader: Shared inputs: [Position, Velocity] }
  pass Dead enabled false
  cache C frames 0..96
  domain Sim tiles [2,2,1]
}
optimize Effect07512 using [node_fusion, dead_pass_removal, attribute_packing, shader_specialization, cache_scheduling, domain_tiling, render_graph_ordering]
lower Effect07512 to DEEPML_VFX_R12
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Node Fusion

Node Fusion is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_07503
policy deterministic
policy no_network
render_graph Effect07503 {
  pass A { shader: Shared inputs: [Position, Velocity] }
  pass B { shader: Shared inputs: [Position, Velocity] }
  pass Dead enabled false
  cache C frames 0..87
  domain Sim tiles [5,5,1]
}
optimize Effect07503 using [node_fusion, dead_pass_removal, attribute_packing, shader_specialization, cache_scheduling, domain_tiling, render_graph_ordering]
lower Effect07503 to DEEPML_VFX_R12
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Attribute Packing

Attribute Packing is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_07505
policy deterministic
policy no_network
render_graph Effect07505 {
  pass A { shader: Shared inputs: [Position, Velocity] }
  pass B { shader: Shared inputs: [Position, Velocity] }
  pass Dead enabled false
  cache C frames 0..89
  domain Sim tiles [3,3,3]
}
optimize Effect07505 using [node_fusion, dead_pass_removal, attribute_packing, shader_specialization, cache_scheduling, domain_tiling, render_graph_ordering]
lower Effect07505 to DEEPML_VFX_R12
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 13: Compiler Pipeline, AST, R12, and MCRT

The reference compiler proceeds through lexing, parsing, AST construction, name resolution, type checking, semantic validation, safety gating, normalization, optimization, R12 lowering, and MCRT emission. The AST preserves source spans and semantic identity. R12 captures relation, operator, vector, sequence, time, state, error, confidence, and status. MCRT provides a stable machine-readable record for replay and cross-suite routing.


## Core Model


Lexing and parsing establish syntactic structure. Name resolution binds identifiers. Type checking validates interfaces. Semantic validation checks domain rules. The safety gate enforces policies. Normalization makes equivalent forms comparable. Optimization is evidence-bearing. R12 lowering captures the semantic relation. MCRT emission creates a stable cross-runtime record. A failure at any stage should prevent later representations from being presented as admitted output.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 14: Runtime, Caches, Replay, and Provenance

The runtime admits only validated packages. It records entrypoints, effects, expected hashes, failure stages, route information, provider versions, cache identities, and deterministic traces. Reproducibility is not merely repeating a picture; it is repeating the semantic route, policy outcome, and declared tolerance result.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 15: Diagnostics and Negative Examples

Negative examples are first-class teaching assets. They show where a program must fail: cyclic render graphs, invalid shader types, missing caches, negative lifetimes, nondeterministic sampling, resource hazards, tolerance violations, and unstable simulation. A good diagnostic names the stage, identifies the responsible declaration, explains the violated contract, and proposes a bounded repair.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Cyclic Render Graph

Cyclic Render Graph is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_09002
policy deterministic
policy no_network
effect Effect09002 { render_graph G { A -> B B -> A } }
certify vfx Effect09002 profile strict
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Invalid Shader Type

Invalid Shader Type is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_09003
policy deterministic
policy no_network
effect Effect09003 { shader S { output color: matrix4 } }
certify vfx Effect09003 profile strict
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Nondeterministic Sampling

Detects random or provider behavior that lacks a declared seed, stable stream partition, or replay identity.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_09008
policy deterministic
policy no_network
effect Effect09008 { sampler S seed none mode random_device }
certify vfx Effect09008 profile strict
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 16: Smithson 8S Coupled Mechanics Integration

The 8S profile adds a five-dimensional latent base with an S^3 fiber, independent elucidation admission, sparse pairwise coupling, selective triadic escalation, and separate tests for latent, product-state, projected, and semantic relations. The compiler must retain claim boundaries: local noncollapsed dimension is eight, but this does not establish standard S^8 topology or physical quantum entanglement.


## Core Model


The fifth coordinate is admitted only when its residual lies materially outside the span of the prior four coordinates, has a declared meaning, and improves held-out efficacy after cost. Pairwise weights combine latent geometry and judgement-space distance. Triadic terms are activated only for unresolved, contradictory, high-risk, or certification-critical clusters. Projection-only overlap must never be rewritten as latent coupling.

Key equations include `eta_ind = ||e_perp||^2 / (||e||^2 + epsilon)`, the sparse weight `W_ij`, phase dynamics, activation support, radius, latent gap `g5`, product-state separation `delta8`, projected gap `g3`, semantic gap `gJ`, and efficacy gain `Delta_8S`.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 17: Using the 1,000-Script Example Pack

The example pack is divided into foundations, simulation, rendering, optimization, diagnostics, and specialized cases. It contains 850 positive programs, 85 negative programs, and all 65 certification records from the source corpus. Each script maps back to a canonical corpus identifier, hashes, expected stage, and explanatory record in the catalog.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Worked Pattern: Portal Effect

Portal Effect is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_05004
policy deterministic
policy no_network
vfx_package Effect05004 {
  weather system Weather6 { wind: vec3(2,0,1) rain: 604/s }
  destruction sequence Collapse4 bind timeline.Destruction
  interaction fluid Smoke with cloth Banner collision two_way
  portal effect Portal0 { particles: Sparks volumetric: Fog shader: Distortion }
  lighting pipeline { key: Sun fill: PortalGlow exposure: auto_deterministic }
  compositing pipeline { passes: [Scene, Weather, Portal, Grade] }
}
package vfx Effect05004 as "vfx_05004.msslb"
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Worked Pattern: Cinematic Effects

Cinematic Effects is represented in the corpus with positive and diagnostic cases.


```deepml
deepml vfx 0.3
module corpus.deepml_vfx.example_05002
policy deterministic
policy no_network
vfx_package Effect05002 {
  weather system Weather4 { wind: vec3(2,0,1) rain: 602/s }
  destruction sequence Collapse2 bind timeline.Destruction
  interaction fluid Smoke with cloth Banner collision two_way
  portal effect Portal7 { particles: Sparks volumetric: Fog shader: Distortion }
  lighting pipeline { key: Sun fill: PortalGlow exposure: auto_deterministic }
  compositing pipeline { passes: [Scene, Weather, Portal, Grade] }
}
package vfx Effect05002 as "vfx_05002.msslb"
```


**Reading the example.** The header identifies the profile; the module provides stable scope; policies govern admission; declarations expose the effect graph; and compiler metadata in the corpus explains the expected stage and result. Treat numeric values as authored parameters rather than universal defaults.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Chapter 18: Studio Workflow and Capstone Practice

A production workflow moves from intent to typed declarations, validation, preview, cache generation, render graph integration, replay capture, and package publication. Capstone work should demonstrate not only a compelling visual effect but also deterministic behavior, explicit policies, stable provenance, bounded tolerances, diagnostics, and a clear separation between latent mechanics and projected appearance.


## Core Model


The domain should be declared in a way that exposes inputs, outputs, tolerances, update order, dependencies, and replay identity. Compiler validation should distinguish syntax, type, semantic, safety, and runtime-validation failures. Runtime evidence should identify the admitted package, providers, caches, and stable result hash.


## Engineering Rules

1. Declare semantic identity before optimization.  
2. Preserve source spans, hashes, and provenance across lowering.  
3. Reject implicit network access and unknown code execution.  
4. Make random streams seedable and partition-stable.  
5. Separate latent mechanics, runtime state, and projected appearance.  
6. Record tolerances and failure stages rather than hiding uncertainty.


## Laboratory

Create or modify one script from the corresponding category in `script_pack_1000`. Change one parameter, predict the compiler and runtime consequences, update the module identity, and write a replay note. For diagnostic chapters, repair the program without weakening the governing policy. For 8S work, report latent, product-state, projected, and semantic results independently.


## Review Questions

- Which declarations carry semantic identity?
- Which compiler stage should reject the most likely error?
- Which values must be hashed or versioned for replay?
- Which optimization would be unsafe without an equivalence proof?
- What evidence distinguishes a visual overlap from a latent relation?


## Evidence Checklist

- [ ] Header and module are present.
- [ ] Policies are explicit.
- [ ] Types, spaces, units, and resource roles are compatible.
- [ ] Randomness and provider behavior are deterministic or explicitly bounded.
- [ ] R12 and MCRT identity can be reconstructed.
- [ ] Runtime and cache provenance are preserved.
- [ ] Tolerances, uncertainty, and limitations are reported.


# Appendix A: Compact Syntax Reference

The normative editorial grammar is located at `grammar/deepml_vfx.ebnf`. The core envelope is:

```text
deepml vfx <version>
module <qualified.name>
policy <policy.name>
<declarations>
```

Primary declaration families include effects, particle systems, emitters, attributes, forces, simulations, shaders, materials, lights, render graphs, passes, resources, caches, masks, and composites. The 8S editorial extension adds `coupling8s` with identity, geometry, elucidation, activation, phase, coupling, projection, relation, efficacy, and certification fields.


# Appendix B: Diagnostic Study Set

Use the negative scripts for deliberate compiler study. Do not treat a rejected program as a runtime test. Record the first failing stage, the diagnostic identifier, the violated contract, the minimal repair, and whether the repaired program preserves the original artistic intent.


# Appendix C: Twelve-Week Course

1. Language envelope and policies  
2. Types, units, spaces, and resources  
3. Particles and emitters  
4. Fields and collisions  
5. Fluids and volumetrics  
6. Cloth and coupled simulation  
7. Destruction and caches  
8. Shaders, materials, and lighting  
9. Render graphs and compositing  
10. Optimization and compiler evidence  
11. Diagnostics, replay, and 8S coupling  
12. Capstone presentation and conformance review


# Appendix D: Glossary

**AST** — Structured representation preserving syntax, source spans, and semantic identity.  
**R12** — Relation-oriented lowering record containing vector, relation, operator, sequence, depth, state, error, time, confidence, and status.  
**MCRT** — Stable machine-readable semantic record used for routing, replay, and cross-suite integration.  
**Replay identity** — The set of source, semantic, asset, provider, cache, projection, and policy identifiers required to reproduce an admitted result.  
**Projection-only** — A case where visible overlap occurs without latent coupling under the declared tolerances.  
**Semantic drift** — A change in behavior or identity introduced by translation, optimization, caching, or provider substitution.  
**Provider boundary** — A named external compiler, runtime, renderer, or solver whose version and trust status must be recorded.
