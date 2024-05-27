import argparse
import os
from repartee import config, prompt_handler, output_formatter, spending_tracker
from repartee.api_clients import openai

def main():
    parser = argparse.ArgumentParser(description="Repartee CLI")
    parser.add_argument('--model', type=str, required=True, help="Select the AI model to use")
    parser.add_argument('--prompt', type=str, help="Provide a prompt")
    parser.add_argument('--temperature', type=float, default=0.7, help="Set the temperature for the model")
    parser.add_argument('--output', type=str, choices=['chat', 'repl', 'file'], default='chat', help="Select the output type")
    args = parser.parse_args()

    model_clients = {
        'gpt-4': openai,
        'gpt-4-turbo': openai,
        'gpt-3.5-turbo': openai,
        #'claude3': claude3,
        #'gemini15': gemini15,
        #'perplexity': perplexity
    }

    if args.model not in model_clients:
        print(f"Model {args.model} is not supported.")
        return

    client = model_clients[args.model]
    
    if not client.api_key_available():
        print(f"API key for {args.model} is not available.")
        return

    response = client.get_response(model=args.model, prompt=args.prompt, temperature=args.temperature)
    spending_tracker.track_usage(model=args.model, tokens_used=response['tokens'])

    if args.output == 'chat':
        print(response['text'])
    elif args.output == 'file':
        output_formatter.to_markdown(response['text'])
    elif args.output == 'repl':
        from repartee import repl
        repl.start_repl(client, args.temperature)

if __name__ == "__main__":
    main()