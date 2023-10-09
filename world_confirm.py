import requests
import json
import jsonpath
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
import datetime
from pyecharts.globals import GeoType, RenderType

# 1.一个目标网站
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# 2.请求资源，获取响应的内容
resp = requests.get(url)
# 3.提取数据
# 4.类型转换 json->dict（字典）
data = json.loads(resp.text)
name = jsonpath.jsonpath(data, "$..name")  # $..name代表根节点下任何子目录下的name标签
confirm = jsonpath.jsonpath(data, "$..confirm")  # $..confirm代表根节点下任何子目录下的confirm标签
# 5.由于获取的世界数据中没有中国的数据，因此需要单独获取中国的疫情数据
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
data = json.loads(requests.get(url).json()['data'])
china_confirm = data['chinaAdd']['confirm']
# 6.从网上获取世界各国的中英文映射列表
nameMap = {
    'Singapore Rep.': '新加坡',
    'Dominican Rep.': '多米尼加',
    'Palestine': '巴勒斯坦',
    'Bahamas': '巴哈马',
    'Timor-Leste': '东帝汶',
    'Afghanistan': '阿富汗',
    'Guinea-Bissau': '几内亚比绍',
    "Côte d'Ivoire": '科特迪瓦',
    'Siachen Glacier': '锡亚琴冰川',
    "Br. Indian Ocean Ter.": '英属印度洋领土',
    'Angola': '安哥拉',
    'Albania': '阿尔巴尼亚',
    'United Arab Emirates': '阿联酋',
    'Argentina': '阿根廷',
    'Armenia': '亚美尼亚',
    'French Southern and Antarctic Lands': '法属南半球和南极领地',
    'Australia': '澳大利亚',
    'Austria': '奥地利',
    'Azerbaijan': '阿塞拜疆',
    'Belgium': '比利时',
    'Bahrain': '巴林',
    'Benin': '贝宁',
    'Burkina Faso': '布基纳法索',
    'Bangladesh': '孟加拉',
    'Bulgaria': '保加利亚',
    'The Bahamas': '巴哈马',
    'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
    'Belarus': '白俄罗斯',
    'Belize': '伯利兹',
    'Bermuda': '百慕大',
    'Bolivia': '玻利维亚',
    'Brazil': '巴西',
    'Brunei': '文莱',
    'Bhutan': '不丹',
    'Botswana': '博茨瓦纳',
    'Central African Rep.': '中非',
    'Canada': '加拿大',
    'Switzerland': '瑞士',
    'Chile': '智利',
    'China': '中国',
    'Ivory Coast': '象牙海岸',
    'Cameroon': '喀麦隆',
    'Dem. Rep. Congo': '刚果民主共和国',
    'Congo': '刚果',
    'Colombia': '哥伦比亚',
    'Costa Rica': '哥斯达黎加',
    'Cuba': '古巴',
    'N. Cyprus': '北塞浦路斯',
    'Cyprus': '塞浦路斯',
    'Czech Rep.': '捷克',
    'Germany': '德国',
    'Djibouti': '吉布提',
    'Denmark': '丹麦',
    'Algeria': '阿尔及利亚',
    'Ecuador': '厄瓜多尔',
    'Egypt': '埃及',
    'Eritrea': '厄立特里亚',
    'Spain': '西班牙',
    'Estonia': '爱沙尼亚',
    'Ethiopia': '埃塞俄比亚',
    'Finland': '芬兰',
    'Fiji': '斐济',
    'Falkland Islands': '福克兰群岛',
    'France': '法国',
    'Gabon': '加蓬',
    'United Kingdom': '英国',
    'Georgia': '格鲁吉亚',
    'Ghana': '加纳',
    'Guinea': '几内亚',
    'Gambia': '冈比亚',
    'Guinea-Bissau': '几内亚比绍',
    'Eq. Guinea': '赤道几内亚',
    'Greece': '希腊',
    'Greenland': '丹麦',
    'Guatemala': '危地马拉',
    'French Guiana': '法属圭亚那',
    'Guyana': '圭亚那',
    'Honduras': '洪都拉斯',
    'Croatia': '克罗地亚',
    'Haiti': '海地',
    'Hungary': '匈牙利',
    'Indonesia': '印度尼西亚',
    'India': '印度',
    'Ireland': '爱尔兰',
    'Iran': '伊朗',
    'Iraq': '伊拉克',
    'Iceland': '冰岛',
    'Israel': '以色列',
    'Italy': '意大利',
    'Jamaica': '牙买加',
    'Jordan': '约旦',
    'Japan': '日本本土',
    'Kazakhstan': '哈萨克斯坦',
    'Kenya': '肯尼亚',
    'Kyrgyzstan': '吉尔吉斯斯坦',
    'Cambodia': '柬埔寨',
    'Korea': '韩国',
    'Kosovo': '科索沃',
    'Kuwait': '科威特',
    'Lao PDR': '老挝',
    'Lebanon': '黎巴嫩',
    'Liberia': '利比里亚',
    'Libya': '利比亚',
    'Sri Lanka': '斯里兰卡',
    'Lesotho': '莱索托',
    'Lithuania': '立陶宛',
    'Luxembourg': '卢森堡',
    'Latvia': '拉脱维亚',
    'Morocco': '摩洛哥',
    'Moldova': '摩尔多瓦',
    'Madagascar': '马达加斯加',
    'Mexico': '墨西哥',
    'Macedonia': '马其顿',
    'Mali': '马里',
    'Myanmar': '缅甸',
    'Montenegro': '黑山',
    'Mongolia': '蒙古',
    'Mozambique': '莫桑比克',
    'Mauritania': '毛里塔尼亚',
    'Malawi': '马拉维',
    'Malaysia': '马来西亚',
    'Namibia': '纳米比亚',
    'New Caledonia': '新喀里多尼亚',
    'Niger': '尼日尔',
    'Nigeria': '尼日利亚',
    'Nicaragua': '尼加拉瓜',
    'Netherlands': '荷兰',
    'Norway': '挪威',
    'Nepal': '尼泊尔',
    'New Zealand': '新西兰',
    'Oman': '阿曼',
    'Pakistan': '巴基斯坦',
    'Panama': '巴拿马',
    'Peru': '秘鲁',
    'Philippines': '菲律宾',
    'Papua New Guinea': '巴布亚新几内亚',
    'Poland': '波兰',
    'Puerto Rico': '波多黎各',
    'Dem. Rep. Korea': '朝鲜',
    'Portugal': '葡萄牙',
    'Paraguay': '巴拉圭',
    'Qatar': '卡塔尔',
    'Romania': '罗马尼亚',
    'Russia': '俄罗斯',
    'Rwanda': '卢旺达',
    'W. Sahara': '西撒哈拉',
    'Saudi Arabia': '沙特阿拉伯',
    'Sudan': '苏丹',
    'S. Sudan': '南苏丹',
    'Senegal': '塞内加尔',
    'Solomon Is.': '所罗门群岛',
    'Sierra Leone': '塞拉利昂',
    'El Salvador': '萨尔瓦多',
    'Somaliland': '索马里兰',
    'Somalia': '索马里',
    'Serbia': '塞尔维亚',
    'Suriname': '苏里南',
    'Slovakia': '斯洛伐克',
    'Slovenia': '斯洛文尼亚',
    'Sweden': '瑞典',
    'Swaziland': '斯威士兰',
    'Syria': '叙利亚',
    'Chad': '乍得',
    'Togo': '多哥',
    'Thailand': '泰国',
    'Tajikistan': '塔吉克斯坦',
    'Turkmenistan': '土库曼斯坦',
    'East Timor': '东帝汶',
    'Trinidad and Tobago': '特里尼达和多巴哥',
    'Tunisia': '突尼斯',
    'Turkey': '土耳其',
    'Tanzania': '坦桑尼亚',
    'Uganda': '乌干达',
    'Ukraine': '乌克兰',
    'Uruguay': '乌拉圭',
    'United States': '美国',
    'Uzbekistan': '乌兹别克斯坦',
    'Venezuela': '委内瑞拉',
    'Vietnam': '越南',
    'Vanuatu': '瓦努阿图',
    'West Bank': '西岸',
    'Yemen': '也门',
    'South Africa': '南非',
    'Zimbabwe': '津巴布韦',
    'Maldives': '马尔代夫',
    'Bosnia and Herzegovina': '波黑',
    'North Macedonia': '北马其顿',
    'Andorra': '安道尔',
    'Malta': '马耳他',
    'San Marino': '圣马力诺',
    'Isle of Man': '马恩岛',
    'Guernsey': '根西岛',
    'Jersey': '泽西岛',
    'Faroe': '法罗群岛',
    'Gibraltar': '直布罗陀',
    'Monaco': '摩纳哥',
    'Liechtenstein': '列支敦士登公国',
    'Vatican': '梵蒂冈',
    'Martinique': '马提尼克岛',
    'Guadeloupe': '瓜德罗普岛',
    'Trinidad and Tobago': '特立尼达和多巴哥',
    'Aruba': '阿鲁巴',
    'Barbados': '巴巴多斯',
    'Cayman Islands': '开曼群岛',
    'Saint Martin': '圣马丁岛',
    'Domnick Hunter': '多米尼克',
    'Saint Lucia': '圣卢西亚',
    'Grenada': '格林那达',
    'Curacao ': '库拉索岛',
    'Montserrat': '蒙特塞拉特',
    'Saint Barths': '圣巴泰勒米岛',
    'Anguilla ': '安圭拉',
    'Reunion': '留尼旺',
    'Mauritius': '毛里求斯',
    'Mamoudzou': '马约特',
    'Dem. Rep. Congo': '刚果（金）',
    'Congo': '刚果（布）',
    'Zambia': '赞比亚共和国',
    'Seychelles': '塞舌尔',
    'Central African Rep.': '中非共和国',
    'Cape Verde': '佛得角',
    'Burundi': '布隆迪共和国',
    'Sao Tome and Principe': '圣多美和普林西比民主共和国',
    'Shang Dan': '尚丹号',
    'The Independent State of Samoa': '萨摩亚',
    'Micronesia':'密克罗尼西亚',
    'Guam': '关岛',
    'French Polynesia': '法属波利尼西亚',
    'CNMI': '北马里亚纳群岛联邦',
    'Suriname': '苏里南',
    'DiamondPrincess': '钻石号邮轮',
    'Zambia': '赞比亚',
    'AG Antigua and Barbuda': '安提瓜和巴布达',
    'Grenada': '格林纳达',
    'The Federation of Saint Kitts and Nevis': '圣基茨和尼维斯',
    'Saint Vincent and the Grenadines': '圣文森特和格林纳丁斯',
    'Burundi': '布隆迪',
    'Comores': '科摩罗',
    'Marshall Islands':'马绍尔群岛'
}

# 7.从数据中将获取的国家名称存入列表
provinceName = []
for i in range(len(name)):
    provinceName.append(name[i])
provinceName.append("中国")
# 8.从数据中将获取的国家对应的确诊人数存入列表
confirmedCount = []
for i in range(len(confirm)):
    confirmedCount.append(confirm[i])
confirmedCount.append(china_confirm)
# 9.创建所有国家对应的英文的集合
countrys_names = []
# 10.将name_Map列表里面的键值互换
nameMap_new = {}
for key, val in nameMap.items():
    nameMap_new[val] = key
# 11.遍历新的列表，将对应英文名字存储到countrys_names列表
for i in range(len(provinceName)):
    countrys_names.append(nameMap_new[provinceName[i]])
# 12.将国家名字和每个国家对应的确诊人数对应起来放入列表中，方便存入excel
excel1 = []
for i in range(len(provinceName)):
    excel1.append([provinceName[i],confirmedCount[i]])
print(excel1)
# 13.爬取的信息中可以看到是已经按照确诊人数从多到少进行排序的，但是爬取的信息中没有中国的信息，所以需要将中国的信息按照确诊人数顺序进行排序
for i in range(len(provinceName)-1):
    for j in range(len(provinceName)-1-i):
        if excel1[j][1] < excel1[j + 1][1]:
            excel1[j], excel1[j + 1] = excel1[j + 1], excel1[j]
# 14.数据可视化调用pyecharts中的Map世界地图，将数据赋值给地图
map = Map(init_opts=opts.InitOpts(width="1750px", height="800px", bg_color="#ADD8E6",
                                  page_title="全球疫情确诊人数", theme="white"))
map.add("确诊人数", [list(z) for z in zip(countrys_names, confirmedCount)], is_map_symbol_show=False,
        maptype="world", label_opts=opts.LabelOpts(is_show=False)
        )
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
map.set_global_opts(title_opts=opts.TitleOpts(title='全球疫情确诊人数  更新时间:' + now_time),
                    legend_opts=opts.LegendOpts(is_show=False),
                    visualmap_opts=opts.VisualMapOpts(max_=100000)
                    )
map.render('world_confirm_map.html')

# 15.写入excel文件
import xlsxwriter
import datetime
# 获取当前的时间
startTime = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')
# 设置excel保存的路径和名称
workbook = xlsxwriter.Workbook(
    'D:\python\PycharmProjects\pythonProject\爬虫\world_confirm_webCrawler\world_confirm_' + startTime + '.xlsx')  # 创建一个Excel文件
worksheet = workbook.add_worksheet()  # 创建一个sheet
title = ["全球疫情确诊人数分布表","更新时间",now_time]  # 表格title
title1 = ['国家名称', '现新冠确诊人数']
# 将数据写入excel
worksheet.write_row('A1', title)
worksheet.write_row('A3', title1)
for i in range(len(provinceName)):
    worksheet.write_row('A' + str(i + 4), excel1[i])
workbook.close()

