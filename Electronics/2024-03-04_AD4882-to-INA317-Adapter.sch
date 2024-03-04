<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="AD8422BRMZ-RL">
<packages>
<package name="SOP65P490X110-8N">
<circle x="-3.74" y="1.475" radius="0.1" width="0.2" layer="21"/>
<circle x="-3.74" y="1.475" radius="0.1" width="0.2" layer="51"/>
<wire x1="-1.6" y1="1.6" x2="1.6" y2="1.6" width="0.127" layer="51"/>
<wire x1="-1.6" y1="-1.6" x2="1.6" y2="-1.6" width="0.127" layer="51"/>
<wire x1="-1.6" y1="1.6" x2="1.6" y2="1.6" width="0.127" layer="21"/>
<wire x1="-1.6" y1="-1.6" x2="1.6" y2="-1.6" width="0.127" layer="21"/>
<wire x1="-1.6" y1="1.6" x2="-1.6" y2="-1.6" width="0.127" layer="51"/>
<wire x1="1.6" y1="1.6" x2="1.6" y2="-1.6" width="0.127" layer="51"/>
<wire x1="-3.18" y1="1.85" x2="3.18" y2="1.85" width="0.05" layer="39"/>
<wire x1="-3.18" y1="-1.85" x2="3.18" y2="-1.85" width="0.05" layer="39"/>
<wire x1="-3.18" y1="1.85" x2="-3.18" y2="-1.85" width="0.05" layer="39"/>
<wire x1="3.18" y1="1.85" x2="3.18" y2="-1.85" width="0.05" layer="39"/>
<text x="-3" y="-2" size="0.8128" layer="27" align="top-left">&gt;VALUE</text>
<text x="-3" y="2" size="0.8128" layer="25">&gt;NAME</text>
<smd name="1" x="-2.12" y="0.975" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="2" x="-2.12" y="0.325" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="3" x="-2.12" y="-0.325" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="4" x="-2.12" y="-0.975" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="5" x="2.12" y="-0.975" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="6" x="2.12" y="-0.325" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="7" x="2.12" y="0.325" dx="1.62" dy="0.5" layer="1" roundness="25"/>
<smd name="8" x="2.12" y="0.975" dx="1.62" dy="0.5" layer="1" roundness="25"/>
</package>
</packages>
<symbols>
<symbol name="AD8422BRMZ-RL">
<text x="-6.35" y="14.605" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-15.24" size="1.778" layer="96" align="top-left">&gt;VALUE</text>
<pin name="-IN" x="-12.7" y="7.62" visible="pad" length="middle" direction="in"/>
<pin name="+IN" x="-12.7" y="-7.62" visible="pad" length="middle" direction="in"/>
<pin name="VOUT" x="17.78" y="0" visible="pad" length="middle" direction="out" rot="R180"/>
<pin name="VS+" x="2.54" y="11.43" visible="pad" length="middle" direction="pwr" rot="R270"/>
<pin name="VS-" x="2.54" y="-11.43" visible="pad" length="middle" direction="pwr" rot="R90"/>
<pin name="REF" x="-12.7" y="0" visible="pad" length="middle" direction="in"/>
<pin name="RG_1" x="-12.7" y="-5.08" visible="pad" length="middle" direction="pas"/>
<pin name="RG_2" x="-12.7" y="5.08" visible="pad" length="middle" direction="pas"/>
<wire x1="-7.62" y1="12.7" x2="-7.62" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="-7.62" y1="-12.7" x2="12.7" y2="0" width="0.1524" layer="94"/>
<wire x1="12.7" y1="0" x2="-7.62" y2="12.7" width="0.1524" layer="94"/>
<text x="-5.08" y="7.62" size="1.778" layer="94" align="center-left">-</text>
<text x="-5.08" y="5.08" size="1.778" layer="94" align="center-left">RG1</text>
<text x="-5.08" y="0" size="1.778" layer="94" align="center-left">REF</text>
<text x="-5.08" y="-5.08" size="1.778" layer="94" align="center-left">RG2</text>
<text x="-5.08" y="-7.62" size="1.778" layer="94" align="center-left">-</text>
<text x="2.54" y="-5.08" size="1.778" layer="94" rot="R90" align="center-left">V-</text>
<text x="2.54" y="2.54" size="1.778" layer="94" rot="R90" align="center-left">V+</text>
<text x="2.54" y="0" size="1.778" layer="94" align="center-left">VOUT</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="AD8422BRMZ-RL" prefix="U">
<description>INSTRUMENT AMP, 2.2MHZ, 80DB, 8 MSOP; No. of Amplifiers: 1; Input Offset Voltage:    &lt;a href="https://pricing.snapeda.com/parts/AD8422BRMZ-RL/Analog%20Devices/view-part?ref=eda"&gt;Check availability&lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="AD8422BRMZ-RL" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOP65P490X110-8N">
<connects>
<connect gate="G$1" pin="+IN" pad="4"/>
<connect gate="G$1" pin="-IN" pad="1"/>
<connect gate="G$1" pin="REF" pad="6"/>
<connect gate="G$1" pin="RG_1" pad="2"/>
<connect gate="G$1" pin="RG_2" pad="3"/>
<connect gate="G$1" pin="VOUT" pad="7"/>
<connect gate="G$1" pin="VS+" pad="8"/>
<connect gate="G$1" pin="VS-" pad="5"/>
</connects>
<technologies>
<technology name="">
<attribute name="AVAILABILITY" value="In Stock"/>
<attribute name="CHECK_PRICES" value="https://www.snapeda.com/parts/AD8422BRMZ-RL/Analog+Devices/view-part/?ref=eda"/>
<attribute name="DESCRIPTION" value=" High Performance, Low Power, Rail-to-Rail Precision Instrumentation Amplifier "/>
<attribute name="MF" value="Analog Devices"/>
<attribute name="MP" value="AD8422BRMZ-RL"/>
<attribute name="PACKAGE" value="MSOP-8 Analog Devices"/>
<attribute name="PRICE" value="None"/>
<attribute name="PURCHASE-URL" value="https://www.snapeda.com/api/url_track_click_mouser/?unipart_id=972475&amp;manufacturer=Analog Devices&amp;part_name=AD8422BRMZ-RL&amp;search_term=ad8422"/>
<attribute name="SNAPEDA_LINK" value="https://www.snapeda.com/parts/AD8422BRMZ-RL/Analog+Devices/view-part/?ref=snap"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="INA317IDGKT">
<packages>
<package name="SOP65P490X110-8N">
<circle x="-3.52" y="1.255" radius="0.1" width="0.2" layer="21"/>
<circle x="-3.52" y="1.255" radius="0.1" width="0.2" layer="51"/>
<wire x1="-1.5" y1="1.5" x2="1.5" y2="1.5" width="0.127" layer="51"/>
<wire x1="-1.5" y1="-1.5" x2="1.5" y2="-1.5" width="0.127" layer="51"/>
<wire x1="-1.5" y1="1.535" x2="1.5" y2="1.535" width="0.127" layer="21"/>
<wire x1="-1.5" y1="-1.535" x2="1.5" y2="-1.535" width="0.127" layer="21"/>
<wire x1="-1.5" y1="1.5" x2="-1.5" y2="-1.5" width="0.127" layer="51"/>
<wire x1="1.5" y1="1.5" x2="1.5" y2="-1.5" width="0.127" layer="51"/>
<wire x1="-3.135" y1="1.75" x2="3.135" y2="1.75" width="0.05" layer="39"/>
<wire x1="-3.135" y1="-1.75" x2="3.135" y2="-1.75" width="0.05" layer="39"/>
<wire x1="-3.135" y1="1.75" x2="-3.135" y2="-1.75" width="0.05" layer="39"/>
<wire x1="3.135" y1="1.75" x2="3.135" y2="-1.75" width="0.05" layer="39"/>
<text x="-3" y="-1.9" size="1.27" layer="27" align="top-left">&gt;VALUE</text>
<text x="-3" y="1.9" size="1.27" layer="25">&gt;NAME</text>
<smd name="1" x="-2.15" y="0.975" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="2" x="-2.15" y="0.325" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="3" x="-2.15" y="-0.325" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="4" x="-2.15" y="-0.975" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="5" x="2.15" y="-0.975" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="6" x="2.15" y="-0.325" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="7" x="2.15" y="0.325" dx="1.47" dy="0.48" layer="1" roundness="25"/>
<smd name="8" x="2.15" y="0.975" dx="1.47" dy="0.48" layer="1" roundness="25"/>
</package>
</packages>
<symbols>
<symbol name="INA317IDGKT">
<text x="-7.62" y="16.24" size="2.0828" layer="95" ratio="10" rot="SR0">&gt;NAME</text>
<text x="-7.62" y="-16.7" size="2.0828" layer="96" ratio="10" rot="SR0">&gt;VALUE</text>
<pin name="REF" x="-12.7" y="0" length="middle" direction="in"/>
<pin name="+" x="-12.7" y="-7.62" length="middle" direction="in"/>
<pin name="RG1" x="-12.7" y="5.08" length="middle"/>
<pin name="RG2" x="-12.7" y="-5.08" length="middle"/>
<pin name="-" x="-12.7" y="7.62" length="middle"/>
<pin name="V-" x="2.54" y="-11.43" length="middle" rot="R90"/>
<pin name="V+" x="2.54" y="11.43" length="middle" direction="pwr" rot="R270"/>
<pin name="VOUT" x="17.78" y="0" length="middle" direction="out" rot="R180"/>
<wire x1="-7.62" y1="12.7" x2="-7.62" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="-7.62" y1="-12.7" x2="12.7" y2="0" width="0.1524" layer="94"/>
<wire x1="-7.62" y1="12.7" x2="12.7" y2="0" width="0.1524" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="INA317IDGKT" prefix="U">
<description> &lt;a href="https://pricing.snapeda.com/parts/INA317IDGKT/Texas%20Instruments/view-part?ref=eda"&gt;Check availability&lt;/a&gt;</description>
<gates>
<gate name="G$1" symbol="INA317IDGKT" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOP65P490X110-8N">
<connects>
<connect gate="G$1" pin="+" pad="3"/>
<connect gate="G$1" pin="-" pad="2"/>
<connect gate="G$1" pin="REF" pad="5"/>
<connect gate="G$1" pin="RG1" pad="1"/>
<connect gate="G$1" pin="RG2" pad="8"/>
<connect gate="G$1" pin="V+" pad="7"/>
<connect gate="G$1" pin="V-" pad="4"/>
<connect gate="G$1" pin="VOUT" pad="6"/>
</connects>
<technologies>
<technology name="">
<attribute name="AVAILABILITY" value="In Stock"/>
<attribute name="CHECK_PRICES" value="https://www.snapeda.com/parts/INA317IDGKT/Texas+Instruments/view-part/?ref=eda"/>
<attribute name="DESCRIPTION" value=" Micro-power (50µA), zero-drift (75µV offset, 0.3µV/˚C), precision RRO instrumentation amplifier "/>
<attribute name="MF" value="Texas Instruments"/>
<attribute name="MP" value="INA317IDGKT"/>
<attribute name="PACKAGE" value="VSSOP-8 Texas Instruments"/>
<attribute name="PRICE" value="None"/>
<attribute name="PURCHASE-URL" value="https://www.snapeda.com/api/url_track_click_mouser/?unipart_id=3077446&amp;manufacturer=Texas Instruments&amp;part_name=INA317IDGKT&amp;search_term=ina317"/>
<attribute name="SNAPEDA_LINK" value="https://www.snapeda.com/parts/INA317IDGKT/Texas+Instruments/view-part/?ref=snap"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U1" library="AD8422BRMZ-RL" deviceset="AD8422BRMZ-RL" device=""/>
<part name="U2" library="INA317IDGKT" deviceset="INA317IDGKT" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U1" gate="G$1" x="0" y="0" smashed="yes"/>
<instance part="U2" gate="G$1" x="0" y="39.37" smashed="yes">
<attribute name="NAME" x="-7.62" y="55.61" size="2.0828" layer="95" ratio="10" rot="SR0"/>
<attribute name="VALUE" x="-7.62" y="22.67" size="2.0828" layer="96" ratio="10" rot="SR0"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="-IN"/>
<wire x1="-12.7" y1="7.62" x2="-15.24" y2="7.62" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="-"/>
<wire x1="-15.24" y1="7.62" x2="-15.24" y2="46.99" width="0.1524" layer="91"/>
<wire x1="-15.24" y1="46.99" x2="-12.7" y2="46.99" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="RG_2"/>
<wire x1="-12.7" y1="5.08" x2="-16.51" y2="5.08" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="RG1"/>
<wire x1="-16.51" y1="5.08" x2="-16.51" y2="44.45" width="0.1524" layer="91"/>
<wire x1="-16.51" y1="44.45" x2="-12.7" y2="44.45" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="REF"/>
<wire x1="-12.7" y1="0" x2="-17.78" y2="0" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="REF"/>
<wire x1="-17.78" y1="0" x2="-17.78" y2="39.37" width="0.1524" layer="91"/>
<wire x1="-17.78" y1="39.37" x2="-12.7" y2="39.37" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="RG_1"/>
<wire x1="-12.7" y1="-5.08" x2="-19.05" y2="-5.08" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="RG2"/>
<wire x1="-19.05" y1="-5.08" x2="-19.05" y2="34.29" width="0.1524" layer="91"/>
<wire x1="-19.05" y1="34.29" x2="-12.7" y2="34.29" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="+IN"/>
<wire x1="-12.7" y1="-7.62" x2="-20.32" y2="-7.62" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="+"/>
<wire x1="-20.32" y1="-7.62" x2="-20.32" y2="31.75" width="0.1524" layer="91"/>
<wire x1="-20.32" y1="31.75" x2="-12.7" y2="31.75" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="VS+"/>
<wire x1="2.54" y1="11.43" x2="2.54" y2="13.97" width="0.1524" layer="91"/>
<wire x1="2.54" y1="13.97" x2="20.32" y2="13.97" width="0.1524" layer="91"/>
<wire x1="20.32" y1="13.97" x2="20.32" y2="52.07" width="0.1524" layer="91"/>
<wire x1="20.32" y1="52.07" x2="2.54" y2="52.07" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="V+"/>
<wire x1="2.54" y1="52.07" x2="2.54" y2="50.8" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="U2" gate="G$1" pin="V-"/>
<wire x1="2.54" y1="27.94" x2="2.54" y2="17.78" width="0.1524" layer="91"/>
<wire x1="2.54" y1="17.78" x2="22.86" y2="17.78" width="0.1524" layer="91"/>
<wire x1="22.86" y1="17.78" x2="22.86" y2="-13.97" width="0.1524" layer="91"/>
<wire x1="22.86" y1="-13.97" x2="2.54" y2="-13.97" width="0.1524" layer="91"/>
<pinref part="U1" gate="G$1" pin="VS-"/>
<wire x1="2.54" y1="-13.97" x2="2.54" y2="-11.43" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="VOUT"/>
<wire x1="17.78" y1="0" x2="24.13" y2="0" width="0.1524" layer="91"/>
<pinref part="U2" gate="G$1" pin="VOUT"/>
<wire x1="24.13" y1="0" x2="24.13" y2="39.37" width="0.1524" layer="91"/>
<wire x1="24.13" y1="39.37" x2="17.78" y2="39.37" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
