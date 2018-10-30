# pix2pix_outliner
Prepares A-B outlined vs. actual images for pix2pix training

### Clone

```bash
git clone https://github.com/simonpinkas/pix2pix_outliner.git
cd pix2pix_outliner
```

### Install Requirements

```bash
pip install matplotlib
pip install opencv-python
```

### Setup Instructions
1. Add images to the 'original' folder
2. Adjust script to fit your dataset (number of samples, width, height, threshold)
3. Run the following:
```bash
python pix2pix_outliner.py
```
4. Output images will be available in 'train', 'val' and 'test' directories.
5. Use with [pix2pix-tensorflow](https://github.com/affinelayer/pix2pix-tensorflow)
