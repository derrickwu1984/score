from lxml import etree

str="""
<html>
<head>
<title>2018年内蒙古普通高校招生批量投档录取最高分最低分数查询</title>
</head>
<style type = "text/css">
<!--
.style1{
	font-family: "宋体";
	font-size: 12px;
	color: #000000;
		}
.style2{
	font-family: "宋体";
	font-size: 14px;
	color:blue;
		}
-->
</style>

<body bgcolor="#ffffff" >


<CENTER>
<FONT face=5 color=#ff00ff size=3>
<P><BR>
<H3>2018年内蒙古普通高校招生批量投档录取最高分最低分数查询</H3>
<HR>
<font color="#8000FF">
<FORM name='form1' method='post' >请先选择批次：
<select name='m_pcdm' title='请先选择批次：' onChange='document.form1.submit()'>
<option value='7' >高职高专</option>
<option>------------</option>
<option value='1' >本科提前A</option>
<option value='2' >本科提前B</option>
<option value='3' >本科一批</option>
<option value='4' >本科二批</option>
<option value='6' >专科提前</option>
<option value='7' >高职高专</option>
<option value='C' >本科一批B</option>
<option value='E' >本科二批B</option>
</select>
<input type='hidden' name='kldm' value=''>

</FORM>

<FORM name="form2" method="post" action="lqmaxmin_18.jsp">
请选择科类：
<select name='m_kldm' onChange='document.form2.submit()'>
<option value='A' >普通文科</option>
<option>--------</option>
<option value='0'>体育类</option>
<option value='1'>采矿类</option>
<option value='@'>汉授编导</option>
<option value='A'>普通文科</option>
<option value='B'>普通理科</option>
<option value='C'>蒙授文科</option>
<option value='D'>蒙授理科</option>
<option value='E'>汉授美术</option>
<option value='F'>蒙授美术</option>
<option value='G'>汉授音乐</option>
<option value='H'>蒙授音乐</option>
<option value='I'>其他艺术</option>
<option value='J'>蒙授其他艺术</option>
<option value='K'>汉授体育</option>
<option value='L'>蒙授体育</option>
<option value='M'>计算机类</option>
<option value='N'>农学类</option>
<option value='O'>牧医类</option>
<option value='P'>烹饪类</option>
<option value='Q'>财会类</option>
<option value='R'>美工设计类</option>
<option value='S'>旅游类</option>
<option value='T'>汽驾类</option>
<option value='U'>建筑类</option>
<option value='V'>机电类</option>
<option value='W'>蒙牧医类</option>
<option value='X'>化工类</option>
<option value='Y'>幼师类</option>
<option value='Z'>医学类</option>
</select>

<input type="hidden" name="pcdm" value="7">
</FORM>

<FORM name="form4" method="post" action="lqmaxmin_18.jsp">
请选择院校排序方式：
<select name='m_pxfs' onChange='document.form4.submit()'>
<option value='1' >院校代号</option>
<option>--------</option>
<option value='1'>院校代号</option>
<option value='2'>院校名称</option>
</select>

<input type="hidden" name="pcdm" value="7">
<input type="hidden" name="kldm" value="A">
</FORM>

<FORM name="form3" method="post" action="lqmaxmin_18.jsp">
请选择院校：
<select name='m_yxdh' title='请选择院校：'>
<option value='204' >204包头职业技术学院</option>
<option>----------------</option>
<option value='032' >032长沙民政职业技术学院</option>
<option value='037' >037齐齐哈尔高等师范专科学校</option>
<option value='039' >039长春金融高等专科学校</option>
<option value='043' >043黑龙江商业职业学院</option>
<option value='058' >058中华女子学院</option>
<option value='059' >059中国劳动关系学院</option>
<option value='087' >087青岛酒店管理职业技术学院</option>
<option value='092' >092大兴安岭职业学院</option>
<option value='093' >093江西工业贸易职业技术学院</option>
<option value='102' >102上海旅游高等专科学校</option>
<option value='103' >103湖南工程学院</option>
<option value='111' >111山西林业职业技术学院</option>
<option value='113' >113长江工程职业技术学院</option>
<option value='123' >123黑龙江职业学院</option>
<option value='124' >124烟台南山学院（民办）</option>
<option value='125' >125河北工程技术学院（民办）</option>
<option value='139' >139黑龙江信息技术职业学院</option>
<option value='140' >140辽阳职业技术学院</option>
<option value='143' >143黄河水利职业技术学院</option>
<option value='149' >149无锡职业技术学院</option>
<option value='152' >152河北对外经贸职业学院</option>
<option value='153' >153石家庄信息工程职业学院</option>
<option value='155' >155湖南信息职业技术学院</option>
<option value='158' >158山西建筑职业技术学院</option>
<option value='163' >163江西交通职业技术学院</option>
<option value='165' >165山东英才学院（民办）</option>
<option value='166' >166石家庄财经职业学院（民办）</option>
<option value='169' >169日照职业技术学院</option>
<option value='174' >174辽宁科技学院</option>
<option value='176' >176西安交通工程学院（民办）</option>
<option value='178' >178湖北交通职业技术学院</option>
<option value='179' >179伊春职业学院</option>
<option value='180' >180牡丹江大学</option>
<option value='183' >183石家庄理工职业学院（民办）</option>
<option value='184' >184通化师范学院</option>
<option value='190' >190吉林工商学院</option>
<option value='196' >196吉林警察学院</option>
<option value='204' >204包头职业技术学院</option>
<option value='206' >206河南职业技术学院</option>
<option value='212' >212山西机电职业技术学院</option>
<option value='215' >215威海职业学院</option>
<option value='216' >216山西财政税务专科学校</option>
<option value='218' >218哈尔滨信息工程学院（民办）</option>
<option value='226' >226北京信息职业技术学院</option>
<option value='227' >227南昌工学院（民办）</option>
<option value='230' >230成都航空职业技术学院</option>
<option value='235' >235北京工业职业技术学院</option>
<option value='239' >239哈尔滨铁道职业技术学院</option>
<option value='241' >241兰州交通大学</option>
<option value='245' >245湖南铁道职业技术学院</option>
<option value='247' >247四川交通职业技术学院</option>
<option value='248' >248武汉软件工程职业学院</option>
<option value='249' >249泰州职业技术学院</option>
<option value='252' >252山东交通学院</option>
<option value='255' >255辽宁广告职业学院（民办）</option>
<option value='256' >256青岛职业技术学院</option>
<option value='257' >257昆明艺术职业学院（民办）</option>
<option value='263' >263潍坊职业学院</option>
<option value='344' >344三亚城市职业学院（民办）</option>
<option value='345' >345黑龙江林业职业技术学院</option>
<option value='346' >346长春工业大学</option>
<option value='351' >351石家庄铁路职业技术学院</option>
<option value='355' >355黑龙江司法警官职业学院</option>
<option value='356' >356长春科技学院（民办）</option>
<option value='359' >359山东商业职业技术学院</option>
<option value='360' >360安徽中医药高等专科学校</option>
<option value='363' >363中国民航大学</option>
<option value='364' >364广州民航职业技术学院</option>
<option value='365' >365湖南邮电职业技术学院</option>
<option value='366' >366山西水利职业技术学院</option>
<option value='367' >367南昌理工学院（民办）</option>
<option value='371' >371河北科技学院（民办）</option>
<option value='372' >372上海出版印刷高等专科学校</option>
<option value='379' >379山东现代学院（民办）</option>
<option value='380' >380哈尔滨职业技术学院</option>
<option value='383' >383山东水利职业学院</option>
<option value='385' >385成都农业科技职业学院</option>
<option value='392' >392锦州师范高等专科学校</option>
<option value='394' >394郑州工业应用技术学院（民办）</option>
<option value='400' >400青岛港湾职业技术学院</option>
<option value='401' >401西安城市建设职业学院（民办）</option>
<option value='402' >402上海工商职业技术学院（民办）</option>
<option value='407' >407武汉警官职业学院</option>
<option value='408' >408江苏食品药品职业技术学院</option>
<option value='412' >412铜仁职业技术学院</option>
<option value='420' >420长沙航空职业技术学院</option>
<option value='421' >421九江学院</option>
<option value='424' >424桂林理工大学</option>
<option value='426' >426保险职业学院</option>
<option value='429' >429长春师范大学</option>
<option value='430' >430长春工程学院</option>
<option value='431' >431大连科技学院（民办）</option>
<option value='434' >434张家界航空工业职业技术学院</option>
<option value='436' >436承德石油高等专科学校</option>
<option value='440' >440东北石油大学</option>
<option value='444' >444江西财经职业学院</option>
<option value='468' >468山东凯文科技职业学院（民办）</option>
<option value='474' >474长春汽车工业高等专科学校</option>
<option value='482' >482青岛理工大学琴岛学院（民办）</option>
<option value='485' >485枣庄科技职业学院</option>
<option value='486' >486抚州职业技术学院</option>
<option value='491' >491宝鸡职业技术学院</option>
<option value='493' >493海南软件职业技术学院</option>
<option value='514' >514西安思源学院（民办）</option>
<option value='520' >520山西国际商务职业学院</option>
<option value='521' >521太原旅游职业学院</option>
<option value='524' >524漳州职业技术学院</option>
<option value='526' >526北京青年政治学院</option>
<option value='534' >534聊城职业技术学院</option>
<option value='536' >536北京经济技术职业学院（民办）</option>
<option value='540' >540淄博师范高等专科学校</option>
<option value='543' >543河北女子职业技术学院</option>
<option value='545' >545四川建筑职业技术学院</option>
<option value='558' >558天津职业大学</option>
<option value='560' >560江西青年职业学院</option>
<option value='561' >561天津天狮学院（民办）</option>
<option value='563' >563天津农学院</option>
<option value='565' >565天津滨海职业学院</option>
<option value='566' >566天津工程职业技术学院</option>
<option value='567' >567天津现代职业技术学院</option>
<option value='568' >568天津轻工职业技术学院</option>
<option value='569' >569天津电子信息职业技术学院</option>
<option value='570' >570天津公安警官职业学院</option>
<option value='571' >571天津机电职业技术学院</option>
<option value='572' >572天津渤海职业技术学院</option>
<option value='573' >573天津中德应用技术大学</option>
<option value='574' >574天津商务职业学院</option>
<option value='577' >577天津医学高等专科学校</option>
<option value='583' >583扬州市职业大学</option>
<option value='587' >587天津交通职业学院</option>
<option value='588' >588湖北城市建设职业技术学院</option>
<option value='593' >593焦作大学</option>
<option value='599' >599郑州工程技术学院</option>
<option value='601' >601开封大学</option>
<option value='606' >606湖南理工职业技术学院</option>
<option value='613' >613九江职业大学</option>
<option value='614' >614陕西国际商贸学院（民办）</option>
<option value='616' >616陕西服装工程学院（民办）</option>
<option value='618' >618陕西职业技术学院</option>
<option value='624' >624四川工程职业技术学院</option>
<option value='626' >626重庆城市管理职业学院</option>
<option value='629' >629重庆工程职业技术学院</option>
<option value='632' >632华北理工大学</option>
<option value='633' >633河北工业职业技术学院</option>
<option value='637' >637河北能源职业技术学院</option>
<option value='641' >641河北建材职业技术学院</option>
<option value='643' >643秦皇岛职业技术学院</option>
<option value='647' >647石家庄城市经济职业学院（民办）</option>
<option value='650' >650河北旅游职业学院</option>
<option value='655' >655江西信息应用职业技术学院</option>
<option value='656' >656江西医学高等专科学校</option>
<option value='657' >657江西电力职业技术学院</option>
<option value='660' >660浙江建设职业技术学院</option>
<option value='661' >661武汉工程职业技术学院</option>
<option value='662' >662荆州理工职业学院</option>
<option value='665' >665荆州职业技术学院</option>
<option value='673' >673武汉职业技术学院</option>
<option value='674' >674咸宁职业技术学院</option>
<option value='675' >675湖北职业技术学院</option>
<option value='682' >682黄冈职业技术学院</option>
<option value='683' >683武汉生物工程学院（民办）</option>
<option value='686' >686昆明冶金高等专科学校</option>
<option value='687' >687湖北理工学院</option>
<option value='688' >688武汉商贸职业学院（民办）</option>
<option value='689' >689鄂州职业大学</option>
<option value='690' >690黄冈师范学院</option>
<option value='694' >694湖南工程职业技术学院</option>
<option value='701' >701吉首大学</option>
<option value='706' >706长沙环境保护职业技术学院</option>
<option value='707' >707湖南医药学院</option>
<option value='708' >708大庆医学高等专科学校</option>
<option value='709' >709武汉信息传播职业技术学院（民办）</option>
<option value='710' >710石家庄医学高等专科学校（民办）</option>
<option value='713' >713山西医科大学</option>
<option value='715' >715天津城市建设管理职业技术学院</option>
<option value='716' >716大连艺术学院（民办）</option>
<option value='719' >719太原学院</option>
<option value='720' >720湖南安全技术职业学院</option>
<option value='721' >721陕西青年职业学院</option>
<option value='724' >724陕西电子科技职业学院（民办）</option>
<option value='725' >725山西药科职业学院</option>
<option value='731' >731滨州职业学院</option>
<option value='732' >732山东力明科技职业学院（民办）</option>
<option value='734' >734德州科技职业学院（民办）</option>
<option value='735' >735山东科技职业学院</option>
<option value='736' >736张家口职业技术学院</option>
<option value='739' >739青岛滨海学院（民办）</option>
<option value='743' >743石家庄工程职业学院（民办）</option>
<option value='744' >744桂林旅游学院</option>
<option value='751' >751内蒙古大学</option>
<option value='752' >752内蒙古师范大学</option>
<option value='754' >754内蒙古财经大学</option>
<option value='755' >755内蒙古农业大学</option>
<option value='758' >758内蒙古医科大学</option>
<option value='761' >761内蒙古民族大学</option>
<option value='762' >762吉林铁道职业技术学院</option>
<option value='763' >763黑龙江交通职业技术学院</option>
<option value='764' >764内蒙古科技大学</option>
<option value='765' >765集宁师范学院</option>
<option value='766' >766呼伦贝尔学院</option>
<option value='767' >767赤峰学院</option>
<option value='769' >769科尔沁艺术职业学院</option>
<option value='770' >770呼和浩特职业学院</option>
<option value='771' >771内蒙古建筑职业技术学院</option>
<option value='772' >772河套学院</option>
<option value='774' >774内蒙古体育职业学院</option>
<option value='775' >775兴安职业技术学院</option>
<option value='776' >776内蒙古机电职业技术学院</option>
<option value='777' >777三峡电力职业学院</option>
<option value='778' >778内蒙古丰州职业学院</option>
<option value='779' >779内蒙古商贸职业学院</option>
<option value='781' >781山东商务职业学院</option>
<option value='782' >782内蒙古化工职业学院</option>
<option value='783' >783内蒙古电子信息职业技术学院</option>
<option value='784' >784山东轻工职业学院</option>
<option value='785' >785锡林郭勒职业学院</option>
<option value='786' >786山东城市建设职业学院</option>
<option value='792' >792乌兰察布职业学院</option>
<option value='794' >794通辽职业学院</option>
<option value='795' >795包头轻工职业技术学院</option>
<option value='811' >811盘锦职业技术学院</option>
<option value='813' >813营口职业技术学院</option>
<option value='815' >815山西职业技术学院</option>
<option value='816' >816辽宁省交通高等专科学校</option>
<option value='818' >818太原城市职业技术学院</option>
<option value='819' >819朝阳师范高等专科学校</option>
<option value='821' >821抚顺职业技术学院</option>
<option value='825' >825大连职业技术学院</option>
<option value='828' >828鹤岗师范高等专科学校</option>
<option value='829' >829长春职业技术学院</option>
<option value='831' >831长春医学高等专科学校</option>
<option value='833' >833吉林工业职业技术学院</option>
<option value='834' >834长春东方职业学院（民办）</option>
<option value='837' >837延边大学</option>
<option value='842' >842吉林工程技术师范学院</option>
<option value='843' >843辽宁机电职业技术学院</option>
<option value='849' >849吉林工程职业学院</option>
<option value='850' >850吉林交通职业技术学院</option>
<option value='852' >852白城师范学院</option>
<option value='854' >854吉林农业科技学院</option>
<option value='855' >855辽源职业技术学院</option>
<option value='856' >856吉林电子信息职业技术学院</option>
<option value='861' >861青岛黄海学院（民办）</option>
<option value='862' >862邢台医学高等专科学校</option>
<option value='866' >866湖北水利水电职业技术学院</option>
<option value='869' >869汉江师范学院</option>
<option value='873' >873黑龙江工业学院</option>
<option value='878' >878哈尔滨医科大学</option>
<option value='885' >885南京工业职业技术学院</option>
<option value='886' >886黑龙江生物科技职业学院</option>
<option value='888' >888黑龙江农垦职业学院</option>
<option value='890' >890黑龙江建筑职业技术学院</option>
<option value='893' >893大庆职业学院</option>
<option value='896' >896黑龙江农业工程职业学院</option>
<option value='898' >898黑龙江农业经济职业学院</option>
<option value='901' >901湖南工业职业技术学院</option>
<option value='902' >902上海工商外国语职业学院（民办）</option>
<option value='906' >906上海东海职业技术学院（民办）</option>
<option value='912' >912江西旅游商贸职业学院</option>
<option value='914' >914江苏建筑职业技术学院</option>
<option value='915' >915江苏农牧科技职业学院</option>
<option value='921' >921淮北职业技术学院</option>
<option value='922' >922淮南职业技术学院</option>
<option value='923' >923海南职业技术学院</option>
<option value='933' >933湖北工业职业技术学院</option>
<option value='935' >935南昌大学</option>
<option value='936' >936江西科技学院（民办）</option>
<option value='945' >945西安外事学院（民办）</option>
<option value='946' >946陕西能源职业技术学院</option>
<option value='948' >948西安欧亚学院（民办）</option>
<option value='949' >949西京学院（民办）</option>
<option value='950' >950西安培华学院（民办）</option>
<option value='951' >951西安翻译学院（民办）</option>
<option value='954' >954陕西工业职业技术学院</option>
<option value='960' >960四平职业大学</option>
<option value='967' >967重庆工业职业技术学院</option>
<option value='970' >970芜湖职业技术学院</option>
<option value='977' >977宁夏警官职业学院</option>
<option value='978' >978广东南华工商职业学院</option>
<option value='A09' >A09北京吉利学院（民办）</option>
<option value='A13' >A13辽宁经济职业技术学院</option>
<option value='A20' >A20武汉交通职业学院</option>
<option value='A22' >A22青岛恒星科技学院（民办）</option>
<option value='A24' >A24石家庄职业技术学院</option>
<option value='A25' >A25重庆电子工程职业学院</option>
<option value='A26' >A26江西外语外贸职业学院</option>
<option value='A28' >A28石家庄邮电职业技术学院</option>
<option value='A32' >A32长春中医药大学</option>
<option value='A34' >A34天津石油职业技术学院</option>
<option value='A37' >A37长春光华学院（民办）</option>
<option value='A38' >A38武汉工商学院（民办）</option>
<option value='A43' >A43淄博职业学院</option>
<option value='A45' >A45北京科技职业学院（民办）</option>
<option value='A51' >A51陕西交通职业技术学院</option>
<option value='A54' >A54江西建设职业技术学院</option>
<option value='A55' >A55西安航空职业技术学院</option>
<option value='A62' >A62曲阜远东职业技术学院（民办）</option>
<option value='A63' >A63河北交通职业技术学院</option>
<option value='A64' >A64北京农业职业学院</option>
<option value='A68' >A68九江职业技术学院</option>
<option value='A71' >A71唐山职业技术学院</option>
<option value='A72' >A72山西交通职业技术学院</option>
<option value='A78' >A78河南科技学院</option>
<option value='A79' >A79常州信息职业技术学院</option>
<option value='A84' >A84河北机电职业技术学院</option>
<option value='A85' >A85莱芜职业技术学院</option>
<option value='A87' >A87常德职业技术学院</option>
<option value='A90' >A90重庆航天职业技术学院</option>
<option value='A94' >A94济宁职业技术学院</option>
<option value='A96' >A96内蒙古交通职业技术学院</option>
<option value='A97' >A97北京京北职业技术学院</option>
<option value='B00' >B00中南林业科技大学</option>
<option value='B01' >B01怀化职业技术学院</option>
<option value='B04' >B04山西金融职业学院</option>
<option value='B06' >B06白城医学高等专科学校</option>
<option value='B07' >B07辽宁农业职业技术学院</option>
<option value='B09' >B09上海电子信息职业技术学院</option>
<option value='B12' >B12桂林电子科技大学</option>
<option value='B14' >B14山西工程职业技术学院</option>
<option value='B15' >B15河北化工医药职业技术学院</option>
<option value='B16' >B16广西工业职业技术学院</option>
<option value='B22' >B22北京培黎职业学院（民办）</option>
<option value='B30' >B30湖南交通职业技术学院</option>
<option value='B36' >B36齐鲁医药学院（民办）</option>
<option value='B43' >B43上海行健职业学院</option>
<option value='B47' >B47武汉商学院</option>
<option value='B49' >B49辽宁林业职业技术学院</option>
<option value='B50' >B50首钢工学院</option>
<option value='B53' >B53江苏经贸职业技术学院</option>
<option value='B56' >B56湖南大众传媒职业技术学院</option>
<option value='B57' >B57山东工业职业学院</option>
<option value='B58' >B58永州职业技术学院</option>
<option value='B59' >B59山东职业学院</option>
<option value='B60' >B60上海城建职业学院</option>
<option value='B61' >B61辽宁职业学院</option>
<option value='B64' >B64云南国土资源职业学院</option>
<option value='B66' >B66上海交通职业技术学院</option>
<option value='B69' >B69保定职业技术学院</option>
<option value='B73' >B73武汉民政职业学院</option>
<option value='B74' >B74海南工商职业学院（民办）</option>
<option value='B80' >B80上海思博职业技术学院（民办）</option>
<option value='B81' >B81北京汇佳职业学院（民办）</option>
<option value='B87' >B87天津国土资源和房屋职业学院</option>
<option value='B93' >B93北京经贸职业学院（民办）</option>
<option value='C00' >C00大连财经学院（民办）</option>
<option value='C01' >C01周口职业技术学院</option>
<option value='C09' >C09鹤壁职业技术学院</option>
<option value='C11' >C11上海立达学院（民办）</option>
<option value='C14' >C14沈阳职业技术学院</option>
<option value='C19' >C19天津艺术职业学院</option>
<option value='C25' >C25上海中侨职业技术学院（民办）</option>
<option value='C30' >C30江西中医药高等专科学校</option>
<option value='C32' >C32山东畜牧兽医职业学院</option>
<option value='C34' >C34吉林司法警官职业学院</option>
<option value='C35' >C35上海济光职业技术学院（民办）</option>
<option value='C36' >C36徐州工业职业技术学院</option>
<option value='C38' >C38东营职业学院</option>
<option value='C39' >C39濮阳职业技术学院</option>
<option value='C41' >C41济源职业技术学院</option>
<option value='C43' >C43湘潭医卫职业技术学院</option>
<option value='C46' >C46广西职业技术学院</option>
<option value='C47' >C47山东交通职业学院</option>
<option value='C52' >C52黑龙江农垦科技职业学院</option>
<option value='C54' >C54石家庄工商职业学院（民办）</option>
<option value='C55' >C55河北外国语学院（民办）</option>
<option value='C63' >C63天津工业职业学院</option>
<option value='C64' >C64天津城市职业学院</option>
<option value='C67' >C67西安汽车科技职业学院（民办）</option>
<option value='C68' >C68西安海棠职业学院（民办）</option>
<option value='C69' >C69黑龙江能源职业学院</option>
<option value='C70' >C70黑龙江生态工程职业学院</option>
<option value='C71' >C71黑龙江旅游职业技术学院</option>
<option value='C72' >C72湖北国土资源职业学院</option>
<option value='C73' >C73江汉艺术职业学院</option>
<option value='C74' >C74湖北生态工程职业技术学院</option>
<option value='C75' >C75湖北生物科技职业学院</option>
<option value='C76' >C76湖北财税职业学院</option>
<option value='C79' >C79郑州旅游职业学院</option>
<option value='C80' >C80湖南石油化工职业技术学院</option>
<option value='C82' >C82湖南财经工业职业技术学院</option>
<option value='C92' >C92武汉铁路职业技术学院</option>
<option value='C93' >C93湖北三峡职业技术学院</option>
<option value='C94' >C94山东协和学院（民办）</option>
<option value='C95' >C95上海科学技术职业学院</option>
<option value='D02' >D02长春信息技术职业学院（民办）</option>
<option value='D04' >D04乌海职业技术学院</option>
<option value='D09' >D09山东经贸职业学院</option>
<option value='D10' >D10山东圣翰财贸职业学院（民办）</option>
<option value='D18' >D18东营科技职业学院（民办）</option>
<option value='D22' >D22沈阳工学院（民办）</option>
<option value='D23' >D23湖南化工职业技术学院</option>
<option value='D25' >D25常州工程职业技术学院</option>
<option value='D26' >D26海南政法职业学院</option>
<option value='D38' >D38山西旅游职业学院</option>
<option value='D42' >D42陕西邮电职业技术学院</option>
<option value='D43' >D43苏州高博软件技术职业学院（民办）</option>
<option value='D44' >D44豫章师范学院</option>
<option value='D45' >D45山东中医药高等专科学校</option>
<option value='D51' >D51武昌工学院（民办）</option>
<option value='D57' >D57山东华宇工学院（民办）</option>
<option value='D60' >D60山东铝业职业学院</option>
<option value='D62' >D62天津铁道职业技术学院</option>
<option value='D63' >D63包头钢铁职业技术学院</option>
<option value='D64' >D64江西工程职业学院</option>
<option value='D67' >D67海南经贸职业技术学院</option>
<option value='D76' >D76松原职业技术学院</option>
<option value='D77' >D77七台河职业学院</option>
<option value='D80' >D80三亚航空旅游职业学院（民办）</option>
<option value='D83' >D83黑龙江民族职业学院</option>
<option value='D85' >D85渭南职业技术学院</option>
<option value='D88' >D88辽宁传媒学院（民办）</option>
<option value='D91' >D91大连枫叶职业技术学院</option>
<option value='D95' >D95天津生物工程职业技术学院</option>
<option value='D96' >D96天津海运职业学院</option>
<option value='D97' >D97湖北青年职业学院</option>
<option value='D99' >D99哈尔滨城市职业学院（民办）</option>
<option value='E04' >E04江苏海事职业技术学院</option>
<option value='E17' >E17辽宁何氏医学院（民办）</option>
<option value='E18' >E18内蒙古科技职业学院</option>
<option value='E19' >E19内蒙古北方职业技术学院</option>
<option value='E21' >E21内蒙古经贸外语职业学院（民办）</option>
<option value='E30' >E30山西警官职业学院</option>
<option value='E34' >E34重庆水利电力职业技术学院</option>
<option value='E37' >E37南阳医学高等专科学校</option>
<option value='E44' >E44长沙电力职业技术学院</option>
<option value='E46' >E46山东药品食品职业学院</option>
<option value='E48' >E48青岛工学院（民办）</option>
<option value='E50' >E50四川中医药高等专科学校</option>
<option value='E60' >E60烟台汽车工程职业学院</option>
<option value='E61' >E61运城幼儿师范高等专科学校</option>
<option value='E62' >E62黑龙江幼儿师范高等专科学校</option>
<option value='E65' >E65辽宁地质工程职业学院</option>
<option value='E66' >E66白城职业技术学院</option>
<option value='E67' >E67哈尔滨科学技术职业学院</option>
<option value='E69' >E69菏泽家政职业学院</option>
<option value='E72' >E72北京社会管理职业学院</option>
<option value='E73' >E73北京艺术传媒职业学院（民办）</option>
<option value='E74' >E74佳木斯职业学院</option>
<option value='E75' >E75包头铁道职业技术学院</option>
<option value='E77' >E77湖南商务职业技术学院</option>
<option value='E79' >E79江苏财经职业技术学院</option>
<option value='E87' >E87内蒙古师范大学鸿德学院（民办）</option>
<option value='E93' >E93黑龙江农业职业技术学院</option>
<option value='F06' >F06台州职业技术学院</option>
<option value='F07' >F07浙江工贸职业技术学院</option>
<option value='F14' >F14浙江警官职业学院</option>
<option value='F16' >F16嘉兴职业技术学院</option>
<option value='F18' >F18辽宁金融职业学院</option>
<option value='F19' >F19上海农林职业技术学院</option>
<option value='F20' >F20上海邦德职业技术学院（民办）</option>
<option value='F21' >F21南京科技职业学院</option>
<option value='F22' >F22郑州澍青医学高等专科学校（民办）</option>
<option value='F33' >F33烟台工程职业技术学院</option>
<option value='F34' >F34德州职业技术学院</option>
<option value='F47' >F47无锡城市职业技术学院</option>
<option value='F51' >F51济南工程职业技术学院</option>
<option value='F52' >F52山东旅游职业学院</option>
<option value='F58' >F58湖南水利水电职业技术学院</option>
<option value='F59' >F59湖南高速铁路职业技术学院</option>
<option value='F60' >F60铜川职业技术学院</option>
<option value='F63' >F63重庆工商职业学院</option>
<option value='F66' >F66齐鲁理工学院（民办）</option>
<option value='F72' >F72北京经济管理职业学院</option>
<option value='F75' >F75天津广播影视职业学院</option>
<option value='F81' >F81重庆财经职业学院</option>
<option value='F82' >F82江西新能源科技职业学院（民办）</option>
<option value='F86' >F86辽宁建筑职业学院</option>
<option value='F87' >F87枣庄职业学院</option>
<option value='F88' >F88湖北工程职业学院</option>
<option value='F90' >F90河北劳动关系职业学院</option>
<option value='F91' >F91大连航运职业技术学院（民办）</option>
<option value='F92' >F92乌兰察布医学高等专科学校</option>
<option value='G03' >G03鄂尔多斯职业学院</option>
<option value='G26' >G26桂林师范高等专科学校</option>
<option value='G29' >G29襄阳职业技术学院</option>
<option value='G31' >G31北京政法职业学院</option>
<option value='G32' >G32长沙商贸旅游职业技术学院</option>
<option value='G33' >G33重庆三峡职业学院</option>
<option value='G37' >G37陕西财经职业技术学院</option>
<option value='G43' >G43山东信息职业技术学院</option>
<option value='G69' >G69厦门华天涉外职业技术学院（民办）</option>
<option value='G70' >G70四川司法警官职业学院</option>
<option value='G74' >G74北京交通职业技术学院</option>
<option value='G75' >G75广州城市职业学院</option>
<option value='G77' >G77湖南现代物流职业技术学院</option>
<option value='G87' >G87北京劳动保障职业学院</option>
<option value='G90' >G90石家庄人民医学高等专科学校（民办）</option>
<option value='G93' >G93山东传媒职业学院</option>
<option value='G94' >G94临沂职业学院</option>
<option value='G96' >G96石家庄科技职业学院（民办）</option>
<option value='G97' >G97西安医学高等专科学校（民办）</option>
<option value='H01' >H01重庆商务职业学院</option>
<option value='H07' >H07黑龙江护理高等专科学校</option>
<option value='H09' >H09呼伦贝尔职业技术学院</option>
<option value='H10' >H10满洲里俄语职业学院</option>
<option value='H11' >H11吉林科技职业技术学院（民办）</option>
<option value='H26' >H26衡水职业技术学院</option>
<option value='H27' >H27浙江商业职业技术学院</option>
<option value='H28' >H28浙江旅游职业学院</option>
<option value='H33' >H33湖南机电职业技术学院</option>
<option value='H39' >H39常州机电职业技术学院</option>
<option value='H68' >H68湖南民族职业学院</option>
<option value='H83' >H83陕西工商职业学院</option>
<option value='H85' >H85厦门软件职业技术学院（民办）</option>
<option value='J03' >J03新乡职业技术学院</option>
<option value='J09' >J09北京交通运输职业学院</option>
<option value='J11' >J11承德护理职业学院</option>
<option value='J13' >J13铁岭卫生职业学院</option>
<option value='J24' >J24河北环境工程学院</option>
<option value='J28' >J28内蒙古能源职业学院</option>
<option value='J29' >J29赤峰工业职业技术学院</option>
<option value='J30' >J30阿拉善职业技术学院</option>
<option value='J48' >J48南京铁道职业技术学院</option>
<option value='J54' >J54唐山科技职业技术学院</option>
<option value='J63' >J63内蒙古美术职业学院</option>
<option value='J82' >J82新疆兵团警官高等专科学校</option>
<option value='J91' >J91山西管理职业学院</option>
<option value='J92' >J92广西电力职业技术学院</option>
<option value='J93' >J93石家庄科技工程职业学院</option>
<option value='J94' >J94辽宁医药职业学院</option>
<option value='J95' >J95石家庄幼儿师范高等专科学校</option>
<option value='J97' >J97上海民航职业技术学院</option>
<option value='J98' >J98河北轨道运输职业技术学院</option>
<option value='J99' >J99运城护理职业学院</option>
<option value='K03' >K03内蒙古民族幼儿师范高等专科学校</option>
<option value='K16' >K16铁岭师范高等专科学校</option>
<option value='K18' >K18江苏工程职业技术学院</option>
<option value='K22' >K22武汉船舶职业技术学院</option>
<option value='K23' >K23辽宁轨道交通职业学院</option>
<option value='K24' >K24岳阳职业技术学院</option>
<option value='K25' >K25江苏农林职业技术学院</option>
<option value='K26' >K26临汾职业技术学院</option>
<option value='K27' >K27石家庄科技信息职业学院（民办）</option>
<option value='K32' >K32柳州城市职业学院</option>
<option value='K33' >K33长白山职业技术学院</option>
<option value='K34' >K34三亚理工职业学院（民办）</option>
<option value='K35' >K35辽宁现代服务职业技术学院</option>
<option value='K36' >K36辽宁工程职业学院</option>
<option value='K42' >K42张家口学院</option>
<option value='K44' >K44辽宁轻工职业学院</option>
<option value='K45' >K45陕西艺术职业学院</option>
<option value='K46' >K46鄂尔多斯生态环境职业学院</option>
<option value='K61' >K61沧州职业技术学院</option>
<option value='K64' >K64仙桃职业学院</option>
<option value='K69' >K69沧州医学高等专科学校</option>
<option value='K73' >K73湖南铁路科技职业技术学院</option>
<option value='K75' >K75益阳医学高等专科学校</option>
<option value='K78' >K78榆林职业技术学院</option>
<option value='K79' >K79延边职业技术学院</option>
<option value='K80' >K80济南护理职业学院</option>
<option value='K84' >K84辽宁水利职业学院</option>
<option value='K87' >K87威海海洋职业学院</option>
<option value='K93' >K93江西师范高等专科学校</option>
<option value='K94' >K94扎兰屯职业学院</option>
<option value='L06' >L06内蒙古农业大学</option>
<option value='L07' >L07内蒙古师范大学</option>
<option value='L09' >L09内蒙古民族大学</option>
<option value='L39' >L39内蒙古科技大学</option>
<option value='L46' >L46包头职业技术学院</option>
<option value='L47' >L47兴安职业技术学院</option>
<option value='L48' >L48呼和浩特职业学院</option>
<option value='L53' >L53内蒙古商贸职业学院</option>
<option value='L54' >L54锡林郭勒职业学院</option>
<option value='L55' >L55乌兰察布职业学院</option>
<option value='L56' >L56通辽职业学院</option>
<option value='L57' >L57内蒙古交通职业技术学院</option>
<option value='L58' >L58乌海职业技术学院</option>
<option value='L66' >L66呼伦贝尔职业技术学院</option>
<option value='M10' >M10娄底职业技术学院</option>
<option value='M11' >M11浙江经贸职业技术学院</option>
<option value='M14' >M14宿迁职业技术学院</option>
<option value='M22' >M22运城师范高等专科学校</option>
<option value='M23' >M23渤海理工职业学院（民办）</option>
<option value='M26' >M26吉林职业技术学院（民办）</option>
<option value='M27' >M27长春师范高等专科学校</option>
<option value='M33' >M33新疆生产建设兵团兴新职业技术学院</option>
<option value='M37' >M37苏州百年职业学院（民办）</option>
<option value='M43' >M43广东酒店管理职业技术学院（民办）</option>
<option value='M45' >M45三亚中瑞酒店管理职业学院（民办）</option>
<option value='M46' >M46重庆信息技术职业学院（民办）</option>
<option value='M52' >M52宁夏建设职业技术学院</option>
<option value='M70' >M70石河子工程职业技术学院</option>
</select><BR><BR>
<INPUT type='submit' value='提交' name='query'>
<INPUT type='reset' value='重置'>

<input type="hidden" name="pcdm" value="7">
<input type="hidden" name="kldm" value="A">
<input type="hidden" name="pxfs" value="1">
</FORM>
</font>
</FONT>
<div align=center class='style2'><STRONG STYLE="COLOR:BLUE">您查询的院校录取的最高最低分如下：</STRONG></div>
<BR>
<font size=2><strong>批次：</strong>
7高职高专
<strong>科类：</strong>
A普通文科
&nbsp;<strong>院校名称：</strong>
204包头职业技术学院</font><p>
<font size=2 color=#8000FF>各次填报最高分最低分情况</font>
<TABLE border=1 align=center cellspacing=0 >
<TR><TD class='style1'><STRONG><P ALIGN=CENTER>填报次序</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最高分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最低分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>录取人数</TD></TR>
<TR><TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>383</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>970</TD></TR>
<TR><TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>318</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>17</TD></TR>
<TR><TD class='style1'><P ALIGN=CENTER>第3次填报</TD>
<TD class='style1'><P ALIGN=CENTER>258</TD>
<TD class='style1'><P ALIGN=CENTER>165</TD>
<TD class='style1'><P ALIGN=CENTER>4</TD></TR>
</TABLE><p>
<font size=2 color=#8000FF>各专业最高分最低分情况</font>
<TABLE border=1 align=center cellspacing=0 >
<TR><TD class='style1'><STRONG><P ALIGN=CENTER>专业代号</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>专业名称</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>填报次序</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最高分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最低分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最低分位次</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>录取人数</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>01</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=01'>电力系统自动化技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>364</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>59</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>216</TD>
<TD class='style1'><P ALIGN=CENTER>214</TD>
<TD class='style1'><P ALIGN=CENTER>39616</TD>
<TD class='style1'><P ALIGN=CENTER>2</TD></TR>
<TR><TD class='style1' rowspan='3'><P ALIGN=CENTER>02</TD>
<TD class='style1' rowspan='3'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=02'>会计</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>383</TD>
<TD class='style1'><P ALIGN=CENTER>291</TD>
<TD class='style1'><P ALIGN=CENTER>34415</TD>
<TD class='style1'><P ALIGN=CENTER>91</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>318</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>6</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第3次填报</TD>
<TD class='style1'><P ALIGN=CENTER>207</TD>
<TD class='style1'><P ALIGN=CENTER>207</TD>
<TD class='style1'><P ALIGN=CENTER>39849</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>07</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=07'>建筑工程技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>292</TD>
<TD class='style1'><P ALIGN=CENTER>171</TD>
<TD class='style1'><P ALIGN=CENTER>40580</TD>
<TD class='style1'><P ALIGN=CENTER>10</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>08</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=08'>计算机网络技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>356</TD>
<TD class='style1'><P ALIGN=CENTER>258</TD>
<TD class='style1'><P ALIGN=CENTER>37307</TD>
<TD class='style1'><P ALIGN=CENTER>60</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>09</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=09'>焊接技术与自动化(机器人焊接技术)</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>328</TD>
<TD class='style1'><P ALIGN=CENTER>227</TD>
<TD class='style1'><P ALIGN=CENTER>39113</TD>
<TD class='style1'><P ALIGN=CENTER>10</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>11</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=11'>应用英语</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>353</TD>
<TD class='style1'><P ALIGN=CENTER>190</TD>
<TD class='style1'><P ALIGN=CENTER>40313</TD>
<TD class='style1'><P ALIGN=CENTER>53</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>13</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=13'>数控技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>309</TD>
<TD class='style1'><P ALIGN=CENTER>186</TD>
<TD class='style1'><P ALIGN=CENTER>40383</TD>
<TD class='style1'><P ALIGN=CENTER>18</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>15</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=15'>工商企业管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>345</TD>
<TD class='style1'><P ALIGN=CENTER>165</TD>
<TD class='style1'><P ALIGN=CENTER>40628</TD>
<TD class='style1'><P ALIGN=CENTER>29</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>172</TD>
<TD class='style1'><P ALIGN=CENTER>172</TD>
<TD class='style1'><P ALIGN=CENTER>40573</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>16</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=16'>商务英语</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>375</TD>
<TD class='style1'><P ALIGN=CENTER>163</TD>
<TD class='style1'><P ALIGN=CENTER>40642</TD>
<TD class='style1'><P ALIGN=CENTER>9</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>17</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=17'>房地产经营与管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>260</TD>
<TD class='style1'><P ALIGN=CENTER>185</TD>
<TD class='style1'><P ALIGN=CENTER>40395</TD>
<TD class='style1'><P ALIGN=CENTER>2</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>18</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=18'>汽车运用与维修技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>296</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>31</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第3次填报</TD>
<TD class='style1'><P ALIGN=CENTER>165</TD>
<TD class='style1'><P ALIGN=CENTER>165</TD>
<TD class='style1'><P ALIGN=CENTER>40628</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>20</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=20'>酒店管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>344</TD>
<TD class='style1'><P ALIGN=CENTER>168</TD>
<TD class='style1'><P ALIGN=CENTER>40603</TD>
<TD class='style1'><P ALIGN=CENTER>41</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>21</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=21'>文秘</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>381</TD>
<TD class='style1'><P ALIGN=CENTER>170</TD>
<TD class='style1'><P ALIGN=CENTER>40586</TD>
<TD class='style1'><P ALIGN=CENTER>41</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>23</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=23'>汽车营销与服务</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>285</TD>
<TD class='style1'><P ALIGN=CENTER>202</TD>
<TD class='style1'><P ALIGN=CENTER>40007</TD>
<TD class='style1'><P ALIGN=CENTER>9</TD></TR>
<TR><TD class='style1' rowspan='3'><P ALIGN=CENTER>25</TD>
<TD class='style1' rowspan='3'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=25'>机械制造与自动化</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>330</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>16</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>292</TD>
<TD class='style1'><P ALIGN=CENTER>292</TD>
<TD class='style1'><P ALIGN=CENTER>34320</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第3次填报</TD>
<TD class='style1'><P ALIGN=CENTER>232</TD>
<TD class='style1'><P ALIGN=CENTER>232</TD>
<TD class='style1'><P ALIGN=CENTER>38875</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='3'><P ALIGN=CENTER>26</TD>
<TD class='style1' rowspan='3'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=26'>机电一体化技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>364</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>84</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>252</TD>
<TD class='style1'><P ALIGN=CENTER>164</TD>
<TD class='style1'><P ALIGN=CENTER>40636</TD>
<TD class='style1'><P ALIGN=CENTER>3</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第3次填报</TD>
<TD class='style1'><P ALIGN=CENTER>258</TD>
<TD class='style1'><P ALIGN=CENTER>258</TD>
<TD class='style1'><P ALIGN=CENTER>37307</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>28</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=28'>旅游管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>334</TD>
<TD class='style1'><P ALIGN=CENTER>173</TD>
<TD class='style1'><P ALIGN=CENTER>40559</TD>
<TD class='style1'><P ALIGN=CENTER>40</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>30</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=30'>审计</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>334</TD>
<TD class='style1'><P ALIGN=CENTER>196</TD>
<TD class='style1'><P ALIGN=CENTER>40162</TD>
<TD class='style1'><P ALIGN=CENTER>60</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>37</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=37'>物联网应用技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>381</TD>
<TD class='style1'><P ALIGN=CENTER>201</TD>
<TD class='style1'><P ALIGN=CENTER>40046</TD>
<TD class='style1'><P ALIGN=CENTER>50</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>294</TD>
<TD class='style1'><P ALIGN=CENTER>294</TD>
<TD class='style1'><P ALIGN=CENTER>34128</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>40</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=40'>文化市场经营管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>334</TD>
<TD class='style1'><P ALIGN=CENTER>177</TD>
<TD class='style1'><P ALIGN=CENTER>40512</TD>
<TD class='style1'><P ALIGN=CENTER>5</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>41</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=41'>工业设计(产品造型设计)</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>261</TD>
<TD class='style1'><P ALIGN=CENTER>179</TD>
<TD class='style1'><P ALIGN=CENTER>40479</TD>
<TD class='style1'><P ALIGN=CENTER>4</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>44</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=44'>机械产品检测检验技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>283</TD>
<TD class='style1'><P ALIGN=CENTER>173</TD>
<TD class='style1'><P ALIGN=CENTER>40559</TD>
<TD class='style1'><P ALIGN=CENTER>6</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>45</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=45'>建筑装饰工程技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>246</TD>
<TD class='style1'><P ALIGN=CENTER>173</TD>
<TD class='style1'><P ALIGN=CENTER>40559</TD>
<TD class='style1'><P ALIGN=CENTER>11</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>185</TD>
<TD class='style1'><P ALIGN=CENTER>185</TD>
<TD class='style1'><P ALIGN=CENTER>40395</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>47</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=47'>模具设计与制造(3D打印与模具逆向技术)</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>366</TD>
<TD class='style1'><P ALIGN=CENTER>179</TD>
<TD class='style1'><P ALIGN=CENTER>40479</TD>
<TD class='style1'><P ALIGN=CENTER>10</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>52</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=52'>工业机器人技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>348</TD>
<TD class='style1'><P ALIGN=CENTER>164</TD>
<TD class='style1'><P ALIGN=CENTER>40636</TD>
<TD class='style1'><P ALIGN=CENTER>10</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>54</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=54'>体育运营与管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>325</TD>
<TD class='style1'><P ALIGN=CENTER>211</TD>
<TD class='style1'><P ALIGN=CENTER>39709</TD>
<TD class='style1'><P ALIGN=CENTER>10</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>56</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=56'>幼儿发展与健康管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>357</TD>
<TD class='style1'><P ALIGN=CENTER>263</TD>
<TD class='style1'><P ALIGN=CENTER>36933</TD>
<TD class='style1'><P ALIGN=CENTER>16</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>61</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=61'>新能源装备技术(风能发电设备制造与维修)</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>340</TD>
<TD class='style1'><P ALIGN=CENTER>203</TD>
<TD class='style1'><P ALIGN=CENTER>39969</TD>
<TD class='style1'><P ALIGN=CENTER>40</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>67</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=67'>安全防范技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>271</TD>
<TD class='style1'><P ALIGN=CENTER>184</TD>
<TD class='style1'><P ALIGN=CENTER>40409</TD>
<TD class='style1'><P ALIGN=CENTER>4</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>68</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=68'>新能源汽车技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>332</TD>
<TD class='style1'><P ALIGN=CENTER>280</TD>
<TD class='style1'><P ALIGN=CENTER>35499</TD>
<TD class='style1'><P ALIGN=CENTER>20</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>70</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=70'>计算机信息管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>259</TD>
<TD class='style1'><P ALIGN=CENTER>223</TD>
<TD class='style1'><P ALIGN=CENTER>39285</TD>
<TD class='style1'><P ALIGN=CENTER>20</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>71</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=71'>老年服务与管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>348</TD>
<TD class='style1'><P ALIGN=CENTER>199</TD>
<TD class='style1'><P ALIGN=CENTER>40091</TD>
<TD class='style1'><P ALIGN=CENTER>8</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>73</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=73'>无人机应用技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>281</TD>
<TD class='style1'><P ALIGN=CENTER>177</TD>
<TD class='style1'><P ALIGN=CENTER>40512</TD>
<TD class='style1'><P ALIGN=CENTER>9</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>76</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=76'>建筑室内设计</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>339</TD>
<TD class='style1'><P ALIGN=CENTER>233</TD>
<TD class='style1'><P ALIGN=CENTER>38826</TD>
<TD class='style1'><P ALIGN=CENTER>15</TD></TR>
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>78</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=78'>金融管理</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>378</TD>
<TD class='style1'><P ALIGN=CENTER>207</TD>
<TD class='style1'><P ALIGN=CENTER>39849</TD>
<TD class='style1'><P ALIGN=CENTER>30</TD></TR>
<TR><TD class='style1' rowspan='2'><P ALIGN=CENTER>94</TD>
<TD class='style1' rowspan='2'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=7&kldm=A&yxdh=204&zydh=94'>电气自动化技术</a></TD>
<TD class='style1'><P ALIGN=CENTER>第1次填报</TD>
<TD class='style1'><P ALIGN=CENTER>367</TD>
<TD class='style1'><P ALIGN=CENTER>161</TD>
<TD class='style1'><P ALIGN=CENTER>40654</TD>
<TD class='style1'><P ALIGN=CENTER>39</TD></TR>
<TR>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>252</TD>
<TD class='style1'><P ALIGN=CENTER>205</TD>
<TD class='style1'><P ALIGN=CENTER>39904</TD>
<TD class='style1'><P ALIGN=CENTER>2</TD></TR>
</TABLE>

<HR>
<BR><BR>
<FONT face=5 color=#00aaff size=2>内蒙古自治区教育招生考试中心版权所有，未经授权，不得转载或链接。</FONT><BR><BR></CENTER>
</body>
</html>
"""
html= etree.HTML(str)
tr = html.xpath("//table[2]/tr[position()>1]")
tr_0=tr[3].xpath("./td/p/text()")
tr_1=tr[2].xpath("./td/p/text()")
tr_2=tr[1].xpath("./td/p/text()")
tr_3=tr[0].xpath("./td/p/text()")
tr_4=tr[0].xpath("./td/p/text()")
def locate_index_1(tr_result, tr_len):
    idx = 0
    for i in range(len(tr_result)):
        if i > 1:
            tr_len = len(tr[i].xpath("./td/p/text()"))
            tr_1_len = len(tr[i - 1].xpath("./td/p/text()"))
            if (tr_len < tr_1_len) and tr_len == tr_len:
                # print (i)
                idx = int(i - 1)
        if i > 2:
            print(2)
            tr_2_len = len(tr[i - 2].xpath("./td/p/text()"))
            if (tr_len == tr_1_len) and (tr_len < tr_2_len) and tr_len == tr_len:
                # print(i)
                idx = int(i - 2)
        if i > 3:
            tr_3_len = len(tr[i - 3].xpath("./td/p/text()"))
            if (tr_len == tr_1_len) and (tr_len == tr_2_len) and (tr_len < tr_3_len) and tr_len == tr_len:
                idx = int(i - 3)
        if i > 4:
            tr_4_len = len(tr[i - 4].xpath("./td/p/text()"))
            if (tr_len == tr_1_len) and (tr_len == tr_2_len) and (tr_len == tr_3_len) and (
                    tr_len < tr_4_len) and tr_len == tr_len:
                idx = int(i - 4)
        if i > tr_len:
            tr_5_len = len(tr[i - tr_len].xpath("./td/p/text()"))
            if (tr_len == tr_1_len) and (tr_len == tr_2_len) and (tr_len == tr_3_len) and (tr_len == tr_4_len) and (
                    tr_len < tr_5_len) and tr_len == tr_len:
                idx = int(i - 5)
    # return  idx

def locate_index(tr,tr_1,tr_2,tr_3,tr_4,tr_len):
    idx = 0
    if (len(tr)<len(tr_1)) and tr_len==tr_len:
        print (1)
        idx = 1
    if (len(tr) == len(tr_1)) and (len(tr) < len(tr_2)) and tr_len == tr_len:
        print(2)
        idx = 2
    if (len(tr) == len(tr_1)) and (len(tr)  == len(tr_2)) and (len(tr)  < len(tr_3)) and tr_len == tr_len:
        print(3)
        idx = 3
    return idx
print (locate_index(tr_0,tr_1,tr_2,tr_3,"",5))