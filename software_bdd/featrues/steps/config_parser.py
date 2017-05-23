import os
import sys
import argparse
import yaml

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
        print("ERROR: ", msg)
        sys.exit(1)






