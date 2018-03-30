# -*- coding: utf-8 -*-
#!/usr/bin/env python

# 验证函数
class Check:
    
    def cdn_pm(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[6]) < 100000
                    and float(line[7]) < 100000
                    and float(line[8]) < 100000
                    and float(line[9]) < 100000
                    and float(line[10]) < 100000
                    and float(line[11]) < 100000
                    and float(line[12]) < 100000
                    and float(line[14]) < 100000
                    and float(line[15]) < 100000
                    and float(line[16]) < 100000):

                    # 对数据逻辑性验证
                    if (float(line[7]) > float(line[6])
                        or float(line[9]) > float(line[10])
                        or float(line[11]) > float(line[12])
                        or float(line[15]) > float(line[16])):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error

    def iptv_link_pm(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (        float(line[3]) < 50
                        and float(line[4]) < 50
                        # and float(line[8])<10000
                        # and float(line[9])<10000
                        # and float(line[10])<1000
                        # and float(line[11])<1000
                        # and float(line[12])<50000
                        # and float(line[13])<1000
                        # and float(line[14])<1000
                        # and float(line[15])<500000
                        # and float(line[16])<1000000                 #非必填项
                        # and float(line[17])<1000000
                        # and float(line[18])<1000000
                        # and float(line[19])<1000000
                        # and float(line[20])<1000
                        # and float(line[21])<1000
                        # and float(line[22])<500000
                ):
                    # file_valid.write(everyline)
                    # 对数据逻辑性验证
                    if (
                            float(line[3]) > float(line[4])
                            # float(line[9])>float(line[8])
                            # or float(line[11])>float(line[10])
                            # or float(line[14])>float(line[13])
                            # or float(line[17]) > float(line[16])
                            # or float(line[21]) > float(line[20])
                    ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error

    def stb_inserv_rtsp(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[6]) < 20000
                        and float(line[7]) < 20000
                        and float(line[8]) < 100000
                        and float(line[9]) < 100000
                        and float(line[10]) < 100000
                        and float(line[11]) < 100000
                        and float(line[12]) < 50000
                        and float(line[13]) < 100000
                        and float(line[14]) < 100000
                        and float(line[15]) < 500000
                        # and float(line[16])<1000000                 #非必填项
                        # and float(line[17])<1000000
                        # and float(line[18])<1000000
                        # and float(line[19])<1000000
                        and float(line[20]) < 100000
                        and float(line[21]) < 100000
                        and float(line[22]) < 500000
                ):
                    # file_valid.write(everyline)
                    # 对数据逻辑性验证
                    if (
                            # float(line[6])>float(line[7])
                            float(line[9]) > float(line[8])
                            or float(line[11]) > float(line[10])
                            or float(line[14]) > float(line[13])
                            # or float(line[17]) > float(line[16])
                            or float(line[21]) > float(line[20])
                    ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error

    def stb_mos(self, file_1, file_error, city_error, city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else:
                if (float(line[5]) <= 5
                        and float(line[6]) <= 5
                        and float(line[7]) <= 5
                        and float(line[8]) <= 5
                        and float(line[9]) <= 5
                        and float(line[10]) <= 5
                        and float(line[11]) <= 900
                        # and float(line[13])<1000000
                        # and float(line[14])<1000000
                        # and float(line[15])<1000000
                        # and float(line[16])<1000000
                        # and float(line[17])<1000000
                        # and float(line[18])<1000000
                        # and float(line[19])<1000000
                        # and float(line[20])<1000000
                        # and float(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    # if (float(line[5]) > float(line[6])
                    #         or float(line[7]) > float(line[5])
                    #         or float(line[8]) > float(line[9])
                    #         or float(line[10]) > float(line[8])
                    # ):
                    #     file_error.write(everyline)
                    #     num_error += 1
                    #     x = float(line[2])
                    #     city_error[x] += 1
                    # else:
                    #     file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1

        return num_valid, num_error

    def stb_pmview(self, file_1, file_error,city_error, city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else:
                if (float(line[7]) <= 100
                        and float(line[9]) <= 900
                        # and float(line[8])<1000000
                        # and float(line[9])<1000000
                        # and float(line[10])<1000000
                        # and float(line[11])<1000000
                        # and float(line[12])<1000000
                        # and float(line[13])<1000000
                        # and float(line[14])<1000000
                        # and float(line[15])<1000000
                        # and float(line[16])<1000000
                        # and float(line[17])<1000000
                        # and float(line[18])<1000000
                        # and float(line[19])<1000000
                        # and float(line[20])<1000000
                        # and float(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    # file_valid.write(everyline)
                    num_valid += 1
                    x = float(line[2])
                    city_valid[x] += 1

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1

        return num_valid, num_error

    def stb_pm_vmos(self, file_1, file_error, city_error, city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else:
                if (float(line[5]) < 100000
                        and float(line[6]) <= 900
                        # and float(line[7])<1000000
                        # and float(line[9])<1000000
                        # and float(line[8])<1000000
                        # and float(line[11])<1000000
                        # and float(line[12])<1000000
                        # and float(line[14])<1000000
                        # and float(line[15])<1000000
                        # and float(line[16])<1000000
                ):
                    # file_valid.write(everyline)
                    num_valid += 1
                    x = float(line[2])
                    city_valid[x] += 1
                # 对数据逻辑性验证
                # if (     float(line[3])>float(line[4])
                # or float(line[8])>float(line[9])
                # or float(line[11])>float(line[12])
                # or float(line[15])>float(line[16])
                # ):
                #     file_error.write(everyline)
                # else:
                #     file_valid.write(everyline)

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1

        return num_valid, num_error

    def stb_trans(self, file_1, file_error, city_error, city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else:
                if (float(line[15]) < 10000000
                        and float(line[16]) < 1000
                        and float(line[17]) <= 100
                        and float(line[18]) <= 100
                        and float(line[19]) < 10000
                        and float(line[20]) < 10000
                        and float(line[21]) < 10000
                        and float(line[22]) < 10000
                        and float(line[25]) <= 100
                        and float(line[26]) <= 900
                        and float(line[27]) <= 100
                        and float(line[28]) <= 100
                        # and float(line[18])<1000000
                        # and float(line[19])<1000000
                        # and float(line[20])<1000000
                        # and float(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    # if (
                    #         float(line[6]) > float(line[7])
                    #         or float(line[8]) > float(line[9])
                    #         or float(line[10]) > float(line[11])
                    #         or float(line[12]) > float(line[13])
                    #         or float(line[17]) > float(line[18])
                    #         or float(line[19]) > float(line[20])
                    #         or float(line[21]) > float(line[22])
                    # ):
                    #     file_error.write(everyline)
                    #     num_error += 1
                    #     x = float(line[2])
                    #     city_error[x] += 1
                    # else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1

                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1

        return num_valid, num_error

    def epg_pm(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[6]) < 100000
                    and float(line[7]) < 100000
                    and float(line[8]) < 100000
                    and float(line[9]) < 100000
                    # and float(line[10]) < 50
                    # and float(line[11]) < 500
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                ):

                    # 对数据逻辑性验证
                    if (   float(line[6]) > float(line[7])
                        or float(line[8]) > float(line[9])
                        # or float(line[11]) > float(line[12])
                        # or float(line[15]) > float(line[16])
                ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def stb_cm2(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[3]) < 100000
                    and float(line[4]) < 100000
                    # and float(line[8]) < 100000
                    # and float(line[9]) < 100000
                    # and float(line[10]) < 50
                    # and float(line[11]) < 500
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                ):

                    # 对数据逻辑性验证
                    if (   float(line[4]) > float(line[3])
                        # or float(line[8]) > float(line[9])
                        # or float(line[11]) > float(line[12])
                        # or float(line[15]) > float(line[16])
                ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def stb_inserv_http(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[10]) < 100000
                    and float(line[11]) < 100000
                    and float(line[13]) < 100000
                    and float(line[14]) < 100000
                    and float(line[15]) < 100000
                    and float(line[16]) < 100000
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                ):

                    # 对数据逻辑性验证
                    if (   float(line[11]) > float(line[10])
                        or float(line[14]) > float(line[13])
                        or float(line[15]) > float(line[16])
                        # or float(line[15]) > float(line[16])
                ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def stb_cm1(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def vsource_mdp(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def vsource_qlt(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def iptv_view_pm(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def iptv_user_pm(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def user_vtime(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[3]) < 1000000000
                    and float(line[4]) < 1000000000
                    and float(line[5]) < 1000000000
                    # and float(line[9]) < 50
                    # and float(line[10]) < 50
                    # and float(line[11]) < 500
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                    ):

                    # 对数据逻辑性验证
                    if (float(line[4]) > float(line[3])
                        or float(line[5]) > float(line[3])
                        # or float(line[11]) > float(line[12])
                        # or float(line[15]) > float(line[16])
                    ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def iptv_liveava(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def vsource_faults1(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[6]) < 1000000000
                    and float(line[7]) < 1000000000
                    and float(line[8]) < 1000000000
                    and float(line[9]) < 1000000000
                    and float(line[10]) < 1000000000
                    and float(line[5]) < 1000000000
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                ):

                    # 对数据逻辑性验证
                    if (float(line[6]) > float(line[5])
                        or float(line[7]) > float(line[5])
                        or float(line[8]) > float(line[5])
                        or float(line[9]) > float(line[5])
                        or float(line[10]) > float(line[5])
                    ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def vsource_faults2(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                if (float(line[6]) < 1000000000
                    and float(line[7]) < 1000000000
                    and float(line[8]) < 1000000000
                    and float(line[9]) < 1000000000
                    and float(line[10]) < 1000000000
                    and float(line[5]) < 1000000000
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
                ):

                    # 对数据逻辑性验证
                    if (float(line[6]) > float(line[5])
                        or float(line[7]) > float(line[5])
                        or float(line[8]) > float(line[5])
                        or float(line[9]) > float(line[5])
                        or float(line[10]) > float(line[5])
                    ):
                        file_error.write(everyline)
                        num_error += 1
                        x = float(line[2])
                        city_error[x] += 1
                    else:
                        # file_valid.write(everyline)
                        num_valid += 1
                        x = float(line[2])
                        city_valid[x] += 1
                else:
                    file_error.write(everyline)
                    num_error += 1
                    x = float(line[2])
                    city_error[x] += 1
        return num_valid,num_error
    
    def vsource_livechninfo(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def vsource_liveconinfo(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    
    def vsource_vodconinfo(self,file_1,file_error,city_error,city_valid):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\n' else x for x in line]
            if float(line[2]) not in city_error:
                file_error.write(everyline)
                num_error += 1
                city_error[10010] += 1
                # return False
            else :
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid,num_error
    

    

