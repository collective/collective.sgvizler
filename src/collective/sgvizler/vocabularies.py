# -*- encoding: utf-8 -*-

from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from collective.sgvizler import _

charts = SimpleVocabulary([
    # Google Visualization API
    SimpleTerm(value=u'google.visualization.AnnotatedTimeLine ', term=_(u'Google Annotated Time Line')),
    SimpleTerm(value=u'google.visualization.AreaChart', term=_(u'Google Area Chart')),
    SimpleTerm(value=u'google.visualization.BarChart', term=_(u'Google Bar Chart')),
    SimpleTerm(value=u'google.visualization.BubbleChart', term=_(u'Google Bubble Chart')),
    SimpleTerm(value=u'google.visualization.CandlestickChart ', term=_(u'Google Candelstick Chart')),
    SimpleTerm(value=u'google.visualization.ColumnChart', term=_(u'Google Column Chart')),
    SimpleTerm(value=u'google.visualization.Gauge', term=_(u'Google Gauge')),
    SimpleTerm(value=u'google.visualization.GeoChart ', term=_(u'Google Geo Chart')),
    SimpleTerm(value=u'google.visualization.GeoMap ', term=_(u'Google Geo Map')),
    SimpleTerm(value=u'google.visualization.ImageSparkLine', term=_(u'Google Image Spark Line')),
    SimpleTerm(value=u'google.visualization.LineChart', term=_(u'Google Line Chart')),
    SimpleTerm(value=u'google.visualization.Map', term=_(u'Google Map')),
    SimpleTerm(value=u'google.visualization.MotionChart', term=_(u'Google Motion Chart')),
    SimpleTerm(value=u'google.visualization.OrgChart', term=_(u'Google Org Chart')),
    SimpleTerm(value=u'google.visualization.PieChart', term=_(u'Google Pie Chart')),
    SimpleTerm(value=u'google.visualization.ScatterChart', term=_(u'Google Scatter Chart')),
    SimpleTerm(value=u'google.visualization.SteppedAreaChart', term=_(u'Google Stepped Area Chart')),
    SimpleTerm(value=u'google.visualization.Table', term=_(u'Google Table')),
    SimpleTerm(value=u'google.visualization.TreeMap', term=_(u'Google Tree Map')),
    # SGVizler Visualization Integration
    SimpleTerm(value=u'sgvizler.visualization.DefList', term=_(u'Sgvizler Definition List')),
    SimpleTerm(value=u'sgvizler.visualization.D3ForceGraph', term=_(u'Sgvizler D3 Force-directed Graph')),
    SimpleTerm(value=u'sgvizler.visualization.DraculaGraph', term=_(u'Sgvizler Dracula Graph')),
    SimpleTerm(value=u'sgvizler.visualization.List', term=_(u'Sgvizler List')),
    SimpleTerm(value=u'sgvizler.visualization.Map', term=_(u'Sgvizler Map')),
    SimpleTerm(value=u'sgvizler.visualization.MapWKT', term=_(u'Sgvizler Well-known Text (WKT) Map')),
    SimpleTerm(value=u'sgvizler.visualization.Table', term=_(u'Sgvizler Table')),
    SimpleTerm(value=u'sgvizler.visualization.Text', term=_(u'Sgvizler Generic HTML')),
])