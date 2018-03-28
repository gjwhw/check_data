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
                if (float(line[6]) < 1000000
                    and float(line[7]) < 100000
                    and float(line[8]) < 500000
                    and float(line[9]) < 500000
                    # and float(line[10]) < 50
                    # and float(line[11]) < 500
                    # and float(line[12]) < 500
                    # and float(line[14]) < 10000
                    # and float(line[15]) < 100000
                    # and float(line[16]) < 100000
					):

                    # 对数据逻辑性验证
                    if (float(line[6]) > float(line[7])
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

    def user_info(self,file_1,file_error,city_error,city_valid):
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
                if (        float(line[3]) < 100000
                        and float(line[4]) < 100000
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

    def stb_pm_opers(self,file_1,file_error,city_error,city_valid):
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
                        and float(line[13]) < 100000
                        and float(line[14]) < 100000
                        and float(line[15]) < 100000
                        and float(line[16])<100000                #非必填项
                        and float(line[17])<100000
                        and float(line[18])<100000
                        and float(line[19])<100000
                        and float(line[20]) < 100000
                        and float(line[21]) < 100000
                        and float(line[22]) < 100000
                        and float(line[23]) < 100000  # 非必填项
                        and float(line[24]) < 100000
                        and float(line[25]) < 100000
                        and float(line[26]) < 100000
                        and float(line[27]) < 100000
                        and float(line[28]) < 100000
                        and float(line[29]) < 100000
                        and float(line[30]) < 100000  # 非必填项
                        and float(line[31]) < 100000
                        and float(line[32]) < 100000
                        and float(line[33]) < 100000
                        and float(line[34]) < 100000
                        and float(line[35]) < 100000
                        and float(line[36]) < 100000
                        and float(line[37]) < 100000
                        and float(line[38]) < 100000
                ):
                    # file_valid.write(everyline)
                    # 对数据逻辑性验证
                    if (
                            float(line[7])>float(line[8])
                            or float(line[9]) > float(line[10])
                            or float(line[13]) > float(line[15])
                            or float(line[14]) > float(line[16])
                            or float(line[17]) > float(line[18])
                            or float(line[19]) > float(line[20])
                            or float(line[21]) > float(line[22])
                            or float(line[23]) > float(line[25])
                            or float(line[24]) > float(line[26])
                            or float(line[27]) > float(line[28])
                            or float(line[29]) > float(line[30])
                            or float(line[31]) > float(line[32])
                            or float(line[33]) > float(line[34])
                            or float(line[35]) > float(line[36])
                            or float(line[37]) > float(line[38])
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

    def stb_cm(self, file_1, file_error, city_error, city_valid):
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
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
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
                if (float(line[9]) < 100
                        and float(line[10]) < 100
                        and float(line[11]) < 100
                        and float(line[12]) < 100
                        # and float(line[10]) < 50
                        # and float(line[11]) < 500
                        # and float(line[12]) < 500
                        # and float(line[14]) < 10000
                        # and float(line[15]) < 100000
                        # and float(line[16]) < 100000
                ):
            
                    # 对数据逻辑性验证
                    if (float(line[13]) > float(line[14])
                            or float(line[16]) > float(line[15])
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

    def nsccs_pm(self, file_1, file_error, city_error, city_valid):
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
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid, num_error
    
    def csss_pm1(self, file_1, file_error, city_error, city_valid):
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
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid, num_error

    def csss_pm2(self, file_1, file_error, city_error, city_valid):
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
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid, num_error
    
    def cdn_link_pm(self, file_1, file_error, city_error, city_valid):
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
                # file_valid.write(everyline)
                num_valid += 1
                x = float(line[2])
                city_valid[x] += 1
        return num_valid, num_error
    
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
                if (float(line[5]) < 100000
                    and float(line[6]) < 100000
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
                    if (   float(line[5]) > float(line[6])
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