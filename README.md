# Virtual Background

Inspiration from: https://elder.dev/posts/open-source-virtual-background/

### Overview of Steps to reproduce

1. Read the camera with cv2 - OpenCV python bindings
2. Use [body-pix](https://github.com/tensorflow/tfjs-models/tree/master/body-pix) tensorflow model to create a mask of your body on the frame [blogpost](https://blog.tensorflow.org/2019/11/updated-bodypix-2.html). 
    Use `tfjs-node` or `tfjs-node-gpu` if you have a graphic card supporting CUDA
3. Combine the background and foreground, using the mask and add holo or other visual effects to the foreground
4. Outputting Video: use 
    - [v4l2loopback](https://github.com/umlaeute/v4l2loopback) - to create a virtual webcam device
      > On Ubuntu 18.04 I needed to build `v4l2loopback` from the source code to use the latest version 0.12
    - [pyfakewebcam](https://github.com/jremmons/pyfakewebcam) to write RGB frames to a fake webcam


### Install
- Body-pix: `cd bodypix && npm install`
- Fake-cam: `cd fakecam && pip3 install --no-cache-dir -r ./requirements.txt`
- Install v4l2loopback
  - Either 
    
    `sudo apt install v4l2loopback-dkms`
  - In my case (Ubuntu 18.04)
    ```bash
    git clone https://github.com/umlaeute/v4l2loopback.git --depth=1
    cd v4l2loopback
    sudo make install
    sudo depmod -a
    ```
- Configure fake webcam device with `v4l2loopback`

    ```bash
    # Reset allvirtual devices
    sudo modprobe -r v4l2loopback
    # Create virtual /dev/video20 with exclusive_cap (required for chrome)
    sudo modprobe v4l2loopback devices=1 video_nr=20 card_label="v4l2loopback" exclusive_caps=1
    # Check if virtual cam created
    v4l2-ctl --list-devices 
  ```
### Run

- `cd bodypix && npm start`
- `cd fakecam && python3 fake.py`
- `ffplay /dev/video20` for debug or use with an online chat 

### Ideas

- [ ] try using facemesh and replace face with something else  
- [ ] experiment with JACK Rack and audio/mic tuning [tutorial](https://digitalsuperpowers.com/blog/2019-03-16-voice-changers.html)

### Links

- [Space free videos ](https://www.pexels.com/search/videos/space/)
- [Office img backgrounds](https://unsplash.com/s/photos/office-background)