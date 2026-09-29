import argparse
import os
import sys

from openai import OpenAI


def main():
    ap = argparse.ArgumentParser(prog="chatsh")
    ap.add_argument("prompt", nargs="*")
    ap.add_argument("--model",
                    default=os.environ.get("MODEL", "gpt-4o-mini"))
    ap.add_argument("--system",
                    default="You are concise and precise.")
    ap.add_argument("--no-stream", action="store_true")
    args = ap.parse_args()

    prompt = " ".join(args.prompt).strip() or sys.stdin.read()
    if not prompt:
        ap.error("empty prompt")
    client = OpenAI()  # reads OPENAI_API_KEY / OPENAI_BASE_URL
    msgs = [{"role": "system", "content": args.system},
            {"role": "user", "content": prompt}]
    if args.no_stream:
        r = client.chat.completions.create(model=args.model, messages=msgs)
        print(r.choices[0].message.content)
        return
    stream = client.chat.completions.create(
        model=args.model, messages=msgs, stream=True)
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        sys.stdout.write(delta)
        sys.stdout.flush()
    print()


if __name__ == "__main__":
    main()
