import os
import sys
import os, sys
PROJECT_ROOT = os.path.abspath(os.path.realpath('%s/../../../../log' % __file__))
sys.path.insert(0, PROJECT_ROOT)
from definition import create_logger
import argparse
import yaml

logger = create_logger('software_bdd')

# def parse_arguments():
    # parser = argparse.ArgumentParser('Run  in parallel mode')
    # parser.add_argument('-e', '--env', choices=['qa', 'stage'], help='testing env')
    # args = parser.parse_args()
    # print ('#' * 40)
    # print (args)
    # return args


def env_setting(env):
    """
    :param env: I can use the Background to set the TEST_ENV
    :return: data
    """
    try:
        environment = env
        file_path = os.path.join(os.path.dirname(os.getcwd()), 'config.yml')
        with open(file_path) as file_obj:
            file_data = yaml.safe_load(file_obj)
            data = file_data[environment]
            data['parents'] = file_data['parents']
            return data
    except Exception as msg:
        print("ERROR: ", msg)
        sys.exit(1)

def test_env_setting():
    """
    Use the TEST_ENV which is in ~/.bash_profile to set the test_env
    :return: data
    """
    try:
        environment = os.environ.get('TEST_ENV')
        file_path = os.path.join(os.path.dirname(os.getcwd()), 'config.yml')
        with open(file_path) as file_obj:
            file_data = yaml.safe_load(file_obj)
            data = file_data[environment]
            data['parents'] = file_data['parents']
            return data
    except Exception as msg:
        logger.error(msg)
        sys.exit(1)




# if __name__=="__main__":
#     test_env_setting()

