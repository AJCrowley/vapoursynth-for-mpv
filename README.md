# Frame Interpolation for mpv

## Note
This was originally set up for mpv.net. I've since switched to [mpv-hero](https://github.com/stax76/mpv-hero), as it's a more actively maintained branch that comes with some really neat plugins. You can download my fork of mpv-hero with VapourSynth integration from [my GitHub](https://github.com/AJCrowley/mpv-hero-vapoursynth)

## Why?
To playback video at a smoother higher framerate. This is colloquially known as "the soap opera effect", and if you've never experienced it, it can be jarring...it certainly was the first time I saw it.

Smoother video playback highlights bad set design, bad acting, bad effects that are otherwise hidden by the layer of "movie magic" that lower framerates provide. For this reason, a lot of people don't like it, but I promise, once you get used to it, it's hard to go back.

The smoother playback almost places you in the room with the action, the enhanced realism as previously mentioned can dissolve the movie magic, but once you get used to it, it's hard to go back.

I have struggled to configure VapourSynth to interpolate frames to increase smooth higher framerate playback to the best of my ability. This can lead to artifacting in scenes of high motion, and it can be particularly notable when a group of vertical lines (such as blinds) move quickly across the screen. I have tweaked the configuration to the best of my ability, but you are welcome to adjust the parameters to try and achieve better results by editing the file VapourSynth\vapoursynth.vpy and playing with the super_params and analyse_params string variables. If you think you've acheived a better result, please feel free to put in a PR, or if you don't know how to do that, just post your config params in the Issues tab and I'll see it and update the script if it works better for me as well.

## How to Install This Script

Just drop the VapourSynth folder into your mpv profile folder, usually %APPDATA%\mpv or Install Location\portable_config. Drop the vapoursynth.lua script into the profile scripts directory. VapourSynth directory should exist alongside the scripts directory, not inside it, so an example file structure:
```
mpv-hero\portable_config\
        ----scripts
            -------vapoursynth.lua
        ----VapourSynth
        ----input.conf
```
If you are not using a portable config, the base folder would be ```%APPDATA\mpv```.

Add the path to the VapourSynth folder to the Windows PATH environment variable, e.g.:
 ```%PROGRAMFILES%\mpv-hero\portable_config\VapourSynth``` or ```%APPDATA%\mpv\VapourSynth```

The plugin used to run as a profile. However, I have written a Lua script and adapted it to integrate seamlessly into your mpv installation, allowing you to choose which framerates you wish to offer.

To set a framerate, just add a bind to your inputs.conf (as seen in the example file):

```
keybind1    script-message vapoursynth_set_fps 0  #menu: VapourSynth > Off
keybind2    script-message vapoursynth_set_fps 120  #menu: VapourSynth > 120fps
```

Replace the word "keybind" with the key which you wish to bind the command to, and replace the number after ```vapoursynth_set_fps``` to the framerate you wish to run at. There is also the code to add these binds to your menu if you are using a dynamic menu.

Hopefully this saves a few people the hours of pain and frustration I endured to get this working.

Note: I did not write [VapourSynth](https://github.com/vapoursynth/vapoursynth) or [mpv-hero](https://github.com/stax76/mpv-hero) which are both superb projects worthy of your support, and [my own fork of mpv-hero](https://github.com/AJCrowley/mpv-hero-vapoursynth) which comes with VapourSynth already baked in.
