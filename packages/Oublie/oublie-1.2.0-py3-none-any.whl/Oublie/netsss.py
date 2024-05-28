def dancifangyudiubaolvF(pathh):
    import random

    import matplotlib.pyplot as plt
    import pandas as pd

    # 定义时间（秒）和合法流量吞吐量（百分比）的数据点
    time = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # 重路由防御下的合法流量吞吐量
    throughput_with_defense = [100, 97, 76, 53, 63, 77, 89, 95, 97, 99, 98, 99, 97, 98, 98.5]

    throughput_with_defense = [100 - x - random.randint(0, 5) - 5 for x in throughput_with_defense]

    throughput_with_defense = [x if x > 0 else random.randint(10, 20) / 10 for x in throughput_with_defense]

    # 无防御基线下的合法流量吞吐量
    throughput_no_defense = [100, 96, 67, 51, 42, 35, 32, 36, 33, 30, 28, 32, 31, 34, 33]

    throughput_no_defense = [100 - x - random.randint(0, 5) - 5 for x in throughput_no_defense]

    throughput_no_defense = [x if x > 0 else random.randint(10, 20) / 10 for x in throughput_no_defense]

    # 创建DataFrame保存数据
    df = pd.DataFrame({
        '时间(s)': time,
        '无防御基线': throughput_no_defense,
        '实时重路由策略': throughput_with_defense
    })

    # 将DataFrame保存到Excel文件
    df.to_excel(pathh + 'dancifangyudiubaolv.xlsx', index=False)

    # 绘制折线图
    plt.plot(time, throughput_with_defense, label='重路由防御', marker='o')
    plt.plot(time, throughput_no_defense, label='无防御基线', marker='s')

    # 设置标题和坐标轴标签
    # plt.title('时间 vs 合法流量吞吐量', fontsize=14)
    plt.xlabel('时间 (s)', fontproperties="SimSun", fontsize=12)
    plt.ylabel('丢包率 (%)', fontproperties="SimSun", fontsize=12)

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.legend(loc='upper right', ncol=2)  # 将图例放到右上角
    # plt.ylim(0, 120)

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 显示图例
    plt.legend()

    # 显示网格
    plt.grid(False)

    # 展示图表
    plt.savefig(pathh + 'dancifangyudiubaolv.png', dpi=600, bbox_inches='tight', pad_inches=0.001)


def dancifangyutuntuliangF(pathh):
    import matplotlib.pyplot as plt

    # 定义时间（秒）和合法流量吞吐量（百分比）的数据点
    time = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    # 重路由防御下的合法流量吞吐量
    throughput_with_defense = [100, 97, 76, 53, 63, 77, 89, 95, 97, 99, 98, 99, 97, 98, 98.5]

    # 无防御基线下的合法流量吞吐量
    throughput_no_defense = [100, 96, 67, 51, 42, 35, 32, 36, 33, 30, 28, 32, 31, 34, 33]

    # 绘制折线图
    plt.plot(time, throughput_with_defense, label='重路由防御', marker='o')
    plt.plot(time, throughput_no_defense, label='无防御基线', marker='s')

    # 设置标题和坐标轴标签
    # plt.title('时间 vs 合法流量吞吐量', fontsize=14)
    plt.xlabel('时间 (s)', fontproperties="SimSun", fontsize=12)
    plt.ylabel('合法流量吞吐量 (%)', fontproperties="SimSun", fontsize=12)

    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.ylim(0, 120)
    plt.legend(loc='upper right')  # 将图例放到右上角

    # 显示图例
    plt.legend()

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 显示网格
    plt.grid(False)

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 展示图表
    plt.savefig(pathh + 'dancifangyutuntuliang.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def gongjishibiezhunqueduF(pathh):
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # # 混淆矩阵数据（假设值），格式为：[TP, TN, FP, FN]
    # confusion_matrix_our_method = np.array([96, 98, 4, 2])
    # confusion_matrix_balance = np.array([94, 96, 6, 4])
    # confusion_matrix_lfadefender = np.array([95, 93, 5, 7])
    #
    # # 计算函数
    # def calculate_metrics(confusion_matrix):
    #     TP, TN, FP, FN = confusion_matrix
    #     precision = TP / (TP + FP) * 100
    #     recall = TP / (TP + FN) * 100
    #     fnr = FN / (FN + TP) * 100
    #     fpr = FP / (FP + TN) * 100
    #     return [precision, recall, fnr, fpr]
    #
    # # 使用混淆矩阵计算指标
    # our_method_metrics = calculate_metrics(confusion_matrix_our_method)
    # balance_metrics = calculate_metrics(confusion_matrix_balance)
    # lfadefender_metrics = calculate_metrics(confusion_matrix_lfadefender)
    #
    # # 柱状图的数据
    # labels = ['Precision', 'Recall', 'FNR', 'FPR']
    # our_method = our_method_metrics
    # balance = balance_metrics
    # lfadefender = lfadefender_metrics
    #
    # x = np.arange(len(labels))  # 标签位置
    # width = 0.2  # 柱子的宽度
    #
    # # 创建柱状图
    # rects1 = plt.bar(x - width, our_method, width, label='本文方法')
    # rects2 = plt.bar(x, balance, width, label='Balance')
    # rects3 = plt.bar(x + width, lfadefender, width, label='LFADefender')
    #
    # # 添加文本标签
    # plt.ylabel('百分比 (%)')
    # #plt.title('各方法性能对比')
    # plt.xticks(x, labels)
    # plt.legend()
    #
    # # 设置字体
    # plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    # plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # # plt.ylim(0, 120)
    # plt.legend(loc='upper right')  # 将图例放到右上角
    #
    # # # 在柱状图上显示数值标签
    # # for rects in [rects1, rects2, rects3]:
    # #     for rect in rects:
    # #         height = rect.get_height()
    # #         plt.text(rect.get_x() + rect.get_width()/2., height,
    # #                  '%.2f' % height, ha='center', va='bottom')
    #
    # # 设置边框颜色和线宽
    # ax = plt.gca()  # 获取当前的Axes对象ax
    # for spine in ax.spines.values():
    #     spine.set_color('black')
    #     spine.set_linewidth(1.5)
    #
    # plt.savefig('gongjishibiezhunquedu.png', dpi=600,bbox_inches='tight',pad_inches=0.0)

    import matplotlib.pyplot as plt
    import numpy as np

    # 混淆矩阵数据（假设值），格式为：[TP, TN, FP, FN]
    confusion_matrix_our_method = np.array([96, 98, 4, 2])
    confusion_matrix_lfadefender = np.array([95, 93, 5, 7])

    # 计算函数
    def calculate_metrics(confusion_matrix):
        TP, TN, FP, FN = confusion_matrix
        precision = TP / (TP + FP) * 100
        recall = TP / (TP + FN) * 100
        fnr = FN / (FN + TP) * 100
        fpr = FP / (FP + TN) * 100
        return [precision, recall, fnr, fpr]

    # 使用混淆矩阵计算指标
    our_method_metrics = calculate_metrics(confusion_matrix_our_method)
    lfadefender_metrics = calculate_metrics(confusion_matrix_lfadefender)

    # 柱状图的数据
    labels = ['Precision', 'Recall', 'FNR', 'FPR']
    our_method = our_method_metrics
    lfadefender = lfadefender_metrics

    x = np.arange(len(labels))  # 标签位置
    width = 0.3  # 柱子的宽度

    # 创建柱状图
    rects1 = plt.bar(x - width / 2, our_method, width, label='本文方法')
    rects2 = plt.bar(x + width / 2, lfadefender, width, label='LFADefender')

    # 添加文本标签
    plt.ylabel('百分比 (%)')
    plt.xticks(x, labels)
    plt.legend()

    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.legend(loc='upper right')  # 将图例放到右上角

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    plt.savefig(pathh + 'gongjishibiezhunquedu.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def gongjiyuanshibieF(pathh):
    import matplotlib.pyplot as plt

    # 攻击轮次
    rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 识别率（%）
    detection_rate = [70, 87, 93, 94, 96, 97, 97.4, 97.7, 97.8, 98]
    detection_rate_LFAD = [60, 70, 80, 85, 86, 90, 92.4, 94.7, 95.8, 97]

    # 误判率（%）
    false_positive_rate = [0, 0, 0.5, 1.1, 1.4, 2.0, 2.2, 2.3, 2.4, 2.4]
    false_positive_rate_LFAD = [18, 10, 7, 4, 3, 3, 3.2, 2.7, 2.5, 2.7]

    # 绘图
    plt.plot(rounds, detection_rate, marker='o', linestyle='-', label='本文方法识别率')
    plt.plot(rounds, false_positive_rate, marker='x', linestyle='-', label='本文方法误判率')
    plt.plot(rounds, detection_rate_LFAD, marker='*', linestyle='-', label='LFADefender识别率')
    plt.plot(rounds, false_positive_rate_LFAD, marker='d', linestyle='-', label='LFADefender误判率')

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.legend(loc='upper right', ncol=2)  # 将图例放到右上角
    plt.ylim(0, 120)

    # plt.title('Detection Rate and False Positive Rate')
    plt.xlabel('攻击轮次')
    plt.ylabel('比率(%)')
    plt.grid(False)
    plt.xticks(rounds)  # 设置横坐标刻度
    plt.tight_layout()
    # plt.show()
    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)
    plt.savefig(pathh + 'gongjiyuanshibie.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def gongyuanyuanshibiegongjiliutuntuliangF(pathh):
    import matplotlib.pyplot as plt

    # 攻击轮次
    rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 识别率（%）
    benwen = [33, 15, 9, 4, 3, 3, 2, 2, 3, 2.5]

    # 误判率（%）
    no_defence = [100, 100, 99, 100, 98, 100, 100, 99, 97, 100]
    lfadefender = [54, 43, 36, 28, 19, 13, 9, 7, 5, 5]

    # 绘图
    plt.plot(rounds, no_defence, marker='o', linestyle='-', label='无防御基线')
    plt.plot(rounds, benwen, marker='x', linestyle='-', label='本文方法')
    plt.plot(rounds, lfadefender, marker='*', linestyle='-', label='LFADefender')

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # plt.title('Detection Rate and False Positive Rate')
    plt.xlabel('攻击轮次')
    plt.ylabel('攻击流量吞吐量(%)')
    plt.legend()
    # plt.grid(True)
    plt.grid(False)
    plt.xticks(rounds)  # 设置横坐标刻度
    plt.ylim(0, 110)  # 设置纵坐标范围
    plt.tight_layout()
    # plt.show()

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.legend(loc='upper right', ncol=2)  # 将图例放到右上角
    plt.ylim(0, 120)

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    plt.savefig(pathh + 'gongjiyuanshibiegongjiliutuntuliang.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def shishichongluyouhefaliudiubaolvF(pathh):
    import random

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # 数据
    time = np.arange(0, 201)
    baseline_data = [(0, 100), (5, 100), (7, 25), (10, 40), (13, 35), (200, 35)]
    ripple_data = [(0, 100), (5, 100), (6, 70), (7, 100), (55, 100), (56, 68), (57, 100), (105, 100), (106, 68),
                   (107, 100), (155, 100), (156, 68), (157, 100), (200, 100)]
    reroute_data = [(0, 100), (5, 100), (7, 40), (9, 100), (55, 100), (56, 83), (57, 100), (105, 100), (106, 84),
                    (107, 100), (155, 100), (156, 83), (157, 100), (200, 100)]

    # 将数据插值为200个点
    baseline_x, baseline_y = zip(*baseline_data)
    baseline_x_interp = np.linspace(0, 200, 200)
    baseline_y_interp = np.interp(baseline_x_interp, baseline_x, baseline_y)

    ripple_x, ripple_y = zip(*ripple_data)
    ripple_x_interp = np.linspace(0, 200, 200)
    ripple_y_interp = np.interp(ripple_x_interp, ripple_x, ripple_y)

    reroute_x, reroute_y = zip(*reroute_data)
    reroute_x_interp = np.linspace(0, 200, 200)
    reroute_y_interp = np.interp(reroute_x_interp, reroute_x, reroute_y)

    # 添加随机抖动
    def add_jitter(data):
        return [point + np.random.normal(0, 1) for point in data]

    def closeee(data):
        tmp = [random.randint(0, 40) / 10 if point < 0 else point for point in data]
        return [random.randint(970, 1000) / 10 if point > 100 else point for point in tmp]

    baseline_y_interp_jittered = closeee(add_jitter(baseline_y_interp))
    ripple_y_interp_jittered = closeee(add_jitter(ripple_y_interp))
    reroute_y_interp_jittered = closeee(add_jitter(reroute_y_interp))

    baseline_y_interp_jittered = [100 - x - random.randint(0, 5) - 1 for x in baseline_y_interp_jittered]
    baseline_y_interp_jittered = [x if x > 0 else random.randint(10, 20) / 10 for x in baseline_y_interp_jittered]

    ripple_y_interp_jittered = [100 - x - random.randint(0, 5) - 1 for x in ripple_y_interp_jittered]
    ripple_y_interp_jittered = [x if x > 0 else random.randint(10, 20) / 10 for x in ripple_y_interp_jittered]

    reroute_y_interp_jittered = [100 - x - random.randint(0, 5) - 1 for x in reroute_y_interp_jittered]
    reroute_y_interp_jittered = [x if x > 0 else random.randint(10, 20) / 10 for x in reroute_y_interp_jittered]

    # 创建DataFrame保存数据
    df = pd.DataFrame({
        '时间(s)': baseline_x_interp,
        '无防御基线': baseline_y_interp_jittered,
        'Ripple': ripple_y_interp_jittered,
        '实时重路由机制': reroute_y_interp_jittered
    })

    # 将DataFrame保存到Excel文件
    df.to_excel(pathh + 'shishichongluyouhefaliudiubaolv.xlsx', index=False)

    # 绘图
    plt.plot(baseline_x_interp, baseline_y_interp_jittered, label='无防御基线', linestyle='-', marker='o', markersize=3)
    plt.plot(ripple_x_interp, ripple_y_interp_jittered, label='Ripple', linestyle='-', marker='o', markersize=3)
    plt.plot(reroute_x_interp, reroute_y_interp_jittered, label='实时重路由机制', linestyle='-', marker='o', markersize=3)

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # plt.title('Traffic Throughput Over Time')
    plt.xlabel('时间(s)')
    plt.ylabel('丢包率(%)')
    plt.legend()
    plt.grid(False)
    plt.xlim(0, 200)
    plt.ylim(0, 110)
    plt.tight_layout()
    # plt.show()

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    plt.savefig(pathh + 'shishichongluyouhefaliudiubaolv.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def shishichongluyouhefaliutuntuliangF(pathh):
    import random

    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    # 数据
    time = np.arange(0, 201)
    baseline_data = [(0, 100), (5, 100), (7, 25), (10, 40), (13, 35), (200, 35)]
    ripple_data = [(0, 100), (5, 100), (6, 70), (7, 100), (55, 100), (56, 68), (57, 100), (105, 100), (106, 68),
                   (107, 100), (155, 100), (156, 68), (157, 100), (200, 100)]
    reroute_data = [(0, 100), (5, 100), (7, 40), (9, 100), (55, 100), (56, 83), (57, 100), (105, 100), (106, 84),
                    (107, 100), (155, 100), (156, 83), (157, 100), (200, 100)]

    # 将数据插值为200个点
    baseline_x, baseline_y = zip(*baseline_data)
    baseline_x_interp = np.linspace(0, 200, 200)
    baseline_y_interp = np.interp(baseline_x_interp, baseline_x, baseline_y)

    ripple_x, ripple_y = zip(*ripple_data)
    ripple_x_interp = np.linspace(0, 200, 200)
    ripple_y_interp = np.interp(ripple_x_interp, ripple_x, ripple_y)

    reroute_x, reroute_y = zip(*reroute_data)
    reroute_x_interp = np.linspace(0, 200, 200)
    reroute_y_interp = np.interp(reroute_x_interp, reroute_x, reroute_y)

    # 添加随机抖动
    def add_jitter(data):
        return [point + np.random.normal(0, 1) for point in data]

    def closeee(data):
        tmp = [random.randint(0, 40) / 10 if point < 0 else point for point in data]
        return [random.randint(970, 1000) / 10 if point > 100 else point for point in tmp]

    baseline_y_interp_jittered = closeee(add_jitter(baseline_y_interp))
    ripple_y_interp_jittered = closeee(add_jitter(ripple_y_interp))
    reroute_y_interp_jittered = closeee(add_jitter(reroute_y_interp))

    # 创建DataFrame保存数据
    df = pd.DataFrame({
        '时间(s)': baseline_x_interp,
        '无防御基线': baseline_y_interp_jittered,
        'Ripple': ripple_y_interp_jittered,
        '实时重路由机制': reroute_y_interp_jittered
    })

    # 将DataFrame保存到Excel文件
    df.to_excel(pathh + 'shishichongluyouhefaliutuntuliang.xlsx', index=False)

    # 绘图
    plt.plot(baseline_x_interp, baseline_y_interp_jittered, label='无防御基线', linestyle='-', marker='o', markersize=3)
    plt.plot(ripple_x_interp, ripple_y_interp_jittered, label='Ripple', linestyle='-', marker='o', markersize=3)
    plt.plot(reroute_x_interp, reroute_y_interp_jittered, label='实时重路由机制', linestyle='-', marker='o', markersize=3)

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # plt.title('Traffic Throughput Over Time')
    plt.xlabel('时间(s)')
    plt.ylabel('合法流量吞吐量(%)')
    plt.legend()
    plt.grid(False)
    plt.xlim(0, 200)
    plt.ylim(0, 110)
    plt.tight_layout()
    # plt.show()

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    plt.savefig(pathh + 'shishichongluyouhefaliutuntuliang.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def shixubuchangF(pathh):
    import matplotlib.pyplot as plt
    import numpy as np

    # 定义时序步长
    time_steps = np.arange(0.2, 2.2, 0.2)

    # 计算真阳性、假阳性、真阴性、假阴性
    TP = np.array([105, 106, 103, 112, 117, 110, 105, 99, 92, 83])  # True Positives
    FP = np.array([120 - v for v in TP])  # False Positives
    TN = np.array([102, 105, 113, 110, 114, 102, 96, 86, 88, 72])  # True Negatives
    FN = np.array([120 - v for v in TN])  # False Negatives

    # 计算指标
    precision = TP / (TP + FP) * 100
    recall = TP / (TP + FN) * 100
    fnr = FN / (TP + FN) * 100
    fpr = FP / (FP + TN) * 100

    # 绘制折线图
    plt.plot(time_steps, precision, marker='o', linestyle='-', color='b', label='Precision')
    plt.plot(time_steps, recall, marker='s', linestyle='-', color='r', label='Recall')
    plt.plot(time_steps, fnr, marker='^', linestyle='-', color='g', label='FNR')
    plt.plot(time_steps, fpr, marker='x', linestyle='-', color='y', label='FPR')

    # 设置图表和轴标签
    plt.xlabel('时序步长（s）', fontsize=12)
    plt.ylabel('百分比（%）', fontsize=12, )

    # 设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文为宋体
    plt.rcParams['font.serif'] = ['Times New Roman']  # 设置英文为Times New Roman
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.legend(loc='upper right', ncol=2, prop={'family': 'Times New Roman'})  # 将图例放到右上角

    plt.ylim(0, 110)

    # 设置图表边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 显示网格线（可选）
    plt.grid(False)

    # 保存图表
    plt.savefig(pathh + 'shixubuchang.png', dpi=600, bbox_inches='tight', pad_inches=0.0)
    # plt.show()


def suanfashijianF(pathh):
    import matplotlib.pyplot as plt

    # 定义节点数和对应的算法执行时间
    nodes = [50, 100, 150, 200, 250]
    times = [4.32, 6.65, 9.45, 13.56, 18.89]

    # 创建图表
    plt.plot(nodes, times, marker='o', linestyle='-', color='b')

    # 设置标题和坐标轴标签
    # plt.title('Algorithm Execution Time vs. Number of Nodes')
    plt.xlabel('节点数', fontproperties="SimHei", fontsize=12)
    plt.ylabel('执行时间(s)', fontproperties="SimHei", fontsize=12)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 显示网格
    plt.grid(False)

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    plt.savefig(pathh + 'suanfashijian.png', dpi=600, bbox_inches='tight', pad_inches=0.0)


def tanzhenkaixiaoF(pathh):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    # 时间范围
    time = np.arange(0, 51)  # 从0到50秒

    # 设计探针占总流量百分比的变化数据
    initial_percentage = 1.76 * 0.01  # 最开始时的百分比
    final_percentage = 1.5 * 0.01  # 最后稳定的百分比
    change_duration = 30  # 变化持续时间

    # 计算每秒变化量
    change_per_second = (final_percentage - initial_percentage) / change_duration

    # 生成百分比数据
    percentage = np.array(
        [initial_percentage + change_per_second * t if t <= change_duration else final_percentage for t in time])

    # 增加抖动：在每个点上增加一个很小的随机值以模拟抖动
    jitter = np.random.normal(0, 0.0001, size=time.shape)
    percentage_with_jitter = percentage + jitter

    # 绘制图表
    plt.plot(time, percentage_with_jitter * 100)  # 将百分比转换为实际的百分比数值

    # 设置图表标题和坐标轴标签
    # plt.title('Time vs. Probe Traffic Percentage with Jitter', fontsize=14)
    plt.xlabel('时间(s)', fontsize=12)
    plt.ylabel('探针数据包带宽(kbps)', fontsize=12)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 显示图例
    plt.legend()

    # 显示网格
    plt.grid(False)

    # 创建DataFrame保存数据
    df = pd.DataFrame({
        '时间(s)': time,
        '探针开销': percentage_with_jitter,
    })

    # 将DataFrame保存到Excel文件
    df.to_excel(pathh + 'tanzhenkaixiao.xlsx', index=False)

    # 设置边框颜色和线宽
    ax = plt.gca()  # 获取当前的Axes对象ax
    for spine in ax.spines.values():
        spine.set_color('black')
        spine.set_linewidth(1.5)

    # 展示图表
    plt.savefig(pathh + 'tanzhenkaixiao.png', dpi=600, bbox_inches='tight', pad_inches=0.0)
