import argparse

from data_loader import load_and_cache_examples
from utils import init_logger


def main(args):
    init_logger()

    tokenizer = 0 # TODO: load tokenizer
    train_dataset = load_and_cache_examples(args, tokenizer, mode="train")


if __name__ == '__main__': # prevents this code from being executed when we don't want to
    parser = argparse.ArgumentParser()

    parser.add_argument("--task", default="ynat", type=str, help="The name of the task to train")

    parser.add_argument("--data_dir", default="./data", type=str, help="The input data dir")
    parser.add_argument("--train_file", default="minidata.json", type=str, help="Train file")

    args = parser.parse_args()
    main(args)