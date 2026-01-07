# SOAP OPERA EFFECT FRAME INTERPOLATION SCRIPT
# Kris McCann (kris@8pi.ca) 2025

import vapoursynth as vs
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
core = vs.core
core.num_threads = 0

if not hasattr(core,'svp1'):
    core.std.LoadPlugin(os.path.join(script_directory, "svpflow1_vs64.dll"))
if not hasattr(core,'svp2'):
    core.std.LoadPlugin(os.path.join(script_directory, "svpflow2_vs64.dll"))

clip = video_in

super_params     = "{scale:{up:0},gpu:1,rc:true, pel:2,hpad:32,vpad:32}"
analyse_params   = "{main:{search:{coarse:{distance:0,bad:{sad:2000,range:24}},type:4}},penalty:{lambda:2000,lsad:1200,pnew:50},refine:[{thsad:200,thsad:150}]}"
smoothfps_params = "{gpuid:11,gpu_qn:2,rate:{num:5,den:2},algo:13,mask:{area:100,cover:75,area_sharp:1},scene:{mode:1,blend:false},misc:{linear:false}}"

src_fps     = container_fps if container_fps>0.1 else 23.976
stereo_type = 0

def interpolate(clip):
    input_um = clip.resize.Point(format=vs.YUV420P10,dither_type="random")
    input_m = input_um
    input_m = input_m.std.CropRel(4,4,0,0)
    input_m8 = input_m.resize.Point(format=vs.YUV420P8)

    super   = core.svp1.Super(input_m8,super_params)
    vectors = core.svp1.Analyse(super["clip"],super["data"],input_m8,analyse_params)
    smooth  = core.svp2.SmoothFps(input_m,super["clip"],super["data"],vectors["clip"],vectors["data"],smoothfps_params,src=input_um,fps=src_fps)
    
    return smooth

if stereo_type == 1:
    lf = interpolate(core.std.CropRel(clip,0,(int)(clip.width/2),0,0))
    rf = interpolate(core.std.CropRel(clip,(int)(clip.width/2),0,0,0))
    smooth = core.std.StackHorizontal([lf, rf])
elif stereo_type == 2:
    lf = interpolate(core.std.CropRel(clip,0,0,0,(int)(clip.height/2)))
    rf = interpolate(core.std.CropRel(clip,0,0,(int)(clip.height/2),0))
    smooth = core.std.StackVertical([lf, rf])
else:
    smooth =  interpolate(clip)

smooth.set_output()