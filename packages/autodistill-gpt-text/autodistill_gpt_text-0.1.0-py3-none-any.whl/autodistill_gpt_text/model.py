import concurrent.futures
import json
import os
from dataclasses import dataclass

import torch
from autodistill.text_classification import TextClassificationOntology
from openai import OpenAI
from tqdm import tqdm

HOME = os.path.expanduser("~")
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


@dataclass
class GPTClassifier:
    ontology: TextClassificationOntology

    def __init__(self, ontology: TextClassificationOntology, api_key: str, model_id = "gpt-3.5-turbo", model_base_url: str = None):
        if model_base_url is None:
            self.client = OpenAI(api_key=api_key)
        else:
            self.client = OpenAI(api_key=api_key, base_url=model_base_url)

        self.ontology = ontology
        self.model_id = model_id

    def predict(self, input: str) -> str:
        classification = self.client.chat.completions.create(
            model=self.model_id,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a text classifier. Classify the following text as either {', '.join(self.ontology.prompts())}. Only return the label name.",
                },
                {"role": "user", "content": input},
            ],
        )

        for label, caption in self.ontology.promptMap.items():
            if caption == classification.choices[0].message.content:
                return label

        return None

    def label(self, input_jsonl: str, output_jsonl: str = "output.jsonl") -> None:
        with open(input_jsonl, "r") as f:
            records = f.readlines()

        results = []

        all_records = []

        for record in tqdm(records):
            record = json.loads(record)
            all_records.append(record)

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(
                executor.map(
                    self.predict, [record["content"] for record in all_records]
                )
            )

        for record, result in zip(all_records, results):
            record["classification"] = result

        with open(output_jsonl, "w") as f:
            for record in results:
                f.write(json.dumps(record) + "\n")
