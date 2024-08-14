
# Create you own Financial Analyst using MLX, Llama3 and Langchain

This project involves fine-tuning the llama 3 8B Instruct model on SEC 10k filing reports to generate financial insights.


## Installation

Setup the Environment.

```bash
conda env create -f environment.yml

```

Also login using huggingface-cli to download the model and the dataset.

```bash
huggingface-cli login

```

Refer to the [huggingface website](https://huggingface.co/docs/huggingface_hub/en/guides/cli) for authentication and generating access-tokens. 

To get sec 10-filings run the following script 

```bash
python crawler.py --name Your-name --ticker company-ticker --email youremail@example.com --start start-year --end end-year

```

## Run Locally

Run the cells in the jupyter notebook in order to fine-tune and run inference on the model. 

The parser code has been borrowed from [this repo](https://github.com/rsljr/edgarParser/tree/master?tab=readme-ov-file).




## Useful Links

[Build Your Own Finance LLM for FREE with SEC Data](https://www.youtube.com/watch?v=GfjUJ1TnI-o)

[Local LLM Fine-tuning on Mac](https://www.youtube.com/watch?v=3PIqhdRzhxE)

[MLX Examples](https://github.com/ml-explore/mlx-examples/tree/main)