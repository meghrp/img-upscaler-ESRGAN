# img-upscaler
a simple web app that upscales images with [ESRGAN](https://github.com/xinntao/ESRGAN). The model runs locally on the user's machine

## Run it

### Dependencies
- Python 3
- PyTorch 7.5+
- Python packages `pip install -r requirements.txt`

### Run it
1. Clone this repo
2. Clone [ESRGAN repo](https://github.com/xinntao/ESRGAN) in the same directory
3. Download ESRGAN pre-trained model from [drive](https://drive.google.com/drive/u/0/folders/17VYV_SoZZesU6mbxz2dMAIccSSlqLecY) and place it into ESRGAN/models folder
4. `python app.py`
