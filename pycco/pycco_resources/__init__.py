css = """\
/*--------------------- Layout and Typography ----------------------------*/
body {
  font-family: "Helvetica", arial, freesans, clean, sans-serif;
  font-size: 16px;
  line-height: 24px;
  color: #252519;
  margin: 0; padding: 0;
  background: #f5f5ff;
}
a {
  color: #261a3b;
}
  a:visited {
    color: #261a3b;
  }
p {
  margin: 0 0 15px 0;
}
h1, h2, h3, h4, h5, h6 {
  margin: 40px 0 15px 0;
}
h2, h3, h4, h5, h6 {
    margin-top: 0;
  }
#container {
  background: white;
 }
#container, div.section {
  position: relative;
}
#background {
  position: absolute;
  top: 0; left: 580px; right: 0; bottom: 0;
  background: #f5f5ff;
  border-left: 1px solid #e5e5ee;
  z-index: 0;
}
#jump_to, #jump_page {
  background: white;
  -webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
  -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
  font: 10px Arial;
  text-transform: uppercase;
  cursor: pointer;
  text-align: right;
  z-index: 1;
}
#jump_to, #jump_wrapper {
  position: fixed;
  right: 0; top: 0;
  padding: 5px 10px;
}
  #jump_wrapper {
    padding: 0;
    display: none;
  }
    #jump_to:hover #jump_wrapper {
      display: block;
    }
    #jump_page {
      padding: 5px 0 3px;
      margin: 0 0 25px 25px;
    }
      #jump_page .source {
        display: block;
        padding: 5px 10px;
        text-decoration: none;
        border-top: 1px solid #eee;
      }
        #jump_page .source:hover {
          background: #f5f5ff;
        }
        #jump_page .source:first-child {
        }
div.docs {
  float: left;
  max-width: 500px;
  min-width: 500px;
  min-height: 5px;
  padding: 10px 25px 50px 50px;
  vertical-align: top;
  text-align: left;
}
  .docs pre {
    margin: 15px 0 15px;
    padding-left: 15px;
  }
  .docs p tt, .docs p code {
    background: #f8f8ff;
    border: 1px solid #dedede;
    font-size: 12px;
    padding: 0 0.2em;
  }
  .octowrap {
    position: relative;
  }
    .octothorpe {
      font: 12px Arial;
      text-decoration: none;
      color: #454545;
      position: absolute;
      top: 3px; left: -20px;
      padding: 1px 2px;
      opacity: 0;
      -webkit-transition: opacity 0.2s linear;
    }
      div.docs:hover .octothorpe {
        opacity: 1;
      }
div.code {
  margin-left: 580px;
  padding: 14px 15px 16px 50px;
  vertical-align: top;
}
  .code pre, .docs p code {
    font-size: 12px;
  }
    pre, tt, code {
      line-height: 18px;
      font-family: Consolas, "Liberation Mono", Courier, monospace;
      margin: 0; padding: 0;
    }
div.clearall {
    clear: both;
}


/*---------------------- Syntax Highlighting -----------------------------*/
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
.hll { background-color: #ffffcc }
.c { color: #999988; font-style: italic } /* Comment */
.err { color: #a61717; background-color: #e3d2d2 } /* Error */
.k { color: #000000; font-weight: bold } /* Keyword */
.o { color: #000000; font-weight: bold } /* Operator */
.cm { color: #999988; font-style: italic } /* Comment.Multiline */
.cp { color: #999999; font-weight: bold; font-style: italic } /* Comment.Preproc */
.c1 { color: #999988; font-style: italic } /* Comment.Single */
.cs { color: #999999; font-weight: bold; font-style: italic } /* Comment.Special */
.gd { color: #000000; background-color: #ffdddd } /* Generic.Deleted */
.ge { color: #000000; font-style: italic } /* Generic.Emph */
.gr { color: #aa0000 } /* Generic.Error */
.gh { color: #999999 } /* Generic.Heading */
.gi { color: #000000; background-color: #ddffdd } /* Generic.Inserted */
.go { color: #888888 } /* Generic.Output */
.gp { color: #555555 } /* Generic.Prompt */
.gs { font-weight: bold } /* Generic.Strong */
.gu { color: #aaaaaa } /* Generic.Subheading */
.gt { color: #aa0000 } /* Generic.Traceback */
.kc { color: #000000; font-weight: bold } /* Keyword.Constant */
.kd { color: #000000; font-weight: bold } /* Keyword.Declaration */
.kn { color: #000000; font-weight: bold } /* Keyword.Namespace */
.kp { color: #000000; font-weight: bold } /* Keyword.Pseudo */
.kr { color: #000000; font-weight: bold } /* Keyword.Reserved */
.kt { color: #445588; font-weight: bold } /* Keyword.Type */
.m { color: #009999 } /* Literal.Number */
.s { color: #d01040 } /* Literal.String */
.na { color: #008080 } /* Name.Attribute */
.nb { color: #0086B3 } /* Name.Builtin */
.nc { color: #445588; font-weight: bold } /* Name.Class */
.no { color: #008080 } /* Name.Constant */
.nd { color: #3c5d5d; font-weight: bold } /* Name.Decorator */
.ni { color: #800080 } /* Name.Entity */
.ne { color: #990000; font-weight: bold } /* Name.Exception */
.nf { color: #990000; font-weight: bold } /* Name.Function */
.nl { color: #990000; font-weight: bold } /* Name.Label */
.nn { color: #555555 } /* Name.Namespace */
.nt { color: #000080 } /* Name.Tag */
.nv { color: #008080 } /* Name.Variable */
.ow { color: #000000; font-weight: bold } /* Operator.Word */
.w { color: #bbbbbb } /* Text.Whitespace */
.mf { color: #009999 } /* Literal.Number.Float */
.mh { color: #009999 } /* Literal.Number.Hex */
.mi { color: #009999 } /* Literal.Number.Integer */
.mo { color: #009999 } /* Literal.Number.Oct */
.sb { color: #d01040 } /* Literal.String.Backtick */
.sc { color: #d01040 } /* Literal.String.Char */
.sd { color: #d01040 } /* Literal.String.Doc */
.s2 { color: #d01040 } /* Literal.String.Double */
.se { color: #d01040 } /* Literal.String.Escape */
.sh { color: #d01040 } /* Literal.String.Heredoc */
.si { color: #d01040 } /* Literal.String.Interpol */
.sx { color: #d01040 } /* Literal.String.Other */
.sr { color: #009926 } /* Literal.String.Regex */
.s1 { color: #d01040 } /* Literal.String.Single */
.ss { color: #990073 } /* Literal.String.Symbol */
.bp { color: #999999 } /* Name.Builtin.Pseudo */
.vc { color: #008080 } /* Name.Variable.Class */
.vg { color: #008080 } /* Name.Variable.Global */
.vi { color: #008080 } /* Name.Variable.Instance */
.il { color: #009999 } /* Literal.Number.Integer.Long */
"""

html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
</head>
<body>
<div id='container'>
  <div id="background"></div>
  
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'>
  {{#sections}}
  <div class='section {{ visibility }}' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
</body>
"""
