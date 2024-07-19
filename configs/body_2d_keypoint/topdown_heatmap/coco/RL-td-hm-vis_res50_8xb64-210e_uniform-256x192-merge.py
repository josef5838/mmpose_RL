_base_ = ['../../../_base_/default_runtime.py']

# runtime
train_cfg = dict(max_epochs=210, val_interval=10)

# optimizer
optim_wrapper = dict(optimizer=dict(
    type='Adam',
    lr=5e-4,
))



# learning policy
param_scheduler = [
    dict(
        type='LinearLR', begin=0, end=500, start_factor=0.001,
        by_epoch=False),  # warm-up
    dict(
        type='MultiStepLR',
        begin=0,
        end=210,
        milestones=[170, 200],
        gamma=0.1,
        by_epoch=True)
]

# automatically scaling LR based on the actual training batch size
auto_scale_lr = dict(base_batch_size=512)

# hooks
default_hooks = dict(checkpoint=dict(save_best='coco/AP', rule='greater'))

# codec settings
codec = dict(
    type='MSRAHeatmap', input_size=(192, 256), heatmap_size=(48, 64), sigma=2)

# model settings
model = dict(
    type='TopdownPoseEstimator',
    data_preprocessor=dict(
        type='PoseDataPreprocessor',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        bgr_to_rgb=True),
    backbone=dict(
        type='ResNet',
        depth=50,
        init_cfg=dict(type='Pretrained', checkpoint='torchvision://resnet50'),
    ),
    head=dict(
        type='VisPredictHead',
        loss=dict(
            type='BCELoss',
            use_target_weight=True,
            use_sigmoid=True,
            loss_weight=1e-3,
        ),
        pose_cfg=dict(
            type='HeatmapHead',
            in_channels=2048,
            out_channels=29,
            loss=dict(type='KeypointMSELoss', use_target_weight=True),
            decoder=codec)),
    test_cfg=dict(
        flip_test=True,
        flip_mode='heatmap',
        shift_heatmap=True,
    ))

# base dataset settings
dataset_type = 'CocoDataset'
data_mode = 'topdown'
data_root = 'data/coco/'

# pipelines
train_pipeline = [
    dict(type='LoadImage'),
    dict(type='GetBBoxCenterScale'),
    dict(type='RandomFlip', direction='horizontal'),
    dict(type='RandomHalfBody'),
    dict(type='RandomBBoxTransform'),
    dict(type='TopdownAffine', input_size=codec['input_size']),
    dict(type='GenerateTarget', encoder=codec),
    dict(type='PackPoseInputs')
]
val_pipeline = [
    dict(type='LoadImage'),
    dict(type='GetBBoxCenterScale'),
    dict(type='TopdownAffine', input_size=codec['input_size']),
    dict(type='PackPoseInputs')
]

# train datasets
dataset_coco = dict(
    type='CocoDataset',
    data_root='data/coco/',
    data_mode=data_mode,
    ann_file='annotations/person_keypoints_train2017.json',
    data_prefix=dict(img='train2017/'),
    pipeline=[
        dict(
            type='KeypointConverter',
            num_keypoints=29,
            mapping=[
                (0, 0),
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
                (10, 10),
                (11, 11),
                (12, 12),
                (13, 13),
                (14, 14),
                (15, 15),
                (16, 16),
            ])],
)
# dataset_aic = dict(
#     type='AicDataset',
#     data_root='data/aic/',
#     data_mode=data_mode,
#     ann_file='annotations/aic_train.json',
#     data_prefix=dict(img='ai_challenger_keypoint_train_20170902/'
#                      'keypoint_train_images_20170902/'),
#     pipeline=[
#         dict(
#             type='KeypointConverter',
#             num_keypoints=29,
#             mapping=[
#                 (0, 6),
#                 (1, 8),
#                 (2, 10),
#                 (3, 5),
#                 (4, 7),
#                 (5, 9),
#                 (6, 12),
#                 (7, 14),
#                 (8, 16),
#                 (9, 11),
#                 (10, 13),
#                 (11, 15),
#                 (12, 20),
#                 (13, 21)
#             ])
#     ],
# )

dataset_mpii = dict(
    type='MpiiDataset',
    data_root='data/mpii/',
    data_mode=data_mode,
    ann_file='annotations/mpii_train.json',
    data_prefix=dict(img='images/'),
    pipeline=[
        dict(
            type='KeypointConverter',
            num_keypoints=29,
            mapping=[
                (0, 16),
                (1, 14),
                (2, 12),
                (3, 11),
                (4, 13),
                (5, 15),
                (6, 17),
                (7, 18),
                (8, 19),
                (9, 20),
                (10, 10),
                (11, 8),
                (12, 6),
                (13, 5),
                (14, 7),
                (15, 9),
            ])
    ],
)

dataset_crowdpose = dict(
    type='CrowdPoseDataset',
    data_root='data/crowdpose/',
    data_mode=data_mode,
    ann_file='annotations/mmpose_crowdpose_trainval.json',
    data_prefix=dict(img='images/'),
    pipeline=[
        dict(
            type='KeypointConverter',
            num_keypoints=29,
            mapping=[
                (0, 5),
                (1, 6),
                (2, 7),
                (3, 8),
                (4, 9),
                (5, 10),
                (6, 11),
                (7, 12),
                (8, 13),
                (9, 14),
                (10, 15),
                (11, 16),
                (12, 20),
                (13, 21),
            ])
    ],
)
dataset_combined = dict(
    type='CombinedDataset',
    # using new dataset meta information file
    metainfo=dict(from_file='configs/_base_/datasets/RL_uniform.py'),
    datasets=[dataset_coco, dataset_crowdpose, dataset_mpii],
    # The pipeline includes typical transforms, such as loading the
    # image and data augmentation
    pipeline=train_pipeline,
    sample_ratio_factor=[1, 1, 1],
    test_mode=False,
)
# ??
# more datasets

# optional:
# dataset_humanart
# dataset_exlpose
# dataset_posetrack2018
# dataset_jhmdb

# data loaders
train_dataloader = dict(
    batch_size=64,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dataset_combined
    )
val_dataloader = dict(
    batch_size=32,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False, round_up=False),
    dataset=dataset_coco
    )
test_dataloader = val_dataloader

# evaluators
val_evaluator = dict(
    type='CocoMetric',
    # score_mode='bbox',
    ann_file=data_root + 'annotations/person_keypoints_val2017.json')
test_evaluator = val_evaluator
