<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" simplifyDrawingHints="0" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" version="3.10.3-A Coruña" simplifyAlgorithm="0" simplifyMaxScale="1" styleCategories="AllStyleCategories" maxScale="0" minScale="1e+08" simplifyLocal="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" enableorderby="0" type="singleSymbol" symbollevels="0">
    <symbols>
      <symbol force_rhr="0" name="0" type="line" alpha="1" clip_to_extent="1">
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="Point" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,1,1,88" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="1.5" k="line_width"/>
          <prop v="Point" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="Point" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="uuid" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory penWidth="0" height="15" sizeType="MM" width="15" backgroundAlpha="255" opacity="1" diagramOrientation="Up" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" maxScaleDenominator="1e+08" scaleDependency="Area" labelPlacementMethod="XHeight" penAlpha="255" penColor="#000000" minScaleDenominator="0" barWidth="5" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" minimumSize="0" scaleBasedVisibility="0" enabled="0" lineSizeType="MM">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" color="#000000" label=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" obstacle="0" placement="2" showAll="1" zIndex="0" priority="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="uuid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gemeinde">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="bachnummer">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lage">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="klasse">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="eingedolt">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="bemerkung">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="uuid" index="0" name=""/>
    <alias field="gemeinde" index="1" name=""/>
    <alias field="bachnummer" index="2" name=""/>
    <alias field="lage" index="3" name=""/>
    <alias field="name" index="4" name=""/>
    <alias field="klasse" index="5" name=""/>
    <alias field="eingedolt" index="6" name=""/>
    <alias field="bemerkung" index="7" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="uuid" expression="" applyOnUpdate="0"/>
    <default field="gemeinde" expression="" applyOnUpdate="0"/>
    <default field="bachnummer" expression="" applyOnUpdate="0"/>
    <default field="lage" expression="" applyOnUpdate="0"/>
    <default field="name" expression="" applyOnUpdate="0"/>
    <default field="klasse" expression="" applyOnUpdate="0"/>
    <default field="eingedolt" expression="" applyOnUpdate="0"/>
    <default field="bemerkung" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint unique_strength="1" field="uuid" exp_strength="0" notnull_strength="1" constraints="3"/>
    <constraint unique_strength="0" field="gemeinde" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="bachnummer" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="lage" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="name" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="klasse" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="eingedolt" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint unique_strength="0" field="bemerkung" exp_strength="0" notnull_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="uuid"/>
    <constraint exp="" desc="" field="gemeinde"/>
    <constraint exp="" desc="" field="bachnummer"/>
    <constraint exp="" desc="" field="lage"/>
    <constraint exp="" desc="" field="name"/>
    <constraint exp="" desc="" field="klasse"/>
    <constraint exp="" desc="" field="eingedolt"/>
    <constraint exp="" desc="" field="bemerkung"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="&quot;eingedolt&quot;" sortOrder="0" actionWidgetStyle="dropDown">
    <columns>
      <column width="-1" hidden="0" name="uuid" type="field"/>
      <column width="-1" hidden="0" name="gemeinde" type="field"/>
      <column width="-1" hidden="0" name="bachnummer" type="field"/>
      <column width="-1" hidden="0" name="lage" type="field"/>
      <column width="165" hidden="0" name="name" type="field"/>
      <column width="-1" hidden="0" name="klasse" type="field"/>
      <column width="-1" hidden="0" name="eingedolt" type="field"/>
      <column width="-1" hidden="0" name="bemerkung" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">D:/OSGeo4W64/apps/qgis-ltr/bin</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="bachnummer" editable="1"/>
    <field name="bemerkung" editable="1"/>
    <field name="eingedolt" editable="1"/>
    <field name="gemeinde" editable="1"/>
    <field name="klasse" editable="1"/>
    <field name="lage" editable="1"/>
    <field name="name" editable="1"/>
    <field name="uuid" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="bachnummer" labelOnTop="0"/>
    <field name="bemerkung" labelOnTop="0"/>
    <field name="eingedolt" labelOnTop="0"/>
    <field name="gemeinde" labelOnTop="0"/>
    <field name="klasse" labelOnTop="0"/>
    <field name="lage" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="uuid" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>uuid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
