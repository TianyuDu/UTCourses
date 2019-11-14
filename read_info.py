import pandas as pd
import argparse


def find_matched():
    raise NotImplementedError


def print_matched(matched: pd.DataFrame):
    LONG = "****************"
    print(LONG + "Result(s)" + LONG)
    for m in matched.values:
        print(*m[1:3])
        print(m[-1])
        print(LONG * 3)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir")
    parser.add_argument("course")
    args = parser.parse_args()
    df = pd.read_csv(f"{args.dir}/{args.course[:3]}.csv")
    matched = df[[args.course.upper() in x for x in df["Code"]]]
    print_matched(matched)
