
from trilaterate import trilaterate

SAMPLE_DATASET = [
    [
        130, 20, 90
    ],
    [
        40, 50, 60
    ],
    [
        70, 80, 90
    ]
]

coordinates = trilaterate(SAMPLE_DATASET)
print("Location:", coordinates)
