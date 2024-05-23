"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[8660],{28660:(e,t,n)=>{n.r(t),n.d(t,{scheme:()=>E});var r="comment",a="string",i="symbol",s="atom",c="number",l="bracket";function o(e){for(var t={},n=e.split(" "),r=0;r<n.length;++r)t[n[r]]=!0;return t}var d=o("λ case-lambda call/cc class cond-expand define-class define-values exit-handler field import inherit init-field interface let*-values let-values let/ec mixin opt-lambda override protect provide public rename require require-for-syntax syntax syntax-case syntax-error unit/sig unless when with-syntax and begin call-with-current-continuation call-with-input-file call-with-output-file case cond define define-syntax define-macro defmacro delay do dynamic-wind else for-each if lambda let let* let-syntax letrec letrec-syntax map or syntax-rules abs acos angle append apply asin assoc assq assv atan boolean? caar cadr call-with-input-file call-with-output-file call-with-values car cdddar cddddr cdr ceiling char->integer char-alphabetic? char-ci<=? char-ci<? char-ci=? char-ci>=? char-ci>? char-downcase char-lower-case? char-numeric? char-ready? char-upcase char-upper-case? char-whitespace? char<=? char<? char=? char>=? char>? char? close-input-port close-output-port complex? cons cos current-input-port current-output-port denominator display eof-object? eq? equal? eqv? eval even? exact->inexact exact? exp expt #f floor force gcd imag-part inexact->exact inexact? input-port? integer->char integer? interaction-environment lcm length list list->string list->vector list-ref list-tail list? load log magnitude make-polar make-rectangular make-string make-vector max member memq memv min modulo negative? newline not null-environment null? number->string number? numerator odd? open-input-file open-output-file output-port? pair? peek-char port? positive? procedure? quasiquote quote quotient rational? rationalize read read-char real-part real? remainder reverse round scheme-report-environment set! set-car! set-cdr! sin sqrt string string->list string->number string->symbol string-append string-ci<=? string-ci<? string-ci=? string-ci>=? string-ci>? string-copy string-fill! string-length string-ref string-set! string<=? string<? string=? string>=? string>? string? substring symbol->string symbol? #t tan transcript-off transcript-on truncate values vector vector->list vector-fill! vector-length vector-ref vector-set! with-input-from-file with-output-to-file write write-char zero?"),u=o("define let letrec let* lambda define-macro defmacro let-syntax letrec-syntax let-values let*-values define-syntax syntax-rules define-values when unless");function m(e,t,n){this.indent=e,this.type=t,this.prev=n}function p(e,t,n){e.indentStack=new m(t,n,e.indentStack)}var f=new RegExp(/^(?:[-+]i|[-+][01]+#*(?:\/[01]+#*)?i|[-+]?[01]+#*(?:\/[01]+#*)?@[-+]?[01]+#*(?:\/[01]+#*)?|[-+]?[01]+#*(?:\/[01]+#*)?[-+](?:[01]+#*(?:\/[01]+#*)?)?i|[-+]?[01]+#*(?:\/[01]+#*)?)(?=[()\s;"]|$)/i),h=new RegExp(/^(?:[-+]i|[-+][0-7]+#*(?:\/[0-7]+#*)?i|[-+]?[0-7]+#*(?:\/[0-7]+#*)?@[-+]?[0-7]+#*(?:\/[0-7]+#*)?|[-+]?[0-7]+#*(?:\/[0-7]+#*)?[-+](?:[0-7]+#*(?:\/[0-7]+#*)?)?i|[-+]?[0-7]+#*(?:\/[0-7]+#*)?)(?=[()\s;"]|$)/i),g=new RegExp(/^(?:[-+]i|[-+][\da-f]+#*(?:\/[\da-f]+#*)?i|[-+]?[\da-f]+#*(?:\/[\da-f]+#*)?@[-+]?[\da-f]+#*(?:\/[\da-f]+#*)?|[-+]?[\da-f]+#*(?:\/[\da-f]+#*)?[-+](?:[\da-f]+#*(?:\/[\da-f]+#*)?)?i|[-+]?[\da-f]+#*(?:\/[\da-f]+#*)?)(?=[()\s;"]|$)/i),x=new RegExp(/^(?:[-+]i|[-+](?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*)i|[-+]?(?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*)@[-+]?(?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*)|[-+]?(?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*)[-+](?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*)?i|(?:(?:(?:\d+#+\.?#*|\d+\.\d*#*|\.\d+#*|\d+)(?:[esfdl][-+]?\d+)?)|\d+#*\/\d+#*))(?=[()\s;"]|$)/i);function b(e){return e.match(f)}function k(e){return e.match(h)}function v(e,t){return!0===t&&e.backUp(1),e.match(x)}function y(e){return e.match(g)}function w(e,t){for(var n,r=!1;null!=(n=e.next());){if(n==t.token&&!r){t.state.mode=!1;break}r=!r&&"\\"==n}}const E={name:"scheme",startState:function(){return{indentStack:null,indentation:0,mode:!1,sExprComment:!1,sExprQuote:!1}},token:function(e,t){if(null==t.indentStack&&e.sol()&&(t.indentation=e.indentation()),e.eatSpace())return null;var n=null;switch(t.mode){case"string":w(e,{token:'"',state:t}),n=a;break;case"symbol":w(e,{token:"|",state:t}),n=i;break;case"comment":for(var o,m=!1;null!=(o=e.next());){if("#"==o&&m){t.mode=!1;break}m="|"==o}n=r;break;case"s-expr-comment":if(t.mode=!1,"("!=e.peek()&&"["!=e.peek()){e.eatWhile(/[^\s\(\)\[\]]/),n=r;break}t.sExprComment=0;default:var f=e.next();if('"'==f)t.mode="string",n=a;else if("'"==f)"("==e.peek()||"["==e.peek()?("number"!=typeof t.sExprQuote&&(t.sExprQuote=0),n=s):(e.eatWhile(/[\w_\-!$%&*+\.\/:<=>?@\^~]/),n=s);else if("|"==f)t.mode="symbol",n=i;else if("#"==f)if(e.eat("|"))t.mode="comment",n=r;else if(e.eat(/[tf]/i))n=s;else if(e.eat(";"))t.mode="s-expr-comment",n=r;else{var h=null,g=!1,x=!0;e.eat(/[ei]/i)?g=!0:e.backUp(1),e.match(/^#b/i)?h=b:e.match(/^#o/i)?h=k:e.match(/^#x/i)?h=y:e.match(/^#d/i)?h=v:e.match(/^[-+0-9.]/,!1)?(x=!1,h=v):g||e.eat("#"),null!=h&&(x&&!g&&e.match(/^#[ei]/i),h(e)&&(n=c))}else if(/^[-+0-9.]/.test(f)&&v(e,!0))n=c;else if(";"==f)e.skipToEnd(),n=r;else if("("==f||"["==f){for(var E,S="",q=e.column();null!=(E=e.eat(/[^\s\(\[\;\)\]]/));)S+=E;S.length>0&&u.propertyIsEnumerable(S)?p(t,q+2,f):(e.eatSpace(),e.eol()||";"==e.peek()?p(t,q+1,f):p(t,q+e.current().length,f)),e.backUp(e.current().length-1),"number"==typeof t.sExprComment&&t.sExprComment++,"number"==typeof t.sExprQuote&&t.sExprQuote++,n=l}else")"==f||"]"==f?(n=l,null!=t.indentStack&&t.indentStack.type==(")"==f?"(":"[")&&(function(e){e.indentStack=e.indentStack.prev}(t),"number"==typeof t.sExprComment&&0==--t.sExprComment&&(n=r,t.sExprComment=!1),"number"==typeof t.sExprQuote&&0==--t.sExprQuote&&(n=s,t.sExprQuote=!1))):(e.eatWhile(/[\w_\-!$%&*+\.\/:<=>?@\^~]/),n=d&&d.propertyIsEnumerable(e.current())?"builtin":"variable")}return"number"==typeof t.sExprComment?r:"number"==typeof t.sExprQuote?s:n},indent:function(e){return null==e.indentStack?e.indentation:e.indentStack.indent},languageData:{closeBrackets:{brackets:["(","[","{",'"']},commentTokens:{line:";;"}}}}}]);