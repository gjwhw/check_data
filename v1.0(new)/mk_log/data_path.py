# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 文件路径定义
def path(x):

    error = '/home/error/'+ x +'-ERROR/'
    log   = '/home/log/'+ x +'-LOG/'
    type1 = x
    return error,log,type1


'''
cdn_pm_error = 'd:\error\cdn_pm_error\\'
cdn_pm_log = 'd:\log\cdn_pm_log\\'
cdn_pm_type = 'CDN-PM'

epg_pm_error = 'd:\error\epg_pm__error\\'
epg_pm_log = 'd:\log\epg_pm__log\\'
epg_pm_type = 'EPG-PM'

stb_cm1_error = 'd:\error\stb_cm1_error\\'
stb_cm1_log = 'd:\log\stb_cm1_log\\'
stb_cm1_type = 'STB-CM1'

stb_cm2_error = 'd:\error\stb_cm2_error\\'
stb_cm2_log = 'd:\log\stb_cm2_log\\'
stb_cm2_type = 'STB-CM2'

stb_inserv_rtsp_error = 'd:\error\stb_inserv_rtsp_error\\'
stb_inserv_rtsp_log = 'd:\log\stb_inserv_rtsp_log\\'
stb_inserv_rtsp_type = 'STB-INSERV-RTSP'

stb_pm_vmos_error = 'd:\error\stb_pm_vmos_error\\'
stb_pm_vmos_log = 'd:\log\stb_pm_vmos_log\\'
stb_pm_vmos_type = 'STB-PM-VMOS'

stb_inserv_http_error = 'd:\error\stb_inserv_http_error\\'
stb_inserv_http_log = 'd:\log\stb_inserv_http_log\\'
stb_inserv_http_type = 'STB-INSERV-HTTP'

stb_trans_error = 'd:\error\stb_trans_error\\'
stb_trans_log = 'd:\log\stb_trans_log\\'
stb_trans_type = 'STB-TRANS'

stb_pmview_error = 'd:\error\stb_pmview_error\\'
stb_pmview_log = 'd:\log\stb_pmview_log\\'
stb_pmview_type = 'STB-PMVIEW'

stb_mos_error = 'd:\error\stb_mos_error\\'
stb_mos_log = 'd:\log\stb_mos_log\\'
stb_mos_type = 'STB-MOS'

vsource_mdp_error = 'd:\error\\vsource_mdp_error\\'
vsource_mdp_log = 'd:\log\\vsource_mdp_log\\'
vsource_mdp_type = 'VSOURCE-MDP'

vsource_qlt_error = 'd:\error\\vsource_qlt_error\\'
vsource_qlt_log = 'd:\log\\vsource_qlt_log\\'
vsource_qlt_type = 'VSOURCE-QLT'

iptv_link_pm_error = 'd:\error\iptv_link_pm_error\\'
iptv_link_pm_log = 'd:\log\iptv_link_pm_log\\'
iptv_link_pm_type = 'IPTV-LINK-PM'

iptv_view_pm_error = 'd:\error\iptv_view_pm_error\\'
iptv_view_pm_log = 'd:\log\iptv_view_pm_log\\'
iptv_view_pm_type = 'IPTV-VIEW-PM'

iptv_user_pm_error = 'd:\error\iptv_user_pm_error\\'
iptv_user_pm_log = 'd:\log\iptv_user_pm_log\\'
iptv_user_pm_type = 'IPTV-USER-PM'

user_vtime_error = 'd:\error\user_vtime_error\\'
user_vtime_log = 'd:\log\user_vtime_log\\'
user_vtime_type = 'USER-VTIME'

iptv_liveava_error = 'd:\error\iptv_liveava_error\\'
iptv_liveava_log = 'd:\log\iptv_liveava_log\\'
iptv_liveava_type = 'IPTV-LIVEAVA-PM'

vsource_faults_error = 'd:\error\\vsource_faults_error\\'
vsource_faults_log = 'd:\log\\vsource_faults_log\\'
vsource_faults_type = 'VSOURCE-FAULTS'

vsource_livechninfo_error = 'd:\error\\vsource_livechninfo_error\\'
vsource_livechninfo_log = 'd:\log\\vsource_livechninfo_log\\'
vsource_livechninfo_type = 'VSOURCE-LIVECHNINFO'

vsource_liveconinfo_error = 'd:\error\\vsource_liveconinfo_error\\'
vsource_liveconinfo_log = 'd:\log\\vsource_liveconinfo_log\\'
vsource_liveconinfo_type = 'VSOURCE-LIVECONINFO'

vsource_vodconinfo_error = 'd:\error\\vsource_vodconinfo_error\\'
vsource_vodconinfo_log = 'd:\log\\vsource_vodconinfo_log\\'
vsource_vodconinfo_type = 'VSOURCE-VODCONINFO'

'''