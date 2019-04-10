# _*_coding:utf-8_*_
__author__ = 'wmx'
__date__ = '2019/4/10 16:11'

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
<option value='2' >本科提前B</option>
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
<option value='@'>汉授编导</option>
<option value='A'>普通文科</option>
<option value='B'>普通理科</option>
<option value='C'>蒙授文科</option>
<option value='D'>蒙授理科</option>
<option value='E'>汉授美术</option>
<option value='G'>汉授音乐</option>
<option value='I'>其他艺术</option>
<option value='K'>汉授体育</option>
<option value='L'>蒙授体育</option>
</select>

<input type="hidden" name="pcdm" value="2">
</FORM>

<FORM name="form4" method="post" action="lqmaxmin_18.jsp">
请选择院校排序方式：
<select name='m_pxfs' onChange='document.form4.submit()'>
<option value='1' >院校代号</option>
<option>--------</option>
<option value='1'>院校代号</option>
<option value='2'>院校名称</option>
</select>

<input type="hidden" name="pcdm" value="2">
<input type="hidden" name="kldm" value="A">
</FORM>

<FORM name="form3" method="post" action="lqmaxmin_18.jsp">
请选择院校：
<select name='m_yxdh' title='请选择院校：'>
<option value='008' >008铁道警察学院</option>
<option>----------------</option>
<option value='008' >008铁道警察学院</option>
<option value='019' >019中国政法大学</option>
<option value='020' >020中南财经政法大学</option>
<option value='021' >021大连民族大学</option>
<option value='035' >035西南财经大学</option>
<option value='049' >049南京财经大学</option>
<option value='058' >058中华女子学院</option>
<option value='061' >061对外经济贸易大学</option>
<option value='082' >082北京林业大学</option>
<option value='084' >084南京森林警察学院</option>
<option value='144' >144河海大学</option>
<option value='277' >277上海外国语大学</option>
<option value='279' >279中山大学</option>
<option value='281' >281北京语言大学</option>
<option value='286' >286中国人民大学</option>
<option value='289' >289四川大学</option>
<option value='294' >294清华大学</option>
<option value='298' >298厦门大学</option>
<option value='302' >302南开大学</option>
<option value='304' >304北京大学</option>
<option value='305' >305武汉大学</option>
<option value='307' >307北京师范大学</option>
<option value='308' >308复旦大学</option>
<option value='312' >312中南大学</option>
<option value='313' >313山东大学威海分校</option>
<option value='320' >320陕西师范大学</option>
<option value='321' >321东北师范大学</option>
<option value='324' >324华中师范大学</option>
<option value='327' >327苏州大学</option>
<option value='338' >338北京体育大学</option>
<option value='354' >354上海海关学院</option>
<option value='357' >357南京信息工程大学</option>
<option value='377' >377暨南大学</option>
<option value='651' >651山东师范大学</option>
<option value='751' >751内蒙古大学</option>
<option value='752' >752内蒙古师范大学</option>
<option value='754' >754内蒙古财经大学</option>
<option value='761' >761内蒙古民族大学</option>
<option value='916' >916内蒙古大学满洲里校区</option>
<option value='A48' >A48浙江师范大学</option>
<option value='L30' >L30东北师范大学</option>
<option value='L31' >L31内蒙古大学</option>
<option value='L32' >L32内蒙古师范大学</option>
<option value='L34' >L34内蒙古财经大学</option>
<option value='L37' >L37内蒙古民族大学</option>
<option value='L40' >L40内蒙古大学满洲里校区</option>
<option value='L65' >L65中南民族大学</option>
<option value='M32' >M32中国社会科学院大学</option>
</select><BR><BR>
<INPUT type='submit' value='提交' name='query'>
<INPUT type='reset' value='重置'>

<input type="hidden" name="pcdm" value="2">
<input type="hidden" name="kldm" value="A">
<input type="hidden" name="pxfs" value="1">
</FORM>
</font>
</FONT>
<div align=center class='style2'><STRONG STYLE="COLOR:BLUE">您查询的院校录取的最高最低分如下：</STRONG></div>
<BR>
<font size=2><strong>批次：</strong>
2本科提前B
<strong>科类：</strong>
A普通文科
&nbsp;<strong>院校名称：</strong>
008铁道警察学院</font><p>
<font size=2 color=#8000FF>各次填报最高分最低分情况</font>
<TABLE border=1 align=center cellspacing=0 >
<TR><TD class='style1'><STRONG><P ALIGN=CENTER>填报次序</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最高分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>最低分</TD>
<TD class='style1'><STRONG><P ALIGN=CENTER>录取人数</TD></TR>
<TR><TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>459</TD>
<TD class='style1'><P ALIGN=CENTER>459</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
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
<TR><TD class='style1' rowspan='1'><P ALIGN=CENTER>2Z</TD>
<TD class='style1' rowspan='1'><P ALIGN=left><a href='lqmaxmin_2.jsp?pcdm=2&kldm=A&yxdh=008&zydh=2Z'>治安学</a></TD>
<TD class='style1'><P ALIGN=CENTER>第2次填报</TD>
<TD class='style1'><P ALIGN=CENTER>459</TD>
<TD class='style1'><P ALIGN=CENTER>459</TD>
<TD class='style1'><P ALIGN=CENTER>12148</TD>
<TD class='style1'><P ALIGN=CENTER>1</TD></TR>
</TABLE>

<HR>
<BR><BR>
<FONT face=5 color=#00aaff size=2>内蒙古自治区教育招生考试中心版权所有，未经授权，不得转载或链接。</FONT><BR><BR></CENTER>
</body>
</html>
"""
html = etree.HTML(str)
def get_xpath_result():
    tr_result=html.xpath("//table[2]/tr[position()>1]/td/p/text()")
    list=[]
    list_temp=[]
    for i in range(len(tr_result)):
 	    if len(tr_result)==5 and (i+1)%5==0 and i!=0:
 		    list_temp=[tr_result[i-4],tr_result[i-3],tr_result[i-2],tr_result[i-1],tr_result[i]]
            list.append(list_temp)
        else:
 		    list_temp=[tr_result[i-5],tr_result[i-4],tr_result[i-3],tr_result[i-2],tr_result[i-1],tr_result[i]]
 		    list.append(list_temp)
    return list