"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[9440],{29440:(e,n,t)=>{function r(e){for(var n={},t=e.split(" "),r=0;r<t.length;++r)n[t[r]]=!0;return n}t.r(n),t.d(n,{sieve:()=>s});var i=r("if elsif else stop require"),u=r("true false not");function o(e,n){var t,r=e.next();if("/"==r&&e.eat("*"))return n.tokenize=a,a(e,n);if("#"===r)return e.skipToEnd(),"comment";if('"'==r)return n.tokenize=(t=r,function(e,n){for(var r,i=!1;null!=(r=e.next())&&(r!=t||i);)i=!i&&"\\"==r;return i||(n.tokenize=o),"string"}),n.tokenize(e,n);if("("==r)return n._indent.push("("),n._indent.push("{"),null;if("{"===r)return n._indent.push("{"),null;if(")"==r&&(n._indent.pop(),n._indent.pop()),"}"===r)return n._indent.pop(),null;if(","==r)return null;if(";"==r)return null;if(/[{}\(\),;]/.test(r))return null;if(/\d/.test(r))return e.eatWhile(/[\d]/),e.eat(/[KkMmGg]/),"number";if(":"==r)return e.eatWhile(/[a-zA-Z_]/),e.eatWhile(/[a-zA-Z0-9_]/),"operator";e.eatWhile(/\w/);var s=e.current();return"text"==s&&e.eat(":")?(n.tokenize=l,"string"):i.propertyIsEnumerable(s)?"keyword":u.propertyIsEnumerable(s)?"atom":null}function l(e,n){return n._multiLineString=!0,e.sol()?("."==e.next()&&e.eol()&&(n._multiLineString=!1,n.tokenize=o),"string"):(e.eatSpace(),"#"==e.peek()?(e.skipToEnd(),"comment"):(e.skipToEnd(),"string"))}function a(e,n){for(var t,r=!1;null!=(t=e.next());){if(r&&"/"==t){n.tokenize=o;break}r="*"==t}return"comment"}const s={name:"sieve",startState:function(e){return{tokenize:o,baseIndent:e||0,_indent:[]}},token:function(e,n){return e.eatSpace()?null:(n.tokenize||o)(e,n)},indent:function(e,n,t){var r=e._indent.length;return n&&"}"==n[0]&&r--,r<0&&(r=0),r*t.unit},languageData:{indentOnInput:/^\s*\}$/}}}}]);