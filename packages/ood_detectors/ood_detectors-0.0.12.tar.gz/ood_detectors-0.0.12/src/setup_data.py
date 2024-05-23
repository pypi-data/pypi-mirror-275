import ood_detectors.vision as vision
import ood_detectors.ops_utils as ops_utils
import torch
import random
import pathlib
import pickle


import multiprocessing as mp

def encode_dataset(encoder_name, dataset_name, device):
    data_root = '/mnt/data/arty/data'
    image_list_root = '/mnt/data/arty/data/benchmark_imglist'
    features = pathlib.Path("/mnt/data/arty/data/features_opt_extra")
    features.mkdir(exist_ok=True)
    encoder_path = features / encoder_name
    encoder_path.mkdir(exist_ok=True)
    dataset_name_path = encoder_path / dataset_name
    dataset_name_path.mkdir(exist_ok=True)
    encoder = vision.get_encoder(encoder_name)
    encoder.eval()
    datasets = vision.get_datasets(dataset_name, data_root=data_root, image_list_root=image_list_root, transform=encoder.transform)
    for type_name, datasets in datasets.items():
        if type_name == 'csid':
            continue
        type_name_path = dataset_name_path / type_name
        type_name_path.mkdir(exist_ok=True)
        for name, dataset in datasets.items():
            name_path = type_name_path / name
            name_path.mkdir(exist_ok=True)
            print(encoder_name, dataset_name, name, len(dataset))
            features_path = name_path / 'feature_data.pkl'
            if features_path.exists():
                continue
            features_vectors = vision.extract_features(encoder, dataset, batch_size=64, num_workers=2, device=device)
            data = {
                'features': features_vectors,
                'encoder': encoder_name,
                'target_dataset': dataset_name,
                'dataset': name,
                'type': type_name
            }
            with open(features_path, 'wb') as f:
                pickle.dump(data, f)
def main():

    # encoders = ['repvgg', 'resnet50d', 'swin', 'deit', 'dino', 'dinov2', 'vit', 'clip', 'vit_b16', 'swin_t']
    encoders = ['vit_b16', 'swin_t']
    # datasets = ['imagenet', 'imagenet200', 'cifar10', 'cifar100']
    datasets = ['imagenet']
    gpu_nodes = [0, 1, 2, 3]

    jobs = []
    for encoder_name in encoders:
        for dataset_name in datasets:
            jobs.append((encoder_name, dataset_name))
        
    # for encoder_name, dataset_name in zip(['resnet18_32x32_cifar10_open_ood', 
    #                             'resnet18_32x32_cifar100_open_ood', 
    #                             'resnet18_224x224_imagenet200_open_ood', 
    #                             'resnet50_224x224_imagenet_open_ood'],
    #                             ['cifar10', 'cifar100', 'imagenet200', 'imagenet']):
    #     jobs.append((encoder_name, dataset_name))

    print(len(jobs))
    random.shuffle(jobs)


    ops_utils.parallelize(encode_dataset, jobs, gpu_nodes, verbose=True, timeout=60*60*24)

if __name__ == '__main__':
    mp.freeze_support()
    main()