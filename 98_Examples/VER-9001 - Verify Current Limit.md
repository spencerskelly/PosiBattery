---
id: VER-9001
type: Verification
kind: test
status: Draft
aliases: []
tags: [model, example]
verifies: ["[[REQ-9001 - Limit Output Current]]"]
appliesTo: ["[[THG-9001 - Example Controller]]"]
startState: ["[[STATE-9001 - Ready]]"]
operatingState: ["[[STATE-9002 - Active]]"]
requiresSource: ["[[THG-9002 - DC Source]]"]
requiresLoad: ["[[THG-9003 - Electronic Load]]"]
---
# Verify Current Limit

Increase commanded current beyond the limit and verify the controller remains within the configured maximum.
