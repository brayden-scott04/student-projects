<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes" encoding="UTF-8"/>

    <xsl:template match="/">
        <html>
            <head>
                <style>
                    table {
                        border: 1px solid black; 
                        }

                    th, td {
                        border: 1px solid black;
                        text-align: center;
                        padding: 10px;}

                    th {
                        background-color: yellow; 
                        font-weight: bold;
                        height: 10px;}

                    td:not(:first-child), th:not(:first-child) {
                        width: 120px;
                        vertical-align: middle;}

                    td:first-child, th:first-child {
                        width: 50px;
                        background-color: yellow;}

                    .yellow {background-color: yellow;}
                    .blue {color: blue;}
                    .orange {color: orange;}
                    .red {color: red;}
                </style>
            </head>

            <body>
                <h2>
                    <xsl:value-of select="/forecast/@queryLocation"/>
                    <xsl:text> [</xsl:text>
                    <xsl:value-of select="/forecast/@queryTime"/>
                    <xsl:text>]</xsl:text>
                </h2>
                <table>
                    <tr>
                        <th class="yellow">Date</th>
                        <th class="yellow">Mon</th>
                        <th class="yellow">Tue</th>
                        <th class="yellow">Wed</th>
                        <th class="yellow">Thurs</th>
                        <th class="yellow">Fri</th>
                        <th class="yellow">Sat</th>
                        <th class="yellow">Sun</th>
                    </tr>
                        
                        <xsl:for-each select="forecast/weather">
                            
                        <xsl:sort select="@yyyymmdd" data-type="text" order="descending"/>
                        <xsl:if test="not(@yyyymmdd = preceding-sibling::weather/@yyyymmdd)">
                        <tr>
                            <td>
                                <xsl:variable name="month" select="substring(@yyyymmdd,5,2)"/>
                                <xsl:value-of select="substring(@yyyymmdd,7,2)"/>
                                <xsl:text> </xsl:text>
                                <xsl:choose>
                                    <xsl:when test="$month='01'">Jan</xsl:when>
                                    <xsl:when test="$month='02'">Feb</xsl:when>
                                    <xsl:when test="$month='03'">Mar</xsl:when>
                                    <xsl:when test="$month='04'">Apr</xsl:when>
                                    <xsl:when test="$month='05'">May</xsl:when>
                                    <xsl:when test="$month='06'">Jun</xsl:when>
                                    <xsl:when test="$month='07'">Jul</xsl:when>
                                    <xsl:when test="$month='08'">Aug</xsl:when>
                                    <xsl:when test="$month='09'">Sep</xsl:when>
                                    <xsl:when test="$month='10'">Oct</xsl:when>
                                    <xsl:when test="$month='11'">Nov</xsl:when>
                                    <xsl:when test="$month='12'">Dec</xsl:when>
                                </xsl:choose>
                            </td>

                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Mon'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Tue'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Wed'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Thurs'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Fri'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Sat'"/>
                            </xsl:call-template>
                            <xsl:call-template name="day-cell" >
                                <xsl:with-param name="date" select="@yyyymmdd"/>
                                <xsl:with-param name="day" select="'Sun'"/>
                            </xsl:call-template>
                        </tr>

                    </xsl:if>
                    </xsl:for-each>
                </table>
            </body>
    </html>
    </xsl:template>

    <xsl:template name="day-cell">
    <xsl:param name="date"/>
    <xsl:param name="day"/>
    <xsl:variable name="weather" select="/forecast/weather[@yyyymmdd=$date and dayOfWeek=$day]"/>
    <td>
        <xsl:choose>
        <xsl:when test="count($weather) &gt; 0">
        <xsl:value-of select="concat($weather[1]/lowest,'°',' ', '&#x2212;',' ', $weather[1]/highest, '°', ' ')"/>
        <br/>
        <img>
        <xsl:attribute name="src">
        <xsl:choose>
            <xsl:when test="$weather[1]/overallCode='cloudy'">cloudy.jpeg</xsl:when>
            <xsl:when test="$weather[1]/overallCode='partlySunny'">partlySunny.jpeg</xsl:when>
            <xsl:when test="$weather[1]/overallCode='rain'">rain.png</xsl:when>
            <xsl:when test="$weather[1]/overallCode='sunny'">sunny.jpeg</xsl:when>
            <xsl:when test="$weather[1]/overallCode='thunderstorm'">thunderstorm.png</xsl:when>
            <xsl:otherwise>default.png</xsl:otherwise>
        </xsl:choose>
        </xsl:attribute>

        <xsl:attribute name="alt">
            <xsl:value-of select="$weather[1]/overall"/>
        </xsl:attribute>

        <xsl:attribute name="width">50</xsl:attribute>
        <xsl:attribute name="height">50</xsl:attribute>
        </img>
        <br/>
        
        <span>
            <xsl:attribute name="class">
                <xsl:choose>
                    <xsl:when test="$weather[1]/overallCode='cloudy'">blue</xsl:when>
                    <xsl:when test="$weather[1]/overallCode='rain'">orange</xsl:when>
                    <xsl:when test="$weather[1]/overallCode='thunderstorm'">orange</xsl:when>
                    <xsl:when test="$weather[1]/overallCode='sunny'">red</xsl:when>
                    <xsl:when test="$weather[1]/overallCode='partlySunny'">red</xsl:when>
                </xsl:choose>
            </xsl:attribute>
            <xsl:value-of select="$weather[1]/overall"/>
        </span>       
        </xsl:when>

        <xsl:otherwise>
        </xsl:otherwise>
        </xsl:choose>
    </td>
</xsl:template>

</xsl:stylesheet>

