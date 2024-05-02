import json
import os
import random
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import imgaug
import numpy as np
import torch
import torch.multiprocessing as mp

seed = 1234
random.seed(seed)
imgaug.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed_all(seed)
np.random.seed(seed)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False


import models
from models import segmentation


def main(config_path):
    """
    This is the main function to make the training up

    Parameters:
    -----------
    config_path : srt
        path to config file
    """
    # load configs and set random seed
    configs = json.load(open(config_path))
    configs["cwd"] = os.getcwd()
    # Ensure model save directory exists
    model_save_dir = os.path.join(configs["cwd"], configs.get("model_save_path", "saved_models"))
    if not os.path.exists(model_save_dir):
        os.makedirs(model_save_dir)

    # load model and data_loader
    model = get_model(configs)

    train_set, val_set, test_set = get_dataset(configs)

    # init trainer and make a training
    # from trainers.fer2013_trainer import FER2013Trainer
    from trainers.eafe_trainer import EafeTrainer

    # from trainers.centerloss_trainer import FER2013Trainer
    trainer = EafeTrainer(model, train_set, val_set, test_set, configs)

    try:
        if configs["distributed"] == 1:
            ngpus = torch.cuda.device_count()
            mp.spawn(trainer.train, nprocs=ngpus, args=())
        else:
            trainer.train()
    finally:
        # Optionally save the model at the end of all training
        final_model_path = os.path.join(model_save_dir, 'eafe_model.pth')
        trainer.save_model(final_model_path)


def get_model(configs):
    """
    This function get raw models from models package

    Parameters:
    ------------
    configs : dict
        configs dictionary
    """
    try:
        return models.__dict__[configs["arch"]]
    except KeyError:
        return segmentation.__dict__[configs["arch"]]


def get_dataset(configs):
    """
    This function get raw dataset
    """
    from utils.datasets.eafe_asian import eafe_asian

    # todo: add transform
    train_set = eafe_asian("train", configs)
    val_set = eafe_asian("val", configs)
    test_set = eafe_asian("test", configs, tta=True, tta_size=10)
    return train_set, val_set, test_set
    # now we are at stage, need to decide the dataset

if __name__ == "__main__":
    main("./configs/eafe_asian_config.json")
