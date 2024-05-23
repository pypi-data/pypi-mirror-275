# SPDX-License-Identifier: Apache-2.0
#
# This file is part of the M2-ISA-R project: https://github.com/tum-ei-eda/M2-ISA-R
#
# Copyright (C) 2022
# Chair of Electrical Design Automation
# Technical University of Munich

"""Tranform M2-ISA-R metamodel to Seal5 metamodel."""

import argparse
import logging
import pathlib
import pickle

from m2isar.metamodel import arch
import seal5.model as seal5_model
from m2isar.metamodel.utils.expr_preprocessor import process_attributes, process_functions, process_instructions

logger = logging.getLogger("seal5_converter")


def main():
    """Main app entrypoint."""

    # read command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("top_level", help="A .m2isarmodel file containing the models to generate.")
    parser.add_argument("--log", default="info", choices=["critical", "error", "warning", "info", "debug"])
    parser.add_argument("--prefix", default="", type=str)
    parser.add_argument("--output", "-o", type=str, default=None)
    args = parser.parse_args()

    # initialize logging
    logging.basicConfig(level=getattr(logging, args.log.upper()))

    # resolve model paths
    top_level = pathlib.Path(args.top_level)
    # abs_top_level = top_level.resolve()

    if args.output is None:
        assert top_level.suffix == ".m2isarmodel", "Can not infer file extension."
        temp = str(top_level)
        temp = temp.replace(".m2isarmodel", ".seal5model")
        model_path = pathlib.Path(temp)
    else:
        model_path = pathlib.Path(args.output)
    # model_path.mkdir(exist_ok=True)

    logger.info("loading models")

    new_model = {}

    # load models
    with open(top_level, "rb") as f:
        # models: "dict[str, arch.CoreDef]" = pickle.load(f)
        sets: "dict[str, arch.InstructionSet]" = pickle.load(f)

    # preprocess model
    for set_name, set_def in sets.items():
        logger.info("preprocessing set %s", set_name)
        process_functions(set_def)
        process_instructions(set_def)
        process_attributes(set_def)

    for set_name, set_def in sets.items():
        logger.info("replacing set %s", set_name)
        for enc, instr_def in set_def.instructions.items():
            if args.prefix:
                instr_def.name = f"{args.prefix.upper()}{instr_def.name}"
                prefix_ = args.prefix.lower().replace("_", ".")
                instr_def.mnemonic = f"{prefix_}{instr_def.mnemonic}"
            set_def.instructions[enc] = seal5_model.Seal5Instruction(
                instr_def.name,
                instr_def.attributes,
                instr_def.encoding,
                instr_def.mnemonic,
                instr_def.assembly,
                instr_def.operation,
                [],
                {},
            )
        sets[set_name] = seal5_model.Seal5InstructionSet(
            set_def.name,
            set_def.extension,
            set_def.constants,
            set_def.memories,
            set_def.functions,
            set_def.instructions,
            {},
            {},
            {},
            {},
            {},
        )

    new_model["sets"] = sets

    logger.info("dumping model")
    with open(model_path, "wb") as f:
        pickle.dump(new_model, f)


if __name__ == "__main__":
    main()
