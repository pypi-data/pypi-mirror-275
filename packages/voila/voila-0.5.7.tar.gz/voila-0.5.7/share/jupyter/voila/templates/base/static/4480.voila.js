"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[4480],{64480:(t,e,n)=>{n.r(e),n.d(e,{shell:()=>h});var r={};function s(t,e){for(var n=0;n<e.length;n++)r[e[n]]=t}var i=["true","false"],o=["if","then","do","else","elif","while","until","for","in","esac","fi","fin","fil","done","exit","set","unset","export","function"],u=["ab","awk","bash","beep","cat","cc","cd","chown","chmod","chroot","clear","cp","curl","cut","diff","echo","find","gawk","gcc","get","git","grep","hg","kill","killall","ln","ls","make","mkdir","openssl","mv","nc","nl","node","npm","ping","ps","restart","rm","rmdir","sed","service","sh","shopt","shred","source","sort","sleep","ssh","start","stop","su","sudo","svn","tee","telnet","top","touch","vi","vim","wall","wc","wget","who","write","yes","zsh"];function a(t,e){if(t.eatSpace())return null;var n,s=t.sol(),i=t.next();if("\\"===i)return t.next(),null;if("'"===i||'"'===i||"`"===i)return e.tokens.unshift(f(i,"`"===i?"quote":"string")),k(t,e);if("#"===i)return s&&t.eat("!")?(t.skipToEnd(),"meta"):(t.skipToEnd(),"comment");if("$"===i)return e.tokens.unshift(l),k(t,e);if("+"===i||"="===i)return"operator";if("-"===i)return t.eat("-"),t.eatWhile(/\w/),"attribute";if("<"==i){if(t.match("<<"))return"operator";var o=t.match(/^<-?\s*(?:['"]([^'"]*)['"]|([^'"\s]*))/);if(o)return e.tokens.unshift((n=o[1]||o[2],function(t,e){return t.sol()&&t.string==n&&e.tokens.shift(),t.skipToEnd(),"string.special"})),"string.special"}if(/\d/.test(i)&&(t.eatWhile(/\d/),t.eol()||!/\w/.test(t.peek())))return"number";t.eatWhile(/[\w-]/);var u=t.current();return"="===t.peek()&&/\w+/.test(u)?"def":r.hasOwnProperty(u)?r[u]:null}function f(t,e){var n="("==t?")":"{"==t?"}":t;return function(r,s){for(var i,o=!1;null!=(i=r.next());){if(i===n&&!o){s.tokens.shift();break}if("$"===i&&!o&&"'"!==t&&r.peek()!=n){o=!0,r.backUp(1),s.tokens.unshift(l);break}if(!o&&t!==n&&i===t)return s.tokens.unshift(f(t,e)),k(r,s);if(!o&&/['"]/.test(i)&&!/['"]/.test(t)){s.tokens.unshift(c(i,"string")),r.backUp(1);break}o=!o&&"\\"===i}return e}}function c(t,e){return function(n,r){return r.tokens[0]=f(t,e),n.next(),k(n,r)}}s("atom",i),s("keyword",o),s("builtin",u);var l=function(t,e){e.tokens.length>1&&t.eat("$");var n=t.next();return/['"({]/.test(n)?(e.tokens[0]=f(n,"("==n?"quote":"{"==n?"def":"string"),k(t,e)):(/\d/.test(n)||t.eatWhile(/\w/),e.tokens.shift(),"def")};function k(t,e){return(e.tokens[0]||a)(t,e)}const h={name:"shell",startState:function(){return{tokens:[]}},token:function(t,e){return k(t,e)},languageData:{autocomplete:i.concat(o,u),closeBrackets:{brackets:["(","[","{","'",'"',"`"]},commentTokens:{line:"#"}}}}}]);