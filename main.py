import os
import librosa
import numpy as np
from scipy.spatial.distance import cosine
import csv

# Supported audio formats
AUDIO_EXTENSIONS = ('.wav', '.mp3', '.flac', '.ogg', '.aac', '.m4a')

def extract_mfcc(file_path, sr=44100):
    """
    Load the full audio file at 44.1kHz and extract averaged MFCCs.
    """
    y, _ = librosa.load(file_path, sr=sr, mono=True)  # Load full duration
    rms = np.sqrt(np.mean(y**2))
    if rms > 0:
        y = y / rms  # Normalize to consistent loudness

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    return np.mean(mfcc, axis=1)


def compare_similarity(reference_vec, target_vec):
    """
    Cosine similarity: 1 = identical, 0 = orthogonal
    """
    return 1 - cosine(reference_vec, target_vec)

def find_reference_file(reference_folder):
    """
    Return the first valid audio file in the reference folder.
    """
    for file in os.listdir(reference_folder):
        if file.lower().endswith(AUDIO_EXTENSIONS):
            return os.path.join(reference_folder, file)
    raise FileNotFoundError("No valid audio file found in reference folder.")

def analyze_audio_similarity(reference_folder, stems_folder, output_csv="results.csv"):
    print(f" Reference: searching in '{reference_folder}'")
    reference_path = find_reference_file(reference_folder)
    print(f" Using reference track: {os.path.basename(reference_path)}\n")

    ref_mfcc = extract_mfcc(reference_path)

    results = []

    for filename in os.listdir(stems_folder):
        file_path = os.path.join(stems_folder, filename)
        if not filename.lower().endswith(AUDIO_EXTENSIONS):
            continue
        try:
            stem_mfcc = extract_mfcc(file_path)
            similarity = compare_similarity(ref_mfcc, stem_mfcc)
            results.append((filename, similarity))
            print(f"{filename}: Similarity = {similarity:.4f}")
        except Exception as e:
            print(f"Error with {filename}: {e}")

    if results:
        results.sort(key=lambda x: x[1], reverse=True)

        print("\n Most similar:", results[0][0], f"(Score: {results[0][1]:.4f})")
        print("Least similar:", results[-1][0], f"(Score: {results[-1][1]:.4f})")

        with open(output_csv, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stem File", "Similarity Score"])
            writer.writerows(results)

        print(f"\n Results saved to '{output_csv}'")
    else:
        print(" No valid audio files found in the stems folder.")

if __name__ == "__main__":
    # Change these paths as needed:
    stems_folder = "stems"
    reference_folder = "reference"
    analyze_audio_similarity(reference_folder, stems_folder)
