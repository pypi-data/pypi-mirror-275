import sys
import argparse
import flowty


class kwargs_append_action(argparse.Action):
    """
    argparse action to split an argument into PARAM=VALUE form on append to a dictionary.
    """

    def __call__(self, parser, args, values, option_string=None):
        try:
            d = dict(map(lambda x: x.split("=", 1), values))
        except ValueError as ex:
            raise argparse.ArgumentError(
                self, f'Could not parse argument "{values}" as p1=v1 p2=v2 ... format'
            )
        setattr(args, self.dest, d)


def main():
    def version():
        from importlib.metadata import version
        return version("flowty")

    argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Flowty command line tool"
    )
    parser.add_argument("-v", "--version", action="version", version=version())
    parser.add_argument(
        "params",
        help="Parameters for the solver",
        nargs="*",
        default=[],
        type=str,
        action=kwargs_append_action,
        metavar="PARAM=VALUE",
    )
    parser.add_argument(
        "instance", help="Instance file in .lp/.mps and .graph format", type=str
    )
    args = parser.parse_args(argv)
    model = flowty.Model()
    for param, value in args.params.items():
        model.setParam(param, value)
    model.read(args.instance)
    model.solve()


if __name__ == "__main__":
    main()
