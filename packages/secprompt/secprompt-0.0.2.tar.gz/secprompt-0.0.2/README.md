# SecPrompt: Protect your LLM-integrated applications

The tool uses the analysis model and two analysis mechanisms (intention analysis and behavior analysis) to detect prompt injection attack. 

**Analysis Model**

Through experiments, it is currently to achieve good attack detection results by letting GPT-3.5-turbo serve as an analysis model.

**two Analysis Mechanisms**

- Intent Analysis(IA): analyze the essential intention of the user prompt before transmitting it to the LLM integrated application, using it as context.
- Behavioral Analysis(BA): decompose user prompt tasks and mobilize analysis models to conduct security checks at each step.

## Installation

```python
# install from PyPI
pip install secprompt
```
