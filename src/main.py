from src._types.args import ArgsModel


def main(args: ArgsModel) -> None:
    if args.verbose:
        print(f"Input file: {args.filename}")
        print(f"Output file: {args.output}")
        if args.format:
            print(f"Output format: {args.format}")
        else:
            print("Output format: wav (default)")
    print("Hello from final!")
