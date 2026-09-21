# Control Classification

## Purpose

Separate elements we own or intentionally modify from elements that are context for the model.

## Property

Use YAML property `control`.

| Value | Meaning | Typical use |
|---|---|---|
| `controlled` | We own the definition/behavior and may intentionally change it. | Product software, owned Functions, internal architecture |
| `modifiable` | We do not fully own it, but intentionally configure, maintain, annotate, or update part of it. | Partner configuration, maintained external data |
| `contextual` | We model it but do not control or modify the actual element. | External systems, users, regulations, environment |
| `reference` | Generic semantic definition used for classification. | Reusable type/taxonomy definitions |

`control` is independent from `boundary`, `subtypeOf`, `instanceOf`, and `status`.

Do not create a subtype merely because one occurrence is controlled and another is contextual.
