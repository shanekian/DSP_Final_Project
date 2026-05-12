import numpy as np
import matplotlib.pyplot as plt

# =========================
# STEP 1: LOAD DATA
# =========================
file_path = "data/raw/LibriNoise_Train_Test_NPY/mat_test/19-198-0034.npy"
data = np.load(file_path)

print("Original shape:", data.shape)

# =========================
# STEP 2: GET SPECTROGRAM
# =========================
spec = data[:, :, 0]

print("Spectrogram shape:", spec.shape)

# =========================
# STEP 3: NOISE ESTIMATION
# (Assume first few time frames = noise)
# =========================
noise_est = np.mean(spec[:, :5], axis=1, keepdims=True)

# =========================
# STEP 4: SPECTRAL SUBTRACTION
# =========================
clean_spec = spec - noise_est
clean_spec = np.maximum(clean_spec, 0)

# =========================
# STEP 5: SIDE-BY-SIDE VISUALIZATION
# =========================
plt.figure(figsize=(14, 5))

# NOISY
plt.subplot(1, 2, 1)
plt.imshow(spec, aspect='auto')
plt.title("Noisy Spectrogram")
plt.xlabel("Time")
plt.ylabel("Frequency")

# CLEANED
plt.subplot(1, 2, 2)
plt.imshow(clean_spec, aspect='auto')
plt.title("Cleaned Spectrogram (Spectral Subtraction)")
plt.xlabel("Time")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()