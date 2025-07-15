#🐶 BitBeagle

BitBeagle is a lightweight audio comparison tool that analyzes audio files and detects similarities (or differences) using MFCC (Mel-Frequency Cepstral Coefficient) features. Like a loyal beagle sniffing out audio differences, this script compares each track to a reference and reports back the most and least similar matches.

---

## Features

  Compare audio files using cosine similarity

  Extract MFCC features for robust analysis

  Supports multiple audio formats: .wav, .mp3, .flac, .ogg, .aac, .m4a

  Outputs a ranked similarity report as CSV

  Prints results directly to console

---

## File Structure
```
project_root/
├── reference/        # Folder containing the reference audio file (first valid audio file found will be used)
├── stems/            # Folder with all audio files to compare against the reference
├── results.csv       # Output similarity report (auto-generated)
├── main.py           # Main script
```
---

## Usage

1. Install required libraries:

  ``` pip install librosa scipy numpy ```

2. Place your reference audio file inside the reference/ folder that you created.

3. Add all audio files you want to compare into the stems/ folder that you created.

4. Run the script:

  ``` python main.py ```

5. View results printed to console or open results.csv for a full report.

---

## How It Works
  
  Loads the reference and each target audio file.
  
  Extracts MFCC features (averaged over time).
  
  Computes cosine similarity between MFCC vectors.
  
  Outputs and ranks results by similarity score (1 = identical, 0 = completely different).
  
---

## Dependencies

  Librosa
  
  Numpy
  
  Scipy

---

## Why "BitBeagle"?

  Because this little utility sniffs out audio differences bit by bit; just like a trusty beagle on the trail.

---

## License

  MIT License: use freely, sniff responsibly. We are not responsible for illegal usage of BitBeagle. This is an Open-Source program for educational purposes only. Please provide proper credit to the repo and creator.

---

## Most Importantly

  Have fun sniffing! Questions? Leave a issue request!

---


  




