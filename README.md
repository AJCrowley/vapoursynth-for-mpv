# Frame Interpolation for mpv.net

I did not write VapourSynth, and I did not write mpv.net. I did however struggle for several hours to create a working frame interpolation filter for mpv.net.

## Why?
To playback video at a smoother higher framerate. This is colloquially known as "the soap opera effect", and if you've never experienced it, it can be jarring...it certainly was the first time I saw it.

Smoother video playback highlights bad set design, bad acting, bad effects that are otherwise hidden by the layer of "movie magic" that lower framerates provide. For this reason, a lot of people don't like it, but I promise, once you get used to it, it's hard to go back.

The smoother playback almost places you in the room with the action, the enhanced realism as previously mentioned can dissolve the movie magic, but once you get used to it, it's hard to go back.

I have struggled to configure VapourSynth to interpolate frames to increase smooth higher framerate playback to the best of my ability. This can lead to artifacting in scenes of high motion, and it can be particularly notable when a group of vertical lines (such as blinds) move quickly across the screen. I have tweaked the configuration to the best of my ability, but you are welcome to adjust the parameters to try and achieve better results by editing the file VapourSynth\vapoursynth.vpy and playing with the super_params and analyse_params string variables.

## How to Install This Script

If you want to use my entire config, simply download the zip, open Explorer, and type "%APPDATA%" into the address bar. If you already have mpv.net in use, there will be a folder called mpv.net, otherwise, just create it and extract the contents of the zip into it.

If you already have mpv.net configured to your liking, simply extract the VapourSynth folder into your %APPDATA%\mpv.net folder and edit mpv.conf and paste the following to the end:
```
[vapoursynth]
vf=vapoursynth="~~/VapourSynth/vapoursynth.vpy"
```
You can remove the square brackets tag if you want the filter always on, but my little mini-PC struggles with 4K video, and you might want to choose when to use this filter.

Use a text editor to open VapourSynth\vapoursynth.vpy and replace "YourAccount" in the path with the actual path of your account (which should be visible in Explorer's address bar) for both of the DLLs that the script loads. I have tried using relative directories and environment variables to remove this step, but the filter demands an absolute path.

You'll also need to add the following to your Path Environment Variables:
```
%APPDATA%\mpv.net\VapourSynth
```

 If you're unsure of how to do this:

- Right click "My Computer" and select "Properties" from the menu
- Click "Advanced system settings" on the window that comes up
- Click "Environment variables on the new window"
- Double click the "Path" environment variable
- Press the "New" button and paste "%APPDATA%\mpv.net\VapourSynth" into the dialog that pops up. On older versions of windows, you might get the entire path variable in one long semi-colon separated string, if this is the case, just pop a semi-colon on the end and paste the above string to the end of your Path variable

Now you're good to go, just load up a video in mpv.net, and if you've kept my profile or kept the square brackets just right click the screen, and select "vapoursynth" under the "Profiles" sub-menu. Bring up the stats (t if you're using my profile), and you should see after the video file's framerate (e.g. 23.97) the adjusted framerate, which on my setup is around 60 (estimated).

## How to Use my Profile

I have included my entire mpv.net configuration, which is optimized for binge watching with useful display info and on-screen controls, placing as little clutter or complications around your viewing experience as possible. Once the file you are watching is finished, it will automatically play the next file in the folder. Once there are no more files in the folder, and it has finished playing, the app will auto quit, so you don't need to worry about launching and loading then closing, just double click the video you want to start with (with file associations set) and sit back and enjoy, the next episode will start playing at the end of the one you are watching, and the program will auto close when you're finished. You are welcome to use my entire profile, or just use the VapourSynth filter with your own existing config. Because my little mini-PC struggles to use this with 4K video, I have put it behind a profile. Other useful shortcuts I have included are listed below (note, anything that requires a multiple key press does not, so my notation for volume (+/-) is actually just "=" and "-" on your keyboard, because why complicate things.

Shortcuts:

- Menu: right mouse click on video
- Volume up: +
- Volume down: -
- Next frame: w
- Previous frame: s
- Next chapter: d
- Previous chapter: a
- Next file: >
- Previous file: <
- Show on screen stats: t
- Toggle full screen: esc or double left mouse click on video
- Quit: q
- Toggle play/pause: space bar
- Toggle stats: t (if you bring this up, it will show you the increased frame rate, which should be matched to your PCs output to the monitor

Hopefully this saves a few people the hours of pain and frustration I endured to get this working.

Note: I did not write [VapourSynth](https://github.com/vapoursynth/vapoursynth) or [mpv.net](https://github.com/mpvnet-player/mpv.net) which are both superb projects worthy of your support.