#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json

from nalibsUtils import json_writer, yaml_writer, yaml_reader

# from .__base import init_logging
try:
    from .__base import init_logging
except ImportError:
    from __base import init_logging

# from .__version import __version__
try:
    from .__version import __version__
except ImportError:
    from __version import __version__

# from .common import NotFoundError, Exit, export_dotenv_config
try:
    from .common import NotFoundError, Exit, export_dotenv_config
except ImportError:
    from common import NotFoundError, Exit, export_dotenv_config

# from .aws_sm_func import get_secret
try:
    from .aws_sm_func import get_secret
except ImportError:
    from aws_sm_func import get_secret

try:
    from .eks_func import update_config_map
except ImportError:
    from eks_func import update_config_map


class OutputFormat:
    def __init__(self, cmdargs: argparse.Namespace, secrets_values, output_filepath):
        self.secrets_values = secrets_values
        self.cmdargs = cmdargs
        self.output_filepath = output_filepath

    def output(self):
        pass


class HumanOutputFormat(OutputFormat):
    def output(self):
        sys.stdout.write(self.secrets_values)
        # for k, v in self.secrets_values.items():
        #     print("{key}={value}".format(key=k,value=v))


class JSONOutputFormat(OutputFormat):
    def output(self):
        json_writer(self.output_filepath, self.secrets_values)


class YAMLOutputFormat(OutputFormat):
    def output(self):
        yaml_writer(self.output_filepath, self.secrets_values)


class DOTENVOutputFormat(OutputFormat):
    def output(self):
        export_dotenv_config(self.output_filepath, self.secrets_values)


# From https://bugs.python.org/msg323681
class ConvertChoices(argparse.Action):
    """
    Argparse action that interprets the `choices` argument as a dict
    mapping the user-specified choices values to the resulting option
    values.
    """

    def __init__(self, *args, choices, **kwargs):
        super().__init__(*args, choices=choices.keys(), **kwargs)
        self.mapping = choices

    def __call__(self, parser, namespace, value, option_string=None):
        setattr(namespace, self.dest, self.mapping[value])


## ==================================================
## CASE: GET / MERGE AWS SECRETS ==> EXPORT TO FILE
## ==================================================

def parse_sys_args_cicd_awssm_to_ekscm() -> argparse.Namespace:
    """Parse command line arguments"""

    parser = argparse.ArgumentParser(
        description="nalibs - tiny tools"
    )

    parser.add_argument(
        "--repo-value-filepath",
        action="store",
        help="Config FilePath on Repository",
    )
    parser.add_argument(
        "--eks-cm-namespace",
        action="store",
        help="EKS - namespace",
    )
    parser.add_argument(
        "--eks-cm-name",
        action="store",
        help="EKS - name",
    )
    parser.add_argument(
        "--secret-app",
        action="store",
        help="AWS Secret Name - app env",
    )
    # parser.add_argument(
    #     "--output-file",
    #     action="store",
    #     default="/tmp/output_example",
    #     help="AWS Secret Name - output filename",
    # )
    parser.add_argument(
        "-r",
        "--region",
        action="store",
        default="ap-southeast-1",
        help="AWS Region",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity level. Warning on -vv (highest level) user input will be printed on screen",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="Check version",
    )

    ## [BEGIN] OUTPUT FORMAT ================
    format_choices = {
        "dotenv": DOTENVOutputFormat,
        "json": JSONOutputFormat,
        "yaml": YAMLOutputFormat,
    }
    parser.add_argument(
        "-f",
        "--format",
        action=ConvertChoices,
        choices=format_choices,
        default=DOTENVOutputFormat,
        help="Format for the output",
    )
    ## [END] OUTPUT FORMAT ==================

    args = parser.parse_args()

    return args


def main_cicd_awssm_to_ekscm() -> None:
    """Main entry point"""
    args = parse_sys_args_cicd_awssm_to_ekscm()

    if args.verbose == 1:
        log_level = 1
    elif args.verbose >= 2:
        log_level = 2
    else:
        log_level = 0

    global logger

    logger = init_logging(log_level)

    # testLog()
    logger.info("Running version: %s", __version__)
    logger.debug("Parsed commandline arguments: %s", args)
    
    ## Get Secrets
    secret_app  = args.secret_app
    if args.repo_value_filepath:
        repo_value_filepath = args.repo_value_filepath
    else:
        repo_value_filepath = "local.yaml"
    region = args.region
    eks_cm_name = args.eks_cm_name
    eks_cm_namespace = args.eks_cm_namespace
    # output_filename = args.output_file
    logger.info("GET DATA [%s]: %s / %s", region, secret_app, repo_value_filepath)
    logger.info("GET DATA [EKS]: %s / %s", eks_cm_namespace, eks_cm_name)
    # logger.info("OUTPUT FILENAME: %s", output_filename)

    kv_app = json.loads(get_secret(secret_app, region))
    try:
        kv_from_repo_file = yaml_reader(repo_value_filepath)
    except:
        kv_from_repo_file = {
            "DO_REPO_VALUES": "NotFound"
        }
    kv_merge_output =  kv_app | kv_from_repo_file
    logger.debug(kv_app)
    logger.debug(kv_from_repo_file)
    logger.info(kv_merge_output)

    ## Export passwords into one of many formats
    # formatter = args.format(args, kv_merge_output, output_filename)
    # formatter.output()

    # Create the ConfigMap
    update_config_map(eks_cm_namespace, eks_cm_name, kv_merge_output)


def run_cicd_awssm_to_ekscm():
    try:
        main_cicd_awssm_to_ekscm()
    except KeyboardInterrupt:
        print("Quit.")
        sys.exit(Exit.KEYBOARD_INTERRUPT)
    except Exit as e:
        sys.exit(e.exitcode)

## ==================================================
## [END] ============================================
## ==================================================

if __name__ == "__main__":
    run_cicd_awssm_to_ekscm()

