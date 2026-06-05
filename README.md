# Rule-Based AI Chatbot (Project 1)

A deterministic, high-efficiency "White-Box" AI chatbot built as the foundational layer for AI safety and guardrails. This project avoids the unstable $O(n)$ linear complexity of traditional if-elif ladders by utilizing an optimized hash map structure for instant, constant-time lookups.

## Architectural Features
* **IPO Model Architecture:** Implements a strict Input-Process-Output pipeline.
* **Phase 1 Sanitization:** Normalizes raw data inflow using string sanitization (`.lower().strip()`) to eliminate formatting variances.
* **Deterministic Logic Engine:** Implements an $O(1)$ constant-time lookup performance utilizing a Python dictionary structure.
* **Atomic Operation Handling:** Leverages the `.get()` fallback method to manage rule validation and fallback actions in a single atomic cycle.

## How to Run
1. Ensure you have Python installed.
2. Clone or download this directory.
3. Run the application via terminal:
```bash
   python chatbot.py