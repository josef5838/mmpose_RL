dataset_info = dict(
    dataset_name='coco',
    paper_info=[
        dict(
            author='Lin, Tsung-Yi and Maire, Michael and '
            'Belongie, Serge and Hays, James and '
            'Perona, Pietro and Ramanan, Deva and '
            r'Doll{\'a}r, Piotr and Zitnick, C Lawrence',
            title='Microsoft coco: Common objects in context',
            container='European conference on computer vision',
            year='2014',
            homepage='http://cocodataset.org/',
        ),
        dict(
            author='Wu, Jiahong and Zheng, He and Zhao, Bo and '
            'Li, Yixin and Yan, Baoming and Liang, Rui and '
            'Wang, Wenjia and Zhou, Shipei and Lin, Guosen and '
            'Fu, Yanwei and others',
            title='Ai challenger: A large-scale dataset for going '
            'deeper in image understanding',
            container='arXiv',
            year='2017',
            homepage='https://github.com/AIChallenger/AI_Challenger_2017',
        ),
    ],
    keypoint_info={
        0:
        dict(name='nose', id=0, color=[51, 153, 255], type='upper', swap=''),
        1:
        dict(
            name='left_eye',
            id=1,
            color=[51, 153, 255],
            type='upper',
            swap='right_eye'),
        2:
        dict(
            name='right_eye',
            id=2,
            color=[51, 153, 255],
            type='upper',
            swap='left_eye'),
        3:
        dict(
            name='left_ear',
            id=3,
            color=[51, 153, 255],
            type='upper',
            swap='right_ear'),
        4:
        dict(
            name='right_ear',
            id=4,
            color=[51, 153, 255],
            type='upper',
            swap='left_ear'),
        5:
        dict(
            name='left_shoulder',
            id=5,
            color=[0, 255, 0],
            type='upper',
            swap='right_shoulder'),
        6:
        dict(
            name='right_shoulder',
            id=6,
            color=[255, 128, 0],
            type='upper',
            swap='left_shoulder'),
        7:
        dict(
            name='left_elbow',
            id=7,
            color=[0, 255, 0],
            type='upper',
            swap='right_elbow'),
        8:
        dict(
            name='right_elbow',
            id=8,
            color=[255, 128, 0],
            type='upper',
            swap='left_elbow'),
        9:
        dict(
            name='left_wrist',
            id=9,
            color=[0, 255, 0],
            type='upper',
            swap='right_wrist'),
        10:
        dict(
            name='right_wrist',
            id=10,
            color=[255, 128, 0],
            type='upper',
            swap='left_wrist'),
        11:
        dict(
            name='left_hip',
            id=11,
            color=[0, 255, 0],
            type='lower',
            swap='right_hip'),
        12:
        dict(
            name='right_hip',
            id=12,
            color=[255, 128, 0],
            type='lower',
            swap='left_hip'),
        13:
        dict(
            name='left_knee',
            id=13,
            color=[0, 255, 0],
            type='lower',
            swap='right_knee'),
        14:
        dict(
            name='right_knee',
            id=14,
            color=[255, 128, 0],
            type='lower',
            swap='left_knee'),
        15:
        dict(
            name='left_ankle',
            id=15,
            color=[0, 255, 0],
            type='lower',
            swap='right_ankle'),
        16:
        dict(
            name='right_ankle',
            id=16,
            color=[255, 128, 0],
            type='lower',
            swap='left_ankle'),
        17:
        dict(name='pelvis', id=17, color=[51, 153, 255], type='lower', swap=''),
        18:
        dict(name='thorax', id=18, color=[51, 153, 255], type='upper', swap=''),
        19:
        dict(
            name='upper_neck',
            id=19,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        20:
        dict(
            name='head_top',
            id=20,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        21:
        dict(name='neck', id=21, color=[51, 153, 255], type='upper', swap=''),
        22:
        dict(
            name='head_bottom',
            id=22,
            color=[51, 153, 255],
            type='upper',
            swap=''),
        23:
        dict(name='head', id=23, color=[51, 153, 255], type='upper', swap=''),
        24:
        dict(name='belly', id=24, color=[255, 128, 0], type='upper', swap=''),    
        25:
        dict(
            name='left_finger',
            id=25,
            color=[0, 255, 0],
            type='lower',
            swap='right_finger'),
        26:
        dict(
            name='right_finger',
            id=26,
            color=[255, 128, 0],
            type='lower',
            swap='left_finger'),
        27:
        dict(
            name='left_toe',
            id=27,
            color=[0, 255, 0],
            type='lower',
            swap='right_toe'),
        28:
        dict(
            name='right_toe',
            id=28,
            color=[255, 128, 0],
            type='lower',
            swap='left_toe'),
            
    },
    skeleton_info={
        0:
        dict(link=('left_ankle', 'left_knee'), id=0, color=[0, 255, 0]),
        1:
        dict(link=('left_knee', 'left_hip'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('right_ankle', 'right_knee'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('right_knee', 'right_hip'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('left_hip', 'right_hip'), id=4, color=[51, 153, 255]),
        5:
        dict(link=('left_shoulder', 'left_hip'), id=5, color=[51, 153, 255]),
        6:
        dict(link=('right_shoulder', 'right_hip'), id=6, color=[51, 153, 255]),
        7:
        dict(
            link=('left_shoulder', 'right_shoulder'),
            id=7,
            color=[51, 153, 255]),
        8:
        dict(link=('left_shoulder', 'left_elbow'), id=8, color=[0, 255, 0]),
        9:
        dict(
            link=('right_shoulder', 'right_elbow'), id=9, color=[255, 128, 0]),
        10:
        dict(link=('left_elbow', 'left_wrist'), id=10, color=[0, 255, 0]),
        11:
        dict(link=('right_elbow', 'right_wrist'), id=11, color=[255, 128, 0]),
        12:
        dict(link=('left_eye', 'right_eye'), id=12, color=[51, 153, 255]),
        13:
        dict(link=('nose', 'left_eye'), id=13, color=[51, 153, 255]),
        14:
        dict(link=('nose', 'right_eye'), id=14, color=[51, 153, 255]),
        15:
        dict(link=('left_eye', 'left_ear'), id=15, color=[51, 153, 255]),
        16:
        dict(link=('right_eye', 'right_ear'), id=16, color=[51, 153, 255]),
        17:
        dict(link=('left_ear', 'left_shoulder'), id=17, color=[51, 153, 255]),
        18:
        dict(
            link=('right_ear', 'right_shoulder'), id=18, color=[51, 153, 255]),
        19:
        dict(link=('head_top', 'neck'), id=19, color=[51, 153, 255]),
        
        # mpii
        20:
        dict(link=('right_hip', 'pelvis'), id=20, color=[255, 128, 0]),
        21:
        dict(link=('pelvis', 'left_hip'), id=21, color=[0, 255, 0]),
        22:
        dict(link=('pelvis', 'thorax'), id=22, color=[51, 153, 255]),
        23:
        dict(link=('thorax', 'upper_neck'), id=23, color=[51, 153, 255]),
        24:
        dict(link=('upper_neck', 'head_top'), id=24, color=[51, 153, 255]),
        25:
        dict(link=('upper_neck', 'right_shoulder'), id=25, color=[255, 128, 0]),
        26:
        dict(link=('upper_neck', 'left_shoulder'), id=26, color=[0, 255, 0]),
        # posetrack
        27:
        dict(link=('nose', 'head_bottom'), id=27, color=[51, 153, 255]),
        28:
        dict(
            link=('head_bottom', 'left_shoulder'), id=28, color=[51, 153,
                                                                 255]),
        29:
        dict(
            link=('head_bottom', 'right_shoulder'),
            id=29,
            color=[51, 153, 255]),
        # jhmdb
        30: dict(link=('right_hip', 'belly'), id=30, color=[255, 128, 0]),
        31: dict(link=('belly', 'left_hip'), id=31, color=[0, 255, 0]),
        32: dict(link=('belly', 'neck'), id=32, color=[51, 153, 255]),
        33: dict(link=('neck', 'head'), id=33, color=[51, 153, 255]),
        
        # humanart21
        34:
        dict(link=('left_ankle', 'left_toe'), id=34, color=[0, 255, 0]),
        35:
        dict(link=('right_ankle', 'right_toe'), id=35, color=[255, 128, 0]),
        36:
        dict(link=('left_wrist', 'left_finger'), id=36, color=[0, 255, 0]),
        37:
        dict(link=('right_wrist', 'right_finger'), id=37, color=[255, 128, 0]),
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1.2, 1.2, 1.5, 
        1.5, 1., 1., 1.2, 1.2, 1.5, 1., 1., 1., 1.,
        1.5, 1.5, 1., 1., 1., 1., 1., 1., 1.,
    ],
    sigmas=[
        0.026, 0.025, 0.025, 0.035, 0.035, 0.079, 0.079, 0.072, 0.072, 0.062,
        0.062, 0.107, 0.107, 0.087, 0.087, 0.089, 0.089, 0.026, 0.026, 0.062,
        0.026, 0.026, 0.025, 0.025, 0.107, 0.089, 0.089, 0.089, 0.089
    ],
)
