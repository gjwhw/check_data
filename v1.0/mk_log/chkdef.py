# -*- coding: utf-8 -*-
#!/usr/bin/env python
import city
# 验证函数
class Check:
    
    def cdn_pm(self,file_1,file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else :
                if (int(line[6]) < 10000
                    and int(line[7]) < 10000
                    and int(line[8]) < 50
                    and float(line[9]) < 50
                    and int(line[10]) < 50
                    and float(line[11]) < 500
                    and int(line[12]) < 500
                    and int(line[14]) < 10000
                    and int(line[15]) < 100000
                    and int(line[16]) < 100000):

                    # 对数据逻辑性验证
                    if (int(line[7]) > int(line[6])
                        or float(line[9]) > int(line[10])
                        or float(line[11]) > int(line[12])
                        or int(line[15]) > int(line[16])):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1
                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid,num_error

    def iptv_link_pm(self,file_1,file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else :
                if (float(line[3]) < 50
                        and float(line[4]) < 50
                        # and int(line[8])<10000
                        # and int(line[9])<10000
                        # and int(line[10])<1000
                        # and int(line[11])<1000
                        # and float(line[12])<50000
                        # and int(line[13])<1000
                        # and int(line[14])<1000
                        # and float(line[15])<500000
                        # and int(line[16])<1000000                 #非必填项
                        # and int(line[17])<1000000
                        # and int(line[18])<1000000
                        # and int(line[19])<1000000
                        # and int(line[20])<1000
                        # and int(line[21])<1000
                        # and float(line[22])<500000
                ):
                    # file_valid.write(everyline)
                    # 对数据逻辑性验证
                    if (
                            float(line[3]) > float(line[4])
                            # int(line[9])>int(line[8])
                            # or int(line[11])>int(line[10])
                            # or int(line[14])>int(line[13])
                            # or int(line[17]) > int(line[16])
                            # or int(line[21]) > int(line[20])
                    ):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1

                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid,num_error

    def stb_inserv_rtsp(self,file_1,file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else :
                if (float(line[6]) < 20000
                        and int(line[7]) < 20000
                        and int(line[8]) < 10000
                        and int(line[9]) < 10000
                        and int(line[10]) < 1000
                        and int(line[11]) < 1000
                        and float(line[12]) < 50000
                        and int(line[13]) < 1000
                        and int(line[14]) < 1000
                        and float(line[15]) < 500000
                        # and int(line[16])<1000000                 #非必填项
                        # and int(line[17])<1000000
                        # and int(line[18])<1000000
                        # and int(line[19])<1000000
                        and int(line[20]) < 1000
                        and int(line[21]) < 1000
                        and float(line[22]) < 500000
                ):
                    # file_valid.write(everyline)
                    # 对数据逻辑性验证
                    if (
                            # float(line[6])>int(line[7])
                            int(line[9]) > int(line[8])
                            or int(line[11]) > int(line[10])
                            or int(line[14]) > int(line[13])
                            # or int(line[17]) > int(line[16])
                            or int(line[21]) > int(line[20])
                    ):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1

                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid,num_error

    def stb_mos(self, file_1, file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else:
                if (float(line[5]) <= 5
                        and float(line[6]) <= 5
                        and float(line[7]) <= 5
                        and float(line[8]) <= 5
                        and float(line[9]) <= 5
                        and float(line[10]) <= 5
                        and float(line[11]) <= 900
                        # and int(line[13])<1000000
                        # and int(line[14])<1000000
                        # and float(line[15])<1000000
                        # and int(line[16])<1000000
                        # and int(line[17])<1000000
                        # and int(line[18])<1000000
                        # and int(line[19])<1000000
                        # and int(line[20])<1000000
                        # and int(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    if (float(line[5]) > float(line[6])
                            or float(line[7]) > float(line[5])
                            or float(line[8]) > float(line[9])
                            or float(line[10]) > float(line[8])
                    ):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1
                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid, num_error

    def stb_pmview(self, file_1, file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else:
                if (float(line[7]) <= 100
                        and int(line[9]) <= 900
                        # and int(line[8])<1000000
                        # and int(line[9])<1000000
                        # and int(line[10])<1000000
                        # and int(line[11])<1000000
                        # and float(line[12])<1000000
                        # and int(line[13])<1000000
                        # and int(line[14])<1000000
                        # and float(line[15])<1000000
                        # and int(line[16])<1000000
                        # and int(line[17])<1000000
                        # and int(line[18])<1000000
                        # and int(line[19])<1000000
                        # and int(line[20])<1000000
                        # and int(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    file_valid.write(everyline)
                    num_valid += 1
                    # x = int(line[2])
                    # city_valid[x] += 1


                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid, num_error

    def stb_pm_vmos(self, file_1, file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else:
                if (float(line[5]) < 2000
                        and float(line[6]) <= 900
                        # and float(line[7])<1000000
                        # and float(line[9])<1000000
                        # and float(line[8])<1000000
                        # and float(line[11])<1000000
                        # and int(line[12])<1000000
                        # and int(line[14])<1000000
                        # and int(line[15])<1000000
                        # and int(line[16])<1000000
                ):
                    file_valid.write(everyline)
                    num_valid += 1
                    # x = int(line[2])
                    # city_valid[x] += 1
                # 对数据逻辑性验证
                # if (     int(line[3])>int(line[4])
                # or float(line[8])>int(line[9])
                # or float(line[11])>int(line[12])
                # or int(line[15])>int(line[16])
                # ):
                #     file_error.write(everyline)
                # else:
                #     file_valid.write(everyline)

                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid, num_error

    def stb_trans(self, file_1, file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else:
                if (float(line[15]) < 10000000
                        and float(line[16]) < 1000
                        and float(line[17]) <= 1
                        and float(line[18]) <= 1
                        and float(line[19]) < 10000
                        and float(line[20]) < 10000
                        and float(line[21]) < 10000
                        and float(line[22]) < 10000
                        and float(line[25]) <= 1
                        and float(line[26]) <= 900
                        and float(line[27]) <= 1
                        and float(line[28]) <= 1
                        # and int(line[18])<1000000
                        # and int(line[19])<1000000
                        # and int(line[20])<1000000
                        # and int(line[21])<1000000
                        # and float(line[22])<1000000
                ):
                    if (
                            float(line[6]) > float(line[7])
                            or float(line[8]) > float(line[9])
                            or float(line[10]) > float(line[11])
                            or float(line[12]) > float(line[13])
                            or float(line[17]) > float(line[18])
                            or float(line[19]) > float(line[20])
                            or float(line[21]) > float(line[22])
                    ):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1

                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid, num_error

    def epg_pm(self,file_1,file_valid,city_error):
        num_error = 0
        num_valid = 0
        for everyline in file_1:
            line = everyline.split('|')
            line = [0 if x == '' or x == '\r\n' else x for x in line]
            if not city_error.has_key(int(line[2])):
                # file_error.write(everyline)
                num_error += 1
                # city_error[10010] += 1
                # return False

            else :
                if (int(line[6]) < 30000
                    and int(line[7]) < 30000
                    and int(line[8]) < 100000
                    and float(line[9]) < 100000
                    # and int(line[10]) < 50
                    # and float(line[11]) < 500
                    # and int(line[12]) < 500
                    # and int(line[14]) < 10000
                    # and int(line[15]) < 100000
                    # and int(line[16]) < 100000
                 ):

                    # 对数据逻辑性验证
                    if (int(line[6]) > int(line[7])
                        or float(line[8]) > int(line[9])
                        # or float(line[11]) > int(line[12])
                        # or int(line[15]) > int(line[16])
                         ):
                        # file_error.write(everyline)
                        num_error += 1
                        # x = int(line[2])
                        # city_error[x] += 1

                    else:
                        file_valid.write(everyline)
                        num_valid += 1
                        # x = int(line[2])
                        # city_valid[x] += 1
                else:
                    # file_error.write(everyline)
                    num_error += 1
                    # x = int(line[2])
                    # city_error[x] += 1

        return num_valid,num_erro

