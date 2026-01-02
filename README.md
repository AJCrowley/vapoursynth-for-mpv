# Frame Interpolation for mpv

## Note
This was originally set up for mpv.net. I've since switched to [mpv-hero](https://github.com/stax76/mpv-hero), as it's a more actively maintained branch that comes with some really neat plugins. I've abstracted the VapourSynth plugin so that no configuration is needed. I've also changed it so that selecting the vapoursynth profile toggles it on/off, as it may not always be desireable to have on.

## Why?
To playback video at a smoother higher framerate. This is colloquially known as "the soap opera effect", and if you've never experienced it, it can be jarring...it certainly was the first time I saw it.

Smoother video playback highlights bad set design, bad acting, bad effects that are otherwise hidden by the layer of "movie magic" that lower framerates provide. For this reason, a lot of people don't like it, but I promise, once you get used to it, it's hard to go back.

The smoother playback almost places you in the room with the action, the enhanced realism as previously mentioned can dissolve the movie magic, but once you get used to it, it's hard to go back.

I have struggled to configure VapourSynth to interpolate frames to increase smooth higher framerate playback to the best of my ability. This can lead to artifacting in scenes of high motion, and it can be particularly notable when a group of vertical lines (such as blinds) move quickly across the screen. I have tweaked the configuration to the best of my ability, but you are welcome to adjust the parameters to try and achieve better results by editing the file VapourSynth\vapoursynth.vpy and playing with the super_params and analyse_params string variables. If you think you've acheived a better result, please feel free to put in a PR, or if you don't know how to do that, just post your config params in the Issues tab and I'll see it and update the script if it works better for me as well.

## How to Install This Script

Just drop the VapourSynth folder into your mpv profile folder, usually %APPDATA%\mpv or Install Location\portable_config. Add the following lines to the end of your mpv.conf file:
```
[vapoursynth]
vf-toggle=@filter:vapoursynth="~~/VapourSynth/vapoursynth.vpy"
```
I've had mixed results with having the VapourSynth folder in the PATH environment variable. If your video crashes out when switching to the vapoursynth profile, add the path to your environment variables, e.g.:
 ```%PROGRAMFILES%\mpv-hero\portable_config\VapourSynth```

This should clear up any issues.
Now you're good to go, just load up a video in your preferred mpv distro, and select "vapoursynth" under the "Profiles" sub-menu. Bring up the stats (t default), and you should see after the video file's framerate (e.g. 23.97) the adjusted framerate, and that it's either using or not using the filter.

Hopefully this saves a few people the hours of pain and frustration I endured to get this working.

Note: I did not write [VapourSynth](https://github.com/vapoursynth/vapoursynth) or [mpv-hero](https://github.com/stax76/mpv-hero) which are both superb projects worthy of your support.