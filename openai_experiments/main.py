from openai_client import OpenAIClient
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument("--model", type=str, default="text-davinci-003")
parser.add_argument("--max_tokens", type=int, default=200)
parser.add_argument("--query", type=str, required=True)

args = parser.parse_args()

if __name__ == "__main__":
    client = OpenAIClient()

    response = client.completion(args.query, args.model, args.max_tokens)
    print(response)
