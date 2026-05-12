

import numpy as np
import matplotlib.pyplot as plt

file_path = "data/raw/LibriNoise_Train_Test_NPY/mat_test/19-198-0034.npy"

data = np.load(file_path)

print("Shape:", data.shape)

# Show one slice instead of full 3D data
plt.imshow(data[:, :, 0], aspect='auto')

plt.title("Spectrogram Slice")

plt.colorbar()

plt.show()