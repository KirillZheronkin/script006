import yaml

import os
import yaml
import logging.config
import logging

def setup_logging(
        default_path='config.yml',
        default_level=logging.INFO,
        env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if os.path.exists(path):
        with open(path, 'r') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')


if __name__ == '__main__':
    setup_logging()
    logging.error("logging test")