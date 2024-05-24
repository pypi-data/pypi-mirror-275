<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="850"
        src="https://media.roboflow.com/open-source/autodistill/autodistill-banner.png"
      >
    </a>
  </p>
</div>

# Autodistill GPT Module

This repository contains the code supporting the GPT (text) base model for use with [Autodistill](https://github.com/autodistill/autodistill).

You can use Autodistill GPT to classify text using OpenAI's GPT models for use in training smaller, fine-tuned text classification models. You can also use Autodistill GPT to use LLaMAfile text generation models.

Read the full [Autodistill documentation](https://autodistill.github.io/autodistill/).

## Installation

To use GPT or LLaMAfile models with Autodistill, you need to install the following dependency:

```bash
pip3 install autodistill-gpt-text
```

## Quickstart (LLaMAfile)

```python
from autodistill_gpt_text import GPTClassifier

# define an ontology to map class names to our GPT prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = GPTClassifier(
    ontology=CaptionOntology(
        {
            "computer vision": "computer vision",
            "natural language processing": "nlp"
        }
    ),
    base_url = "http://localhost:8080/v1", # your llamafile server
    model_id="LLaMA_CPP"
)

# label a single text
result = GPTClassifier.predict("This is a blog post about computer vision.")

# label a JSONl file of texts
base_model.label("data.jsonl", output="output.jsonl")
```

## Quickstart (GPT)

```python
from autodistill_gpt_text import GPTClassifier

# define an ontology to map class names to our GPT prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = GPTClassifier(
    ontology=CaptionOntology(
        {
            "computer vision": "computer vision",
            "natural language processing": "nlp"
        }
    )
)

# label a single text
result = GPTClassifier.predict("This is a blog post about computer vision.")

# label a JSONl file of texts
base_model.label("data.jsonl", output="output.jsonl")
```

The output JSONl file will contain all the data in your original file, with a new `classification` key in each entry that contains the predicted text label associated with that entry.

## License

This project is licensed under an [MIT license](LICENSE).

## 🏆 Contributing

We love your input! Please see the core Autodistill [contributing guide](https://github.com/autodistill/autodistill/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!
