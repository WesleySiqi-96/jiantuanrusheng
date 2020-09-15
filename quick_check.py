# coding=gbk

#尖团入声快速查询

from tkinter import *
import tkinter.font as tkFont
import ctypes

jianzi = '腊胥稰楈藇諝湑蝑揟疽岨砠趄苴沮狙蛆雎蒩伹坥徐俆且須鬚需娶緰嬃蕦鑐趨趍娵齊臍麡蠐懠癠妻萋淒凄悽鶈郪緀齌霋西棲栖犀屖樨粞齎賷齏櫅擠躋隮虀新辛薪親寴津璡濜秦螓荀郇詢眴峋珣洵恂檈姰逡竣踆夋跧旬巡馴循揗紃灥先躚蹮前歬騚湔千圱阡汘仟芊谸迁杄箋牋瀳帴韉淺濺籛仙僊苮秈鮮鱻廯錢遷櫏韆煎葏鬋全泉牷葲宣揎愃瑄鐫鋑朘旋璿琁璇蜁嫙鏇涎詮銓硂痊佺悛駩筌絟縓恮荃峑鐉輇蕭簫彇蟰蠨橚踃箾翛撨瀟消宵霄逍痟綃銷焇硝蛸莦揱奞魈樵藮劁憔顦譙嶕鐎僬菬瞧焦蕉膲鷦椒茮噍蟭醮燋鍫鍬鐰篍幧嗟罝謯袓怚衺斜邪些詳翔庠祥襄廂湘相緗纕忀驤鑲瓖欀箱葙將漿鱂蔣螿摪牆廧墻嬙檣薔蘠戕槍鏘瑲蹌蹡斨牄嶈搶謒嗆篬鶬錆清圊情晴請夝精菁鶄蜻晶鼱婧睛旌旍箐聙餳騂垶觪青靑鯖靘星曐腥鮏鯹醒篂猩惺秋秌鞧緧鞦湫鶖鰍鰌楸萩蟗趥遒鮂蝤啾揂揫揪鬏酋崷煪脩修羞樇饈囚泅汓苬稵侵駸浸綅尋鐔潯鱏樳鄩襑枔撏灊心杺祲梫兓埐嶜銛暹枮韱襳纖憸孅彡籤鹼槧僉譣簽尖殲瀸漸虃熸鑯鋟潛朁螹燅燖爓醑糈咀跙敘緒序漵鱮聚取薺鱭濟洗洒盡笉栒銑跣毨姺燹箲筅冼獮尠尟癬蘚踐諓餞俴剪翦揃戩媊譾臇雋隽選篠筱謏劋小悄愀釥剿勦灺寫瀉姐飷像象蟓橡襐勨鱌潒嶑獎槳想鯗摤靜靖妌穽阱竫井省睲汫箵滫糔酒寑寢伈蕈蔪覰覷刞絮埾趣霽穧劑嚌砌切摖細壻婿祭際穄鰶信訊訙迅囟顖卂汛阠賮燼藎贐晉搢縉進枃瑨瀙峻濬浚陖埈鵕晙迿殉徇侚儁俊餕畯駿寯焌霰軐蒨茜輤綪倩棈篟薦牮荐洊臶栫袸線綫腺箭葥榗漩縼繏渲賤羡嘯歗熽笑肖韒鞘誚陗峭俏帩釂皭潐爝癄謝榭褯藉躤卸唶借匠醬凊性姓淨靚掅岫袖秀繡琇宿銹鏽僦就鷲殧沁吣唚吢壍塹嬱僭悉厀膝蟋僁窸七柒漆桼疾嫉蒺揤愱槉堲唧蝍楖卹恤戌訹珬賉銊欰黢屑楔揳榍糏偰竊沏節卩癤楶幯截巀蠞薛紲緤褻辥泄渫禼媟齛絬疶絏絕蕝雪敠蠽尐踅削爵雀嚼鵲舄趞碏皵踖昔惜潟磶蕮焟棤積脊蹐迹跡鰿鯽蹟襀庴磧洓席夕穸汐蓆籍耤塉瘠膌簎錫析裼皙緆蜥菥淅惁晰績勣寂戚慼鏚慽磩息媳鄎瘜蒠熄即卽稷畟緝葺諿咠習襲隰鰼騽飁槢霫集輯檝亼鏶箿湒潗蓻卌接椄睫楫婕菨鯜捷疌倢崨踕誱妾緁淁穕踥燮屧屟躞韘鞢徢浹谞须媭趋齐脐蛴赍齑挤跻亲琎浕询驯跹笺鞯浅溅篯籼鲜钱镌镟诠铨辁萧箫蟏潇绡销谯鹪锹详厢缃骧镶将浆鳉蒋螀墙嫱樯蔷枪锵玱跄抢呛锖请饧骍鲭鹙鳅馐骎寻镡浔桪挦铦纤签碱椠佥歼渐锓潜叙绪溆荠鲚济尽铣狝癣藓践饯戬谫选写泻奖桨鲞静寝觑霁剂哜细际讯烬荩赆晋缙进馂骏线贱啸诮谢酱净靓绣锈鹫堑窃节疖绁亵绝鹊积鲫碛锡绩缉习袭鳛辑浃'
duoyinzi = '腊藇蒩伹緰麡郪粞齎濜郇眴姰跧揗紃灥帴愃鋑涎恮輇蟰橚箾莦揱奞菬鐰幧謯些鑲欀薔鶬猩趥稵鱏襑梫枮襳彡鹼譣朁爓糈薺洒姺燹媊臇勦蟓勨潒省糔卂阠瀙迿焌綪臶栫袸鞘癄宿殧楖楔巀渫蕝敠鰿簎菥畟騽韘鞢碱赍浕辁镶蔷鸧荠'
rushengzi = '一七不业乏乐乙乞习亍亟亦亳亵亿什仂仄仆仈伏伐伯佚佛作佰佶佾侄侠侧促俗俠倏倔倜借倬值偪側傑僕僻億兀克入八六冊册冒冪决冽凸出击凿切划刖列则別别刮刷刹刻則削剌剎剔剝剟剥剧副割剳劃劇劈力劣劫劼劾勃勒勖勗勰勺勿匍匐北匝匣匹匿十卅协卒卓協博卜卡即却卹卻厄历压厌厝厥厭及发叔叠只叭叱叶吃各合吉吊吓吶吸告呐呷咂咄咋咒咽哈哑哭哲唧唿啄啜啞啧啬啮喀喋喔喝喾嗇嗑嗒嗫嗾嘎嘖嘱噎噗噩噱嚇嚳嚼囁囑囓国囿國圾坼垡垤垩域執堀堊堞塌塔塞塾墨墼壁壑壓壳壹复夕夙失夹夺夾契奕奪妁妯妲妾姪婕媳嫉嫡孑孛学孰學孽宅实客室宿寂密寞察實射尉尺尼局屈屋屐屑属屬屹岌岳峄峡峪峽崛嵴嶧嶷帅帕帖帙帛帥席帻帼幂幄幅幕幗幘度庹廓廿弈弋式弗弱弼录役彻律得德徹必忆忒忽怍怗怛急怫怯怵怿恤恪息恰恶恻悅悉悒悖悦悫惑惕惙惚惜惡惬惻愎愕愜愨慑慝憋憶懌懾戌或戚戛戟戢截戮扎扑托执扩批扼抉抑折抹押拂拆拉拍拓拔拙拨择括拭拮拽拾挈挖挞挟挹挾捉捋捌捏捩捷捺捻捽掇掐掖掘掠掣接掬掷插揖揠握揭搁搉搏搐搕搦搨搭摄摘摭摸摺撅撇撒撤撥撮撲撷撻擇擊擘擢擦擱擲擴擷攝攫敌敕数敵數斛斡斥斫斲族日旭昃易昔昨昱昵晔晰暱暴曄曝曰曲曷月服朔木末札术朳朴杀杂杌束杰极析枥柏柒柚柝柞柵栅栉栎栗栝核栻格桀桌桎桔桷梏棘椁植椟楅楔楫業極榷榻榼槊槨槲樂樸樾橇橐橘橛檄檗櫛櫝櫟櫪欲歃歇歙歷歿殁殖殛殺殼毂毒毓毕汁汐汔汨汲決沃沏沐沒沓没沥沫沸泄泊泌法泣泼泽洁洛洩洫活洽浃浊测浙浥浴浹涅涉涤涩液涸淅淑淥淴渌渎渤渥測渴湿溘溢溧溺溽滅滌滑滗滴漆漉漠潑潔澀澈澤激濁濕濮濯瀆瀑瀝瀹灭灼炙烁烈烙烛烨热焯煜煞熄熟熠熨熱燁燭燮爆爇爍爵牍牒牘牧物特牿犊犖犢狄狎独狭狱狹猎猝猾獄獗獨獭獲獵獺率玉玐玦珀珞琢瑟璞璧甓甲画畜畢略畫疊疖疙疟疫疾瘌瘠瘧癖癤發白百的皙益盍盒目直眨着督睦睫瞌瞎瞥瞩矍矗矚石矻砸砾硕硖硤确碌碛碟碡碣碧碩確磔磕磧礫礴祓祝祿禄福禿秃秣秩秫积秸稙稷穆積穑穡穴穵穸突窃窄窒窟竊立竭竹竺笃笈笏笔笛笠筆筏筑答策筚箔箦箧箨箬節築篋篤篥篳篾簀簇簌簏簿籍籜籴粒粕粟粤粥粵糴約紇納級索紩紱紲紼絀結絕絜絡給絷綠綴綽緝縛縟縠縮縶績織繳繹纈續纛纥约级纳绁绂织绋绌绎结给络绝绩续绰绿缀缉缚缛缩缬缴缺缽罚罰羯翊翌習翕翟翮翼耋聂职聒聶職聿肃肅肉肋育胁胛胳脅脈脉脊脖脚脫脱腊腋腳腹膈膊膜膝臆臘臬臼舄舌舳舴舶色艴节芍芨芴苜若苾茀茁茉茯荚荜荦药荻莢莫获菂菉菊菔菽萚萨萼落葉葖著葛葺蒴蒺蒻蓄蓦蓽蓿蔑蔚蔟蕨薄薏薛薜薩藉藥藿蘀蘖蘗虌虐虢虱蚀蚱蛤蛭蛰蛱蛺蜀蜇蜜蜡蜥蜮蜴蜺蝈蝎蝕蝠蝨蝮蝶螫蟀蟄蟈蟋蠍蠖蠟血術衲袜袭袱袷裂裰裼褐褡褥褶褻襞襪襲覆覓覡覺覿觅觉觋觌角觖触觫觱觳觸訐訖訣訥設詘詟詰說諜諤諾謁謐謔謖謫譎識譯讀讋讦讫讷设诀识诎译诘说诺读谍谑谒谔谡谧谪谲谷豁貉貊責貼賊質贖责质贴贼赎赤赫越趣足趵趿跃跋跌跖跡跫跸跼踏踘踢踧踬踯踱蹀蹋蹐蹑蹕蹙蹠蹩蹳蹴蹶蹼躅躇躍躐躑躓躞躡躩軋軛軸軼軾較輒輟輯輻轂轄轆轍轢轧轭轴轶轹轼较辄辍辐辑辖辘辙辟辣辱达迄迪迫迭迮述迹适逆逐逖速逯逸逼遏達遢適邈邋邑邺郁郅郏郝郟郦郭鄂鄴酈酌酢酪酷醭醵释釋釟鈸鈺鉀鉞銍鋏鋦錄錫錯鍔鍘鍤鍥鎩鎰鏃鏑鐲鐵鐸鑊鑕鑠鑰鑷鑿钥钰钵钹钺钾铁铄铎铗铚铡铩锔错锡锧锲锷锸镊镒镝镞镢镬镯閉閘閣閥閱閼闃闊闋闔闕闢闥闭闸闼阀阁阅阋阏阒阔阕阖阙陆陌陟陧陸隉隔隙隰隻雀集雒雜雪雳雹霍霎霓霸霹靂靥靨革靸靼鞑鞠韃韨頁頡頰額顎顳页颉颊颚额颞颯飒食飭飾餑餮饬饰饽馥駁駱驀驋驌驛驳驿骆骕骨骼髑鬣鬩鬱鬲鬻魄魇魘鯽鰈鱉鱖鱷鲫鲽鳄鳖鳜鴂鴨鴰鴿鵒鵓鵠鵩鵲鶩鶴鶺鶻鷁鷫鷸鸭鸹鸽鹁鹄鹆鹊鹔鹘鹜鹡鹢鹤鹬鹿麓麥麦黑默黜黠黩黷黻齪齷龊龌龠一七不业乏乐乙乞习亟亦亳亵亿什仄仆伏伐伯佚佛作佶侄侠侧促俗俠倔倜借側傑僕僻億兀克入八六冊册冒决冽凸出击凿切刖列则別别刮刷刹刻則削剌剎剔剝剥剧副割劇力劣劫劾勃勒勺勿匐北匝匣匹匿十协卒卓協博卡即却卹卻历压厝厥及发叔叱叶吃各合吉吊吓吶吸告呐呷咄咋咒咽哭哲唧啄啜啧啬喋喔喝嗇嗑嘎嘖噎噩嚇国囿國垡域執堀塔塞塾墨壁壑壓壹复夕夙失夹夺夾契奕奪妲妾婕嫉嫡孛学孰學宅实客室宿寂密寞察實射尉尺尼局屈屋屐屑属屬屹岌岳峡峽崛嶷帅帖帛帥席帼幄幅幕幗度廓弈弋式弗弼录役彻律得德徹必忆忒忽急怯怵恤恪息恰恶恻悅悉悖悦惑惕惜惡惻愎愕慑憶懾戌或戚戛戟戮扑托执批抉抑折抹押拂拉拍拓拔拙拨择括拭拾挈挞挟挹挾捉捋捏捩捷捻掇掐掖掘掠掣接掬掷插揖握揭搏搦搭摄摘摭摸摺撤撥撮撲撷撻擇擊擢擲擷攝攫敌敕数敵數斛斡斥日旭易昔昨昵晰暱暴曰曲曷月服朔木末札术朴杀杂束杰极析枥柏柚柝柞柵栅栉栎栗核格桎桷棘植椟楔楫業極榻樂樸樾橇橐橘檄櫛櫝櫟櫪欲歇歙歷歿殁殖殛殺毂毒毓毕汁汐汨汲決沃沐沒沓没沥沫泄泊泌法泣泼泽洁洛洩活洽浊测浙浴涅涉涤涩液涸淅淑淥渌渎渤測渴湿溘溢溺滅滌滑滴漆漠潑潔澀澈澤激濁濕濮濯瀆瀑瀝灭灼炙烁烈烙烛烨热焯煜熄熟熠熨熱燁燭燮爆爍爵牍牒牘牧物特犊犢狄狎独狭狱狹猎猝猾獄獨獭獲獵獺率玉琢瑟璞璧甲画畜畢略畫疖疟疫疾瘠瘧癖癤發白百的益盍目直眨着督睦睫瞎瞩矍矗矚石砾硕确碌碛碣碧碩確磧礫礴祝祿禄福禿秃秣秩秫积秸稷穆積穑穡穴突窃窄窒窟竊立竭竹竺笏笔笛笠筆筏筑答策箔箧節築篋簇籍籴粒粕粟粤粥粵糴約紇納級索紱結絕絡給綠綴綽緝縛縮績織繳繹續纥约级纳绂织绎结给络绝绩续绰绿缀缉缚缩缴缽罚罰羯翌習翟翮翼聂职聒聶職聿肃肅肉肋育胁脅脈脉脊脚脫脱腊腋腳腹膊膜膝臘舌舳舶色节芍芴苜若茁茯荚药荻莢莫获菊菽萨落葉著葛蒺蓄蔑蔚蕨薄薩藉藥虐虢虱蚀蛤蛭蛰蜀蜜蜡蜮蜴蝈蝕蝠蝨蝮蝶螫蟀蟄蟈蠖蠟血術衲袜袭裂褐褥褶褻襪襲覆覓覡覺觅觉觋角触觫觸訐訖訣訥設詘詰說諜諤諾謁謐謔謖謫譎識譯讀讦讫讷设诀识诎译诘说诺读谍谑谒谔谡谧谪谲谷豁貉貊責貼賊質贖责质贴贼赎赤赫越足趵跃跋跌跡踏踢踱蹀蹑蹙蹩蹴蹶躅躍躡軋軸軼軾較輒輟輯輻轂轆轍轧轴轶轼较辄辍辐辑辘辙辟辱达迄迫迭迮迹适逆逐逖速逯逸逼遏達適邈邑邺郁郅郝郭鄂鄴酌酪酷释釋鉀鉞錄錫錯鏃鏑鐲鐵鐸鑠鑰鑿钥钵钺钾铁铄铎错锡镝镞镯閣閥閱閼闊闔闕闢阀阁阅阋阏阔阖阙陆陌陟陸隔隙隰雀集雜雪雹霍霎霓霸霹靥靨革頡頰額颉颊额颯飒食飭飾餑饬饰饽馥駁駱驛驳驿骆骨骼髑鬩鬱鬲鬻魄鯽鱷鲫鳄鴨鴿鵠鵲鶩鶴鸭鸽鹄鹊鹜鹤鹿麓麥麦黑默黜黠黩黷'


def isjian(cha):
    if cha in jianzi and cha in duoyinzi:
        return ('多')
    elif cha in jianzi:
        return ('尖')
    else:
        return ('非')


def isru(cha):
    if cha in rushengzi:
        return ('入声')
    else:
        return ('非入')



def UI():
    def click():

        var=t1.get("1.0",END)
        t2.delete("1.0",END)
        n=1
        for i in var:
            if var1.get()==1 and var2.get()==1:
                if isjian(i) =='尖'and isru(i)=='入声':
                    t2.insert(END, i, 'jianru')

                    t2.tag_add('jianru', str(n)+'.0')
                    t2.tag_config('jianru', foreground='red', font=defaut1, underline=1)


                elif isjian(i)=='多' and isru(i)=='入声':
                    t2.insert(END, i, 'duoru')

                    t2.tag_add('duoru', str(n)+'.0')
                    t2.tag_config('duoru', foreground='blue', font=defaut1, underline=1)



                elif isjian(i)=='尖':
                    t2.insert(END, i, 'jian')

                    t2.tag_add('jian', str(n)+'.0')
                    t2.tag_config('jian', foreground='red', font=defaut1)


                elif isjian(i) == '多':
                    t2.insert(END, i, 'duo')
                    t2.tag_add('duo', str(n) + '.0')
                    t2.tag_config('duo', foreground='blue', font=defaut1)


                elif isru(i)=='入声':
                    t2.insert(END, i,'ru')

                    t2.tag_add('ru', str(n)+'.0')
                    t2.tag_config('ru', font=defaut1, underline=1)
                else:

                    t2.insert(END, i)



                n += 1
            elif var1.get()==1:
                if isjian(i)=='尖':

                    t2.tag_add('jian', str(n) + '.0')
                    t2.tag_config('jian', foreground='red', font=defaut1)

                    t2.insert(END, i, 'jian')
                elif isjian(i) == '多':
                    t2.tag_add('duo', str(n) + '.0')
                    t2.tag_config('duo', foreground='blue', font=defaut1)
                    t2.insert(END, i, 'duo')
                else:
                    t2.insert(END, i)
                n += 1
            elif var2.get()==1:
                if isru(i) == '入声':
                    t2.insert(END, i, 'ru')

                    t2.tag_add('ru', str(n) + '.0')
                    t2.tag_config('ru', font=defaut1, underline=1)


                else:

                    t2.insert(END, i)
                n += 1
            else:
                t2.delete("1.0",END)

                t2.insert(END, '什么都不选莫不是来消遣洒家')

    win = Tk()

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # if ScaleFactor==150:
    #     win.geometry('1285x1400')
    # else:
    #     win.geometry('855x900')
    # # 设置程序缩放
    win.tk.call('tk', 'scaling', ScaleFactor / 75)


    #标题
    win.title('尖了牌尖团入声快速查询')
    label1 = Label(win, text='尖了牌尖团入声快速查询', font=('Kaiti', 36)).pack()
    Label(win, text="红色表示尖字，蓝色表示可尖可团，下划线表示入声", font=('Kaiti', 20)).pack()
    Label(win, text="本程序存在一定误差，具体情况请参考韵书", font=('Kaiti', 20)).pack()
    Label(win, text="请于框内输入要查询的文字",font=('Kaiti', 26)).pack()

    t1=Text(win,height=10)
    t1.pack(expand=True, fill=BOTH)

    defaut1=tkFont.Font(family="Kaiti", size=16)
    t1.configure(font=defaut1)

    bot1=Button(win,text='查询',width=10,height=2,command=click)
    bot1['font']=tkFont.Font(family="Kaiti", size=26)
    bot1.pack()

    var1 = IntVar()
    var1.set(1)
    c1=Checkbutton(win, text="尖字", variable=var1)
    c1['font']=tkFont.Font(family="Kaiti", size=26)
    c1.pack()

    var2 = IntVar()
    var2.set(1)
    c2=Checkbutton(win, text="入声", variable=var2)
    c2['font']=tkFont.Font(family="Kaiti", size=26)
    c2.pack()


    Label(win, text="查询结果", font=('Kaiti', 26)).pack()

    t2 = Text(win, height=25)
    t2.pack(expand=True, fill=BOTH)
    t2.configure(font=defaut1)








    win.mainloop()


UI()