# -*- coding:utf-8 -*-
__author__ = 'Christen'

toc = ['history', 'novel', 'swordsman', 'fairytales', 'biography', 'manage', 'essay', 'philosophy', 'program']

toc = ['ch-male', 'ch-female', 'ch-band']

toc = ['getting-to-know-the-work-area', 'basic-photo-corrections', 'working-with-selections', 'layer-basics',
       'correcting-and-enhancing-digital-photographs', 'masks-and-channels', 'typographic-design',
       'vector-drawing-techniques', 'advanced-compositing', 'editing-video', 'paninting-with-the-mixer-brush',
       'working-with-3d-images', 'prearing-files-for-the-web', 'producing-and-printing-consistent-color']

toc = ['china', 'taiwan', 'hongkong', 'Europe America', 'korea japan', 'other']

toc = ['china', 'taiwan', 'hongkong', 'amercia', 'britain', 'france', 'germany', 'korea', 'russia', 'japan', 'india',
       'thailand', 'other']

toc = ['lottery', 'knowledge', 'select', 'drive', 'maintenance']

toc = ['pregnant', 'health', 'nutrition', 'ece']

toc = ['sina', 'baidu', 'Ali', 'tencent', '360', 'github', 'pconline']


toc = ['Search', 'Analytics', 'DoubleClick', 'Chrome', 'Android', 'Maps', 'AngularJS','Calendar','App Engine', 'Chromium','HTML5 Rocks','Hosted Libraries','Public DNS','reCAPTCHA']


toc = ['SIEMENS M55','Samsung X108','Motorola E398','Motorola E770','Nokia E63','Nokia 5800 XM','HTC G14','iPhone 4S','Nokia 2050','Nokia 255']


toc = ['CSS3 Border','CSS3 Background','CSS3 Text Effect','CSS3 Font','CSS3 2D Transform','CSS3 3D Transform','CSS3 Transition','CSS3 Animation','CSS3 Multiple Columns','CSS3 User Interface']


toc = ['Bootstrap Scaffolding', 'Bootstrap CSS', 'Bootstrap Layout Components', 'Bootstrap JavaScript Plugins', 'Bootstrap Using Bootstrap']

toc = ['Creating Enterprise Applications', 'Adding Spring Framework', 'Persisting Data with JPA', 'Securing Your Application']

toc = ['JSP-Overview','JSP-Environment','JSP-Architecture','JSP-Life-Cycle','JSP-Syntax','JSP-Directives','JSP-Actions','JSP-Implicit-Objects','JSP-Client-Request','JSP-Server-Response','JSP-Http-Codes','JSP-Form-Processing','JSP-Writing-Filters','JSP-Cookies-Handling','JSP-Session-Tracking','JSP-File-Uploading','JSP-Handling-Date','JSP-Page-Redirect','JSP-Hits-Counter','JSP-Auto-Refresh','JSP-Sending-Email']


toc = ['JSP-Standard-Tag-Library','JSP-Database-Access','JSP-XML-Data','JSP-Java-Beans','JSP-Custom-Tags','JSP-Expression-Language','JSP-Exception-Handling','JSP-Debugging','JSP-Security','JSP-Internationalization']


toc = ['Overview','Architecture','Environment-Setup','Hello-World-Example','IoC-Containers','Bean-Definition','Bean-Scopes','Bean-Life-Cycle','Bean-Post-Processors','Bean-Definition-Inheritance','Dependency-Injection','Injecting-Inner-Beans','Injecting-Collection','Spring-Beans-Auto-Wiring','Annotation-Based-Configuration','Java-Based-Configuration','Event-Handling-in-Spring','Custom-Events-in-Spring','AOP-with-Spring-Framework','Spring-JDBC-Framework','Transaction-Management','Spring-Web-MVC-Framework','Spring-Logging-with-Log4J']

toc = ['Overview','Basics','Selectors','Attributes','Traversing','CSS','DOM','Events','AJAX','Effects']

toc = ['CSS and Documents','Selectors','Structure and the Cascade','Values and Units','Fonts','Text Properties','Basic Visual Formatting','Padding, Borders, and Margins','Colors and Backgrounds','Floating and Positioning','Table Layout','Lists and Generated Content','User Interface Styles','Non-Screen Media']

noteType = "CSS"

#toc.sort()

s = '''

Cascading Style Sheets (CSS) are a powerful way to affect the presentation of a document or a collection of documents.

Obviously, CSS is basically useless without a document of some sort, since it would have no content to present.

## 二级标题

## 二级标题

'''

for fa in toc:
    # print "[" + fa.replace("-", " ").capitalize() + "](#docs/" + fa + ")"
    print "1. [" + fa.replace("-"," ") + "](#docs/css/" + fa.lower().replace(" ","-") + ")"
    with open("doc/css/" + fa.lower().replace(" ","-") + ".md", "w") as f:
        f.write("# " + noteType + " - " + fa.replace("JSP-","").replace("-"," ") )
        f.write(s)